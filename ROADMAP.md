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
  *Details*: analyse BG trends between 00:00–05:00 to highlight rising or falling patterns.
  *Acceptance*: unit tests cover typical, high and low drift scenarios; report lists nights with detected drift; docs describe usage.
* [ ] **MVP‑04** `report`: include “events sampled / events skipped” stats block
  *Enhances transparency.*
  *Details*: add section in Markdown and JSON summarising number of candidate events versus discarded ones.
  *Acceptance*: stats appear in both output formats; tests verify counts; README updated.
* [ ] **INT‑01** `ingest`: Dexcom real‑time API connector
  Link to Issue #12.
  *Details*: pull glucose readings via Dexcom OAuth API and store tokens locally.
  *Acceptance*: CLI flag `--dexcom` fetches data when credentials supplied; token refresh handled; mocked tests; docs updated.
* [ ] **INT‑02** `ingest`: Nightscout REST importer
  Permits DIY Loop users to sync.  Requires token auth.
  *Details*: fetch glucose, carbs and insulin data from a Nightscout instance using REST endpoints.
  *Acceptance*: CLI `--nightscout URL` imports recent records with token auth; unit tests mock API; docs describe setup.
* [ ] **INT‑03** `notify`: weekly summary email (SendGrid)
  Funnel: `analysis → Jinja → email`.  Add opt‑in flag to CLI.
  *Details*: generate email from Jinja template summarising last week's metrics and send via SendGrid.
  *Acceptance*: CLI `--email ADDRESS` sends summary when SendGrid key configured; tests mock network calls; README outlines opt‑in.
* [ ] **CTX‑01** `context`: Fitbit/Google Fit step detector
  Mark exercise windows in analysis.
  *Details*: import step counts from Fitbit or Google Fit to tag moderate/vigorous activity periods.
  *Acceptance*: analysis marks exercise segments when step data provided; tests cover sample files; docs list expected columns.
* [ ] **ADV‑01** `ml`: prototype simple linear BG prediction
  Use last 30 clean meals to fit sensitivity model.
  *Details*: implement regression predicting BG 2 h after meal based on carbs and insulin.
  *Acceptance*: model trains locally; prediction error reported in output; unit tests with synthetic data; docs explain limitations.
* [ ] **DEV‑tooling** `ci`: add doc‑sync checker
  Fails CI if README not touched when CLI changes.
  *Details*: CI step verifies commits modifying `cli.py` also modify `README.md`.
  *Acceptance*: checker runs in GitHub Actions and blocks merge on mismatch; contributing docs mention the rule.

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
