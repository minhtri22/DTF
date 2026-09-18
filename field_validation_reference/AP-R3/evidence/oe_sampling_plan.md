# OEPLAN-AP-R3-FC01 — OE Sampling Plan

- Initiative: AP-R3
- Plan approval timestamp: **2026-09-17T10:45:00+07:00** (retrofit validation plan; created before FC sample selection)
- Population: `source/transactions_90d.csv`; size **2700**; synthetic 90-day population.
- Period under review: full synthetic 90-day run.
- Sampling unit: one transaction.
- Method: **stratified: 15 duplicate + 30 high-value + 45 other random**.
- Reproducible seed: **94032**.
- Target sample size: **90**.
- Rare/adverse requirement: Minimum 15 duplicate invoices + 30 high-value (>50m VND where available); remainder other transactions.
- Exclusions: no transaction removed because of control result; groups deduplicated by transaction ID.
- Evidence source: source transaction CSV + executable SQLite audit database.
- Reviewer: Final Candidate retrofit assurance.
- Sample selection timestamp: **after plan write in FC build run**.
