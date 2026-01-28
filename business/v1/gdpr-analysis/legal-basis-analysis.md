# GDPR Compliance Assessment
## Legal Basis Analysis

---

| **Document** | 02 - Legal Basis Analysis |
|:---|:---|
| **Reference** | GDPR Articles 6, 7, 9 |
| **Status** | Critical Gap Identified |

---

## 1. Overview

Under GDPR Article 6, personal data processing is only lawful if at least one of six legal bases applies. This document analyzes the appropriate legal basis for each processing activity in the Milo application.

### GDPR Article 6(1) - Lawful Bases

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        SIX LAWFUL BASES FOR PROCESSING                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  (a) CONSENT                 │  Data subject has given consent              │
│  (b) CONTRACT                │  Processing necessary for contract           │
│  (c) LEGAL OBLIGATION        │  Processing required by law                  │
│  (d) VITAL INTERESTS         │  Protect life of data subject                │
│  (e) PUBLIC TASK             │  Official authority or public interest       │
│  (f) LEGITIMATE INTERESTS    │  Controller's legitimate interests           │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Processing Activities & Legal Basis Assessment

### 2.1 User Account Management

| Processing Activity | Recommended Basis | Justification |
|:---|:---|:---|
| Account creation | **Contract (Art. 6(1)(b))** | Necessary to provide the service |
| Email storage | **Contract (Art. 6(1)(b))** | Account identification |
| Name storage | **Contract (Art. 6(1)(b))** | Service personalization |
| Profile data | **Contract (Art. 6(1)(b))** | Core functionality |

```
✅ ASSESSMENT: Contract basis is appropriate for core account data
⚠️  ACTION REQUIRED: Document in privacy policy and terms of service
```

### 2.2 Receipt Processing

| Processing Activity | Recommended Basis | Justification |
|:---|:---|:---|
| Receipt upload | **Contract (Art. 6(1)(b))** | Core service feature |
| OCR extraction | **Contract (Art. 6(1)(b))** | Processing user's receipts |
| Transaction storage | **Contract (Art. 6(1)(b))** | Service delivery |
| Image storage | **Contract (Art. 6(1)(b))** | User-requested backup |

```
✅ ASSESSMENT: Contract basis appropriate for receipt processing
⚠️  ACTION REQUIRED:
    - Document data sharing with Veryfi (processor)
    - Ensure DPA in place with Veryfi
    - Define retention periods in contract terms
```

### 2.3 AI Categorization

| Processing Activity | Recommended Basis | Justification |
|:---|:---|:---|
| Item categorization | **Contract (Art. 6(1)(b))** | Core analytics feature |
| Store normalization | **Contract (Art. 6(1)(b))** | Service functionality |

```
✅ ASSESSMENT: Contract basis appropriate for categorization
⚠️  ACTION REQUIRED:
    - Document data sharing with Google Gemini
    - Ensure DPA in place
```

### 2.4 Health Scoring ⚠️ SPECIAL CATEGORY DATA

| Processing Activity | Required Basis | Justification |
|:---|:---|:---|
| Health score calculation | **Explicit Consent (Art. 9(2)(a))** | Health data = special category |
| Dietary pattern analysis | **Explicit Consent (Art. 9(2)(a))** | Health-related insights |
| Health trend display | **Explicit Consent (Art. 9(2)(a))** | Health information |

```
🔴 CRITICAL FINDING: Health scores constitute "data concerning health" under
   Article 9. Standard contract basis is INSUFFICIENT.

REQUIRED ACTIONS:
1. Implement explicit consent mechanism for health features
2. Allow users to opt-out while using other features
3. Document consent in clear, plain language
4. Provide granular control (health scoring ON/OFF)
5. Ensure consent is freely given, specific, informed, and unambiguous
```

#### Health Data Definition (Article 9)

> "Data concerning health" means personal data related to the physical or mental health of a natural person, including the provision of health care services, which reveal information about his or her health status.

The Milo health scoring system (0-5 scale) provides:
- Nutritional assessment of food purchases
- Dietary pattern insights
- Health-related recommendations via AI chat

**This constitutes health data requiring explicit consent.**

### 2.5 AI Chat Service

| Processing Activity | Recommended Basis | Justification |
|:---|:---|:---|
| Chat message processing | **Contract (Art. 6(1)(b))** | Core feature |
| Context provision to AI | **Consent (Art. 6(1)(a))** | Extensive data sharing |
| Chat history retention | **Consent (Art. 6(1)(a))** | Not strictly necessary |

