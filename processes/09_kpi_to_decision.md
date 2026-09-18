# 09 KPI-to-Decision — Management

> **SIMULATED EXAMPLE — NOT PRODUCTION EVIDENCE**

- Initiative ID: **K2D**
- Risk tier: **R1** (Risk Artifact: `RISK-K2D-001`, score 3)
- Evidence verdict: **PASS**
- Next gate/action: **G3/Institutionalize**
- Process owner: Management Operating Review Owner
- Service/support owner: BI/Data Reporting Owner
- Lineage source: `SME-DTF v0.1/processes/09_kpi_to_decision.md`

## Baseline & hypothesis
- Baseline Evidence ID: `BASE-K2D-001` — Weekly pack 2,5d; 34% KPI reconcile; action owner+deadline 62%.
- Hypothesis/target: Prep <1 day; action ownership >=90%.
- Experiment/sample/window Evidence ID: `EXP-K2D-001` — 4 tuần; 12 core KPIs.

## Evidence
- Evidence Pack ID: `EVD-K2D-001`
- Result: Prep 4h; reconcile 6%; action owner+deadline 94%; meeting time -30%.
- Confound/limitation: Metric definition drift/cherry-picking.

## Control & assurance
- Mandatory/local Control IDs: `GOV-001`, `GOV-002`, `DAT-001`, `CHG-001`, `RES-002`
- Control owner(s): Process Owner + domain/service owners defined above; local mapping required at G3.
- Condition Register: `COND-K2D-001` — metric dictionary version ownership + cutoff/SLA.
- Condition closure rule: must be CLOSED before blocking gate; evidence/validator required.
- Funding: T0/T1 simulated only; real implementation must record T0–T3 in FUND-BEN ledger.
- Benefit treatment: Capacity release + decision effectiveness; avoid claiming causal revenue uplift.

## Gate decision trace
The simulated verdict is preserved from v0.1. v0.3 Final Candidate does **not** reinterpret FAIL/INCONCLUSIVE as PASS. Production/scale decision requires fresh G3/G4 evidence in a real SME.
