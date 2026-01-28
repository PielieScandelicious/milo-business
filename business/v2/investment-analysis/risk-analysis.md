<div align="center">

# **MILO**
## Risk Analysis v2.0

### *Comprehensive Risk Assessment & Mitigation Strategies*

---

**DeepmAInd B.V.**

**Document Version:** 2.0 | January 28, 2026

---

![Model](https://img.shields.io/badge/Analysis-Conservative-orange)

</div>

---

## Risk Summary

| Category | Critical | High | Medium | Low | Total |
|:---------|:--------:|:----:|:------:|:---:|:-----:|
| **Market** | 0 | 2 | 2 | 1 | 5 |
| **Technical** | 0 | 1 | 2 | 1 | 4 |
| **Financial** | 1 | 1 | 1 | 0 | 3 |
| **Regulatory** | 1 | 1 | 1 | 0 | 3 |
| **Operational** | 0 | 0 | 2 | 1 | 3 |
| **Total** | **2** | **5** | **8** | **3** | **18** |

---

## Risk Matrix

```
                              IMPACT
                    Low         Medium        High       Critical
                ┌───────────┬───────────┬───────────┬───────────┐
           High │           │ M5        │ F2        │           │
                │           │           │           │           │
    P          │           │           │           │           │
    R          ├───────────┼───────────┼───────────┼───────────┤
    O          │           │ T2 T3     │ M1 M2     │ R1 F1     │
    B     Med  │           │ O1        │ M3 T1     │           │
    A          │           │           │           │           │
    B          ├───────────┼───────────┼───────────┼───────────┤
    I          │ O3        │ T4 O2     │ M4 R2     │ R3        │
    L     Low  │           │           │           │           │
    I          │           │           │           │           │
    T          └───────────┴───────────┴───────────┴───────────┘
    Y

    LEGEND:
    M = Market    T = Technical    F = Financial
    R = Regulatory    O = Operational
```

---

## Critical Risks

### R1: GDPR Non-Compliance at Launch

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  RISK: GDPR NON-COMPLIANCE                                    CRITICAL      ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  DESCRIPTION:                                                                ║
║  Failure to achieve GDPR compliance before launch blocks EU operations      ║
║  and B2B data monetization (52% of Year 3 revenue)                         ║
║                                                                              ║
║  CURRENT STATUS:                                                             ║
║  Readiness Score: 25/100 (Non-Compliant)                                    ║
║  Timeline to Compliance: 12 weeks                                           ║
║  Investment Required: €75K-115K                                             ║
║                                                                              ║
║  IMPACT IF MATERIALIZED:                                                     ║
║  • Cannot launch in EU/EEA markets                                          ║
║  • B2B data sales blocked ($1.25M Y3 at risk)                              ║
║  • Potential regulatory action if proceeding anyway                        ║
║                                                                              ║
║  PROBABILITY: Medium (30%)                                                   ║
║  IMPACT: Critical                                                            ║
║                                                                              ║
║  MITIGATION:                                                                 ║
║  ✓ Dedicated €75-115K compliance budget allocated                          ║
║  ✓ 12-week remediation roadmap documented                                  ║
║  ✓ External GDPR counsel engaged                                           ║
║  ✓ Compliance milestone gates funding tranches                             ║
║                                                                              ║
║  RESIDUAL RISK: Low (after mitigation)                                      ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

### F1: Insufficient Seed Funding

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  RISK: FUNDING SHORTFALL                                      CRITICAL      ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  DESCRIPTION:                                                                ║
║  Failure to secure adequate seed funding ($400K-$600K) prevents launch      ║
║  and operation                                                              ║
║                                                                              ║
║  IMPACT IF MATERIALIZED:                                                     ║
║  • Operations cease or significantly limited                                ║
║  • Cannot complete GDPR compliance                                         ║
║  • Cannot execute marketing strategy                                       ║
║  • Product development halted                                              ║
║                                                                              ║
║  PROBABILITY: Medium (35%)                                                   ║
║  IMPACT: Critical                                                            ║
║                                                                              ║
║  MITIGATION:                                                                 ║
║  ✓ Conservative projections increase investor confidence                   ║
║  ✓ Multiple investor outreach (diversified sources)                        ║
║  ✓ Milestone-based tranches reduce investor risk                           ║
║  ✓ Lean burn rate extends runway                                           ║
║  ✓ Bridge funding options identified                                       ║
║                                                                              ║
║  RESIDUAL RISK: Medium                                                       ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

---

## High-Priority Risks

### M1: Trial-to-Paid Conversion Below 15%

| Attribute | Value |
|:----------|:------|
| **Description** | Users don't convert from 14-day trial to paid |
| **Probability** | Medium (40%) |
| **Impact** | High |
| **Y3 Revenue at Risk** | $334K (if 12% instead of 15%) |
| **Mitigation** | A/B test trial length, offers, paywall design |
| **Residual Risk** | Medium |

### M2: Data Consent Rate Below 40%

| Attribute | Value |
|:----------|:------|
| **Description** | Users don't opt-in to data monetization |
| **Probability** | Medium (45%) |
| **Impact** | High |
| **Y3 Revenue at Risk** | $312K (if 32% instead of 40%) |
| **Mitigation** | Clear value exchange, gradual consent tiers |
| **Residual Risk** | Medium |

### M3: Subscription Fatigue Impact

| Attribute | Value |
|:----------|:------|
| **Description** | 41% of consumers report subscription fatigue |
| **Probability** | Medium (50%) |
| **Impact** | High |
| **Effect** | Lower conversion, higher churn |
| **Mitigation** | Trial model, flexible pricing, clear value |
| **Residual Risk** | Medium |

### T1: Veryfi API Cost Increase

| Attribute | Value |
|:----------|:------|
| **Description** | OCR provider raises prices significantly |
| **Probability** | Medium (30%) |
| **Impact** | High |
| **Current Cost** | $0.08/receipt |
| **If +50%** | Margins drop 8-10 percentage points |
| **Mitigation** | Volume contracts, alternative providers |
| **Residual Risk** | Low |

### F2: High Monthly Churn

| Attribute | Value |
|:----------|:------|
| **Description** | Churn exceeds 10% Gold / 8% Platinum |
| **Probability** | Medium-High (50%) |
| **Impact** | High |
| **Effect** | Lower LTV, worse unit economics |
| **Mitigation** | Engagement features, win-back campaigns |
| **Residual Risk** | Medium |

---

## Medium-Priority Risks

### Market Risks

| Risk | Description | Probability | Impact | Mitigation |
|:-----|:------------|:-----------:|:------:|:-----------|
| **M4** | Big Tech entry | Low | High | Speed, niche focus |
| **M5** | Economic downturn | High | Medium | Essential positioning |

### Technical Risks

| Risk | Description | Probability | Impact | Mitigation |
|:-----|:------------|:-----------:|:------:|:-----------|
| **T2** | OCR accuracy issues | Medium | Medium | Veryfi SLA, fallback |
| **T3** | Scalability problems | Medium | Medium | Railway auto-scaling |
| **T4** | Security breach | Low | Medium | Firebase, encryption |

### Regulatory Risks

| Risk | Description | Probability | Impact | Mitigation |
|:-----|:------------|:-----------:|:------:|:-----------|
| **R2** | Apple policy changes | Low | High | Policy monitoring |
| **R3** | US federal privacy law | Low | Critical | Already compliant |

### Operational Risks

| Risk | Description | Probability | Impact | Mitigation |
|:-----|:------------|:-----------:|:------:|:-----------|
| **O1** | Key person dependency | Medium | Medium | Documentation |
| **O2** | B2B sales execution | Low | Medium | Hire experienced |
| **O3** | Support volume | Low | Low | Self-service tools |

---

## Risk Scenarios

### Worst Case Scenario

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          WORST CASE SCENARIO                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  CONDITIONS:                                                                │
│  • Trial conversion: 10% (vs. 15% base)                                    │
│  • Data consent: 25% (vs. 40% base)                                        │
│  • Churn: 15%/12% (vs. 10%/8% base)                                       │
│  • No B2B deals closed                                                     │
│                                                                             │
│  OUTCOME:                                                                   │
│  • Year 3 Revenue: ~$600K (vs. $2.4M base)                                │
│  • Operating Loss: ~($150K)                                                │
│  • Runway exhausted: Month 16                                              │
│                                                                             │
│  INVESTOR RETURN: 0-1x                                                      │
│                                                                             │
│  PROBABILITY: 15%                                                           │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Base Case Scenario

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           BASE CASE SCENARIO                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  CONDITIONS:                                                                │
│  • Trial conversion: 15%                                                   │
│  • Data consent: 40%                                                       │
│  • Churn: 10%/8%                                                           │
│  • 8-10 B2B deals closed                                                   │
│                                                                             │
│  OUTCOME:                                                                   │
│  • Year 3 Revenue: $2.4M                                                   │
│  • Operating Profit: $1.39M (58% margin)                                   │
│  • Runway: Sustainable                                                      │
│                                                                             │
│  INVESTOR RETURN: 6-8x                                                      │
│                                                                             │
│  PROBABILITY: 40%                                                           │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Best Case Scenario

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          BEST CASE SCENARIO                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  CONDITIONS:                                                                │
│  • Trial conversion: 22%                                                   │
│  • Data consent: 55%                                                       │
│  • Churn: 7%/5%                                                            │
│  • 15+ B2B deals closed                                                    │
│  • Strategic interest emerges                                              │
│                                                                             │
│  OUTCOME:                                                                   │
│  • Year 3 Revenue: $4.5M+                                                  │
│  • Operating Profit: $2.8M+ (62% margin)                                   │
│  • Series A ready                                                          │
│                                                                             │
│  INVESTOR RETURN: 12-15x                                                    │
│                                                                             │
│  PROBABILITY: 20%                                                           │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Risk Monitoring Framework

### Key Risk Indicators (KRIs)

| KRI | Target | Warning | Critical |
|:----|:------:|:-------:|:--------:|
| Trial Conversion | ≥15% | 12-15% | <12% |
| Data Consent | ≥40% | 30-40% | <30% |
| Monthly Churn (Gold) | ≤10% | 10-15% | >15% |
| CAC | ≤$17 | $17-25 | >$25 |
| D7 Retention | ≥35% | 28-35% | <28% |
| D30 Retention | ≥20% | 15-20% | <15% |
| NPS | ≥30 | 20-30 | <20 |

### Monitoring Cadence

| Metric | Frequency | Owner |
|:-------|:----------|:------|
| Conversion rates | Daily | Product |
| Churn | Weekly | Product |
| CAC/LTV | Weekly | Marketing |
| Revenue | Weekly | Finance |
| Compliance | Monthly | Legal |
| Competitive | Monthly | Strategy |

---

## Risk Response Plan

### If Trial Conversion < 12%

```
Week 1:  Analyze funnel drop-off points
Week 2:  A/B test paywall variants
Week 3:  Test extended trial (21 days)
Week 4:  Implement winning variant
Week 5:  If no improvement, test pricing
Week 6:  Consider free tier reintroduction
```

### If Data Consent < 30%

```
Week 1:  Survey non-consenters for reasons
Week 2:  Redesign consent flow/value prop
Week 3:  Test incentive offers
Week 4:  Implement consent nudges
Week 5:  If no improvement, reduce B2B projections
Week 6:  Pivot to subscription-first model
```

### If Funding Shortfall

```
Week 1:  Identify bridge funding options
Week 2:  Reduce burn to minimum viable
Week 3:  Accelerate angel outreach
Week 4:  Consider strategic partnerships
Week 5:  If no progress, pause non-essential spend
Week 6:  Evaluate pivot/shutdown options
```

---

## Conclusion

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                          OVERALL RISK ASSESSMENT                             ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  RISK LEVEL:        MODERATE-HIGH                                           ║
║                                                                              ║
║  CRITICAL RISKS:    2 (GDPR compliance, funding)                            ║
║  HIGH RISKS:        5 (conversion, consent, churn, Veryfi, fatigue)        ║
║  MEDIUM RISKS:      8                                                       ║
║  LOW RISKS:         3                                                       ║
║                                                                              ║
║  KEY FINDINGS:                                                               ║
║  • All critical risks have actionable mitigation plans                      ║
║  • Conservative projections provide buffer for underperformance            ║
║  • Revenue diversification limits single-point-of-failure exposure         ║
║  • No risks are insurmountable with proper execution                       ║
║                                                                              ║
║  RISK-ADJUSTED EXPECTED RETURN: 6.2x                                        ║
║                                                                              ║
║  RECOMMENDATION: Proceed with investment, implement milestone gates         ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

---

<div align="center">

**Document Version:** 2.0
**Last Updated:** January 28, 2026

</div>