```
⚠️  ASSESSMENT: Mixed basis required

CONTRACT appropriate for:
- Basic chat functionality
- Minimal context (current query)

CONSENT required for:
- Sharing 90-day transaction history with AI
- Retention of chat history beyond session
- Personalization features using health data
```

#### Context Data Shared with AI Providers

| Data Element | Basis Required |
|:---|:---|
| First name | Contract |
| Last name | Contract |
| Gender | Contract |
| 90-day transactions | Consent |
| Store names | Contract |
| Item names | Contract |
| Prices | Contract |
| Categories | Contract |
| **Health scores** | **Explicit Consent (Art. 9)** |
| Purchase dates | Contract |

### 2.6 Analytics & Insights

| Processing Activity | Recommended Basis | Justification |
|:---|:---|:---|
| Spending summaries | **Contract (Art. 6(1)(b))** | Core feature |
| Category breakdowns | **Contract (Art. 6(1)(b))** | Core feature |
| Trend analysis | **Contract (Art. 6(1)(b))** | Core feature |
| Store analytics | **Contract (Art. 6(1)(b))** | Core feature |

```
✅ ASSESSMENT: Contract basis appropriate for user-facing analytics
```

### 2.7 Firebase Analytics

| Processing Activity | Recommended Basis | Justification |
|:---|:---|:---|
| App usage tracking | **Legitimate Interest (Art. 6(1)(f))** | Service improvement |
| Event logging | **Legitimate Interest (Art. 6(1)(f))** | Debugging, improvement |
| Performance monitoring | **Legitimate Interest (Art. 6(1)(f))** | Service reliability |

```
⚠️  ASSESSMENT: Legitimate interest may apply with proper documentation

REQUIRED ACTIONS:
1. Document legitimate interest assessment (LIA)
2. Implement opt-out mechanism for analytics
3. Disclose in privacy policy
4. Consider using consent for enhanced tracking
```

### 2.8 Data Monetization (B2B) 🔴 CRITICAL

| Processing Activity | Required Basis | Justification |
|:---|:---|:---|
| Anonymization | **Legitimate Interest** | If truly anonymized |
| Aggregated reporting | **Consent (Art. 6(1)(a))** | Beyond original purpose |
| Individual-level data | **Explicit Consent** | Sensitive profiling |
| Health data sales | **Explicit Consent (Art. 9)** | Special category |

```
🔴 CRITICAL FINDING: Data monetization requires tiered consent architecture

TIER 1 - AGGREGATED STATISTICS (may use legitimate interest):
├─ Minimum 50+ users per aggregation
├─ No individual-level patterns identifiable
├─ Regional/category summaries only
└─ STILL recommend consent for transparency

TIER 2 - ANONYMIZED INDIVIDUAL DATA (requires consent):
├─ K-anonymity verified (k≥10)
├─ Differential privacy applied
├─ No direct identifiers
└─ User explicitly opted in

TIER 3 - ENHANCED BEHAVIORAL DATA (requires explicit consent):
├─ Detailed shopping patterns
├─ Health-related insights
├─ Higher value data products
└─ Premium consent with clear value exchange
```

---

## 3. Special Category Data Analysis

### Article 9 - Health Data

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      HEALTH DATA PROCESSING IN MILO                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  DATA ELEMENT              │  CLASSIFICATION        │  CONSENT REQUIRED     │
│                                                                             │
│  Health scores (0-5)       │  Health data           │  ✅ Explicit          │
│  Dietary patterns          │  Health data           │  ✅ Explicit          │
│  Nutrition insights        │  Health data           │  ✅ Explicit          │
│  Health trend analysis     │  Health data           │  ✅ Explicit          │
│                                                                             │
│  LEGAL BASIS: Article 9(2)(a) - Explicit consent                            │
│                                                                             │
│  IMPLEMENTATION REQUIREMENTS:                                               │
│  □ Separate consent toggle for health features                              │
│  □ Clear explanation of health data processing                              │
│  □ Ability to use app without health features                               │
│  □ Easy withdrawal of consent                                               │
│  □ Documentation of consent timestamp                                       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Article 9(2) - Exceptions Analysis

