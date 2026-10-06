---
name: week-notes
description: Write study notes (notes.md + notes.pdf) for one week of a course in this repo, from that week's lecture PDF. Use when the user asks for notes for a week/lecture, e.g. "/week-notes computer-security week04".
argument-hint: <course> <weekNN>   e.g. computer-security week04
---

# Week notes

Arguments: `$ARGUMENTS` — a course folder (`computer-security`, `iot`, `operating-systems`) and a
week folder (`week04`). If either is missing, look at which `weekNN/lecture/` folders have a PDF but
still have a placeholder `notes.md` (contains `_TODO_`), and ask which one to do.

Paths below are relative to the repo root (the folder containing this `.claude/`).

## 1. Find and read the lecture

1. The lecture is `<course>/<weekNN>/lecture/*.pdf`. If there's no PDF there, stop and tell the user.
   If the slides are still somewhere else (e.g. just downloaded), offer to move them in first, named
   `weekNN-topic-in-lowercase-hyphens.pdf`, using `git mv` if the file is tracked.
2. Extract the text into the scratchpad (not the repo):
   `pdftotext -layout "<lecture.pdf>" "<scratchpad>/weekNN.txt"`
3. Read **the whole** extracted text. If it is nearly empty, the PDF is image-only: tell the user
   and read the PDF pages directly instead.
4. Also look at `<course>/<weekNN>/assignment/` (task and submission) and the previous week's
   `notes.md` so the notes can link back to earlier topics.

## 2. Write `<course>/<weekNN>/notes.md`

Match the style of `computer-security/week01..03/notes.md` (read one of them first). Rules:

- **Follow the lecture's order exactly**: every section and every slide topic, in sequence, with
  the lecture's own headings. Don't skip slides and don't reorder.
- **Header:** `# Week NN — <Lecture title>`, then a quote block with the subtitle and a link to the
  slides (`lecture/<file>.pdf`), then the lecture's objectives or contents list.
- If the lecture uses real cases, add a **"Real cases used this week"** table near the top (case,
  date, what happened, what it teaches).
- **Explain, don't just copy.** Give each term a bold definition, then one or two plain sentences on
  what it means and why it matters. Use the lecture's own examples, names and cases, not new ones.
- Turn the slides' comparisons and letter grids (e.g. C / I / A, Prevent / Detect / Recover) into
  **tables**.
- **Case studies:** what happened, then the lesson, tied to the course framework (e.g. asset /
  threat / vulnerability / control, CIA).
- **Activities and in-slide questions:** quote the prompt, then give an **answer with reasons**.
  Use the lecture's answer when a slide provides one. When it doesn't, write the answer and add
  *"(The slides don't give the answer; this follows from …)"*.
- **Review Q&A:** every question with its answer, in bold-question / answer format.
- **Assignment:** restate the task, give guidance on how to approach it, and link to
  `assignment/submission.*` if it exists. Don't rewrite the user's submission.
- Keep the reading list and sources from the slides.
- End with **`## Most important for exams`**: 8–12 dense bullets covering the definitions,
  distinctions, formulas/tables and cases most likely to be tested.
- Plain English (the user studies in English as an exchange student). No copying long passages
  verbatim; short definitions are fine.

## 3. Make the PDF

Run from the repo root:

```bash
bash .claude/skills/week-notes/render-notes-pdf.sh <course>/<weekNN>/notes.md
```

It writes `notes.pdf` next to `notes.md` (via Edge headless and marked.js from the CDN). Check that
the script printed the output file and that `pdftotext <pdf> - | grep -c '|---'` is `0`, meaning the
tables rendered. Send the PDF to the user.

## 4. Update the course README and finish

- In `<course>/README.md`, make sure the week's row exists and links to `notes.md`. Add the row if
  the week is new.
- Show the user a short summary: sections covered, and which answers were your own (not on slides).
- **Don't commit or push unless the user asks.** When they do, commit with a message like
  `Add <Course> notes for week NN`.
