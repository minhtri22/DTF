#!/usr/bin/env python3
from pathlib import Path
import sys,re,json,csv,subprocess
root=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parents[1]
tests=[]
def T(i,d,ok,e): tests.append({'test_id':i,'description':d,'result':'PASS' if ok else 'FAIL','evidence':e})
def txt(rel):
    p=root/rel; return p.read_text(encoding='utf-8') if p.exists() else ''
# Preserve 6-HIGH regression by invoking inherited RC validator.
proc=subprocess.run([sys.executable,str(root/'tools/validate_release.py'),str(root)],capture_output=True,text=True)
try: reg=json.loads(proc.stdout.strip().splitlines()[-1])
except Exception: reg={'total':0,'passed':0,'failed':1}
T('FC-REG-001','Inherited RC regression remains green',proc.returncode==0 and reg.get('failed')==0,f"validate_release.py => {reg}")
# FV01
G=txt('governance/03_gate_control_matrix.md'); E=txt('governance/11_environment_representativeness_standard.md'); tpl=txt('templates/20_environment_representativeness_statement.md')
for phrase in ['Environment Representativeness Statement','SANDBOX','PRODUCTION-LIKE','production resilience']:
    T('FC-ENV-'+str(len(tests)),phrase+' encoded',phrase.lower() in (G+E+tpl).lower(),'gate/environment standard/template')
# FV02
O=txt('governance/12_oe_sampling_standard.md'); TPL=txt('templates/21_oe_sampling_plan.md'); G4=txt('templates/16_benefits_oe_scale_gate.md')
for phrase in ['before','Population','Period','seed','Rare','Sample selection timestamp']:
    T('FC-OE-'+str(len(tests)),phrase+' sampling field/rule present',phrase.lower() in (O+TPL+G4).lower(),'OE standard/template/G4')
# FV03
F=txt('governance/05_funding_benefits_governance.md'); L=txt('templates/13_funding_benefit_ledger.md')
for phrase in ['MODELED','OBSERVED','BOOKED','realized hard cash','Finance source/reconciliation']:
    T('FC-BEN-'+str(len(tests)),phrase+' benefit rule present',phrase.lower() in (F+L).lower(),'funding-benefits governance + ledger')
# FV04
R=txt('governance/06_resilience_standard.md'); RA=txt('templates/11_resilience_annex.md')
for phrase in ['RTO start event','RTO stop event','unit','dependencies covered','RPO measurement method','Last successful recovery date','Test environment']:
    T('FC-RES-'+str(len(tests)),phrase+' resilience context present',phrase.lower() in (R+RA).lower(),'resilience standard + annex')
# Retrofit evidence across 3 initiatives
for iid in ['CS-R2','AP-R3','WH-R2']:
    base=root/'field_validation_reference'/iid/'evidence'
    env=(base/'environment_representativeness.md').read_text(encoding='utf-8')
    ctx=(base/'rto_rpo_measurement_context.md').read_text(encoding='utf-8')
    plan=(base/'oe_sampling_plan.md').read_text(encoding='utf-8')
    oe=json.loads((base/'oe_reperformance_fc.json').read_text(encoding='utf-8'))
    with open(base/'benefit_evidence_grades.csv',encoding='utf-8-sig') as f: grades=list(csv.DictReader(f))
    T(f'FC-{iid}-ENV','SANDBOX boundary explicit','SANDBOX' in env and 'production resilience NOT validated' in env, str(base/'environment_representativeness.md'))
    T(f'FC-{iid}-CTX','RTO/RPO context complete',all(x in ctx for x in ['RTO start event','RTO stop event','Dependencies covered','transactions lost','component recovery timing only']),str(base/'rto_rpo_measurement_context.md'))
    T(f'FC-{iid}-PLAN','OE plan has seed and pre-selection statement','Reproducible seed' in plan and 'created before FC sample selection' in plan,str(base/'oe_sampling_plan.md'))
    T(f'FC-{iid}-OE','Fresh OE re-performance PASS',oe.get('overall')=='PASS' and all(c.get('pass') for c in oe.get('controls',[])),str(base/'oe_reperformance_fc.json'))
    T(f'FC-{iid}-GRADE','Synthetic benefit grades are MODELED only',len(grades)>0 and all(g['evidence_grade']=='MODELED' for g in grades) and not any(g['evidence_grade']=='BOOKED' for g in grades),str(base/'benefit_evidence_grades.csv'))
# closure register
C=txt('assurance/final_candidate_amendment_closure_register.md')
for f in ['FV-01','FV-02','FV-03','FV-04']:
    T('FC-CLOSE-'+f,f+' closed with boundary',f in C and 'CLOSED' in C,'assurance/final_candidate_amendment_closure_register.md')
summary={'total':len(tests),'passed':sum(x['result']=='PASS' for x in tests),'failed':sum(x['result']=='FAIL' for x in tests),'inherited_regression':reg}
(root/'assurance/final_candidate_test_results.json').write_text(json.dumps({'summary':summary,'tests':tests},ensure_ascii=False,indent=2),encoding='utf-8')
with open(root/'assurance/final_candidate_test_results.csv','w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['test_id','description','result','evidence']);w.writeheader();w.writerows(tests)
print(json.dumps(summary,ensure_ascii=False))
sys.exit(1 if summary['failed'] else 0)
