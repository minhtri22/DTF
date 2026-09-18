# SME Digital Transformation Framework v0.3 Final Candidate (0.3-FC1)

SME-DTF là operating framework cho chuyển đổi số SME theo chuỗi Strategy & Portfolio → Initiative Lifecycle → Operate & Benefits, với backbone F0–F10 / G0–G4 và nguyên tắc assurance-by-design.

> Status: Final Candidate — ready for controlled real pilot.
> Not claimed: production-validated, organization-real Operating Effectiveness (OE), certification, hoặc BOOKED business benefits trong một doanh nghiệp thật.

## Validation ladder

Design / Artifact QA
→ Executable Synthetic Field
→ Historical Real-World Data (completed)
→ Controlled Real Pilot (next required transition)
→ Organization-Real OE + BOOKED Benefits
→ v0.3 Final consideration

## Validation status

SME-DTF v0.3 Final Candidate đã đi qua:

1. Independent design/artifact QA — 6 HIGH findings đã được remediation và CLOSED ở design/artifact level.
2. Executable synthetic-field validation — 3 initiatives (R2/R3), có DE/resilience/OE samples và gate decisions khác nhau.
3. Final Candidate hardening — 4 MEDIUM findings đã trở thành executable controls:
   - Environment Representativeness;
   - predeclared OE Sampling Plan;
   - Benefit Evidence Grade MODELED / OBSERVED / BOOKED;
   - RTO/RPO Measurement Context.
4. Historical real-world data gate validation — stress-test G0→G4 trên 3 nguồn real-world anonymized datasets.
5. Controlled real pilot — chưa thực hiện; đây là bước chuyển pha còn thiếu.

### Test regression snapshot

- Previous RC regression: 60/60 PASS
- Final Candidate amendment/retrofit suite: 42/42 PASS
- Historical real-data gate suite: 14/14 PASS
- Organization-real OE: NOT TESTED

## Historical real-world datasets đã kiểm thử

| Initiative | Dataset | Risk | G2 Evidence | G3 Production | G4 Scale |
|---|---|---:|---|---|---|
| Purchase-to-Pay payment-block / repeat-invoice | BPI Challenge 2019 | R3 | PASS | REMEDIATE | HOLD / NOT ELIGIBLE |
| Request for Payment approval/rework | BPI Challenge 2020 | R3 | INCONCLUSIVE | NOT ELIGIBLE / REMEDIATE | HOLD / NOT ELIGIBLE |
| Order-to-Delivery exception detection | Olist Brazilian E-Commerce | R2 | PASS — bounded claim | REMEDIATE | HOLD / NOT ELIGIBLE |

Kết quả này là chủ ý của framework: real dataset không đồng nghĩa auto-PASS.

- G2 kiểm evidence sufficiency/validity.
- G3 kiểm production/environment readiness.
- G4 kiểm organization-real OE, realized benefit và scale eligibility.

Chi tiết: validation/historical_real_data/

## Claim boundary — bắt buộc đọc trước khi sử dụng/public

SME-DTF được phép tuyên bố:

Framework đã được QA độc lập ở mức design/artifact, kiểm thử trên executable synthetic-field environment, và stress-test gate mechanics trên nhiều historical real-world operational/commercial datasets độc lập.

SME-DTF không được phép tuyên bố:

- đã production-validated trong một SME thật;
- đã chứng minh organization-real operating effectiveness;
- G3 production resilience đã được xác nhận trên ERP/CRM/WMS/network/IAM thật;
- benefit đã được Finance của doanh nghiệp xác nhận ở mức BOOKED;
- framework đã đạt certification/compliance với một chuẩn bên ngoài;
- historical replay đại diện trực tiếp cho mọi SME hoặc mọi ngành.

## Vì sao public dataset chưa thể vượt G3/G4

Historical datasets có transaction/event thật nhưng không cung cấp đầy đủ:

- Process Owner, Finance authority và người dùng thật;
- ERP/CRM/WMS cùng configuration thật;
- IAM, network, integrations và vendor dependencies;
- support/on-call, backup/restore, incident/change process;
- adoption, bypass, workaround dưới áp lực vận hành thật;
- 30/60/90 post-intervention observation;
- Finance evidence ở mức BOOKED.

Vì vậy giới hạn hiện tại là môi trường tổ chức thử nghiệm, không phải một kết luận FAIL của framework.

