# SME-DTF v0.3 Final Candidate — Historical Real-Data Gate Test

**Ngày:** 17/09/2026  
**Phạm vi:** 3 dataset vận hành/thương mại thực đã anonymize; historical replay, không phải production pilot.  
**Framework baseline:** SME-DTF v0.3 Final Candidate; regression trước test: 60/60 + 42/42 PASS.

## 1. Mục tiêu
Kiểm tra liệu G0–G4 có phân biệt được: (a) dữ liệu thực nhưng bằng chứng đủ/thiếu, (b) evidence PASS nhưng environment chưa đủ production, và (c) historical benefit khác BOOKED benefit hay không.

## 2. Kết quả gate
| Initiative | Risk | G0 | G1 | G2 | G3 | G4 |
|---|---|---|---|---|---|---|
| BPI19-R3 | R3 | DISCOVER | RUN | PASS | REMEDIATE | HOLD / NOT ELIGIBLE |
| BPI20-R3 | R3 | DISCOVER | RUN | INCONCLUSIVE | NOT ELIGIBLE / REMEDIATE | HOLD / NOT ELIGIBLE |
| OLIST-R2 | R2 | DISCOVER | RUN | PASS (BOUNDED) | REMEDIATE | HOLD / NOT ELIGIBLE |

## 3. Phát hiện chính
### BPI19-R3 — gate cho phép evidence nhưng chặn production
Toàn bộ artifact full-dataset cho thấy 1.595.923 events / 251.734 cases. Payment-block cohort có median cycle 85,1 ngày so với overall 64,0 ngày (+21,1 ngày); repeat-invoice chiếm 3,83% và median 104,8 ngày. Hypothesis diagnostic đạt, nên G2 PASS. Tuy nhiên G3 REMEDIATE vì chỉ có historical data/derived artifacts, không có ERP/IAM/network/support/dependency equivalence của môi trường gốc.

### BPI20-R3 — gate chặn ngay tại evidence validity
Raw trace thật cho thấy rejection/resubmission và cycle-time variance. Sample tiện lợi n=3 cho delta median rework-vs-straight khoảng 31.50 ngày, nhưng đây không phải probability sample được predeclare và full 36.796-event log chưa được reprocess độc lập trong runtime này. Vì vậy G2 = INCONCLUSIVE. Đây là kết quả đúng của fail-closed evidence gate.

### OLIST-R2 — PASS có claim boundary
Mẫu raw-order thật n=12 parse được 100%; phát hiện 2 giao hàng sau estimated date. G2 chỉ PASS cho claim hẹp “exception tồn tại và có thể detect deterministically”, không PASS cho prevalence/causality. G3 vẫn REMEDIATE vì thiếu marketplace/carrier/seller production dependencies.

## 4. Test chính các gate
1. **G0 không auto-reject historical public data:** cho phép discovery khi scope/claim boundary rõ.
2. **G1 cho phép experiment read-only/reversible:** không cần production system để chạy diagnostic.
3. **G2 phân hóa:** BPI19 PASS, BPI20 INCONCLUSIVE, Olist PASS-BOUNDED. Dataset “thật” không làm bằng chứng tự động đủ mạnh.
4. **G3 fail-closed:** 3/3 bị chặn khỏi production claim vì Environment Class chỉ là SANDBOX/HISTORICAL REPLAY.
5. **G4 fail-closed:** 3/3 không được Scale vì không có G3 Deploy, organization-real OE, 30/60/90 intervention và BOOKED Finance benefit.

## 5. Kết luận assurance
**Gate mechanics: EFFECTIVE IN HISTORICAL REAL-DATA TEST.** Không có dấu hiệu rubber-stamp: G2 tạo verdict khác nhau, G3 chặn cả hai case G2-PASS, và G4 không cho historical observation bị diễn giải thành realized production benefit.

**External-validity uplift:** từ synthetic-only lên historical real-world operational/commercial evidence.  
**Giới hạn còn lại:** chưa test organization-real operating effectiveness; chưa có production-like/production environment của chính doanh nghiệp; chưa có Process Owner/Finance authority thật; benefit tối đa OBSERVED/MODELED, không BOOKED.

## 6. Quyết định framework
Không có bằng chứng buộc phải thay backbone F0–F10/G0–G4. Kết quả ngược lại cho thấy các rule mới của Final Candidate đang làm đúng nhiệm vụ: **evidence gate chặn overclaim, environment gate chặn production overclaim, benefit gate chặn financial overclaim.**

Bước còn thiếu để chuyển v0.3 Final là controlled real pilot. Historical public datasets không thể thay thế G3/G4 trong tổ chức thật.
