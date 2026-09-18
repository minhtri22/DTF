# OEPLAN-WH-R2-FC01 — OE Sampling Plan

- Initiative: WH-R2
- Plan approval timestamp: **2026-09-17T10:45:00+07:00** (retrofit validation plan; created before FC sample selection)
- Population: `source/transactions_90d.csv`; size **8100**; synthetic 90-day population.
- Period under review: full synthetic 90-day run.
- Sampling unit: one transaction.
- Method: **stratified: 20 invalid + 20 bypass + 40 clean**.
- Reproducible seed: **84033**.
- Target sample size: **80**.
- Rare/adverse requirement: Minimum 20 truth_bad + 20 bypass transactions; remainder clean transactions.
- Exclusions: no transaction removed because of control result; groups deduplicated by transaction ID.
- Evidence source: source transaction CSV + executable SQLite audit database.
- Reviewer: Final Candidate retrofit assurance.
- Sample selection timestamp: **after plan write in FC build run**.
