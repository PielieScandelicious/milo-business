<div align="center">

# **MILO**
## Legal Basis Analysis v2.0

---

**DeepmAInd B.V.** | January 28, 2026

</div>

---

## Legal Basis Overview

| Basis | GDPR Article | Use Cases | Count |
|:------|:-------------|:----------|:-----:|
| **Contract** | Art. 6(1)(b) | Core app functionality | 5 |
| **Consent** | Art. 6(1)(a) | Optional features, marketing | 4 |
| **Legitimate Interest** | Art. 6(1)(f) | Analytics, security | 3 |
| **Explicit Consent** | Art. 9(2)(a) | Health data processing | 1 |

---

## Contract Basis (Art. 6(1)(b))

### Processing Necessary for Service Delivery

| Processing Activity | Necessity Justification |
|:--------------------|:-----------------------|
| **User account creation** | Cannot provide personalized service without account |
| **Receipt scanning** | Core service functionality |
| **Spending categorization** | Primary app feature |
| **Data storage** | Service cannot function without storage |
| **Authentication** | Security requirement for service access |

### Documentation

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                        CONTRACT BASIS REQUIREMENTS                            ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   ✓ Terms of Service clearly describe processing activities                  ║
║   ✓ Processing is objectively necessary (not just convenient)                ║
║   ✓ No viable alternative to deliver the service                             ║
║   ✓ Data subject expects this processing                                     ║
║                                                                               ║
║   STATUS: ⬜ Terms of Service need drafting                                  ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

## Consent Basis (Art. 6(1)(a))

### Requirements for Valid Consent

| Requirement | MILO Implementation |
|:------------|:--------------------|
| **Freely given** | Service works without consent features |
| **Specific** | Granular consent per purpose |
| **Informed** | Clear explanation before collection |
| **Unambiguous** | Affirmative action required |
| **Withdrawable** | Easy withdrawal in settings |

### Consent-Based Processing

| Processing Activity | Consent Type | Withdrawal Impact |
|:--------------------|:-------------|:------------------|
| **B2B data sharing** | Explicit opt-in | Feature disabled |
| **Marketing emails** | Opt-in | Unsubscribe |
| **Push notifications** | System prompt | Disable in iOS |
| **Analytics (optional)** | Soft opt-in | Limited insights |

### Consent UI Requirements

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                         CONSENT COLLECTION FLOW                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   Onboarding Screen 3/5:                                                     ║
║   ┌─────────────────────────────────────────────────────────────────────┐    ║
║   │                                                                     │    ║
║   │   Your Privacy Choices                                              │    ║
║   │   ─────────────────────                                             │    ║
║   │                                                                     │    ║
║   │   ☐ Health Insights (Required for health scoring)                  │    ║
║   │     We'll analyze your purchases to show health trends.            │    ║
║   │                                                                     │    ║
║   │   ☐ Anonymous Data Contribution                                     │    ║
║   │     Help improve products by sharing anonymized trends.            │    ║
║   │     Your identity is never shared.                                 │    ║
║   │                                                                     │    ║
║   │   ☐ Product Updates                                                 │    ║
║   │     Occasional emails about new features.                          │    ║
║   │                                                                     │    ║
║   │   [Skip]                              [Continue]                    │    ║
║   │                                                                     │    ║
║   └─────────────────────────────────────────────────────────────────────┘    ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

## Explicit Consent (Art. 9(2)(a))

### Health Data Processing

| Attribute | Requirement |
|:----------|:------------|
| **Data Type** | Dietary patterns, health scores |
| **GDPR Article** | Article 9 - Special Categories |
| **Basis Required** | Explicit consent |
| **Form** | Written/recorded consent |

### Implementation

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                    EXPLICIT CONSENT FOR HEALTH DATA                          ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   Before enabling Health Scoring feature:                                    ║
║   ┌─────────────────────────────────────────────────────────────────────┐    ║
║   │                                                                     │    ║
║   │   🩺 Health Insights Consent                                        │    ║
║   │                                                                     │    ║
║   │   MILO can analyze your purchases to provide insights about        │    ║
║   │   your dietary patterns and health-related spending.               │    ║
║   │                                                                     │    ║
║   │   This involves:                                                    │    ║
║   │   • Identifying food and health products in your receipts          │    ║
║   │   • Calculating nutritional scores based on purchases              │    ║
║   │   • Tracking trends in your dietary choices                        │    ║
║   │                                                                     │    ║
║   │   This data is considered health-related under GDPR.               │    ║
║   │   You can withdraw consent anytime in Settings.                    │    ║
║   │                                                                     │    ║
║   │   ☑ I explicitly consent to health data processing                 │    ║
║   │                                                                     │    ║
║   │   [Cancel]                        [Enable Health Insights]         │    ║
║   │                                                                     │    ║
║   └─────────────────────────────────────────────────────────────────────┘    ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

## Legitimate Interest (Art. 6(1)(f))

### Balancing Test Required

| Processing Activity | Interest | Necessity | Balance |
|:--------------------|:---------|:----------|:--------|
| **Security logging** | Fraud prevention | Essential | ✅ Passes |
| **Basic analytics** | Service improvement | Proportionate | ✅ Passes |
| **Crash reporting** | Bug fixing | Minimal intrusion | ✅ Passes |

### Legitimate Interest Assessment (LIA)

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                    LEGITIMATE INTEREST ASSESSMENT                             ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   Processing: Basic Analytics (app usage patterns)                           ║
║                                                                               ║
║   1. PURPOSE TEST                                                             ║
║      Interest: Improve service quality and user experience                   ║
║      Is it legitimate? YES - standard business operation                     ║
║                                                                               ║
║   2. NECESSITY TEST                                                           ║
║      Can purpose be achieved without this processing? NO                     ║
║      Is processing proportionate? YES - aggregated data only                 ║
║                                                                               ║
║   3. BALANCING TEST                                                           ║
║      Impact on individuals: MINIMAL - no sensitive data                      ║
║      Reasonable expectations: YES - common in apps                           ║
║      Safeguards: Data minimization, 13-month retention                       ║
║                                                                               ║
║   CONCLUSION: Legitimate interest applies                                    ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

## Legal Basis Matrix

| Processing Activity | Contract | Consent | Legit Interest | Art. 9 |
|:--------------------|:--------:|:-------:|:--------------:|:------:|
| Account creation | ✅ | | | |
| Receipt scanning | ✅ | | | |
| Spending categories | ✅ | | | |
| Health scoring | | | | ✅ |
| B2B data sharing | | ✅ | | |
| Marketing emails | | ✅ | | |
| Basic analytics | | | ✅ | |
| Security logging | | | ✅ | |
| Crash reporting | | | ✅ | |

---

## Documentation Requirements

### Required Records

| Document | Status | Owner |
|:---------|:------:|:------|
| Privacy Policy | ⬜ To draft | Legal |
| Terms of Service | ⬜ To draft | Legal |
| Consent records | ⬜ To build | Engineering |
| LIA documentation | ⬜ To complete | Legal |
| Processing register | ⬜ To create | Legal |

---

<div align="center">

**Document Version:** 2.0 | January 28, 2026

</div>
