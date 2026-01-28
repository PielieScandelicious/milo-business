# GDPR Compliance Assessment
## AI & Automated Decision-Making Analysis

---

| **Document** | 07 - AI Processing Analysis |
|:---|:---|
| **Reference** | GDPR Articles 13, 14, 22, 35 |
| **Status** | Assessment & Recommendations |

---

## 1. Overview

The Milo application employs multiple AI systems for core functionality. This document analyzes GDPR compliance requirements for AI-based processing, focusing on transparency, automated decision-making rights, and data protection impact assessments.

### AI Systems Inventory

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                         AI SYSTEMS IN MILO APP                               ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  SYSTEM               │ PROVIDER   │ PURPOSE            │ GDPR CONCERN      ║
║  ─────────────────────┼────────────┼────────────────────┼─────────────────  ║
║  Veryfi OCR           │ Veryfi     │ Receipt extraction │ Data accuracy     ║
║  Gemini Categorizer   │ Google     │ Item categorization│ Automated decision║
║  Gemini Health Score  │ Google     │ Health assessment  │ Special category  ║
║  Gemini Chat (V2)     │ Google     │ AI assistant       │ Profiling         ║
║  Claude Chat (V1)     │ Anthropic  │ AI assistant       │ Profiling         ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

---

## 2. Article 22 Analysis: Automated Decision-Making

### 2.1 Article 22 Requirements

> "The data subject shall have the right not to be subject to a decision based solely on automated processing, including profiling, which produces legal effects concerning him or her or similarly significantly affects him or her."

### 2.2 Assessment of AI Processing

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    AUTOMATED DECISION-MAKING ASSESSMENT                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  CRITERIA FOR ARTICLE 22 APPLICATION:                                       │
│                                                                             │
│  1. Solely automated (no human involvement) ............... ✓              │
│  2. Decision based on that processing .................... ✓              │
│  3. Produces legal effects OR significantly affects ....... ?              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### Process-by-Process Assessment

| AI Process | Solely Automated | Decision Made | Significant Effect | Art. 22 Applies |
|:---|:---:|:---|:---|:---:|
| **OCR Extraction** | Yes | Data extraction | No - just digitization | ❌ No |
| **Category Assignment** | Yes | Which category | No - informational | ❌ No |
| **Health Scoring** | Yes | Health rating (0-5) | **Possibly** - health advice | ⚠️ Maybe |
| **Duplicate Detection** | Yes | Block/allow upload | **Yes** - feature denial | ✅ Yes |
| **Rate Limiting** | Yes | Block features | **Yes** - feature denial | ✅ Yes |
| **AI Chat Responses** | Yes | Personalized advice | **Possibly** - influences behavior | ⚠️ Maybe |

### 2.3 Processes Requiring Safeguards

#### Duplicate Detection (Article 22 Applies)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         DUPLICATE DETECTION                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  CURRENT BEHAVIOR:                                                          │
│  • Veryfi assigns duplicate confidence score                               │
│  • If duplicate detected: receipt rejected, record deleted                 │
│  • User receives error message                                             │
│  • No appeal mechanism exists                                               │
│                                                                             │
│  GDPR CONCERN:                                                              │
│  Automated decision that denies user access to a feature                   │
│  (receipt upload) with significant effect on service usage.                │
│                                                                             │
│  REQUIRED SAFEGUARDS:                                                       │
│  □ Right to obtain human intervention                                      │
│  □ Right to express point of view                                          │
│  □ Right to contest the decision                                           │
│                                                                             │
│  IMPLEMENTATION:                                                            │
│  • Add "Appeal Duplicate Decision" button                                   │
│  • Allow user to provide context                                            │
│  • Manual review process (within 48 hours)                                  │
│  • Override capability for false positives                                  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### Rate Limiting (Article 22 Applies)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                            RATE LIMITING                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  CURRENT BEHAVIOR:                                                          │
│  • 15 receipts per 30-day rolling window (free tier)                       │
│  • 100 chat messages per 30-day window                                     │
│  • Automated blocking when limit reached                                   │
│  • No override mechanism                                                    │
│                                                                             │
│  GDPR CONCERN:                                                              │
│  While rate limiting is legitimate, the automated nature of                │
│  feature denial may trigger Article 22.                                     │
│                                                                             │
│  MITIGATION:                                                                │
│  • Clear disclosure of limits before signup                                │
│  • Transparent counter showing remaining usage                             │
│  • Clear explanation of how to upgrade                                     │
│  • This is likely covered by contract exception (Art. 22(2)(a))           │
│                                                                             │
│  RECOMMENDATION:                                                            │
│  Document rate limiting as "necessary for contract performance"            │
│  and include clear terms in service agreement.                             │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### Health Scoring (Special Consideration)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           HEALTH SCORING                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  CURRENT BEHAVIOR:                                                          │
│  • Google Gemini assigns health score (0-5) to food items                  │
│  • Based on AI assessment of nutritional value                             │
│  • Displayed in analytics, used in AI chat                                 │
│  • User cannot override scores                                              │
│                                                                             │
│  GDPR CONCERNS:                                                             │
│                                                                             │
│  1. SPECIAL CATEGORY DATA (Article 9)                                       │
│     Health scores = "data concerning health"                               │
│     Requires explicit consent                                              │
│                                                                             │
│  2. AUTOMATED DECISION-MAKING (Article 22)                                  │
│     If health scores influence user behavior (diet choices),               │
│     this could be "significantly affecting" the data subject.              │
│                                                                             │
│  3. TRANSPARENCY (Article 13/14)                                            │
│     Users must be informed about the logic involved                        │
│     in health score calculation.                                           │
│                                                                             │
│  REQUIRED ACTIONS:                                                          │
│  □ Implement explicit consent for health features                          │
│  □ Document and disclose health scoring methodology                        │
│  □ Allow users to override/correct health scores                           │
│  □ Provide option to disable health scoring entirely                       │
│  □ Consider DPIA for health scoring system                                 │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Transparency Requirements (Articles 13 & 14)

