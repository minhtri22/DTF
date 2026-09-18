# OEPLAN-CS-R2-FC01 — OE Sampling Plan

- Initiative: CS-R2
- Plan approval timestamp: **2026-09-17T10:45:00+07:00** (retrofit validation plan; created before FC sample selection)
- Population: `source/transactions_90d.csv`; size **2520**; synthetic 90-day population.
- Period under review: full synthetic 90-day run.
- Sampling unit: one transaction.
- Method: **stratified: 10 high-risk + 50 non-high random**.
- Reproducible seed: **74031**.
- Target sample size: **60**.
- Rare/adverse requirement: Minimum 10 high-risk tickets; remainder random non-high-risk.
- Exclusions: no transaction removed because of control result; groups deduplicated by transaction ID.
- Evidence source: source transaction CSV + executable SQLite audit database.
- Reviewer: Final Candidate retrofit assurance.
- Sample selection timestamp: **after plan write in FC build run**.
