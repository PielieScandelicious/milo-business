# GDPR Compliance Assessment
## Third-Party Processor Analysis

---

| **Document** | 04 - Third-Party Processor Analysis |
|:---|:---|
| **Reference** | GDPR Articles 28, 29, 32 |
| **Status** | Critical Gaps in Processor Management |

---

## 1. Overview

Under GDPR Article 28, controllers must only use processors providing sufficient guarantees to implement appropriate technical and organizational measures. This document analyzes all third-party processors engaged by the Milo application.

### Processor Inventory Summary

| # | Processor | Service | Data Exposure | DPA Status | Risk Level |
|:---:|:---|:---|:---|:---:|:---:|
| 1 | Veryfi Inc. | OCR Processing | High | ❌ Missing | 🔴 Critical |
| 2 | Google LLC | Gemini AI | High | ❌ Missing | 🔴 Critical |
| 3 | Anthropic PBC | Claude AI | Critical | ❌ Missing | 🔴 Critical |
| 4 | Firebase/Google | Auth & Storage | Critical | ❌ Missing | 🔴 Critical |
| 5 | Railway Corp. | Hosting | Critical | ❌ Missing | 🔴 Critical |
| 6 | Apple Inc. | Payments | Medium | ✅ Standard | 🟢 Low |

---

## 2. Detailed Processor Analysis

### 2.1 Veryfi Inc.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         PROCESSOR: VERYFI INC.                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  SERVICE: Intelligent Document Processing (OCR)                             │
│  LOCATION: San Mateo, California, USA                                       │
│  API VERSION: v8                                                            │
│                                                                             │
│  DATA RECEIVED:                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ • Receipt images (base64 encoded)                                   │   │
│  │ • File type (PDF, JPG, PNG)                                         │   │
│  │ • File size (up to 20MB)                                            │   │
│  │ • API credentials (authentication)                                  │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  DATA EXTRACTED & RETURNED:                                                 │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ • Vendor/store name                                                 │   │
│  │ • Transaction date                                                  │   │
│  │ • Total amount                                                      │   │
│  │ • Line items (name, price, quantity)                                │   │
│  │ • Confidence scores                                                 │   │
│  │ • Duplicate detection flag                                          │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  PROCESSING FREQUENCY: Every receipt upload (estimated 15-150/user/month)   │
│                                                                             │
│  INTEGRATION METHOD:                                                        │
│  • Synchronous API call via POST /api/v8/partner/documents                 │
│  • Base64 encoded file in request body                                     │
│  • Response contains extracted data                                        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### Risk Assessment

| Risk Factor | Assessment | Mitigation Required |
|:---|:---|:---|
| Data Volume | High - All receipts | DPA with data limits |
| Data Sensitivity | Medium - Financial receipts | Encryption requirements |
| Data Retention | Unknown | Define max retention |
| Sub-processors | Unknown | Require disclosure |
| Security Measures | Unknown | Security questionnaire |
| Location | USA (no adequacy) | SCCs required |

#### Required Actions

- [ ] Execute Data Processing Agreement
- [ ] Implement Standard Contractual Clauses
- [ ] Complete Transfer Impact Assessment
- [ ] Request SOC 2 Type II report
- [ ] Obtain sub-processor list
- [ ] Define data retention requirements (suggest: 24 hours max)
- [ ] Implement audit rights clause

#### DPA Key Clauses

```
1. PURPOSE LIMITATION
   Veryfi shall only process receipt images for OCR extraction
   purposes and shall not use data for training, analytics,
   or any secondary purpose.

2. DATA RETENTION
   All uploaded images and extracted data shall be deleted
   within 24 hours of processing completion.

3. SUB-PROCESSORS
   Veryfi shall provide 30-day notice of new sub-processors
   with right to object.

4. SECURITY MEASURES
   - TLS 1.3 encryption in transit
   - AES-256 encryption at rest
   - Annual SOC 2 Type II audit
   - No persistent storage of original images
```

---