### 3.1 Required Disclosures

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    ARTICLE 13(2)(f) REQUIREMENTS                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  For automated decision-making including profiling, disclose:              │
│                                                                             │
│  (1) THE EXISTENCE of automated decision-making                            │
│      "We use AI to automatically categorize your purchases and             │
│       assign health scores to food items."                                  │
│                                                                             │
│  (2) MEANINGFUL INFORMATION about the logic involved                       │
│      "Health scores are based on nutritional guidelines and                │
│       AI assessment of ingredients, portion sizes, and food types."        │
│                                                                             │
│  (3) SIGNIFICANCE and ENVISAGED CONSEQUENCES                               │
│      "Health scores help you understand the nutritional quality            │
│       of your purchases. Low scores indicate less healthy items."          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 3.2 Implementation: AI Transparency Page

```
In-App AI Transparency:
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│  🤖 How Milo Uses AI                                                       │
│                                                                             │
│  ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│  📄 RECEIPT PROCESSING                                                      │
│  ────────────────────────────────────────────────────────────────────────  │
│  When you upload a receipt, we use AI to:                                  │
│  • Extract text from the image (Veryfi OCR)                                │
│  • Identify the store, date, and items                                     │
│  • Detect duplicate receipts                                                │
│                                                                             │
│  Accuracy: ~95%. You can edit any extracted data.                          │
│                                                                             │
│  ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│  📦 CATEGORY ASSIGNMENT                                                     │
│  ────────────────────────────────────────────────────────────────────────  │
│  Items are automatically sorted into 16 categories:                        │
│  Fruits & Vegetables, Dairy, Meat, etc.                                    │
│                                                                             │
│  How it works:                                                              │
│  • Google Gemini AI analyzes item names                                    │
│  • Matches items to most relevant category                                 │
│  • Learns from common shopping patterns                                    │
│                                                                             │
│  You can change any category assignment.                                   │
│                                                                             │
│  ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│  🏥 HEALTH SCORES                                                           │
│  ────────────────────────────────────────────────────────────────────────  │
│  Food items receive a health score from 0 (least healthy)                  │
│  to 5 (most healthy).                                                       │
│                                                                             │
│  How scores are calculated:                                                 │
│  • Based on nutritional guidelines                                         │
│  • AI assesses likely ingredients and nutritional value                    │
│  • Fresh produce scores higher; processed foods score lower               │
│                                                                             │
│  Important notes:                                                           │
│  • Scores are estimates, not medical advice                                │
│  • Based on general nutrition principles                                   │
│  • May not account for individual dietary needs                            │
│                                                                             │
│  You can:                                                                   │
│  • Override any health score                                               │
│  • Disable health scoring in Settings                                      │
│                                                                             │
│  ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│  💬 AI CHAT ASSISTANT                                                       │
│  ────────────────────────────────────────────────────────────────────────  │
│  Milo's chat assistant uses your transaction history to                    │
│  provide personalized spending insights.                                    │
│                                                                             │
│  Data used in chat:                                                         │
│  • Your name (for personalization)                                         │
│  • Recent transactions (stores, items, amounts)                            │
│  • Categories and health scores (if enabled)                               │
│                                                                             │
│  AI responses are generated by Google Gemini or Anthropic Claude.         │
│  Responses are suggestions only, not financial or health advice.          │
│                                                                             │
│  [Manage AI Settings]                                                      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. Data Protection Impact Assessment

### 4.1 DPIA Requirement

GDPR Article 35 requires a DPIA when processing is "likely to result in a high risk to the rights and freedoms of natural persons."

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         DPIA THRESHOLD ASSESSMENT                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  EDPB CRITERIA (2+ triggers DPIA requirement):                             │
│                                                                             │
│  □ Evaluation/Scoring ............................ ✅ Health scoring       │
│  □ Automated decision with legal/significant effect  ⚠️ Maybe             │
│  □ Systematic monitoring ......................... ❌ No                   │
│  □ Sensitive data ................................ ✅ Health data          │
│  □ Large scale processing ........................ ❌ Not yet              │
│  □ Data matching/combining ....................... ✅ Multiple sources     │
│  □ Vulnerable data subjects ...................... ❌ No                   │
│  □ Innovative technology ......................... ✅ Generative AI        │
│  □ Prevents exercising rights .................... ❌ No                   │
│                                                                             │
│  TRIGGERS MET: 4 (Scoring, Sensitive, Combining, Innovative)               │
│                                                                             │
│  CONCLUSION: DPIA REQUIRED FOR AI PROCESSING                               │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 4.2 DPIA Template for Health Scoring

```
DATA PROTECTION IMPACT ASSESSMENT
═══════════════════════════════════════════════════════════════════════════════