## Dataset provenance & licensing

Repo này không vendor raw copies của third-party datasets. Reproduction yêu cầu tải dữ liệu trực tiếp từ publisher và tuân thủ license hiện hành tại nguồn.

| Dataset | Source | License tại nguồn | Public-repo note |
|---|---|---|---|
| BPI Challenge 2019 | https://figshare.com/articles/dataset/BPI_Challenge_2019/12715853 | CC BY 4.0 | Attribution required |
| BPI Challenge 2020 | https://figshare.com/articles/dataset/BPI_Challenge_2020_Domestic_Declarations/12692543 | CC BY-NC 4.0 | Non-Commercial |
| Olist Brazilian E-Commerce | https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce | CC BY-NC-SA 4.0 | Non-Commercial + ShareAlike |

Đây là release/provenance guidance, không phải tư vấn pháp lý. Luôn kiểm tra license hiện hành tại nguồn trước khi redistributing hoặc dùng dữ liệu/derivative artifacts trong commercial distribution.

## Repository structure

- docs/ — Core specification, Final Candidate report, Controlled Real Pilot Readiness.
- governance/ — gate, risk, control, funding/benefit, resilience, environment và OE sampling standards.
- templates/ — 22 executable governance/assurance templates.
- processes/ — 10 SIMULATED EXAMPLE process cards.
- evidence_packs/ — simulated evidence packs để test traceability.
- field_validation_reference/ — public-safe synthetic-field control/evidence artifacts; SQLite và 90-day raw transaction dumps intentionally omitted.
- validation/historical_real_data/ — public historical real-data gate test; không chứa raw third-party datasets.
- assurance/ — closure registers, artifact/evidence traceability và Final Candidate assurance report.
- tools/ — release validators.

## Backbone

Lifecycle F0–F10:
F0 Strategic Mandate; F1 Context & Value; F2 AS-IS, Baseline & Data Readiness; F3 Priority & Business Case; F4 Hypothesis & Metric Stack; F5 Minimum Experiment; F6 Evidence Gate; F7 TO-BE & Control Design; F8 Production & Change Readiness; F9 Deploy & Hypercare; F10 Operate, Benefits & Scale.

Gates G0–G4:
G0 Portfolio Entry; G1 Experiment Ready; G2 Evidence; G3 Production Ready; G4 Benefits & Scale.

Canonical rules: governance/03_gate_control_matrix.md

## Four Final Candidate hardening rules

1. Environment Representativeness: G3 phân loại DEV / SANDBOX / UAT / PRODUCTION-LIKE / PRODUCTION. SANDBOX không được gọi là production-resilience validated.
2. OE Sampling Plan: G4 bắt buộc plan tồn tại và approved trước sample selection, có population / period / method / seed-query / rare-adverse rules.
3. Benefit Evidence Grade: MODELED / OBSERVED / BOOKED. Chỉ BOOKED + Hard Cash taxonomy mới có thể được gọi realized hard cash.
4. RTO/RPO Context: mọi resilience measurement phải ghi unit, start/stop points, dependency scope, environment và recovery evidence.

## Run validators

Main framework regression:
python tools/validate_release.py .
python tools/validate_final_candidate.py .

Historical gate test:
python validation/historical_real_data/tools/validate_historical_gate_test.py

Public-source repo intentionally omits large/raw synthetic populations và SQLite DBs. Một số local retrofit/re-performance step cần full controlled validation package thay vì GitHub snapshot.

## Điều kiện để xét Final Candidate → v0.3 Final

Ít nhất một controlled real pilot, ưu tiên có >=1 R2 + >=1 R3, phải đi full G0→G4 với:

- environment phù hợp risk; R3 end-to-end resilience cần PRODUCTION-LIKE hoặc PRODUCTION critical path;
- DE + resilience evidence có thể re-perform;
- OE Sampling Plan predeclared trên transaction population thật;
- Process Owner / Service Owner / users thật;
- 30/60/90 post-intervention observation;
- Finance validation; mọi realized hard-cash claim phải đạt BOOKED;
- independent field assurance xác nhận gate decisions và không có HIGH finding mở.

Cho đến khi các điều kiện này xảy ra, tên đúng của release vẫn là SME-DTF v0.3 Final Candidate.
