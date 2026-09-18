# 10 Request-to-Approval — HR + Finance + Admin + Management

> **SIMULATED EXAMPLE — NOT PRODUCTION EVIDENCE**

- Initiative ID: **R2A**
- Risk tier: **R3** (Risk Artifact: `RISK-R2A-001`, score 9)
- Evidence verdict: **PASS**
- Next gate/action: **G3**
- Process owner: Cross-functional Approval Process Owner
- Service/support owner: Workflow Platform Owner
- Lineage source: `SME-DTF v0.1/processes/10_request_to_approval.md`

## Baseline & hypothesis
- Baseline Evidence ID: `BASE-R2A-001` — Cycle 3,4d; missing info 21%; status-chasing 17%.
- Hypothesis/target: Cycle giảm >=40%; missing <8%.
- Experiment/sample/window Evidence ID: `EXP-R2A-001` — 3 request types; 3 tuần.

## Evidence
- Evidence Pack ID: `EVD-R2A-001`
- Result: Cycle 1,2d (-65%); missing 4%; status-chasing 3%; 2 routing errors caught by log.
- Confound/limitation: Approval matrix correctness and policy bypass.

## Control & assurance
- Mandatory/local Control IDs: `GOV-001`, `GOV-002`, `IAM-001`, `APR-001`, `SOD-001`, `DAT-001`, `RES-002`, `CHG-001`
- Control owner(s): Process Owner + domain/service owners defined above; local mapping required at G3.
- Condition Register: `COND-R2A-001` — validate authority matrix + SoD + bypass monitoring.
- Condition closure rule: must be CLOSED before blocking gate; evidence/validator required.
- Funding: T0/T1 simulated only; real implementation must record T0–T3 in FUND-BEN ledger.
- Benefit treatment: Capacity release; control quality must not degrade.

## Gate decision trace
The simulated verdict is preserved from v0.1. v0.3 Final Candidate does **not** reinterpret FAIL/INCONCLUSIVE as PASS. Production/scale decision requires fresh G3/G4 evidence in a real SME.
