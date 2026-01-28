<div align="center">

# **MILO**
## Data Processor Analysis v2.0

---

**DeepmAInd B.V.** | January 28, 2026

</div>

---

## Processor Overview

| Processor | Service | Location | DPA Status | Risk Level |
|:----------|:--------|:---------|:----------:|:----------:|
| **Veryfi Inc.** | OCR Processing | USA | ❌ Missing | 🔴 High |
| **Google LLC** | Gemini AI | USA | ❌ Missing | 🔴 High |
| **Firebase (Google)** | Auth, Storage, Analytics | USA | ❌ Missing | 🔴 High |
| **Railway Corp.** | Backend Hosting | EU-available | ❌ Missing | 🟡 Medium |
| **Apple Inc.** | Payments (IAP) | USA | ✅ Standard | 🟢 Low |

---

## Veryfi Inc.

### Service Description

| Attribute | Details |
|:----------|:--------|
| **Service** | Receipt OCR and data extraction |
| **Data Processed** | Receipt images, extracted text |
| **Processing Location** | United States |
| **Retention** | Transient (stated <24 hours) |

### Data Flow

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                           VERYFI DATA FLOW                                    ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   iOS App → HTTPS/TLS → Veryfi API → OCR Processing → JSON Response          ║
║      │                      │              │               │                  ║
║      │                      │              │               └─→ Line items     ║
║      │                      │              │                   Merchant       ║
║      │                      │              │                   Total          ║
║      │                      │              │                   Date           ║
║      │                      │              │                                  ║
║      │                      │              └─→ Image deleted (claimed)        ║
║      │                      │                                                 ║
║      │                      └─→ USA servers                                   ║
║      │                                                                        ║
║      └─→ Receipt image (JPEG/PNG)                                            ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

### DPA Requirements

| Clause | Requirement | Status |
|:-------|:------------|:------:|
| Art. 28(3)(a) | Process only on documented instructions | ⬜ |
| Art. 28(3)(b) | Confidentiality obligations | ⬜ |
| Art. 28(3)(c) | Security measures | ⬜ |
| Art. 28(3)(d) | Sub-processor restrictions | ⬜ |
| Art. 28(3)(e) | Assist with rights requests | ⬜ |
| Art. 28(3)(f) | Assist with compliance | ⬜ |
| Art. 28(3)(g) | Delete/return data | ⬜ |
| Art. 28(3)(h) | Audit rights | ⬜ |

### Risk Assessment

| Risk | Level | Mitigation |
|:-----|:-----:|:-----------|
| No DPA in place | 🔴 High | Execute DPA immediately |
| US data transfer | 🔴 High | SCCs required |
| Image retention | 🟡 Medium | Verify deletion policy |
| Sub-processors | 🟡 Medium | Identify in DPA |

**Estimated DPA Cost:** €5,000

---

## Google LLC (Gemini AI)

### Service Description

| Attribute | Details |
|:----------|:--------|
| **Service** | Gemini 2.0 Flash AI for health scoring |
| **Data Processed** | Line items text, prompts |
| **Processing Location** | United States |
| **Retention** | API calls not retained (Gemini policy) |

### Data Flow

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                          GEMINI AI DATA FLOW                                  ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   Backend (Railway) → Gemini API → AI Processing → JSON Response             ║
║         │                  │              │               │                   ║
║         │                  │              │               └─→ Health scores   ║
║         │                  │              │                   Categories      ║
║         │                  │              │                   Insights        ║
║         │                  │              │                                   ║
║         │                  │              └─→ No model training (API)         ║
║         │                  │                                                  ║
║         │                  └─→ US servers (Google Cloud)                      ║
║         │                                                                     ║
║         └─→ Anonymized line items (no user ID in prompt)                     ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

### DPA Requirements

| Requirement | Google Status | MILO Action |
|:------------|:--------------|:------------|
| Standard DPA | Available | Execute |
| SCCs | Included | Verify |
| Security | SOC 2, ISO 27001 | Document |
| Sub-processors | Listed | Review |

**Estimated DPA Cost:** €5,000 (legal review)

---

## Firebase (Google)

### Services Used

