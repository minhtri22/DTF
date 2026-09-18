# 03 Ticket-to-Resolution — Customer Service

> **SIMULATED EXAMPLE — NOT PRODUCTION EVIDENCE**

- Initiative ID: **T2R**
- Risk tier: **R2** (Risk Artifact: `RISK-T2R-001`, score 8)
- Evidence verdict: **PASS**
- Next gate/action: **G3**
- Process owner: CS Head
- Service/support owner: CS Platform/Knowledge Owner
- Lineage source: `SME-DTF v0.1/processes/03_ticket_to_resolution.md`

## Baseline & hypothesis
- Baseline Evidence ID: `BASE-T2R-001` — First response 42 phút; resolution 11,2h; reopen 6,1%; SLA breach 9%.
- Hypothesis/target: First response giảm >=60%; reopen không tăng >1đ%.
- Experiment/sample/window Evidence ID: `EXP-T2R-001` — 3 agents; 2 tuần.

## Evidence
- Evidence Pack ID: `EVD-T2R-001`
- Result: First response 9 phút (-79%); resolution 6,7h; reopen 6,5%; SLA breach 3%.
- Confound/limitation: Cần segment high-risk intents và KB freshness.

## Control & assurance
- Mandatory/local Control IDs: `GOV-001`, `GOV-002`, `IAM-001`, `DAT-001`, `RES-002`, `CHG-001`, `INC-001`
- Control owner(s): Process Owner + domain/service owners defined above; local mapping required at G3.
- Condition Register: `COND-T2R-001` — privacy + high-risk escalation + KB expiry/owner.
- Condition closure rule: must be CLOSED before blocking gate; evidence/validator required.
- Funding: T0/T1 simulated only; real implementation must record T0–T3 in FUND-BEN ledger.
- Benefit treatment: Capacity release/service-level; CSAT/FCR là quality guardrail.

## Gate decision trace
The simulated verdict is preserved from v0.1. v0.3 Final Candidate does **not** reinterpret FAIL/INCONCLUSIVE as PASS. Production/scale decision requires fresh G3/G4 evidence in a real SME.
