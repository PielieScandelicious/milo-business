<div align="center">

# **MILO**
## GDPR Risk Assessment v2.0

---

**DeepmAInd B.V.** | January 28, 2026

</div>

---

## Risk Overview

| Risk Category | Count | Max Financial Impact |
|:--------------|:-----:|---------------------:|
| 🔴 Critical | 5 | €144,000 |
| 🟡 High | 6 | €72,000 |
| 🟠 Medium | 4 | €36,000 |
| 🟢 Low | 3 | €18,000 |

---

## Financial Exposure Framework

### GDPR Fine Calculation

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                       FINE CALCULATION BASIS                                  ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   MILO Y3 Projected Revenue: $2.4M (~€2.2M)                                  ║
║                                                                               ║
║   ARTICLE 83(5) VIOLATIONS (Higher Tier):                                    ║
║   Maximum: €20M or 4% of annual turnover                                     ║
║   For MILO: max(€20M, 4% × €2.2M) = €88K                                    ║
║                                                                               ║
║   Applies to:                                                                 ║
║   • Art. 5: Data processing principles                                       ║
║   • Art. 6: Lawfulness of processing                                         ║
║   • Art. 7: Conditions for consent                                           ║
║   • Art. 9: Special categories                                               ║
║   • Art. 44-49: International transfers                                      ║
║                                                                               ║
║   ARTICLE 83(4) VIOLATIONS (Lower Tier):                                     ║
║   Maximum: €10M or 2% of annual turnover                                     ║
║   For MILO: max(€10M, 2% × €2.2M) = €44K                                    ║
║                                                                               ║
║   Applies to:                                                                 ║
║   • Art. 28: Processor agreements                                            ║
║   • Art. 33-34: Breach notification                                          ║
║   • Art. 35-36: DPIAs                                                        ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

## Critical Risks (🔴)

### Risk 1: No Legal Basis for Processing

| Attribute | Assessment |
|:----------|:-----------|
| **GDPR Article** | Art. 6 |
| **Current State** | Legal basis undocumented |
| **Likelihood** | Certain (if audited) |
| **Impact** | All processing potentially unlawful |
| **Max Fine** | €88,000 |
| **Mitigation** | Document legal basis per activity |
| **Cost to Fix** | €3,000 |
| **Timeline** | Week 1-2 |

---

### Risk 2: Health Data Without Explicit Consent

| Attribute | Assessment |
|:----------|:-----------|
| **GDPR Article** | Art. 9 |
| **Current State** | No Art. 9 consent mechanism |
| **Likelihood** | Certain |
| **Impact** | Health scoring unlawful |
| **Max Fine** | €88,000 |
| **Mitigation** | Implement explicit consent |
| **Cost to Fix** | €10,000 |
| **Timeline** | Week 3-4 |

---

### Risk 3: Illegal International Transfers

| Attribute | Assessment |
|:----------|:-----------|
| **GDPR Article** | Art. 44-49 |
| **Current State** | No SCCs with US processors |
| **Likelihood** | Certain |
| **Impact** | All US processing unlawful |
| **Max Fine** | €88,000 |
| **Mitigation** | Execute SCCs, verify DPF |
| **Cost to Fix** | €8,000 |
| **Timeline** | Week 2-3 |

---

### Risk 4: Missing Data Processing Agreements

| Attribute | Assessment |
|:----------|:-----------|
| **GDPR Article** | Art. 28 |
| **Current State** | 0/5 DPAs executed |
| **Likelihood** | Certain |
| **Impact** | Joint liability with processors |
| **Max Fine** | €44,000 |
| **Mitigation** | Execute DPAs with all processors |
| **Cost to Fix** | €16,000 |
| **Timeline** | Week 2-3 |

---

### Risk 5: No Privacy Policy

| Attribute | Assessment |
|:----------|:-----------|
| **GDPR Article** | Art. 13, 14 |
| **Current State** | No privacy policy exists |
| **Likelihood** | Certain |
| **Impact** | Cannot lawfully collect data |
| **Max Fine** | €88,000 |
| **Mitigation** | Draft and publish privacy policy |
| **Cost to Fix** | €8,000 |
| **Timeline** | Week 1-2 |