### 2.2 Google LLC (Gemini AI)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      PROCESSOR: GOOGLE LLC (GEMINI)                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  SERVICE: Generative AI - Item Categorization & Health Scoring              │
│  LOCATION: Mountain View, California, USA                                   │
│  MODEL: Gemini 2.0 Flash                                                    │
│                                                                             │
│  DATA RECEIVED:                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ Receipt Processing Context:                                         │   │
│  │ • Item names (cleaned text)                                         │   │
│  │ • Store name                                                        │   │
│  │ • Categorization request (JSON format)                              │   │
│  │                                                                      │   │
│  │ Chat Context (V2 API):                                              │   │
│  │ • User's first name                                                 │   │
│  │ • User's last name                                                  │   │
│  │ • User's gender                                                     │   │
│  │ • 90 days of transaction history:                                   │   │
│  │   - Store names, item names, prices                                 │   │
│  │   - Categories, health scores, dates                                │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  DATA RETURNED:                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ Categorization Response:                                            │   │
│  │ • Category assignment (1 of 16 categories)                          │   │
│  │ • Health score (0-5 scale)                                          │   │
│  │ • Cleaned store name                                                │   │
│  │                                                                      │   │
│  │ Chat Response:                                                      │   │
│  │ • AI-generated advice (streaming SSE)                               │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  PROCESSING FREQUENCY:                                                      │
│  • Categorization: Every receipt (all items)                               │
│  • Chat: Per user message (rate limited to 100/30 days)                    │
│                                                                             │
│  CRITICAL CONCERN:                                                          │
│  Health scores are generated by Gemini, meaning health-related             │
│  data processing occurs at this processor.                                  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### Risk Assessment

| Risk Factor | Assessment | Mitigation Required |
|:---|:---|:---|
| Data Volume | Very High - All items + chat context | Minimize context |
| Data Sensitivity | Critical - Health data generated | Special protections |
| Data Retention | Google AI logs unknown | Confirm no training use |
| Model Training | Risk of data in training | Explicit exclusion clause |
| Sub-processors | GCP infrastructure | Standard GCP DPA |
| Location | USA (no adequacy) | SCCs required |

#### Required Actions

- [ ] Execute Google Cloud/AI Platform DPA
- [ ] Confirm Gemini API data not used for training
- [ ] Implement Standard Contractual Clauses
- [ ] Complete Transfer Impact Assessment
- [ ] Review Google Cloud sub-processor list
- [ ] Request data processing addendum for AI services
- [ ] Implement data minimization (reduce chat context)

#### DPA Key Clauses

```
1. NO TRAINING USE
   Customer data submitted to Gemini API shall not be used
   for model training, improvement, or any purpose beyond
   the immediate API response.

2. DATA RETENTION
   API inputs and outputs shall not be logged or retained
   beyond the API session (or maximum 30 days for abuse
   prevention if required).

3. HEALTH DATA PROCESSING
   Processor acknowledges that health-related insights
   (health scores) are generated and commits to additional
   Article 9 safeguards.

4. SECURITY MEASURES
   - SOC 2 Type II certified
   - ISO 27001 certified
   - Data encrypted in transit (TLS 1.3) and at rest (AES-256)
```

---

### 2.3 Anthropic PBC (Claude AI)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      PROCESSOR: ANTHROPIC PBC (CLAUDE)                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  SERVICE: Generative AI - Chat Assistant (V1 API)                           │
│  LOCATION: San Francisco, California, USA                                   │
│  MODEL: Claude (Sonnet 4 referenced)                                        │
│                                                                             │
│  DATA RECEIVED (Every Chat Request):                                        │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ FULL USER CONTEXT:                                                  │   │
│  │                                                                      │   │
│  │ Profile Data:                                                       │   │
│  │ • First name                                                        │   │
│  │ • Last name                                                         │   │
│  │ • Gender                                                            │   │
│  │                                                                      │   │
│  │ Transaction History (90 Days):                                      │   │
│  │ • All store names                                                   │   │
│  │ • All item names                                                    │   │
│  │ • All prices and quantities                                         │   │
│  │ • All assigned categories                                           │   │
│  │ • All health scores (SPECIAL CATEGORY DATA)                         │   │
│  │ • All purchase dates                                                │   │
│  │                                                                      │   │
│  │ Current Message:                                                    │   │
│  │ • User's chat message                                               │   │
│  │ • Conversation history                                              │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ⚠️  HIGHEST DATA EXPOSURE OF ANY PROCESSOR                                │
│                                                                             │
│  This processor receives comprehensive user profile including              │
│  financial behavior and health-related data for 90 days.                    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### Risk Assessment

