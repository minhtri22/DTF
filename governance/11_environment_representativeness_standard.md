# ENV-STD-001 — Environment Representativeness Standard

## Purpose
Ngăn việc ngoại suy kết quả DEV/SANDBOX thành production assurance.

## Mandatory statement fields
- Initiative ID / Environment Statement ID.
- Environment Class: DEV / SANDBOX / UAT / PRODUCTION-LIKE / PRODUCTION.
- Workload/data representativeness.
- Dependency matrix: identity, network, vendor/API, database, queue, monitoring, backup, integrations.
- Security/IAM equivalence.
- Failure-mode coverage.
- Known deviations and expected impact.
- Conclusion: representative for what / not representative for what.
- Owner + IT/Risk challenge + date.

## Claim boundary
A resilience result inherits the weakest material dependency in scope. If a critical production dependency is absent, the result must be described as component/sandbox evidence rather than production resilience validation.