| Exception | Applicability to Milo |
|:---|:---|
| (a) Explicit consent | ✅ **Primary basis to use** |
| (b) Employment/social law | ❌ Not applicable |
| (c) Vital interests | ❌ Not applicable |
| (d) Foundation/association | ❌ Not applicable |
| (e) Made public by subject | ❌ Not applicable |
| (f) Legal claims | ❌ Not applicable |
| (g) Substantial public interest | ❌ Not applicable |
| (h) Health care | ❌ Not a healthcare provider |
| (i) Public health | ❌ Not applicable |
| (j) Research/statistics | ⚠️ Potentially for anonymized B2B |

---

## 4. Consent Requirements

### 4.1 Valid Consent Criteria (Article 7)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        GDPR CONSENT REQUIREMENTS                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ✓ FREELY GIVEN                                                             │
│    └─ Service must work without optional consents                           │
│    └─ No penalty for refusing non-essential consent                         │
│                                                                             │
│  ✓ SPECIFIC                                                                 │
│    └─ Separate consent for each distinct purpose                            │
│    └─ No bundled consents for unrelated processing                          │
│                                                                             │
│  ✓ INFORMED                                                                 │
│    └─ Clear explanation of what data is processed                           │
│    └─ Identity of controller and any recipients disclosed                   │
│    └─ Purpose of processing explained                                       │
│                                                                             │
│  ✓ UNAMBIGUOUS                                                              │
│    └─ Clear affirmative action (no pre-ticked boxes)                        │
│    └─ Active opt-in required                                                │
│                                                                             │
│  FOR SPECIAL CATEGORIES (Health Data):                                      │
│  ✓ EXPLICIT                                                                 │
│    └─ Express statement of consent                                          │
│    └─ Signature or equivalent electronic mechanism                          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 4.2 Required Consent Collection Points

| Consent Point | Type | Processing Covered |
|:---|:---|:---|
| **Onboarding** | Standard | Terms, Privacy Policy acceptance |
| **Health Features** | Explicit | Health scoring, dietary insights |
| **AI Chat Context** | Standard | Transaction history sharing with AI |
| **Data Monetization Tier 2** | Standard | Anonymized panel participation |
| **Data Monetization Tier 3** | Explicit | Enhanced behavioral tracking |
| **Analytics** | Soft opt-out | Firebase analytics |

### 4.3 Consent UI Requirements

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    RECOMMENDED CONSENT ARCHITECTURE                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ONBOARDING SCREEN 1: Essential Terms                                       │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                                                                       │  │
│  │  To use Milo, we need to process your:                                │  │
│  │  • Account information (email, name)                                  │  │
│  │  • Receipts you upload                                                │  │
│  │  • Transaction data for your analytics                                │  │
│  │                                                                       │  │
│  │  [Read Privacy Policy]  [Read Terms of Service]                       │  │
│  │                                                                       │  │
│  │  [ I Accept ] ← Required for service                                  │  │
│  │                                                                       │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│  ONBOARDING SCREEN 2: Optional Features                                     │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                                                                       │  │
│  │  HEALTH INSIGHTS (Optional)                                           │  │
│  │  Get health scores and dietary insights for your food purchases.      │  │
│  │  This involves processing health-related data.                        │  │
│  │                                                                       │  │
│  │  [ ] Enable health scoring (requires explicit consent)                │  │
│  │                                                                       │  │
│  │  AI PERSONALIZATION (Optional)                                        │  │
│  │  Allow Milo AI to access your transaction history for better advice.  │  │
│  │                                                                       │  │
│  │  [ ] Share transaction history with AI assistant                      │  │
│  │                                                                       │  │
│  │  DATA CONTRIBUTION (Optional)                                         │  │
│  │  Contribute anonymized data to help improve products.                 │  │
│  │  Learn more about our data partnership program.                       │  │
│  │                                                                       │  │
│  │  [ ] Participate in anonymized research panel                         │  │
│  │                                                                       │  │
│  │  [Continue] or [Skip for now]                                         │  │
│  │                                                                       │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 5. Legitimate Interest Assessment

### 5.1 Firebase Analytics

| Assessment Element | Analysis |
|:---|:---|
| **Purpose** | App improvement, debugging, performance |
| **Necessity** | Proportionate to purpose |
| **Balance Test** | Low privacy impact vs. significant business benefit |
| **Safeguards** | Pseudonymization, limited retention |
| **User Expectations** | Reasonable for mobile apps |

```
LEGITIMATE INTEREST ASSESSMENT RESULT: ✅ Likely valid

CONDITIONS:
1. Implement opt-out mechanism
2. Disclose in privacy policy
3. Minimize data collected
4. Set reasonable retention (90 days recommended)
```

