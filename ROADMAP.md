# 📌 BG Analyzer • Product Roadmap

*A living kanban board for agents 🤖 and humans 🧑‍💻 to coordinate work*

> **How to use this file**
>
> * Each line item is a **task card**.  Move it between sections or change its checkbox when status changes.
> * Keep descriptions short; link to an Issue/PR for details.
> * When a task alters user‑visible behaviour or CLI flags, **update the docs** (`README.md`, `agents.md`, samples) in the same PR.
> * Add yourself as owner with `@handle` so everyone knows who’s on it.

---

## Milestones & Epics

| Tag     | Milestone                     | Goal                                                        |
| ------- | ----------------------------- | ----------------------------------------------------------- |
| **MVP** | Phase 1 — Core Insight        | Import CSV, compute ICR/ICF, generate report                |
| **INT** | Phase 2 — Integrations        | Pull data automatically from CGM / pump / pen APIs          |
| **CTX** | Phase 3 — Context AI          | Time‑of‑day ratios, exercise & sleep awareness, goal alerts |
| **ADV** | Phase 4 — Advanced / Clinical | Predictive simulation, clinician portal, optional FDA path  |

---

## ⏳ Backlog (not started)

* [ ] **MVP‑03** `analysis`: add overnight basal drift detector
  *Helps flag basal mis‑settings before bolus advice.*
  *Docs*: update `README (Capabilities)` once merged.
* [ ] **MVP‑04** `report`: include “events sampled / events skipped” stats block
  *Enhances transparency.*
* [ ] **INT‑01** `ingest`: Dexcom real‑time API connector
  Link to Issue #12.
* [ ] **INT‑02** `ingest`: Nightscout REST importer
  Permits DIY Loop users to sync.  Requires token auth.
* [ ] **INT‑03** `notify`: weekly summary email (SendGrid)
  Funnel: `analysis → Jinja → email`.  Add opt‑in flag to CLI.
* [ ] **CTX‑01** `context`: Fitbit/Google Fit step detector
  Mark exercise windows in analysis.
* [ ] **ADV‑01** `ml`: prototype simple linear BG prediction
  Use last 30 clean meals to fit sensitivity model.
* [ ] **DEV‑tooling** `ci`: add doc‑sync checker
  Fails CI if README not touched when CLI changes.

## 🚧 In Progress

* [ ] **MVP‑01** `ingest`: generic CSV parser w/ schema validation (@alice) – PR #23
* [ ] **MVP‑02** `analysis`: clean‑event finder algorithm (@bob) – drafting tests

## 🔍 Review / QA

* [ ] **DEV‑02** `tests`: coverage > 90% gate (@carol) – awaiting review PR #25

## ✅ Done

* [x] **SCF‑00** repo skeleton, `cli.py`, poetry setup – merged #1
* [x] **DOC‑01** initial `README.md` + `agents.md` – merged #2

---

### Legend

* **Code area**: `ingest`, `analysis`, `report`, `cli`, `notify`, `context`, `ml`, `ci`, `docs`…
* **Owner**: GitHub handle(s) responsible for the task.
* **Tag** / **Milestone**: see table above.

Happy shipping 🚀  — remember: small PRs, passing tests, fresh docs!
