#!/usr/bin/env bash
# Render one or more notes.md files to notes.pdf (next to each .md) using Edge headless.
# Usage: bash .claude/skills/week-notes/render-notes-pdf.sh path/to/notes.md [more.md ...]
set -euo pipefail

EDGE="${EDGE:-/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe}"
[ -x "$EDGE" ] || EDGE="/c/Program Files/Google/Chrome/Application/chrome.exe"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

for md in "$@"; do
  [ -f "$md" ] || { echo "not found: $md" >&2; exit 1; }
  html="$TMP/$(basename "$(dirname "$md")").html"
  pdf="${md%.md}.pdf"

  cat > "$html" <<'EOF'
<!doctype html><html><head><meta charset="utf-8">
<script src="https://cdn.jsdelivr.net/npm/marked@12/marked.min.js"></script>
<style>
@page { size: A4; margin: 16mm 15mm; }
body { font-family: "Segoe UI", Arial, sans-serif; font-size: 10.5pt; line-height: 1.5; color: #1a1a1a; }
h1 { font-size: 20pt; color: #1f3a68; border-bottom: 3px solid #1f3a68; padding-bottom: 4px; margin-top: 0; }
h2 { font-size: 15pt; color: #1f3a68; border-bottom: 1px solid #c8d1e0; padding-bottom: 3px; margin-top: 22px; break-after: avoid; }
h3 { font-size: 12pt; color: #2c5282; margin: 16px 0 6px; break-after: avoid; }
table { border-collapse: collapse; width: 100%; margin: 8px 0 12px; font-size: 9.5pt; break-inside: avoid; }
th, td { border: 1px solid #c8d1e0; padding: 5px 7px; vertical-align: top; text-align: left; }
th { background: #eaf0f8; }
tr:nth-child(even) td { background: #f8fafc; }
blockquote { margin: 8px 0; padding: 6px 12px; background: #fff8e6; border-left: 4px solid #e0a800; }
blockquote p { margin: 3px 0; }
code { font-family: Consolas, monospace; font-size: 9.5pt; background: #f1f3f5; padding: 1px 4px; border-radius: 3px; }
pre { background: #f1f3f5; padding: 8px 10px; border-radius: 4px; break-inside: avoid; }
pre code { background: none; padding: 0; }
hr { border: none; border-top: 1px solid #ddd; margin: 18px 0; }
a { color: #2c5282; text-decoration: none; }
ul, ol { margin: 4px 0 8px; padding-left: 22px; }
li { margin: 2px 0; }
p { margin: 6px 0; }
</style></head><body><div id="out"></div>
<script type="text/plain" id="md">
EOF
  # Keep a literal "</script>" in the notes from ending the embedded block early.
  sed 's#</script#<\\/script#g' "$md" >> "$html"
  cat >> "$html" <<'EOF'
</script>
<script>
var src = document.getElementById('md').textContent.replace(/<\\\/script/g, '</script');
document.getElementById('out').innerHTML = marked.parse(src);
</script>
</body></html>
EOF

  rm -f "$pdf"
  "$EDGE" --headless=new --disable-gpu --no-pdf-header-footer --virtual-time-budget=15000 \
    --print-to-pdf="$(cygpath -w "$(realpath -m "$pdf")")" "file:///$(cygpath -m "$html")" 2>/dev/null || true
  [ -s "$pdf" ] || { echo "failed to render $pdf" >&2; exit 1; }
  echo "wrote $pdf"
done
