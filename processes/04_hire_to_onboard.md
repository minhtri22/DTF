# 04 Hire-to-Onboard — HR

> **SIMULATED EXAMPLE — NOT PRODUCTION EVIDENCE**

- Initiative ID: **H2O**
- Risk tier: **R3** (Risk Artifact: `RISK-H2O-001`, score 11)
- Evidence verdict: **PASS CÓ ĐIỀU KIỆN**
- Next gate/action: **G3**
- Process owner: HR/Recruitment Head
- Service/support owner: HRIS/Recruiting Ops
- Lineage source: `SME-DTF v0.1/processes/04_hire_to_onboard.md`

## Baseline & hypothesis
- Baseline Evidence ID: `BASE-H2O-001` — First screen 3,2 ngày; missing info 21%; onboarding on-time 68%.
- Hypothesis/target: Giảm first-screen >=50%, không bỏ ứng viên đạt mandatory criteria.
- Experiment/sample/window Evidence ID: `EXP-H2O-001` — 2 vị trí; 60 CV; recruiter review 100%.

## Evidence
- Evidence Pack ID: `EVD-H2O-001`
- Result: First screen 1,1 ngày (-66%); missing 6%; không có auto-reject.
- Confound/limitation: Fairness/privacy/retention cần production controls.

## Control & assurance
- Mandatory/local Control IDs: `GOV-001`, `GOV-002`, `IAM-001`, `PRV-001`, `DAT-001`, `CHG-001`, `RES-002`
- Control owner(s): Process Owner + domain/service owners defined above; local mapping required at G3.
- Condition Register: `COND-H2O-001` — assist-only authority + privacy/fairness/retention controls.
- Condition closure rule: must be CLOSED before blocking gate; evidence/validator required.
- Funding: T0/T1 simulated only; real implementation must record T0–T3 in FUND-BEN ledger.
- Benefit treatment: Capacity release + candidate/manager experience; không claim hiring quality nếu chưa đo.

## Gate decision trace
The simulated verdict is preserved from v0.1. v0.3 Final Candidate does **not** reinterpret FAIL/INCONCLUSIVE as PASS. Production/scale decision requires fresh G3/G4 evidence in a real SME.
