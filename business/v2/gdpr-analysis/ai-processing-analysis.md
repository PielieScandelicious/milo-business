<div align="center">

# **MILO**
## AI Processing GDPR Analysis v2.0

---

**DeepmAInd B.V.** | January 28, 2026

</div>

---

## AI Processing Overview

| AI Component | Provider | Purpose | GDPR Implications |
|:-------------|:---------|:--------|:------------------|
| **Receipt OCR** | Veryfi | Text extraction | Processor, US transfer |
| **Health Scoring** | Google Gemini | Dietary analysis | Special category data |
| **Categorization** | Gemini | Spending categories | Profiling |
| **Insights** | Gemini | Trend analysis | Automated decision-making |

---

## Gemini 2.0 Flash Integration

### Processing Details

| Attribute | Value |
|:----------|:------|
| **Model** | Gemini 2.0 Flash |
| **Provider** | Google LLC |
| **Location** | USA (Google Cloud) |
| **Data Input** | Line items, purchase context |
| **Data Output** | Health scores, categories, insights |
| **Retention** | Not retained (Gemini API policy) |

### Data Flow

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                          AI PROCESSING FLOW                                   ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   Receipt Data (PostgreSQL)                                                  ║
║        │                                                                      ║
║        ▼                                                                      ║
║   ┌─────────────────────────────────────────────────────────────────────┐    ║
║   │  ANONYMIZATION LAYER                                                 │    ║
║   │  • Remove user ID from prompt                                        │    ║
║   │  • Remove location data                                              │    ║
║   │  • Keep only: line items, date, merchant category                   │    ║
║   └─────────────────────────────────────────────────────────────────────┘    ║
║        │                                                                      ║
║        ▼                                                                      ║
║   Gemini API Request                                                         ║
║   {                                                                           ║
║     "items": ["Organic Milk 2L", "Whole Grain Bread", "Coca-Cola 6pk"],     ║
║     "merchant_type": "grocery"                                               ║
║   }                                                                           ║
║        │                                                                      ║
║        ▼                                                                      ║
║   Gemini API Response                                                        ║
║   {                                                                           ║
║     "health_scores": [85, 78, 25],                                          ║
║     "categories": ["dairy", "grains", "beverages"],                         ║
║     "insights": "Consider reducing sugary drinks"                           ║
║   }                                                                           ║
║        │                                                                      ║
║        ▼                                                                      ║
║   Re-associate with User (PostgreSQL)                                        ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

## Article 22: Automated Decision-Making

### Assessment

| Criterion | MILO's AI | Applicable? |
|:----------|:----------|:-----------:|
| Solely automated decision | No human in loop | ⚠️ Partially |
| Legal effects | No | ❌ No |
| Significant effects | Informational only | ❌ No |

### Analysis

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                    ARTICLE 22 APPLICABILITY ASSESSMENT                        ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   MILO's AI processing:                                                       ║
║                                                                               ║
║   1. SOLELY AUTOMATED?                                                        ║
║      Health scores are AI-generated without human review                     ║
║      → YES, processing is automated                                          ║
║                                                                               ║
║   2. PRODUCES LEGAL EFFECTS?                                                  ║
║      • Does not affect contracts                                             ║
║      • Does not affect legal rights                                          ║
║      → NO legal effects                                                      ║
║                                                                               ║
║   3. SIMILARLY SIGNIFICANT EFFECTS?                                           ║
║      • Does not affect access to services                                    ║
║      • Does not affect credit or employment                                  ║
║      • Purely informational/advisory                                         ║
║      → NO significant effects                                                ║
║                                                                               ║
║   CONCLUSION: Article 22 does NOT strictly apply                             ║
║                                                                               ║
║   HOWEVER: Best practice is to implement safeguards anyway:                  ║
║   • Transparency about AI usage                                              ║
║   • Explanation of scoring methodology                                       ║
║   • Ability to contest scores                                                ║
║   • Option to disable AI features                                            ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

## Article 9: Health Data Processing

### Classification Analysis

| Data Type | Health-Related? | Article 9? |
|:----------|:---------------:|:----------:|
| Receipt line items | Indirect | ⚠️ Borderline |
| Health scores | Yes | ✅ Yes |
| Dietary patterns | Yes | ✅ Yes |
| Food categories | Indirect | ⚠️ Borderline |

### Legal Analysis

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                    ARTICLE 9 HEALTH DATA ANALYSIS                             ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   QUESTION: Are AI-generated health scores "health data" under Art. 9?       ║
║                                                                               ║
║   CONSERVATIVE INTERPRETATION:                                                ║
║   ───────────────────────────                                                 ║
║   Recital 35: "personal data concerning health should include all data      ║
║   pertaining to the health status of a data subject which reveal             ║
║   information relating to the past, current or future physical or mental    ║
║   health status"                                                              ║
║                                                                               ║
║   Health scores derived from food purchases:                                  ║
║   • Reveal information about dietary habits                                  ║
║   • Could indicate health conditions (diabetic-friendly purchases)           ║
║   • Predict future health outcomes                                           ║
║                                                                               ║
║   CONCLUSION: Treat as Article 9 data (conservative approach)                ║
║                                                                               ║
║   REQUIRED: Explicit consent under Art. 9(2)(a)                              ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

