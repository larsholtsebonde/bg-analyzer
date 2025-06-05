# 🤖 AI Contributor Guide

Welcome, autonomous agent!  This document explains the project layout, coding conventions, and the extra steps you—an AI system—should follow when proposing changes to **BG Analyzer**.

> **If your modification changes user‑visible behaviour or usage instructions, you must also update** `README.md`, sample configuration files, and any other helper docs needed to keep everything in sync.

---

## 1 · Repository Map

| Path                     | What you’ll find                                                                     | Typical agent tasks                                          |
| ------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------ |
| `/bg_analyzer/ingest/`   | Parsers that convert device exports (CGM, pump, pen, food logs) into a common schema | Add a new `*.py` parser, expand the schema, write unit tests |
| `/bg_analyzer/analysis/` | Core algorithms for event filtering and ICR/ICF estimation                           | Optimise maths, add new metrics or context‑aware models      |
| `/bg_analyzer/report/`   | Renderers that turn analysis results into Markdown & JSON                            | Create new output formats, tweak visualisation               |
| `/cli.py`                | Click‑based command‑line interface entry point                                       | Extend CLI flags, improve UX messages                        |
| `/samples/`              | Example CSV files for manual and CI tests                                            | Add fresh samples when supporting new devices                |
| `/tests/`                | Pytest suite & fixtures                                                              | Write tests for every new behaviour                          |
| `/docs/`                 | Longer‑form design/architecture docs (optional)                                      | Add detailed specs, diagrams                                 |

---

## 2 · Workflow for Agents

1. **Sync and plan**
   *Read open issues or create one describing the change.*  Reference it in your PR.
   If anything is unclear, add a bullet to `QUESTIONS.md` so the product owner can respond.
2. **Create a feature branch**
   `feature/<short‑slug>` or `fix/<short‑slug>`.
3. **Write the code**

   * Follow existing folder conventions.
   * Add/modify docstrings in *Google‑style* format.
   * Maintain type hints (`mypy` passes).
   * Keep functions <50 LOC where feasible.
4. **Update documentation**

   * If UX or CLI changes, update `README.md`.
   * If developer‑facing behaviour changes, update `agents.md` or create a doc under `/docs/`.
   * Refresh examples in `/samples/` if data format changes.
   * When a question in `QUESTIONS.md` is answered, reflect it in the docs and remove that bullet.
5. **Validate**

   * Run `pre‑commit run --all-files` (black, isort, flake8, mypy, etc.).
   * Run `pytest ‑q`—tests must pass and coverage ≥ 90 %.
   * Execute `python cli.py --help` to ensure CLI still works.
6. **Commit**
   Use *Conventional Commits*:
   `feat(ingest): add Abbott Libre CSV parser`
   `fix(analysis): handle zero‑carb corrections`
7. **Pull Request**

   * Title = concise, imperative.
   * Body = *What + Why + How*, link the issue.
   * Checklist ticked (tests, docs, coverage).
   * Tag `@maintainers` for review.

---

## 3 · Design Principles

* **Local‑first privacy**: never send raw health data to external APIs unless an integration is explicitly enabled.
* **Predictability over complexity**: favour transparent calculations before opaque ML.  Include comments & references if statistical methods are added.
* **User empathy**: error messages must be actionable and non‑alarmist; analytics should default to safe, conservative suggestions.

---

## 4 · Updating Helper Files

When your change alters:

| Change type             | Docs to update                                                                    |
| ----------------------- | --------------------------------------------------------------------------------- |
| CLI flag, config option | `README.md` (Quick Start & Expected CSV columns)                                  |
| Device/data source      | `README.md` (Capabilities) + `/samples/`                                          |
| Repo structure          | `agents.md` + `/docs/architecture.md`                                             |
| Algorithms/metrics      | `README.md` (Current capabilities) + Possibly a new doc under `/docs/algorithms/` |

Failing to update docs will trigger **CI Doc‑Check** and block merge.

---

## 5 · Test & Documentation Utilities

* **Generate latest user report**: `make demo-report` → writes to `reports/`.
* **Open coverage HTML**: `make cov`.
* **Lint markdown**: `mdformat -i *.md`  (runs in pre‑commit).

---

## 6 · Semantic Versioning & Changelog

The project follows **SemVer**.  The `CHANGELOG.md` is auto‑generated from Conventional Commits during release (`npm version`‑style script).  When you merge to `main`, CI may tag a version bump.  *Breaking changes require a `!` in the commit scope.*

---

Happy coding, fellow agent – keep the loops tight, the tests green, and the docs fresh! 🚀