### 5.2 Service Improvement

| Assessment Element | Analysis |
|:---|:---|
| **Purpose** | Product development, feature improvement |
| **Necessity** | Aggregated usage data sufficient |
| **Balance Test** | Must be anonymized/aggregated |
| **Safeguards** | K-anonymity, no individual tracking |
| **User Expectations** | Reasonable if disclosed |

```
LEGITIMATE INTEREST ASSESSMENT RESULT: ⚠️ Valid only for aggregated data

NOT VALID FOR:
- Individual-level behavioral analysis
- Detailed profiling
- Health-related insights
- Data monetization
```

---

## 6. Legal Basis Summary Matrix

| Processing Activity | Art. 6 Basis | Art. 9 Required | Status |
|:---|:---|:---:|:---:|
| Account creation | Contract | No | 🟡 Document |
| Receipt processing | Contract | No | 🟡 Document |
| Transaction storage | Contract | No | 🟡 Document |
| Basic analytics | Contract | No | 🟡 Document |
| AI categorization | Contract | No | 🟡 Document |
| **Health scoring** | Consent | **Yes** | 🔴 Implement |
| **AI chat (full context)** | Consent | **Yes** | 🔴 Implement |
| Firebase analytics | Legit. Interest | No | 🟡 Document LIA |
| **Data monetization** | Consent | **If health** | 🔴 Implement |

---

## 7. Action Items

### 🔴 Critical (Before Launch)

1. **Implement explicit consent for health features**
   - Separate toggle for health scoring
   - Clear disclosure of health data processing
   - Store consent timestamp and version

2. **Implement consent for data monetization**
   - Tiered consent architecture
   - Clear value exchange communication
   - Easy withdrawal mechanism

3. **Document all legal bases in Privacy Policy**
   - Table of processing activities
   - Legal basis for each
   - User rights for each basis

### 🟠 High Priority (Within 30 Days)

4. **Create Legitimate Interest Assessments**
   - Firebase analytics LIA
   - Service improvement LIA
   - Document balancing tests

5. **Implement consent management system**
   - Consent collection UI
   - Consent storage (timestamp, version, IP)
   - Consent withdrawal mechanism

### 🟡 Medium Priority (Within 60 Days)

6. **Review consent regularly**
   - Re-consent on material changes
   - Consent refresh for long-term users
   - Audit consent records quarterly

---

## 8. Legal Basis Decision Tree

```
                         ┌─────────────────────────┐
                         │    IS PROCESSING        │
                         │    NECESSARY FOR        │
                         │    THE SERVICE?         │
                         └───────────┬─────────────┘
                                     │
                    ┌────────────────┼────────────────┐
                    │                │                │
                   YES              MAYBE             NO
                    │                │                │
                    ▼                ▼                ▼
            ┌───────────┐    ┌───────────────┐   ┌───────────┐
            │ CONTRACT  │    │ ASSESS        │   │ CONSENT   │
            │ Art 6(1)b │    │ LEGIT INT     │   │ REQUIRED  │
            └───────────┘    └───────┬───────┘   └───────────┘
                                     │
                                     │
                         ┌───────────┴───────────┐
                         │                       │
                     BALANCED               NOT BALANCED
                         │                       │
                         ▼                       ▼
                 ┌───────────────┐       ┌───────────────┐
                 │ LEGIT INT     │       │ CONSENT       │
                 │ Art 6(1)f     │       │ REQUIRED      │
                 └───────────────┘       └───────────────┘


                 ┌─────────────────────────────────────┐
                 │    IS DATA HEALTH-RELATED?          │
                 │    (Special Category)               │
                 └────────────────┬────────────────────┘
                                  │
                    ┌─────────────┼─────────────┐
                    │             │             │
                   YES           MAYBE         NO
                    │             │             │
                    ▼             ▼             ▼
            ┌───────────┐  ┌───────────┐  ┌───────────┐
            │ EXPLICIT  │  │ SEEK      │  │ STANDARD  │
            │ CONSENT   │  │ LEGAL     │  │ BASIS     │
            │ Art 9(2)a │  │ ADVICE    │  │ APPLIES   │
            └───────────┘  └───────────┘  └───────────┘
```

---

*Document prepared as part of GDPR Compliance Assessment for DeepmAInd/Milo Application*
