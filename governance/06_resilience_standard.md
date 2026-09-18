# RES-ANNEX-001 — Non-Functional & Resilience Standard

## Bắt buộc cho R2-R4 trước G3
- Business/service criticality và peak operating window.
- Environment Representativeness Statement (`ENV-[INIT]-NNN`) với Environment Class: DEV / SANDBOX / UAT / PRODUCTION-LIKE / PRODUCTION.
- Dependency coverage: identity, network, vendor/API, database, queue, monitoring, backup, integrations; mỗi dependency ghi covered/not covered và deviation.
- **RTO**: target + measured value, unit, start event, stop event, covered dependencies, test environment, last successful recovery date, evidence location.
- **RPO**: target + measured value, unit (time/data/transactions), measurement method, covered data/dependencies, business rationale, test environment, evidence location.
- Peak volume + growth assumption + capacity/load threshold.
- Backup scope/frequency + restore test date/result.
- Cutover rehearsal + rollback trigger + measured rollback time.
- Data migration/interface reconciliation before/after cutover.
- Failure mode: network/service/vendor outage; manual/fallback mode.
- Vendor SLA/OLA, support hours, escalation contact/role.
- Monitoring/alert thresholds and owner.
- Hypercare exit criteria: incident severity/count, adoption, data reconciliation, backlog, response SLA.

## Environment claim rules
- **DEV/SANDBOX:** valid for design mechanics/component tests only; cannot be labelled “production resilience validated”.
- **UAT:** may validate deployment/functionality; resilience claim only for dependencies shown equivalent.
- **PRODUCTION-LIKE:** may support G3 resilience when critical dependencies and load/failure characteristics are materially representative and deviations are accepted.
- **PRODUCTION:** evidence from controlled production/pilot; test safety and rollback authority required.
- R3/R4 measured resilience requires PRODUCTION-LIKE or PRODUCTION for end-to-end claims. A SANDBOX test may remain supporting evidence, not the sole G3 resilience basis.

## Minimum evidence
R2: tabletop/drill acceptable for low criticality only when reversible and environment boundary explicit. R3: measured recovery/rollback on production-like/production critical path required for end-to-end claim. R4: staged rollout + measured recovery + BCP/DR evidence + independent challenge.