PROCESSING: Health Scoring of Food Items
DATE: [To be completed]
ASSESSOR: [DPO/Privacy Lead]

───────────────────────────────────────────────────────────────────────────────
1. DESCRIPTION OF PROCESSING
───────────────────────────────────────────────────────────────────────────────

Purpose:
To provide users with health scores (0-5) for food items in their receipts,
enabling dietary insights and health-conscious shopping decisions.

Data processed:
• Item names extracted from receipts
• Store context
• AI-generated health assessments

Processing operations:
1. User uploads receipt
2. Veryfi extracts item names
3. Item names sent to Google Gemini
4. Gemini assigns health score (0-5)
5. Score stored in database
6. Score displayed to user
7. Score used in analytics and AI chat

Technology used:
• Google Gemini 2.0 Flash (generative AI)
• Structured JSON prompts
• Automated processing pipeline

───────────────────────────────────────────────────────────────────────────────
2. NECESSITY AND PROPORTIONALITY
───────────────────────────────────────────────────────────────────────────────

Legal basis: Explicit consent (Article 9(2)(a))

Necessity:
• Health scoring is a key differentiator of the Milo app
• Users specifically want dietary insights
• Feature is optional (can be disabled)

Data minimization:
✅ Only item names sent to AI (no user identity)
✅ Scores are simple integers (0-5)
⚠️ Could minimize by sending fewer items per request

Purpose limitation:
✅ Scores used only for user insights
✅ Aggregated scores may be used in anonymized analytics
❌ Health scores currently included in chat context to AI

───────────────────────────────────────────────────────────────────────────────
3. RISK ASSESSMENT
───────────────────────────────────────────────────────────────────────────────

RISK 1: Inaccurate health scores
Likelihood: MEDIUM (AI may misinterpret items)
Severity: MEDIUM (may influence dietary decisions)
Impact: User makes suboptimal food choices based on incorrect scores
Mitigation:
• Allow user override of scores
• Disclaimer that scores are estimates
• Do not present as medical advice

RISK 2: Re-identification through health patterns
Likelihood: LOW (would require additional data)
Severity: MEDIUM (health data is sensitive)
Impact: User's health profile could be inferred
Mitigation:
• K-anonymity in any aggregated data
• Explicit consent for data sharing
• Health scores excluded from data monetization (or separate consent)

RISK 3: Discrimination based on health scores
Likelihood: LOW (B2B use case, anonymized)
Severity: HIGH (if insurance/employers accessed)
Impact: Adverse decisions about user
Mitigation:
• Never sell individual-level health data
• Strict anonymization requirements
• DPA restrictions on B2B data use

RISK 4: Distress from health assessments
Likelihood: LOW
Severity: LOW-MEDIUM
Impact: User experiences negative emotions about eating habits
Mitigation:
• Positive framing of insights
• Focus on improvement, not judgment
• Clear option to disable

