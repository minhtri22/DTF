# Evidence Pack `EVD-O2F-001` — Order-to-Fulfillment

> **SIMULATED EXAMPLE** — evidence re-packaged from the v0.1 simulated case solely to test v0.3 Final Candidate traceability.

- Initiative: O2F — Order-to-Fulfillment
- Risk: R2 / `RISK-O2F-001`
- Baseline artifact: `BASE-O2F-001`
- Experiment artifact: `EXP-O2F-001`
- Source lineage: `SME-DTF v0.1/processes/08_order_to_fulfillment.md`
- Sample/window: 1 zone; 1 tuần; 800 orders.
- Baseline: Pick 7,4 min/order; mispick 0,8%; 6,2% order wait from stock mismatch.
- Hypothesis/threshold: Pick time giảm >=20%; mispick increase <=0,2đ%.
- Actual result: Pick 5,6 min (-24%); mispick 1,4% (+0,6đ%) => guardrail breached.
- Confounds/limitations: Location labeling/slotting inconsistency.
- Verdict: **FAIL/REVISE**
- Reviewer role: Second-assurance traceability test only; no operating-effectiveness conclusion.
- Sign-off status: SIMULATED / NOT APPLICABLE
- Open Condition: `COND-O2F-001`
- Mandatory Control IDs: GOV-001, GOV-002, DAT-001, DAT-002, RES-002, CHG-001

## Re-performance note
A reviewer can trace the baseline/result to the named v0.1 source card and can verify that the v0.3 card preserves the same verdict. Raw transactional data does not exist because the case is simulated; therefore no real-world OE assurance is asserted.