## Article 35: DPIA Requirement

### DPIA Triggers Assessment

| Trigger | Present in MILO? |
|:--------|:----------------:|
| Large-scale processing of special categories | ✅ Health data |
| Systematic evaluation/profiling | ✅ Health scoring |
| Innovative technology | ✅ Gemini AI |
| Data concerning vulnerable subjects | ⚠️ Possible |

### DPIA Required

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                         DPIA REQUIREMENT                                      ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   TRIGGERS PRESENT:                                                           ║
║   ✅ Innovative technology (AI/ML)                                           ║
║   ✅ Special category data (health inferences)                               ║
║   ✅ Systematic profiling                                                    ║
║                                                                               ║
║   CONCLUSION: DPIA is MANDATORY                                              ║
║                                                                               ║
║   DPIA must cover:                                                            ║
║   • Systematic description of processing                                     ║
║   • Assessment of necessity and proportionality                              ║
║   • Assessment of risks to individuals                                       ║
║   • Measures to address risks                                                ║
║                                                                               ║
║   Timeline: Complete before launch                                           ║
║   Budget: €8,000-12,000                                                      ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

## AI Transparency Requirements

### GDPR Transparency Obligations

| Requirement | Implementation |
|:------------|:---------------|
| Existence of automated processing | Privacy policy disclosure |
| Logic involved | Methodology explanation |
| Significance and consequences | User-facing explanation |
| Right to human intervention | Contest mechanism |

### User-Facing Transparency

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                      AI TRANSPARENCY UI                                       ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   Health Score Card:                                                         ║
║   ┌─────────────────────────────────────────────────────────────────────┐    ║
║   │                                                                     │    ║
║   │   🩺 Health Score: 72/100                                           │    ║
║   │   ─────────────────────────                                         │    ║
║   │                                                                     │    ║
║   │   🤖 AI-Generated Score                                             │    ║
║   │                                                                     │    ║
║   │   This score is calculated by AI based on the nutritional          │    ║
║   │   profile of items in your receipt.                                │    ║
║   │                                                                     │    ║
║   │   [ℹ️ How is this calculated?]  [🚩 Flag as incorrect]             │    ║
║   │                                                                     │    ║
║   └─────────────────────────────────────────────────────────────────────┘    ║
║                                                                               ║
║   "How is this calculated?" Modal:                                           ║
║   ┌─────────────────────────────────────────────────────────────────────┐    ║
║   │                                                                     │    ║
║   │   How MILO Calculates Health Scores                                │    ║
║   │                                                                     │    ║
║   │   Our AI analyzes each item on your receipt and assigns a          │    ║
║   │   health score from 0-100 based on:                                │    ║
║   │                                                                     │    ║
║   │   • Nutritional density                                            │    ║
║   │   • Processing level                                               │    ║
║   │   • Sugar and sodium content                                       │    ║
║   │   • Whole food vs processed ratio                                  │    ║
║   │                                                                     │    ║
║   │   This is not medical advice. Scores are informational only.       │    ║
║   │                                                                     │    ║
║   │   [Settings: Disable Health Scores]                                │    ║
║   │                                                                     │    ║
║   └─────────────────────────────────────────────────────────────────────┘    ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

## Risk Mitigation Measures

### Technical Safeguards

| Measure | Description | Status |
|:--------|:------------|:------:|
| Anonymization | Remove user ID before API call | ⬜ To implement |
| Data minimization | Only send necessary fields | ⬜ To implement |
| Encryption | TLS 1.3 for all API calls | ✅ Standard |
| Audit logging | Log all AI processing | ⬜ To implement |

### Organizational Safeguards

| Measure | Description | Status |
|:--------|:------------|:------:|
| AI policy | Document AI usage rules | ⬜ To draft |
| Human oversight | Review flagged scores | ⬜ To implement |
| Regular audits | AI accuracy/bias review | ⬜ To schedule |
| Staff training | AI ethics training | ⬜ To plan |

---

## Compliance Checklist

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                      AI COMPLIANCE CHECKLIST                                  ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   ⬜ Explicit consent for health data processing                             ║
║   ⬜ Privacy policy updated with AI disclosure                               ║
║   ⬜ DPIA for AI processing completed                                        ║
║   ⬜ DPA with Google (Gemini) executed                                       ║
║   ⬜ Anonymization layer implemented                                         ║
║   ⬜ "AI-generated" labels in UI                                             ║
║   ⬜ Scoring methodology documented                                          ║
║   ⬜ Contest/flag mechanism built                                            ║
║   ⬜ Opt-out mechanism available                                             ║
║   ⬜ Regular bias audits scheduled                                           ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

## Budget Summary

| Item | Cost |
|:-----|-----:|
| DPIA for AI processing | €8,000 |
| Privacy policy AI section | €1,500 |
| Anonymization implementation | €3,000 |
| Transparency UI | €2,000 |
| Staff training | €1,500 |
| **Total** | **€16,000** |

---

<div align="center">

**Document Version:** 2.0 | January 28, 2026

</div>
