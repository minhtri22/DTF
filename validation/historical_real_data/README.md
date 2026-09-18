# SME-DTF v0.3 FC — Historical Real-Data Gate Test

Gói kiểm thử G0→G4 trên ba nguồn dữ liệu vận hành/thương mại thực đã anonymize:

- **BPI Challenge 2019 — Purchase-to-Pay (R3)**
- **BPI Challenge 2020 — Request for Payment (R3)**
- **Olist Brazilian E-Commerce — Order-to-Delivery (R2)**

Điểm cố ý: đây là **historical real-data replay**, không phải production pilot. Real-world data không làm initiative tự động PASS. G2 phải kiểm evidence validity; G3/G4 phải chặn các claim vượt quá environment/OE/benefit evidence.

## Gate results

| Initiative | G0 | G1 | G2 | G3 | G4 |
|---|---|---|---|---|---|
| BPI19-R3 | DISCOVER | RUN | PASS | REMEDIATE | HOLD / NOT ELIGIBLE |
| BPI20-R3 | DISCOVER | RUN | INCONCLUSIVE | NOT ELIGIBLE / REMEDIATE | HOLD / NOT ELIGIBLE |
| OLIST-R2 | DISCOVER | RUN | PASS (BOUNDED) | REMEDIATE | HOLD / NOT ELIGIBLE |

## Kết luận

**Gate mechanics: EFFECTIVE IN HISTORICAL REAL-DATA TEST.**

- G2 phân biệt được PASS / INCONCLUSIVE / PASS-BOUNDED.
- G3 fail-closed vì historical replay không tương đương production environment.
- G4 không cho historical observation bị diễn giải thành organization-real OE hoặc BOOKED Finance benefit.

Giới hạn còn lại là **controlled real organizational environment**, không phải thiếu thêm public transaction data.

## Data provenance / license

Raw third-party datasets không nên được vendored vào public framework repo. Người dùng nên tải từ nguồn gốc và tuân thủ license:

- BPI Challenge 2019 — CC BY 4.0 — https://figshare.com/articles/dataset/BPI_Challenge_2019/12715853
- BPI Challenge 2020 — CC BY-NC 4.0 — https://figshare.com/articles/dataset/BPI_Challenge_2020_Domestic_Declarations/12692543
- Olist Brazilian E-Commerce — CC BY-NC-SA 4.0 — https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

## Chạy validator

```bash
python tools/validate_historical_gate_test.py
```

Xem:

- `docs/Historical_Real_Data_Gate_Test_Report_VI.md`
- `gate_records/gate_results.csv`

## Claim boundary

Gói này chỉ chứng minh rằng **gate mechanics hoạt động trên historical real-world datasets trong phạm vi đã kiểm**. Nó không chứng minh production readiness, organization-real OE hay realized/booked financial benefits.

## Public package note

Raw/source transaction samples used during the internal run are intentionally omitted from this public package. See `evidence/DATA_NOT_INCLUDED.md`. The included metrics and gate records are for auditability of framework decisions; reproduction requires downloading the original datasets from their publishers.
