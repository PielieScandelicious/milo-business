<div align="center">

# **MILO**
## Data Mapping & Inventory v2.0

---

**DeepmAInd B.V.** | January 28, 2026

</div>

---

## Data Categories Overview

| Category | Type | Volume | Retention | Legal Basis |
|:---------|:-----|:-------|:----------|:------------|
| **User Identity** | Personal | All users | Account lifetime + 30 days | Contract |
| **Receipt Data** | Personal/Financial | 25-50/user/mo | 24 months | Consent |
| **Health Scores** | Special Category | Per receipt | 24 months | Explicit Consent |
| **Analytics** | Behavioral | All users | 13 months | Legitimate Interest |
| **Device Data** | Technical | All users | Session | Contract |

---

## User Identity Data

### Collection Points

| Data Element | Source | Purpose | Storage |
|:-------------|:-------|:--------|:--------|
| Email address | Registration | Account, notifications | PostgreSQL |
| Display name | Registration | Personalization | PostgreSQL |
| Profile photo | Optional upload | Personalization | Firebase Storage |
| Apple ID token | Sign in with Apple | Authentication | Firebase Auth |
| Google ID token | Google Sign-In | Authentication | Firebase Auth |

### Data Flow

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                           USER IDENTITY FLOW                                  ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   User Input → iOS App → Firebase Auth → PostgreSQL (Railway)                ║
║                              ↓                                                ║
║                         Token stored                                          ║
║                         locally (Keychain)                                    ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

## Receipt Data

### Collection Points

| Data Element | Source | Purpose | Storage |
|:-------------|:-------|:--------|:--------|
| Receipt image | Camera/Photos | OCR processing | Veryfi (transient) |
| Merchant name | OCR extraction | Categorization | PostgreSQL |
| Transaction date | OCR extraction | Analytics | PostgreSQL |
| Line items | OCR extraction | Health scoring | PostgreSQL |
| Total amount | OCR extraction | Spending analytics | PostgreSQL |
| Payment method | OCR extraction | Analytics | PostgreSQL |
| Location | OCR extraction | Categorization | PostgreSQL |

### Data Flow

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                           RECEIPT DATA FLOW                                   ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   Camera → iOS App → Veryfi API → FastAPI Backend → PostgreSQL               ║
║              │           │              │                                     ║
║              │           │              └─→ Gemini AI (health scoring)       ║
║              │           │                                                    ║
║              │           └─→ Image deleted after OCR                         ║
║              │                                                                ║
║              └─→ Local cache (encrypted)                                     ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

## Health Score Data

### Collection Points

| Data Element | Source | Purpose | Storage |
|:-------------|:-------|:--------|:--------|
| Item health score | AI inference | User insight | PostgreSQL |
| Category score | Aggregation | Dashboard | PostgreSQL |
| Trend data | Calculation | Analytics | PostgreSQL |
| Dietary flags | AI inference | Recommendations | PostgreSQL |

### Special Category Handling

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                    ARTICLE 9 - HEALTH DATA HANDLING                          ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   REQUIREMENT: Explicit consent for health-related processing                ║
║                                                                               ║
║   Implementation:                                                             ║
║   ┌─────────────────────────────────────────────────────────────────────┐    ║
║   │ ☑ I consent to MILO analyzing my purchases to provide              │    ║
║   │   health and wellness insights. I understand this involves         │    ║
║   │   processing data about my dietary choices.                        │    ║
║   └─────────────────────────────────────────────────────────────────────┘    ║
║                                                                               ║
║   Withdrawal: Settings → Privacy → Disable Health Scoring                    ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

## Analytics Data

### Collection Points

| Data Element | Source | Purpose | Storage |
|:-------------|:-------|:--------|:--------|
| App opens | Firebase | Engagement | Firebase Analytics |
| Feature usage | Firebase | Product improvement | Firebase Analytics |
| Screen views | Firebase | UX optimization | Firebase Analytics |
| Crash data | Firebase | Debugging | Firebase Crashlytics |
| Device type | Firebase | Compatibility | Firebase Analytics |

### Retention Policy

| Data Type | Retention | Justification |
|:----------|:----------|:--------------|
| Event data | 13 months | Year-over-year analysis |
| User properties | Account lifetime | Personalization |
| Crash logs | 90 days | Debugging window |

---

## Data Storage Locations

### Primary Storage

| System | Location | Data Types | Encryption |
|:-------|:---------|:-----------|:-----------|
| PostgreSQL | Railway (EU) | Core user data | AES-256 at rest |
| Firebase Auth | Google Cloud | Auth tokens | Google encryption |
| Firebase Storage | Google Cloud | Profile images | Google encryption |
| Firebase Analytics | Google Cloud | Event data | Google encryption |

### Processor Storage

| Processor | Location | Data Types | Retention |
|:----------|:---------|:-----------|:----------|
| Veryfi | USA | Receipt images | Transient (<24h) |
| Google Gemini | USA | Line items (text) | Not retained |
| Railway | EU-available | All core data | As configured |

---

## Data Inventory Summary

### By Volume (Monthly - Conservative)

| Data Type | Records/Month | Storage Size |
|:----------|:-------------:|:------------:|
| User registrations | ~2,000 | 200 KB |
| Receipt records | ~75,000 | 15 MB |
| Line items | ~500,000 | 50 MB |
| Health scores | ~500,000 | 25 MB |
| Analytics events | ~2,000,000 | 100 MB |

### By Sensitivity

| Level | Data Types | Protection |
|:------|:-----------|:-----------|
| 🔴 **Critical** | Health scores, dietary data | Explicit consent, encryption |
| 🟠 **High** | Financial data, receipts | Standard consent, encryption |
| 🟡 **Medium** | Contact info, preferences | Contract basis, encryption |
| 🟢 **Low** | Analytics, device info | Legitimate interest |

---

## Cross-Border Transfers

| Data Flow | Origin | Destination | Mechanism |
|:----------|:-------|:------------|:----------|
| Receipt OCR | EU | USA (Veryfi) | SCCs required |
| AI Processing | EU | USA (Google) | SCCs required |
| Analytics | EU | USA (Firebase) | Google DPA |
| Core storage | EU | EU (Railway) | No transfer |

---

<div align="center">

**Document Version:** 2.0 | January 28, 2026

</div>