---

## High Risks (🟡)

### Risk 6: No Data Subject Rights Portal

| Attribute | Assessment |
|:----------|:-----------|
| **GDPR Article** | Art. 15-22 |
| **Impact** | Cannot fulfill rights requests |
| **Max Fine** | €44,000 |
| **Mitigation** | Build rights portal |
| **Cost to Fix** | €15,000 |
| **Timeline** | Week 5-6 |

---

### Risk 7: No DPIA for AI Processing

| Attribute | Assessment |
|:----------|:-----------|
| **GDPR Article** | Art. 35 |
| **Impact** | Regulatory violation |
| **Max Fine** | €44,000 |
| **Mitigation** | Complete DPIA |
| **Cost to Fix** | €8,000 |
| **Timeline** | Week 9-10 |

---

### Risk 8: No DPIA for Data Monetization

| Attribute | Assessment |
|:----------|:-----------|
| **GDPR Article** | Art. 35 |
| **Impact** | Cannot monetize data |
| **Max Fine** | €44,000 |
| **Mitigation** | Complete DPIA |
| **Cost to Fix** | €4,000 |
| **Timeline** | Week 9-10 |

---

### Risk 9: No Incident Response Plan

| Attribute | Assessment |
|:----------|:-----------|
| **GDPR Article** | Art. 33, 34 |
| **Impact** | Cannot respond to breach |
| **Max Fine** | €44,000 |
| **Mitigation** | Document procedures |
| **Cost to Fix** | €3,000 |
| **Timeline** | Week 11 |

---

### Risk 10: Undefined Data Retention

| Attribute | Assessment |
|:----------|:-----------|
| **GDPR Article** | Art. 5(1)(e) |
| **Impact** | Storage limitation violation |
| **Max Fine** | €88,000 |
| **Mitigation** | Define retention periods |
| **Cost to Fix** | €2,000 |
| **Timeline** | Week 3 |

---

### Risk 11: No DPO Assessment

| Attribute | Assessment |
|:----------|:-----------|
| **GDPR Article** | Art. 37-39 |
| **Impact** | Potential requirement unfulfilled |
| **Max Fine** | €44,000 |
| **Mitigation** | Assess and appoint if required |
| **Cost to Fix** | €2,000 |
| **Timeline** | Week 11 |

---

## Medium Risks (🟠)

| # | Risk | Article | Max Fine | Mitigation Cost |
|:-:|:-----|:--------|:--------:|----------------:|
| 12 | No consent records | Art. 7 | €88K | €3,000 |
| 13 | Insufficient transparency | Art. 12 | €88K | €2,000 |
| 14 | No processing records | Art. 30 | €44K | €2,000 |
| 15 | Inadequate security docs | Art. 32 | €44K | €3,000 |

---

## Low Risks (🟢)

| # | Risk | Article | Max Fine | Mitigation Cost |
|:-:|:-----|:--------|:--------:|----------------:|
| 16 | Staff training gaps | Art. 39 | €44K | €2,000 |
| 17 | Cookie compliance | ePrivacy | N/A | €1,000 |
| 18 | Minor policy gaps | Various | €44K | €1,000 |

---

## Risk Matrix

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                            RISK MATRIX                                        ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   IMPACT                                                                      ║
║     ▲                                                                         ║
║     │                                                                         ║
║   H │  🟡 Rights    🔴 Legal Basis   🔴 Health Data                          ║
║   I │     Portal       Processing       Consent                               ║
║   G │                                                                         ║
║   H │  🟡 DPIA      🔴 No Privacy    🔴 Int'l Transfers                      ║
║     │     Missing      Policy           Illegal                               ║
║     │                                                                         ║
║   M │  🟠 Records   🟡 No DPO        🔴 Missing DPAs                         ║
║   E │     Missing      Assessment                                             ║
║   D │                                                                         ║
║     │  🟢 Training  🟠 Security      🟡 No Incident                          ║
║   L │     Gaps         Docs             Response                              ║
║   O │                                                                         ║
║   W │  🟢 Cookies   🟢 Minor Gaps                                            ║
║     │                                                                         ║
║     └──────────────────────────────────────────────────────────────────────▶  ║
║         LOW           MEDIUM           HIGH           CERTAIN                 ║
║                                                                               ║
║                           LIKELIHOOD                                          ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