| Risk Factor | Assessment | Mitigation Required |
|:---|:---|:---|
| Data Volume | Critical - Full user profile | Strict minimization |
| Data Sensitivity | Critical - Health data included | Article 9 protections |
| Data Retention | Anthropic policies vary | Confirm zero retention |
| Model Training | Anthropic may use for training | Explicit exclusion |
| Sub-processors | AWS infrastructure | Review AWS DPA |
| Location | USA (no adequacy) | SCCs required |

#### Required Actions

- [ ] Execute Anthropic Enterprise DPA
- [ ] Confirm Claude API zero-retention policy
- [ ] Request written confirmation: no training use
- [ ] Implement Standard Contractual Clauses
- [ ] Complete Transfer Impact Assessment
- [ ] Implement context minimization strategy
- [ ] Consider removing health scores from chat context

#### Data Minimization Recommendations

```
CURRENT STATE:
┌─────────────────────────────────────────────────────────────────────────────┐
│ All 90 days of transactions sent with every chat message                   │
│ Including: names, items, prices, categories, HEALTH SCORES                 │
└─────────────────────────────────────────────────────────────────────────────┘

RECOMMENDED STATE:
┌─────────────────────────────────────────────────────────────────────────────┐
│ Minimal context based on message relevance:                                │
│                                                                             │
│ Level 1 (Default):                                                         │
│ • User first name only                                                     │
│ • Last 7 days summary (aggregated, no item details)                       │
│                                                                             │
│ Level 2 (If user asks about spending):                                     │
│ • Recent 30 days aggregated by category                                    │
│ • No individual item names                                                 │
│                                                                             │
│ Level 3 (If user explicitly requests):                                     │
│ • Specific store/category detail (limited scope)                          │
│                                                                             │
│ NEVER SEND:                                                                │
│ • Health scores to chat AI (unless user explicitly consents)              │
│ • Full 90-day history                                                      │
│ • Last name                                                                │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 2.4 Firebase/Google (Authentication & Storage)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    PROCESSOR: FIREBASE (GOOGLE LLC)                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  SERVICES:                                                                  │
│  • Firebase Authentication (identity management)                           │
│  • Firebase Storage (receipt image storage)                                │
│  • Firebase Analytics (usage tracking)                                     │
│                                                                             │
│  PROJECT ID: dobby-dd70e                                                   │
│  LOCATION: USA (default)                                                   │
│                                                                             │
│  DATA STORED:                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ Firebase Auth:                                                      │   │
│  │ • Email address                                                     │   │
│  │ • Display name                                                      │   │
│  │ • Firebase UID                                                      │   │
│  │ • Authentication tokens                                             │   │
│  │ • Login timestamps                                                  │   │
│  │                                                                      │   │
│  │ Firebase Storage:                                                   │   │
│  │ • All uploaded receipt images                                       │   │
│  │ • File metadata                                                     │   │
│  │ • Estimated capacity: ~20GB                                         │   │
│  │                                                                      │   │
│  │ Firebase Analytics:                                                 │   │
│  │ • App events                                                        │   │
│  │ • User properties                                                   │   │
│  │ • Session data                                                      │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  CLASSIFICATION: Joint Controller / Processor (depending on service)       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### Risk Assessment

| Risk Factor | Assessment | Mitigation Required |
|:---|:---|:---|
| Data Volume | Very High - All images, all auth | Implement retention |
| Data Sensitivity | High - Includes financial images | Encryption at rest |
| Data Retention | Google default policies | Custom retention rules |
| Analytics | Tracking without consent | Implement opt-out |
| Sub-processors | GCP infrastructure | Standard GCP DPA |
| Location | USA | SCCs via Google DPA |

#### Required Actions

- [ ] Review and accept Google Cloud DPA
- [ ] Configure Firebase Storage retention (90 days)
- [ ] Review Firebase Analytics data collection settings
- [ ] Implement analytics opt-out mechanism
- [ ] Configure data residency (if EU option available)
- [ ] Enable Firebase Storage encryption settings
- [ ] Review Google sub-processor list

---

### 2.5 Railway Corp.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        PROCESSOR: RAILWAY CORP.                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  SERVICE: Backend Hosting (Docker containers)                               │
│  LOCATION: USA                                                              │
│                                                                             │
│  ENVIRONMENTS:                                                              │
│  • Production: scandalicious-api-production.up.railway.app                 │
│  • Non-Prod: scandalicious-api-non-prod.up.railway.app                     │
│                                                                             │
│  DATA PROCESSED:                                                            │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ ALL APPLICATION DATA FLOWS THROUGH RAILWAY                         │   │
│  │                                                                      │   │
│  │ • All API requests and responses                                    │   │
│  │ • All user data in transit                                          │   │
│  │ • Application logs (may contain PII)                                │   │
│  │ • Environment variables (API keys, secrets)                         │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  DATABASE:                                                                  │
│  • PostgreSQL hosted on Railway                                            │
│  • Contains ALL structured user data                                       │
│                                                                             │
│  CLASSIFICATION: Critical Infrastructure Processor                          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### Risk Assessment

| Risk Factor | Assessment | Mitigation Required |
|:---|:---|:---|
| Data Volume | Critical - All data | DPA essential |
| Data Sensitivity | Critical - Complete database | Encryption required |
| Data Retention | Logs unknown | Define log retention |
| Sub-processors | Unknown | Require disclosure |
| Security Measures | Unknown | Security questionnaire |
| Location | USA | SCCs required |

#### Required Actions

- [ ] Execute Railway DPA
- [ ] Request Railway security documentation
- [ ] Implement Standard Contractual Clauses
- [ ] Complete Transfer Impact Assessment
- [ ] Obtain sub-processor list
- [ ] Configure log retention (30 days max)
- [ ] Verify database encryption at rest
- [ ] Review backup and disaster recovery

---

### 2.6 Apple Inc.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          PROCESSOR: APPLE INC.                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  SERVICE: App Store & StoreKit 2 (In-App Purchases)                        │
│  LOCATION: Cupertino, California, USA                                       │
│                                                                             │
│  DATA PROCESSED:                                                            │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ • Subscription purchase data                                        │   │
│  │ • Payment method (Apple handles, not exposed to app)                │   │
│  │ • Subscription status                                               │   │
│  │ • Transaction IDs                                                   │   │
│  │ • Entitlement information                                           │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  DPA STATUS: Standard Apple Developer Agreement includes DPA terms         │
│                                                                             │
│  RISK LEVEL: 🟢 Low                                                        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### Risk Assessment

| Risk Factor | Assessment | Mitigation Required |
|:---|:---|:---|
| Data Volume | Low - Payment data only | None |
| Data Sensitivity | Medium - Payment related | Apple handles security |
| Data Retention | Apple policies apply | None |
| Security Measures | Apple enterprise security | None |
| Location | USA | Apple SCCs in place |

#### Required Actions

- [x] Standard developer agreement provides coverage
- [ ] Review Apple privacy nutrition labels
- [ ] Ensure app privacy policy reflects Apple processing

---

## 3. Processor Management Requirements

### 3.1 Data Processing Agreement Checklist

All DPAs must include the following clauses per Article 28(3):

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    REQUIRED DPA CLAUSES (Article 28(3))                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  □ (a) Process only on documented instructions from controller              │
│                                                                             │
│  □ (b) Ensure persons processing have confidentiality obligations          │
│                                                                             │
│  □ (c) Take all measures required under Article 32 (security)              │
│                                                                             │
│  □ (d) Conditions for engaging sub-processors:                             │
│        - Prior authorization (general or specific)                         │
│        - Flow-down of data protection obligations                          │
│        - Liability for sub-processor actions                               │
│                                                                             │
│  □ (e) Assist controller with data subject requests                        │
│                                                                             │
│  □ (f) Assist controller with Articles 32-36 obligations:                  │
│        - Security measures                                                 │
│        - Breach notification                                               │
│        - DPIA                                                              │
│        - Prior consultation                                                │
│                                                                             │
│  □ (g) Delete or return data at end of services                            │
│                                                                             │
│  □ (h) Make available information for audits and inspections               │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 3.2 Sub-Processor Management

| Processor | Known Sub-Processors | Status |
|:---|:---|:---:|
| Veryfi | Unknown | ❌ Require list |
| Google | GCP sub-processors (public list) | ✅ Available |
| Anthropic | AWS | ⚠️ Confirm |
| Firebase | Google Cloud | ✅ Same as Google |
| Railway | Unknown | ❌ Require list |

### 3.3 Transfer Impact Assessment Requirements

For each US processor, document:

```
TRANSFER IMPACT ASSESSMENT TEMPLATE
═══════════════════════════════════════════════════════════════════════════════

