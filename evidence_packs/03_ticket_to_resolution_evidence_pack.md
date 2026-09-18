# Evidence Pack `EVD-T2R-001` — Ticket-to-Resolution

> **SIMULATED EXAMPLE** — evidence re-packaged from the v0.1 simulated case solely to test v0.3 Final Candidate traceability.

- Initiative: T2R — Ticket-to-Resolution
- Risk: R2 / `RISK-T2R-001`
- Baseline artifact: `BASE-T2R-001`
- Experiment artifact: `EXP-T2R-001`
- Source lineage: `SME-DTF v0.1/processes/03_ticket_to_resolution.md`
- Sample/window: 3 agents; 2 tuần.
- Baseline: First response 42 phút; resolution 11,2h; reopen 6,1%; SLA breach 9%.
- Hypothesis/threshold: First response giảm >=60%; reopen không tăng >1đ%.
- Actual result: First response 9 phút (-79%); resolution 6,7h; reopen 6,5%; SLA breach 3%.
- Confounds/limitations: Cần segment high-risk intents và KB freshness.
- Verdict: **PASS**
- Reviewer role: Second-assurance traceability test only; no operating-effectiveness conclusion.
- Sign-off status: SIMULATED / NOT APPLICABLE
- Open Condition: `COND-T2R-001`
- Mandatory Control IDs: GOV-001, GOV-002, IAM-001, DAT-001, RES-002, CHG-001, INC-001

## Re-performance note
A reviewer can trace the baseline/result to the named v0.1 source card and can verify that the v0.3 card preserves the same verdict. Raw transactional data does not exist because the case is simulated; therefore no real-world OE assurance is asserted.
