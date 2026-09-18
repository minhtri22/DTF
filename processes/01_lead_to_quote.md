# 01 Lead-to-Quote — Sales

> **SIMULATED EXAMPLE — NOT PRODUCTION EVIDENCE**

- Initiative ID: **L2Q**
- Risk tier: **R2** (Risk Artifact: `RISK-L2Q-001`, score 7)
- Evidence verdict: **PASS**
- Next gate/action: **G3**
- Process owner: Sales Manager / Quote Process Owner
- Service/support owner: Sales Operations / CRM owner
- Lineage source: `SME-DTF v0.1/processes/01_lead_to_quote.md`

## Baseline & hypothesis
- Baseline Evidence ID: `BASE-L2Q-001` — Quote time median 95 phút; rework 7,8%; internal clarification 38%.
- Hypothesis/target: Giảm quote time >=50% và rework <=4%.
- Experiment/sample/window Evidence ID: `EXP-L2Q-001` — 2 tuần; 5 sales.

## Evidence
- Evidence Pack ID: `EVD-L2Q-001`
- Result: Median 28 phút (-70,5%); rework 2,1%; clarification 14%.
- Confound/limitation: Pilot nhỏ; cần theo dõi margin/win-rate khi production.

## Control & assurance
- Mandatory/local Control IDs: `GOV-001`, `GOV-002`, `APR-001`, `DAT-001`, `RES-002`, `CHG-001`
- Control owner(s): Process Owner + domain/service owners defined above; local mapping required at G3.
- Condition Register: `COND-L2Q-001` — khóa margin floor/discount authority + adoption threshold trước G3.
- Condition closure rule: must be CLOSED before blocking gate; evidence/validator required.
- Funding: T0/T1 simulated only; real implementation must record T0–T3 in FUND-BEN ledger.
- Benefit treatment: Capacity release; không monetize nếu không có reuse action.

## Gate decision trace
The simulated verdict is preserved from v0.1. v0.3 Final Candidate does **not** reinterpret FAIL/INCONCLUSIVE as PASS. Production/scale decision requires fresh G3/G4 evidence in a real SME.
