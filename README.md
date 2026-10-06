# Kyungsung Study

My coursework from Kyungsung University (Busan), Fall 2026.

| Course | Topics so far |
|---|---|
| [Computer Security](computer-security/README.md) | Security basics and the CIA triad, assets, threats and risk, social engineering and phishing |
| [IoT](iot/README.md) | Virtual sensors, moving averages, data logging, a cold-chain monitoring device |
| [Operating Systems and System Programming](operating-systems/README.md) | OS basics, Python OS tools, a CPU/memory monitor |

## Layout

Every course uses the same layout:

```
<course>/
├── README.md
└── weekNN/
    ├── lecture/      slides
    ├── exercises/    in-class practice
    ├── assignment/   task + my submission
    └── notes.md
```

Files are named in lowercase with hyphens, e.g. `week01-introduction-to-computer-security.pdf`.
In `assignment/`, `task.*` is the brief and `submission.*` is what I handed in.

## Making notes for a new week

1. Put the lecture slides in `<course>/weekNN/lecture/`.
2. In Claude Code, run `/week-notes <course> weekNN`, for example `/week-notes computer-security week04`.

It reads the slides and writes `notes.md` (every topic in order, the lecture's cases, activities and
review Q&A with answers, and a "most important for exams" summary), then renders `notes.pdf` next to it.
The instructions live in [.claude/skills/week-notes/SKILL.md](.claude/skills/week-notes/SKILL.md).