## Mitigation Priority

### Immediate (Week 1-2)

| Risk | Action | Cost |
|:-----|:-------|-----:|
| No privacy policy | Draft and review | €8,000 |
| No legal basis | Document per activity | €3,000 |
| Missing DPAs | Initiate negotiations | €0 |

### Short-term (Week 3-4)

| Risk | Action | Cost |
|:-----|:-------|-----:|
| Health data consent | Build consent system | €10,000 |
| Int'l transfers | Execute SCCs | €8,000 |
| Missing DPAs | Execute agreements | €16,000 |

### Medium-term (Week 5-8)

| Risk | Action | Cost |
|:-----|:-------|-----:|
| Rights portal | Build and deploy | €15,000 |
| Retention policy | Define and implement | €2,000 |

### Long-term (Week 9-12)

| Risk | Action | Cost |
|:-----|:-------|-----:|
| DPIA - AI | Complete assessment | €8,000 |
| DPIA - Data | Complete assessment | €4,000 |
| Incident response | Document procedures | €3,000 |

---

## Total Risk Exposure

### Without Mitigation

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                    UNMITIGATED RISK EXPOSURE                                  ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   REGULATORY FINES                                                            ║
║   Maximum theoretical: €132,000 (multiple violations)                        ║
║   Realistic estimate: €50,000 - €80,000                                      ║
║                                                                               ║
║   BUSINESS IMPACT                                                             ║
║   B2B revenue blocked: $1,445,000 (3 years)                                  ║
║   EU launch blocked: $800,000+ (3 years)                                     ║
║   Reputational damage: Unquantifiable                                        ║
║                                                                               ║
║   TOTAL EXPOSURE: €2,000,000+                                                ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

### With Full Mitigation

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                     MITIGATED RISK POSITION                                   ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   INVESTMENT REQUIRED: €75,000 - €115,000                                    ║
║                                                                               ║
║   RESIDUAL RISKS:                                                             ║
║   • Breach despite controls: Insurable                                       ║
║   • Regulatory interpretation changes: Monitor                               ║
║   • Processor non-compliance: Audit rights                                   ║
║                                                                               ║
║   BENEFITS UNLOCKED:                                                          ║
║   • EU market access: ✅                                                     ║
║   • B2B data monetization: ✅                                                ║
║   • Competitive advantage: ✅                                                ║
║   • Investor confidence: ✅                                                  ║
║                                                                               ║
║   ROI: 15-25x over 3 years                                                   ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

## Recommendations

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                       EXECUTIVE RECOMMENDATIONS                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   1. IMMEDIATE ACTION REQUIRED                                                ║
║      Allocate €75-115K for 12-week compliance program                        ║
║      Start Week 1: Privacy policy and legal basis documentation              ║
║                                                                               ║
║   2. NO LAUNCH WITHOUT COMPLIANCE                                             ║
║      52% of Y3 revenue depends on GDPR compliance                            ║
║      Risk of €100K+ fines without mitigation                                 ║
║                                                                               ║
║   3. COMPLIANCE AS COMPETITIVE ADVANTAGE                                      ║
║      "Privacy-first" positioning against Fetch, Ibotta                       ║
║      Enterprise buyers require documented compliance                         ║
║                                                                               ║
║   4. ONGOING INVESTMENT                                                       ║
║      Budget €15-20K annually for compliance maintenance                      ║
║      Regular audits and policy updates                                       ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

<div align="center">

**Document Version:** 2.0 | January 28, 2026

</div>
