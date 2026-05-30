# CLAUDE.md — AI Engineering from Scratch

This file tells Claude Code how to work in this repository.

## What This Project Is

An open-source curriculum with 435 lessons across 20 phases covering AI engineering from math foundations to production systems. Each lesson lives in `phases/XX-phase-name/NN-lesson-name/` and contains runnable code (Python, TypeScript, Rust, Julia), docs, and outputs (prompts, skills, agents).

## Key References

- **@CONTRIBUTING.md** — how lessons are structured, PR process, code style rules, and how to add new lessons/outputs
- **@ROADMAP.md** — full phase breakdown with time estimates and lesson status glyphs (✅ 🚧 ⬚)
- **@README.md** — curriculum overview and lesson index
- **@PROGRESS.md** — personal learning progress tracker (local only, do not commit)

## Progress Tracking

**@PROGRESS.md** is the source of truth for where the learner is in the curriculum.

When the user asks about their progress, what to study next, or wants to update a lesson status — read `PROGRESS.md` first.

Valid status values:
- `done` — lesson complete, concept understood
- `in progress` — currently working through this lesson
- `need to improve` — completed but weak, should revisit theory
- `practise needed` — theory understood, needs more coding practice

## Lesson Structure

Every lesson follows this format (from CONTRIBUTING.md):

```
NN-lesson-name/
├── code/           # At least one runnable implementation
├── notebook/       # Jupyter notebook (optional)
├── docs/
│   └── en.md       # Lesson doc: motto → problem → concept → build → use → ship
└── outputs/        # Prompts, skills, agents produced by this lesson
```

## Code Rules (from CONTRIBUTING.md)

- Code must run without errors
- No comments in code — docs explain, code demonstrates
- Build from scratch first, framework version second
- No AI slop — write direct prose

## Session Setup (run every time you open this project)

```bash
source .venv/bin/activate
```

Without this, `python` points to the system Python 3.9.6 and none of the installed packages (torch, numpy, anthropic, etc.) are available. The venv lives in `.venv/` and must be re-activated each terminal session.

## Do Not Commit

- `PROGRESS.md` — personal progress tracker, local only
- `.env` files — API keys go in environment variables only
- `.claude/` directory — local skills and config

## Learning Mode

When working through lessons, Claude operates in explain-first mode:

- **Wait for instructions.** Do not run code, update PROGRESS.md, or take any
  action until explicitly asked. State the plan and stop.
- **Explain before acting.** When asked to do something, explain what it does
  and why it matters before running it.
- **Expand AI/ML abbreviations on first use.** The user knows general
  engineering (Java, AWS, REST, SQL, etc.) but not AI-specific shorthand.
  Always expand on first mention — write "IMDB (a movie review dataset used
  as a standard benchmark)" not just "IMDB", write "BPE (Byte-Pair Encoding,
  a tokenization algorithm)" not just "BPE", and so on.
- **Define AI/ML jargon in plain English.** Terms like "streaming", "split",
  "Parquet", "fine-tuning", "embedding", "tokenizer" are not obvious — give
  a one-liner on first use.
- **No silent steps.** Every terminal command gets a one-sentence explanation
  of what it does before it runs.
- **Exercises are interactive.** Walk through each exercise as a guided
  conversation, not a batch of copy-paste commands.