| Service | Data Type | Purpose |
|:--------|:----------|:--------|
| **Authentication** | User tokens | Sign-in |
| **Cloud Storage** | Profile images | User content |
| **Analytics** | Usage events | Product insights |
| **Crashlytics** | Crash reports | Debugging |

### Data Flow

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                          FIREBASE DATA FLOW                                   ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   Firebase Auth ←────────────────────→ iOS App                               ║
║        │                                   │                                  ║
║        └─→ User tokens, session data       │                                  ║
║                                            │                                  ║
║   Firebase Storage ←─────────────────→ iOS App                               ║
║        │                                   │                                  ║
║        └─→ Profile images                  │                                  ║
║                                            │                                  ║
║   Firebase Analytics ←───────────────→ iOS App                               ║
║        │                                   │                                  ║
║        └─→ Events, user properties         │                                  ║
║                                            │                                  ║
║   All services: US servers (Google Cloud)                                    ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

### DPA Status

| Attribute | Status |
|:----------|:-------|
| Google Cloud DPA | Available |
| Firebase-specific terms | Included |
| SCCs | Pre-signed by Google |
| Action required | Accept DPA, configure settings |

**Estimated Cost:** €0 (standard terms) + €3,000 (legal review)

---

## Railway Corp.

### Service Description

| Attribute | Details |
|:----------|:--------|
| **Service** | Backend hosting (FastAPI + PostgreSQL) |
| **Data Processed** | All core user data |
| **Processing Location** | EU region available |
| **Data Sovereignty** | Can be EU-only |

### Data Flow

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                          RAILWAY DATA FLOW                                    ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   iOS App → Railway (EU) → PostgreSQL                                        ║
║      │           │              │                                             ║
║      │           │              └─→ User accounts                             ║
║      │           │                  Receipt data                              ║
║      │           │                  Health scores                             ║
║      │           │                  All core data                             ║
║      │           │                                                            ║
║      │           └─→ FastAPI backend                                          ║
║      │                                                                        ║
║      └─→ All API requests                                                    ║
║                                                                               ║
║   KEY: Railway can be configured for EU-only hosting                         ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

### DPA Requirements

| Clause | Requirement | Status |
|:-------|:------------|:------:|
| Processing location | EU only | ⬜ Configure |
| Security measures | SOC 2 Type II | ✅ Available |
| Sub-processors | List required | ⬜ Request |
| Audit rights | Required | ⬜ Negotiate |

**Estimated DPA Cost:** €3,000

---

## Apple Inc.

### Service Description

| Attribute | Details |
|:----------|:--------|
| **Service** | In-App Purchases (StoreKit) |
| **Data Processed** | Transaction IDs, purchase records |
| **Processing Location** | Global |
| **DPA Status** | Standard Apple developer terms |

### Assessment

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                          APPLE IAP ASSESSMENT                                 ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   Apple acts as:                                                              ║
║   • Payment processor (independent controller for payments)                  ║
║   • Data processor (for purchase verification API)                           ║
║                                                                               ║
║   Standard Apple Developer Agreement includes:                               ║
║   ✅ Data processing terms                                                   ║
║   ✅ Security commitments                                                    ║
║   ✅ Privacy requirements                                                    ║
║                                                                               ║
║   ACTION: No additional DPA required                                         ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

## DPA Implementation Priority

| Priority | Processor | Reason | Timeline | Budget |
|:--------:|:----------|:-------|:---------|-------:|
| 1 | Veryfi | Processes all receipt images | Week 2 | €5,000 |
| 2 | Google (Gemini) | Processes health-related data | Week 2 | €5,000 |
| 3 | Firebase | Multiple services, US transfer | Week 2 | €3,000 |
| 4 | Railway | Core data storage | Week 3 | €3,000 |
| - | Apple | Already covered | - | €0 |

**Total DPA Budget:** €16,000

---

## Sub-Processor Management

### Required Actions

| Action | Timeline |
|:-------|:---------|
| Request sub-processor lists from all vendors | Week 1 |
| Review sub-processor locations | Week 2 |
| Document sub-processor chain | Week 2 |
| Establish notification process for changes | Week 3 |

---

<div align="center">

**Document Version:** 2.0 | January 28, 2026

</div>
