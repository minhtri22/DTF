# Evidence Pack `EVD-P2P-001` — Procure-to-Pay

> **SIMULATED EXAMPLE** — evidence re-packaged from the v0.1 simulated case solely to test v0.3 Final Candidate traceability.

- Initiative: P2P — Procure-to-Pay
- Risk: R3 / `RISK-P2P-001`
- Baseline artifact: `BASE-P2P-001`
- Experiment artifact: `EXP-P2P-001`
- Source lineage: `SME-DTF v0.1/processes/06_procure_to_pay.md`
- Sample/window: Replay 300 historical invoices; no live payment.
- Baseline: Manual match 14 min/invoice; mismatch 11%; suspected supplier duplicate 8%.
- Hypothesis/threshold: >85% auto-match; exception <3%.
- Actual result: Auto-match 63%; exception 14%; duplicate supplier/tax/unit defects found.
- Confounds/limitations: Master-data defects invalidate automation premise.
- Verdict: **FAIL**
- Reviewer role: Second-assurance traceability test only; no operating-effectiveness conclusion.
- Sign-off status: SIMULATED / NOT APPLICABLE
- Open Condition: `COND-P2P-001`
- Mandatory Control IDs: GOV-001, GOV-002, IAM-001, APR-001, SOD-001, DAT-001, DAT-002, RES-002

## Re-performance note
A reviewer can trace the baseline/result to the named v0.1 source card and can verify that the v0.3 card preserves the same verdict. Raw transactional data does not exist because the case is simulated; therefore no real-world OE assurance is asserted.
