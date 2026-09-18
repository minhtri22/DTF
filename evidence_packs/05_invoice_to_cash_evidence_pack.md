# Evidence Pack `EVD-I2C-001` — Invoice-to-Cash

> **SIMULATED EXAMPLE** — evidence re-packaged from the v0.1 simulated case solely to test v0.3 Final Candidate traceability.

- Initiative: I2C — Invoice-to-Cash
- Risk: R3 / `RISK-I2C-001`
- Baseline artifact: `BASE-I2C-001`
- Experiment artifact: `EXP-I2C-001`
- Source lineage: `SME-DTF v0.1/processes/05_invoice_to_cash.md`
- Sample/window: 40 B2B customers; 6 tuần.
- Baseline: DSO 48d; overdue >30d 18%; reminder coverage 52%; missing dispute owner 23%.
- Hypothesis/threshold: Overdue >30d giảm >=20% relative.
- Actual result: Overdue 13% (-27,8% relative); reminder 96%; missing owner 2%; cohort DSO -5d.
- Confounds/limitations: Seasonality/customer-mix cohort comparability.
- Verdict: **PASS**
- Reviewer role: Second-assurance traceability test only; no operating-effectiveness conclusion.
- Sign-off status: SIMULATED / NOT APPLICABLE
- Open Condition: `COND-I2C-001`
- Mandatory Control IDs: GOV-001, GOV-002, IAM-001, SOD-001, DAT-001, DAT-002, RES-002, BEN-001

## Re-performance note
A reviewer can trace the baseline/result to the named v0.1 source card and can verify that the v0.3 card preserves the same verdict. Raw transactional data does not exist because the case is simulated; therefore no real-world OE assurance is asserted.
