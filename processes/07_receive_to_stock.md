# 07 Receive-to-Stock — Warehouse

> **SIMULATED EXAMPLE — NOT PRODUCTION EVIDENCE**

- Initiative ID: **R2S**
- Risk tier: **R2** (Risk Artifact: `RISK-R2S-001`, score 7)
- Evidence verdict: **PASS**
- Next gate/action: **G3**
- Process owner: Warehouse Manager
- Service/support owner: WMS/Device Support Owner
- Lineage source: `SME-DTF v0.1/processes/07_receive_to_stock.md`

## Baseline & hypothesis
- Baseline Evidence ID: `BASE-R2S-001` — Dock-to-stock 190 min; discrepancy 3,8%; late receipt >4h 16%.
- Hypothesis/target: Dock-to-stock giảm >=30%; discrepancy không tăng.
- Experiment/sample/window Evidence ID: `EXP-R2S-001` — 1 receiving door; 2 tuần.

## Evidence
- Evidence Pack ID: `EVD-R2S-001`
- Result: Dock-to-stock 115 min (-39,5%); discrepancy 2,9%; late >4h 3%.
- Confound/limitation: Device/network/label/offline behavior.

## Control & assurance
- Mandatory/local Control IDs: `GOV-001`, `GOV-002`, `DAT-001`, `DAT-002`, `RES-001`, `RES-002`, `RES-003`, `CHG-001`
- Control owner(s): Process Owner + domain/service owners defined above; local mapping required at G3.
- Condition Register: `COND-R2S-001` — offline fallback + device/network support + cycle-count reconciliation.
- Condition closure rule: must be CLOSED before blocking gate; evidence/validator required.
- Funding: T0/T1 simulated only; real implementation must record T0–T3 in FUND-BEN ledger.
- Benefit treatment: Capacity/throughput; inventory quality guardrail.

## Gate decision trace
The simulated verdict is preserved from v0.1. v0.3 Final Candidate does **not** reinterpret FAIL/INCONCLUSIVE as PASS. Production/scale decision requires fresh G3/G4 evidence in a real SME.