───────────────────────────────────────────────────────────────────────────────
4. MEASURES TO ADDRESS RISKS
───────────────────────────────────────────────────────────────────────────────

Technical measures:
□ Encryption of health data in transit and at rest
□ Pseudonymization where possible
□ Automated deletion per retention policy
□ Access controls limiting who can view raw data

Organizational measures:
□ Staff training on health data sensitivity
□ Audit logging of health data access
□ Regular review of AI accuracy
□ User feedback mechanism

Rights safeguards:
□ Easy withdrawal of health scoring consent
□ Override capability for any health score
□ Export of health scores in data portability
□ Deletion of health scores on request

───────────────────────────────────────────────────────────────────────────────
5. CONSULTATION
───────────────────────────────────────────────────────────────────────────────

Internal consultation:
□ Legal team
□ Engineering team
□ Product team

External consultation:
□ Consider consulting supervisory authority (not required if risks mitigated)
□ User feedback during beta testing

───────────────────────────────────────────────────────────────────────────────
6. CONCLUSION
───────────────────────────────────────────────────────────────────────────────

Overall risk level: MEDIUM (reducible to LOW with mitigations)

Proceed with processing: YES, with conditions

Conditions:
1. Implement explicit consent for health features
2. Add override capability for health scores
3. Include clear disclaimers
4. Exclude health data from standard data monetization
5. Review AI accuracy quarterly

Review date: [Date + 12 months]
```

---

## 5. AI Model Training Considerations

### 5.1 Data Use for Model Training

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    AI MODEL TRAINING CONSIDERATIONS                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  CONCERN:                                                                   │
│  Some AI providers may use input data to train or improve models.          │
│  This could constitute:                                                     │
│  • New processing purpose (requiring consent)                              │
│  • Indefinite retention of user data                                       │
│  • Data sharing with third parties (training collaborators)                │
│                                                                             │
│  PROVIDER ASSESSMENT:                                                       │
│                                                                             │
│  VERYFI:                                                                    │
│  • Review terms of service for training provisions                         │
│  • Request contractual exclusion from training use                         │
│                                                                             │
│  GOOGLE GEMINI:                                                             │
│  • Google Cloud AI Platform typically doesn't use customer data            │
│  • Verify in DPA/terms of service                                          │
│  • Enterprise agreements usually exclude training                          │
│                                                                             │
│  ANTHROPIC CLAUDE:                                                          │
│  • API terms typically exclude training use                                │
│  • Verify current terms                                                    │
│  • Request contractual confirmation                                        │
│                                                                             │
│  REQUIRED ACTION:                                                           │
│  Obtain written confirmation from each AI provider that user data          │
│  will NOT be used for model training, improvement, or any purpose          │
│  beyond the immediate API response.                                         │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 6. Recommendations

### 6.1 Immediate Actions

| Priority | Action | Timeline |
|:---:|:---|:---|
| 1 | Implement explicit consent for health scoring | Week 1-2 |
| 2 | Add AI transparency page in app | Week 2-3 |
| 3 | Create health score override capability | Week 3-4 |
| 4 | Add duplicate detection appeal mechanism | Week 4-5 |
| 5 | Complete DPIA for health scoring | Week 2-3 |

### 6.2 Medium-term Actions

| Priority | Action | Timeline |
|:---:|:---|:---|
| 6 | Complete DPIA for AI chat profiling | Month 2 |
| 7 | Obtain AI provider training exclusion confirmations | Month 2 |
| 8 | Implement AI accuracy monitoring | Month 2-3 |
| 9 | Review and minimize chat context data | Month 1-2 |

### 6.3 Ongoing Requirements

- Quarterly review of AI processing accuracy
- Annual DPIA refresh
- Monitor regulatory guidance on AI (EU AI Act)
- Update transparency disclosures as AI features evolve

---

## 7. EU AI Act Considerations

### 7.1 Upcoming Requirements

The EU AI Act (effective 2024-2027) introduces additional requirements for AI systems. Consider future compliance:

| AI Act Category | Milo AI Systems | Requirements |
|:---|:---|:---|
| High-risk | Health scoring (possibly) | Risk management, data governance, transparency |
| Limited risk | Chat assistant | Transparency obligations |
| Minimal risk | OCR, categorization | Minimal requirements |

### 7.2 Preparation Recommendations

- Monitor AI Act implementation guidance
- Consider health scoring risk classification
- Prepare technical documentation
- Plan for potential registration requirements

---

*Document prepared as part of GDPR Compliance Assessment for DeepmAInd/Milo Application*