1. NATURE OF DATA TRANSFERRED
   - Personal data categories
   - Volume and frequency
   - Special categories (if any)

2. TRANSFER MECHANISM
   - Standard Contractual Clauses (module)
   - Supplementary measures

3. LEGAL FRAMEWORK ASSESSMENT
   - US surveillance laws applicable
   - FISA 702 exposure risk
   - EO 14086 protections

4. SUPPLEMENTARY MEASURES
   - Technical (encryption, pseudonymization)
   - Contractual (additional clauses)
   - Organizational (access controls)

5. RISK ASSESSMENT
   - Likelihood of government access
   - Impact on data subjects
   - Overall risk level

6. CONCLUSION
   - Transfer permissible: YES/NO
   - Conditions for transfer
   - Review frequency
```

---

## 4. Processor Risk Summary

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                         PROCESSOR RISK MATRIX                                ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  PROCESSOR      │ DATA VOLUME │ SENSITIVITY │ DPA │ TRANSFER │ OVERALL      ║
║  ───────────────┼─────────────┼─────────────┼─────┼──────────┼─────────     ║
║  Veryfi         │    HIGH     │   MEDIUM    │  ❌  │    ❌     │ 🔴 CRITICAL ║
║  Google Gemini  │    HIGH     │   HIGH*     │  ❌  │    ❌     │ 🔴 CRITICAL ║
║  Anthropic      │  CRITICAL   │   HIGH*     │  ❌  │    ❌     │ 🔴 CRITICAL ║
║  Firebase       │    HIGH     │   MEDIUM    │  ❌  │    ❌     │ 🔴 CRITICAL ║
║  Railway        │  CRITICAL   │   HIGH      │  ❌  │    ❌     │ 🔴 CRITICAL ║
║  Apple          │    LOW      │   LOW       │  ✅  │    ✅     │ 🟢 LOW      ║
║                                                                              ║
║  * Includes health-related data (Article 9 special category)                ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

---

## 5. Action Plan

### Immediate (Week 1-2)

| Priority | Processor | Action | Owner |
|:---:|:---|:---|:---|
| 1 | All | Draft standard DPA template | Legal |
| 2 | Veryfi | Initiate DPA negotiation | Legal/Eng |
| 3 | Google | Accept Google Cloud DPA | Legal |
| 4 | Anthropic | Request enterprise DPA | Legal/Eng |
| 5 | Railway | Request DPA/Terms review | Legal |

### Short-term (Week 3-4)

| Priority | Processor | Action | Owner |
|:---:|:---|:---|:---|
| 6 | All US | Draft SCCs for each processor | Legal |
| 7 | All US | Complete Transfer Impact Assessments | DPO |
| 8 | All | Request sub-processor lists | Legal |
| 9 | All | Request security documentation | Security |

### Medium-term (Month 2)

| Priority | Processor | Action | Owner |
|:---:|:---|:---|:---|
| 10 | All | Execute all DPAs | Legal |
| 11 | All | Implement supplementary measures | Eng |
| 12 | Chat AI | Implement data minimization | Eng |
| 13 | All | Establish audit schedule | DPO |

---

*Document prepared as part of GDPR Compliance Assessment for DeepmAInd/Milo Application*
