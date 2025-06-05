# BG Analyzer

> **Personalised insulin‑dose insights from your own data**

BG Analyzer is an open‑source tool that helps people with Type 1 Diabetes fine‑tune their **Insulin‑to‑Carbohydrate Ratio (ICR)** and **Insulin Correction Factor (ICF)**.  It turns everyday glucose, insulin, and meal logs into clear, actionable recommendations—reducing guess‑work and supporting safer, more confident dosing decisions.

---

## Why it matters

Managing T1D means juggling many variables: food, insulin, exercise, hormones, stress—and each person’s response is unique and ever‑changing.  Clinic visits every few months rarely keep pace with real‑life variability, so most people end up **trial‑and‑error‑tweaking** their doses on their own.

BG Analyzer analyses **your** data continuously and highlights when a ratio no longer fits (e.g. “breakfast ICR looks too weak; try 1 U per 10 g instead of 1 U per 12 g”).  By shortening the feedback loop, it aims to improve *time‑in‑range* and reduce both highs and lows.

---

## Current capabilities (MVP 0.1 α)

* ⚙️ **CSV importer** – Load CGM / finger‑stick glucose, insulin bolus, and carb records exported from common devices or apps.
* 📊 **Event filtering engine** – Finds “clean” meal or correction events (single bolus, stable BG beforehand) suitable for ratio calculation.
* 🧮 **ICR / ICF estimator** – Calculates observed carb‑coverage and correction sensitivity and compares them to your current settings.
* 📝 **Markdown & JSON reports** – Summaries are saved to `reports/` so humans *and* AIs can read them.

> *Disclaimer – BG Analyzer is **decision‑support only**. It does **not** automatically dose insulin and is **not** a regulated medical device. Always confirm changes with a healthcare professional.*

---

## Quick Start

```bash
# 1. Clone & install
$ git clone https://github.com/larsholtsebonde/bg-analyzer.git
$ cd bg-analyzer
$ python -m venv .venv && source .venv/bin/activate
$ pip install -r requirements.txt

# 2. Prepare data (example: Dexcom CSV + InPen CSV)
$ mkdir data
$ cp ~/Downloads/dexcom_export.csv data/glucose.csv
$ cp ~/Downloads/inpen_export.csv   data/insulin.csv

# 3. Run analysis
$ python -m bg_analyzer --glucose data/glucose.csv \
                       --insulin data/insulin.csv \
                       --carbs   data/carb_log.csv

# 4. Open the report
$ open reports/latest_report.md          # or view JSON in reports/latest_report.json
```

### Expected CSV columns

| File           | Required Columns                     |
| -------------- | ------------------------------------ |
| `glucose.csv`  | `timestamp, bg_mmol`                 |
| `insulin.csv`  | `timestamp, bolus_units, bolus_type` |
| `carb_log.csv` | `timestamp, carbs_grams, meal_label` |

Blood glucose values are expressed in **mmol/L**.

(See [`/samples`](./samples) for example data.)

---

## Roadmap (abridged)

| Phase               | Goal                           | Key features                                                                       |
| ------------------- | ------------------------------ | ---------------------------------------------------------------------------------- |
| **1 MVP**           | Validate core insight          | Manual import, ICR/ICF maths, markdown report                                      |
| **2 Integrations**  | Reduce logging burden          | Direct Dexcom API, Nightscout, smart‑pen / pump imports, weekly push notifications |
| **3 Context AI**    | Personalised guidance          | Time‑of‑day ratios, exercise & sleep tagging, goal‑based alerts                    |
| **4 Clinical + ML** | Advanced predictions & sharing | Predictive dose simulation, clinician portal, optional FDA clearance               |

---

## Architecture

```
/ bg_analyzer
    │
    ├── ingest/        # parsers for CGM, pump, pen & food logs
    ├── analysis/      # event filtering + ratio calculators
    ├── report/        # markdown + JSON renderers
    └── cli.py         # command‑line interface entry‑point
```

All heavy computation runs **locally**; nothing is sent to external servers unless you enable an integration.

---

## Contributing

1. **Open an issue** to discuss ideas or bugs.
2. **Fork & PR** – follow the conventional‑commits style for concise commit messages.
3. **Pre‑commit hooks** run formatting & tests (`pre‑commit install`).
4. **Need clarification?** Add a bullet to `QUESTIONS.md` so the product owner can respond.

If you live with T1D, your real‑world feedback is invaluable—please share how the tool could fit (or already fits) into your routine.

### Code of Conduct

We follow the [Contributor Covenant](CODE_OF_CONDUCT.md) to ensure an inclusive, respectful space.

### Clarifications workflow

If a developer (human or AI) needs more detail from the product owner:

1. Add a bullet point question to `QUESTIONS.md`.
2. The product owner replies beneath the question.
3. Once the answer has been incorporated into docs or code, remove the entry from `QUESTIONS.md`.

---

## Data privacy & ethics

Your health data stays on your machine unless **you** choose to sync a cloud service.  BG Analyzer never sells or shares data.

This project is for **informational purposes only** and does not replace professional medical advice.

---

## License

Released under the MIT License — see [`LICENSE`](LICENSE) for details.
