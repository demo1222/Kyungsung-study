#!/usr/bin/env bash
# Render midterm study guides (.md) to .pdf next to each .md, styled like the IoT midterm guide:
# navy table headers, coloured callout boxes and flow strips.
# Usage: bash .claude/skills/week-notes/render-guide-pdf.sh path/to/guide.md [more.md ...]
#
# Markdown conventions the styling relies on:
#   - A paragraph that is only inline code containing "→" becomes a flow strip:  `A → B → C`
#   - A blockquote becomes a callout; its colour follows the first bold words
#     (Important / Do not confuse = yellow, Trade-off / Trap = red, Key / High-yield / Exam = green, else blue).
set -euo pipefail

EDGE="${EDGE:-/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe}"
[ -x "$EDGE" ] || EDGE="/c/Program Files/Google/Chrome/Application/chrome.exe"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP" 2>/dev/null || true' EXIT

for md in "$@"; do
  [ -f "$md" ] || { echo "not found: $md" >&2; exit 1; }
  html="$TMP/$(basename "${md%.md}").html"
  pdf="${md%.md}.pdf"

  cat > "$html" <<'EOF'
<!doctype html><html><head><meta charset="utf-8">
<script src="https://cdn.jsdelivr.net/npm/marked@12/marked.min.js"></script>
<style>
@page { size: A4; margin: 15mm 15mm 16mm; }
body { font-family: "Segoe UI", Arial, sans-serif; font-size: 10pt; line-height: 1.45; color: #1a1a1a; }
h1 { font-size: 24pt; color: #17365d; text-align: center; border-bottom: 2px solid #4f81bd; padding-bottom: 6px; margin: 0 0 6px; }
h1 + p { text-align: center; font-size: 12pt; color: #17365d; }
h2 { font-size: 17pt; color: #17365d; margin: 0 0 8px; break-before: page; break-after: avoid; }
h3 { font-size: 12.5pt; color: #17365d; margin: 14px 0 5px; break-after: avoid; }
h4 { font-size: 10.5pt; color: #2c5282; margin: 10px 0 4px; break-after: avoid; }
table { border-collapse: collapse; width: 100%; margin: 6px 0 10px; font-size: 9.2pt; break-inside: avoid; }
th, td { border: 1px solid #1a1a1a; padding: 5px 7px; vertical-align: middle; text-align: left; }
th { background: #17365d; color: #fff; font-weight: 600; }
blockquote { margin: 8px 0; padding: 7px 12px; background: #dce9f5; break-inside: avoid; }
blockquote.yellow { background: #fff2cc; }
blockquote.red { background: #fde4d8; }
blockquote.green { background: #e2efd9; }
blockquote p { margin: 2px 0; }
blockquote strong:first-child { color: #17365d; }
.flow { display: flex; margin: 6px 0 8px; border: 1px solid #1a1a1a; break-inside: avoid; }
.flow span { flex: 1; text-align: center; font-weight: 600; font-size: 9pt; color: #17365d; padding: 8px 4px;
  border-left: 1px solid #1a1a1a; display: flex; align-items: center; justify-content: center; }
.flow span:first-child { border-left: none; }
.flow span:nth-child(odd) { background: #dce6f1; }
.flow span:nth-child(even) { background: #eef3fa; }
code { font-family: Consolas, monospace; font-size: 9pt; background: #f1f3f5; padding: 1px 4px; border-radius: 3px; }
th code { background: none; color: #fff; }
pre { background: #f5f5f5; padding: 8px 12px; break-inside: avoid; margin: 6px 0 8px; }
pre code { background: none; padding: 0; }
hr { display: none; }
a { color: #2c5282; text-decoration: none; }
ul, ol { margin: 4px 0 8px; padding-left: 22px; }
li { margin: 2px 0; }
p { margin: 5px 0; }
</style></head><body><div id="out"></div>
<script type="text/plain" id="md">
EOF
  # Keep a literal "</script>" in the guide from ending the embedded block early.
  sed 's#</script#<\\/script#g' "$md" >> "$html"
  cat >> "$html" <<'EOF'
</script>
<script>
var src = document.getElementById('md').textContent.replace(/<\\\/script/g, '</script');
var out = document.getElementById('out');
out.innerHTML = marked.parse(src);

// `A → B → C` on its own line becomes a flow strip.
out.querySelectorAll('p').forEach(function (p) {
  var c = p.firstElementChild;
  if (p.children.length !== 1 || !c || c.tagName !== 'CODE') return;
  if (p.textContent.trim() !== c.textContent.trim() || c.textContent.indexOf('→') < 0) return;
  var flow = document.createElement('div');
  flow.className = 'flow';
  c.textContent.split('→').forEach(function (step) {
    var s = document.createElement('span');
    s.textContent = step.trim();
    flow.appendChild(s);
  });
  p.replaceWith(flow);
});

// Callout colour follows the first bold words of the blockquote.
out.querySelectorAll('blockquote').forEach(function (b) {
  var s = b.querySelector('strong');
  var t = s ? s.textContent.toLowerCase() : '';
  if (/^(important|do not|don't|note)/.test(t)) b.className = 'yellow';
  else if (/^(trade-off|trap|warning|careful)/.test(t)) b.className = 'red';
  else if (/^(key|high-yield|exam|best|scope)/.test(t)) b.className = 'green';
});
</script>
</body></html>
EOF

  rm -f "$pdf"
  "$EDGE" --headless=new --disable-gpu --no-pdf-header-footer --virtual-time-budget=15000 \
    --print-to-pdf="$(cygpath -w "$(realpath -m "$pdf")")" "file:///$(cygpath -m "$html")" 2>/dev/null || true
  # Edge can return before the PDF is written, so wait for it (up to 60 s) before cleaning up.
  for _ in $(seq 60); do [ -s "$pdf" ] && break; sleep 1; done
  [ -s "$pdf" ] || { echo "failed to render $pdf" >&2; exit 1; }
  echo "wrote $pdf"
done
