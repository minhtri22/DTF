# RTO-RPO-CS-R2-FC01 — Measurement Context

- Environment: SANDBOX / local single-host SQLite.
- RTO target/measured/unit: 2.0 / 0.000362 / **seconds**.
- RTO start event: immediately before copying local backup database over failed primary.
- RTO stop event: after backup copy completes and application system object reconnects/initializes; record-count validation follows.
- Dependencies covered: local filesystem + SQLite database initialization.
- Dependencies excluded: network, IdP, vendor/API, distributed queue, load balancer, external integrations.
- RPO target/measured/unit: 0 / 0 / **transactions lost**.
- RPO method: compare transaction count immediately before simulated failure with restored database count.
- Business rationale: zero-loss target chosen to stress evidence mechanics; not a real-business SLA.
- Last successful recovery date: 17/09/2026 synthetic field run.
- Recovery evidence: `source/g3_resilience.json` + database copy in this reference folder.
- Assurance boundary: **component recovery timing only; not end-to-end production RTO/RPO.**
