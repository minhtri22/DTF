# Source Register — Historical Real-Data Gate Test

| Dataset | Authoritative source | Convenience/reproducibility source used | Status |
|---|---|---|---|
| BPI Challenge 2019 | DOI: 10.4121/uuid:d06aff4b-79f0-45e6-8ec8-e19730c248f1 | ProcessLens derived artifacts from full log | Real operational event log; full-dataset aggregate evidence |
| BPI Challenge 2020 — Request for Payment | DOI: 10.4121/uuid:895b26fb-6f25-46eb-9e48-0dca26fcd030 | bptlab/bpi-challenge-2020 + XES mirror | Real operational event log; raw trace sample inspected; population not locally reprocessed |
| Olist Brazilian E-Commerce | Kaggle `olistbr/brazilian-ecommerce` | Public GitHub mirror of orders CSV | Real anonymized commercial orders; bounded raw-row sample inspected |

## Claim boundary
- Public historical data is **real-world data**, but the original production ERP/workflow/marketplace, IAM, network, people and support model are unavailable.
- Therefore environment class for this exercise is **SANDBOX / HISTORICAL REPLAY**.
- G3 cannot claim production resilience; G4 cannot claim organization-real OE or BOOKED benefit.
- Mirrors are processing conveniences, not authoritative substitutes. Dataset identity/provenance is anchored to the authoritative sources above.
