# 08 Order-to-Fulfillment — Sales + Warehouse

> **SIMULATED EXAMPLE — NOT PRODUCTION EVIDENCE**

- Initiative ID: **O2F**
- Risk tier: **R2** (Risk Artifact: `RISK-O2F-001`, score 8)
- Evidence verdict: **FAIL/REVISE**
- Next gate/action: **Remediation then G1**
- Process owner: Warehouse Fulfillment Owner
- Service/support owner: WMS Owner
- Lineage source: `SME-DTF v0.1/processes/08_order_to_fulfillment.md`

## Baseline & hypothesis
- Baseline Evidence ID: `BASE-O2F-001` — Pick 7,4 min/order; mispick 0,8%; 6,2% order wait from stock mismatch.
- Hypothesis/target: Pick time giảm >=20%; mispick increase <=0,2đ%.
- Experiment/sample/window Evidence ID: `EXP-O2F-001` — 1 zone; 1 tuần; 800 orders.

## Evidence
- Evidence Pack ID: `EVD-O2F-001`
- Result: Pick 5,6 min (-24%); mispick 1,4% (+0,6đ%) => guardrail breached.
- Confound/limitation: Location labeling/slotting inconsistency.

## Control & assurance
- Mandatory/local Control IDs: `GOV-001`, `GOV-002`, `DAT-001`, `DAT-002`, `RES-002`, `CHG-001`
- Control owner(s): Process Owner + domain/service owners defined above; local mapping required at G3.
- Condition Register: `COND-O2F-001` — 100% location audit + inventory accuracy/slotting gate before rerun.
- Condition closure rule: must be CLOSED before blocking gate; evidence/validator required.
- Funding: T0/T1 simulated only; real implementation must record T0–T3 in FUND-BEN ledger.
- Benefit treatment: No scale benefit claim while quality guardrail failed.

## Gate decision trace
The simulated verdict is preserved from v0.1. v0.3 Final Candidate does **not** reinterpret FAIL/INCONCLUSIVE as PASS. Production/scale decision requires fresh G3/G4 evidence in a real SME.
