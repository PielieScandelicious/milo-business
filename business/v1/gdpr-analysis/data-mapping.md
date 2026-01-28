# GDPR Compliance Assessment
## Data Mapping & Flow Analysis

---

| **Document** | 01 - Data Mapping & Flow Analysis |
|:---|:---|
| **Reference** | GDPR Articles 5, 13, 14, 30 |
| **Status** | Assessment Complete |

---

## 1. Overview

This document provides a comprehensive mapping of all personal data processed by the Milo application, including data sources, processing activities, storage locations, and data flows to third parties.

### GDPR Article 30 - Records of Processing Activities

> Controllers must maintain records of processing activities under their responsibility, including purposes, data categories, recipients, transfers, retention periods, and security measures.

---

## 2. Data Inventory

### 2.1 Personal Data Categories

#### 🟢 Standard Personal Data

| Data Element | Source | Purpose | Storage |
|:---|:---|:---|:---|
| **Email Address** | Google Sign-In | Account identification | PostgreSQL |
| **Display Name** | Google Sign-In | Personalization | PostgreSQL |
| **First Name** | User input | Chat personalization | PostgreSQL |
| **Last Name** | User input | Profile completion | PostgreSQL |
| **Gender** | User input | Analytics, personalization | PostgreSQL |
| **Firebase UID** | Firebase Auth | Primary identifier | PostgreSQL |

#### 🟠 Sensitive Personal Data

| Data Element | Source | Purpose | Storage |
|:---|:---|:---|:---|
| **Transaction History** | Receipt processing | Core functionality | PostgreSQL |
| **Spending Patterns** | Derived data | Analytics, B2B | PostgreSQL |
| **Store Locations** | Receipt extraction | Analytics | PostgreSQL |
| **Purchase Items** | Receipt extraction | Categorization | PostgreSQL |
| **Item Prices** | Receipt extraction | Budgeting | PostgreSQL |
| **Shopping Frequency** | Derived data | Analytics, B2B | PostgreSQL |

#### 🔴 Special Category Data (Article 9)

| Data Element | Source | Purpose | Storage | Legal Basis Required |
|:---|:---|:---|:---|:---|
| **Health Scores** | AI processing | Dietary insights | PostgreSQL | Explicit Consent |
| **Dietary Patterns** | Derived data | Health analytics | PostgreSQL | Explicit Consent |
| **Nutritional Assessment** | AI processing | Health guidance | PostgreSQL | Explicit Consent |

> ⚠️ **Critical Finding**: Health scoring data (0-5 scale) constitutes "data concerning health" under GDPR Article 9 and requires explicit consent for processing.

#### 🟣 Technical/Behavioral Data

| Data Element | Source | Purpose | Storage |
|:---|:---|:---|:---|
| **Authentication Tokens** | Firebase | Session management | Keychain (iOS) |
| **Rate Limit Counters** | System-generated | Usage enforcement | PostgreSQL |
| **Chat History** | User interaction | AI context | PostgreSQL |
| **Receipt Images** | User upload | OCR processing | Firebase Storage |
| **App Usage Patterns** | Firebase Analytics | Product analytics | Firebase |

---

## 3. Data Flow Diagrams

### 3.1 User Registration Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         USER REGISTRATION FLOW                              │
└─────────────────────────────────────────────────────────────────────────────┘

    ┌──────────┐         ┌──────────────┐         ┌──────────────┐
    │   USER   │────────▶│ GOOGLE OAUTH │────────▶│   FIREBASE   │
    │ (iOS App)│         │   (Sign-In)  │         │     AUTH     │
    └──────────┘         └──────────────┘         └──────────────┘
         │                                               │
         │ Data Shared:                                  │ Data Received:
         │ - Email                                       │ - Firebase UID
         │ - Name                                        │ - Email
         │ - Profile Picture                             │ - Display Name
         │                                               │
         │                                               ▼
         │                                        ┌──────────────┐
         │                                        │   BACKEND    │
         │                                        │    (API)     │
         │                                        └──────────────┘
         │                                               │
         │                                               │ Creates:
         │                                               │ - User record
         │                                               │ - Profile record
         │                                               │ - Rate limit record
         │                                               ▼
         │                                        ┌──────────────┐
         │                                        │  POSTGRESQL  │
         │                                        │  (Database)  │
         │                                        └──────────────┘
         │
         └─────────────────────────────────────────────────┐
                                                           │
    Data Collected at Registration:                        │
    ┌───────────────────────────────────────────────────────────┐
    │ • Email address (from Google)                             │
    │ • Display name (from Google)                              │
    │ • Firebase UID (system-generated)                         │
    │ • Account creation timestamp                              │
    └───────────────────────────────────────────────────────────┘
```

### 3.2 Receipt Processing Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         RECEIPT PROCESSING FLOW                             │
└─────────────────────────────────────────────────────────────────────────────┘

    ┌──────────┐                                              EXTERNAL
    │   USER   │                                              PROCESSORS
    │ (iOS App)│                                         ┌─────────────────┐
    └────┬─────┘                                         │                 │
         │                                               │   ┌─────────┐   │
         │ Upload                                        │   │ VERYFI  │   │
         │ Receipt                                       │   │   API   │   │
         │ Image                                         │   │  (OCR)  │   │
         │                                               │   └────┬────┘   │
         ▼                                               │        │        │
    ┌──────────┐        Base64          ┌──────────┐    │        │        │
    │ BACKEND  │──────────────────────▶│  VERYFI  │◀───┼────────┘        │
    │   API    │       Image            │   API    │    │                 │
    └────┬─────┘                        └────┬─────┘    │                 │
         │                                   │          │   ┌─────────┐   │
         │                                   │ Returns: │   │ GOOGLE  │   │
         │                                   │ - Store  │   │ GEMINI  │   │
         │                                   │ - Date   │   │  (AI)   │   │
         │                                   │ - Total  │   └────┬────┘   │
         │                                   │ - Items  │        │        │
         │                                   │          │        │        │
         │                                   ▼          │        │        │
         │                              ┌──────────┐    │        │        │
         │◀─────────────────────────────│ OCR DATA │    │        │        │
         │                              └──────────┘    │        │        │
         │                                              │        │        │
         │ Send Items                                   │        │        │
         │ for Categorization                           │        │        │
         │──────────────────────────────────────────────┼───────▶│        │
         │                                              │        │        │
         │                                              │ Returns:        │
         │                                              │ - Categories    │
         │◀─────────────────────────────────────────────┼────────│        │
         │                                              │ - Health Scores │
         │                                              │                 │
         │                                              └─────────────────┘
         │
         │ Store All Data
         ▼
    ┌──────────────┐
    │  POSTGRESQL  │
    │  - Receipts  │
    │  - Transactions
    │  - Categories│
    │  - Health    │
    └──────────────┘

    ┌───────────────────────────────────────────────────────────────────────┐
    │ DATA SHARED WITH EXTERNAL PROCESSORS:                                 │
    │                                                                       │
    │ To Veryfi (USA):                    To Google Gemini (USA):           │
    │ ├─ Full receipt image (base64)      ├─ Item names (text)              │
    │ ├─ File type (pdf/jpg/png)          ├─ Store name (text)              │
    │ └─ User's Firebase UID (indirect)   └─ Categorization request         │
    │                                                                       │
    │ ⚠️  No Data Processing Agreements in place                            │
    │ ⚠️  No encryption specifications documented                           │
    │ ⚠️  International transfer (EU→USA) not addressed                     │
    └───────────────────────────────────────────────────────────────────────┘
```

### 3.3 AI Chat Processing Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          AI CHAT PROCESSING FLOW                            │
└─────────────────────────────────────────────────────────────────────────────┘

    ┌──────────┐
    │   USER   │
    │ (iOS App)│
    └────┬─────┘
         │
         │ Chat Message
         │
         ▼
    ┌──────────────┐
    │   BACKEND    │
    │     API      │
    └──────┬───────┘
           │
           │ Prepares Context:
           │ ┌─────────────────────────────────────────────────────────────┐
           │ │ USER CONTEXT SENT TO AI:                                    │
           │ │                                                             │
           │ │ • First name                                                │
           │ │ • Last name                                                 │
           │ │ • Gender                                                    │
           │ │ • Last 90 days of transactions:                             │
           │ │   - Store names                                             │
           │ │   - Item names                                              │
           │ │   - Prices                                                  │
           │ │   - Categories                                              │
           │ │   - Health scores                                           │
           │ │   - Purchase dates                                          │
           │ └─────────────────────────────────────────────────────────────┘
           │
           │                              ┌─────────────────────────────────┐
           │ V1 API                       │       EXTERNAL AI SERVICES      │
           │────────────────────────────▶ │   ┌────────────────────────┐   │
           │                              │   │    ANTHROPIC CLAUDE    │   │
           │                              │   │      (San Francisco)   │   │
           │                              │   └────────────────────────┘   │
           │ V2 API                       │                                │
           │────────────────────────────▶ │   ┌────────────────────────┐   │
           │                              │   │     GOOGLE GEMINI      │   │
           │                              │   │    (Mountain View)     │   │
           │◀───────────────────────────  │   └────────────────────────┘   │
           │   Streaming Response (SSE)   │                                │
           │                              └─────────────────────────────────┘
           │
           ▼
    ┌──────────────┐
    │  POSTGRESQL  │ ◀─── Chat history stored
    │  (Database)  │
    └──────────────┘

    ┌───────────────────────────────────────────────────────────────────────┐
    │ ⚠️  CRITICAL GDPR CONCERNS:                                           │
    │                                                                       │
    │ 1. FULL TRANSACTION HISTORY (90 days) sent to US-based AI providers   │
    │ 2. Personal profile data (name, gender) included in every request     │
    │ 3. Health scores transmitted to third parties                         │
    │ 4. No Data Processing Agreements documented                           │
    │ 5. Chat history retention period: UNDEFINED                           │
    │ 6. User cannot delete chat history (no mechanism exists)              │
    └───────────────────────────────────────────────────────────────────────┘
```

### 3.4 Data Monetization Flow (Planned)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     DATA MONETIZATION FLOW (PLANNED)                        │
└─────────────────────────────────────────────────────────────────────────────┘

    ┌──────────────┐
    │  POSTGRESQL  │
    │  (All User   │
    │   Data)      │
    └──────┬───────┘
           │
           │ Raw Data Extraction
           ▼
    ┌──────────────────────────────────────────────────────────────────┐
    │                    ANONYMIZATION PIPELINE                        │
    │                                                                  │
    │  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐          │
    │  │ PII Removal │───▶│ K-Anonymity │───▶│Differential │          │
    │  │             │    │  Check      │    │  Privacy    │          │
    │  └─────────────┘    └─────────────┘    └─────────────┘          │
    │        │                  │                  │                   │
    │        ▼                  ▼                  ▼                   │
    │  Remove:            Min cell size:     Add noise to              │
    │  - Names            <10 users          prevent re-ID             │
    │  - Emails           excluded                                     │
    │  - Phone numbers                                                 │
    │                                                                  │
    └──────────────────────────┬───────────────────────────────────────┘
                               │
                               │ Anonymized Data Products
                               ▼
    ┌──────────────────────────────────────────────────────────────────┐
    │                      B2B DATA PRODUCTS                           │
    │                                                                  │
    │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐  │
    │  │   Syndicated    │  │   Data Feeds    │  │    Custom       │  │
    │  │   Reports       │  │   (DaaS)        │  │   Research      │  │
    │  │   $2.5K-50K     │  │   $2.5K-15K/mo  │  │   $5K-100K+     │  │
    │  └────────┬────────┘  └────────┬────────┘  └────────┬────────┘  │
    │           │                    │                    │           │
    └───────────┼────────────────────┼────────────────────┼───────────┘
                │                    │                    │
                ▼                    ▼                    ▼
    ┌───────────────────────────────────────────────────────────────────┐
    │                         B2B CLIENTS                               │
    │                                                                   │
    │  CPG Brands    Retailers    Financial    Market       Health &    │
    │  (Nestlé,      (Grocery     Services     Research     Wellness    │
    │   P&G)         Chains)      (Hedge       Firms        Companies   │
    │                             Funds)                                │
    └───────────────────────────────────────────────────────────────────┘

    ┌───────────────────────────────────────────────────────────────────────┐
    │ ⚠️  CRITICAL COMPLIANCE REQUIREMENTS FOR DATA MONETIZATION:           │
    │                                                                       │
    │ 1. EXPLICIT OPT-IN CONSENT required (not opt-out)                     │
    │ 2. Tiered consent system needed (aggregated vs. individual-level)     │
    │ 3. Anonymization effectiveness must be independently verified         │
    │ 4. Users must be able to withdraw consent at any time                 │
    │ 5. Clear disclosure of data buyers required                           │
    │ 6. Regular re-anonymization audits (quarterly recommended)            │
    │ 7. Data Processing Agreements with ALL B2B clients required           │
    │                                                                       │
    │ CURRENT STATUS: ❌ CONSENT SYSTEM NOT IMPLEMENTED                     │
    └───────────────────────────────────────────────────────────────────────┘
```

---

## 4. Data Storage Locations

### 4.1 Primary Storage

| Location | Data Stored | Encryption | Region |
|:---|:---|:---|:---|
| **PostgreSQL (Railway)** | All structured data | In-transit (TLS) | USA |
| **Firebase Storage** | Receipt images | At-rest (AES-256) | USA |
| **Firebase Auth** | Auth tokens | Google-managed | USA |

### 4.2 Client-Side Storage (iOS)

| Location | Data Stored | Security |
|:---|:---|:---|
| **Keychain** | Auth tokens | Hardware-backed |
| **App Group** | Share extension data | Sandboxed |
| **Memory** | Session data | App lifecycle |

### 4.3 Third-Party Storage

| Processor | Data Stored | Retention | Location |
|:---|:---|:---|:---|
| Veryfi | Receipt images | Unknown | USA |
| Google Gemini | Processing logs | Unknown | USA |
| Anthropic Claude | Processing logs | Unknown | USA |

> ⚠️ **Finding**: Data retention policies at third-party processors are not documented. GDPR Article 28 requires processors to delete data upon controller instruction.

---

## 5. Data Retention Schedule

### 5.1 Current Implementation

| Data Type | Retention Period | Deletion Mechanism |
|:---|:---|:---|
| User Profile | Indefinite | None implemented |
| Transactions | Tier-based (3-12 months) | None implemented |
| Receipt Images | Indefinite | None implemented |
| Chat History | Indefinite | None implemented |
| Rate Limit Data | 30-day rolling | Auto-expire |

### 5.2 Recommended Retention Periods

| Data Type | Recommended Retention | Justification |
|:---|:---|:---|
| User Profile | Account lifetime + 30 days | Service delivery |
| Transactions | User tier limit + 90 days | Feature delivery |
| Receipt Images | 90 days or on request | Processing complete |
| Chat History | 12 months or on request | Service improvement |
| Rate Limit Data | 30 days | Current implementation |
| Anonymized B2B Data | 24 months | Business purpose |

---

## 6. Cross-Border Data Transfers

### 6.1 Transfer Map

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       INTERNATIONAL DATA TRANSFERS                          │
└─────────────────────────────────────────────────────────────────────────────┘

    EU/EEA DATA SUBJECTS
           │
           │ Data originates from EU users
           │
           ▼
    ┌──────────────┐
    │   RAILWAY    │ ◀─── Backend hosted in USA
    │   (USA)      │      (No adequacy decision)
    └──────┬───────┘
           │
           ├─────────────────────────────────────────────────────────────┐
           │                                                             │
           ▼                                                             ▼
    ┌──────────────┐                                              ┌──────────────┐
    │   VERYFI     │                                              │   FIREBASE   │
    │   (USA)      │                                              │   (USA)      │
    │              │                                              │              │
    │ Receives:    │                                              │ Receives:    │
    │ - Images     │                                              │ - Auth data  │
    │ - Metadata   │                                              │ - Images     │
    └──────────────┘                                              └──────────────┘
           │
           ├─────────────────────────────────────────────────────────────┐
           │                                                             │
           ▼                                                             ▼
    ┌──────────────┐                                              ┌──────────────┐
    │   GOOGLE     │                                              │  ANTHROPIC   │
    │   GEMINI     │                                              │   CLAUDE     │
    │   (USA)      │                                              │   (USA)      │
    │              │                                              │              │
    │ Receives:    │                                              │ Receives:    │
    │ - Item data  │                                              │ - Full user  │
    │ - Store data │                                              │   context    │
    └──────────────┘                                              └──────────────┘

    ┌───────────────────────────────────────────────────────────────────────┐
    │ TRANSFER MECHANISM STATUS:                                            │
    │                                                                       │
    │ ❌ Standard Contractual Clauses (SCCs): NOT IMPLEMENTED              │
    │ ❌ Binding Corporate Rules: NOT APPLICABLE                           │
    │ ❌ Adequacy Decision: USA has no adequacy (post-Schrems II)          │
    │ ❌ Derogations (Art. 49): Not documented                             │
    │                                                                       │
    │ REQUIREMENT: SCCs must be executed with ALL US-based processors      │
    └───────────────────────────────────────────────────────────────────────┘
```

---

## 7. Data Subject Categories

| Category | Description | Special Considerations |
|:---|:---|:---|
| **App Users** | Primary data subjects | Standard GDPR rights |
| **Household Members** | Implied from receipts | No direct consent |
| **Minors (<18)** | Potential users | Parental consent if <16 |
| **Children (<13)** | Potential users | COPPA + special GDPR protections |

> ⚠️ **Finding**: No age verification mechanism exists. Users under 16 require parental consent under GDPR Article 8.

---

## 8. Summary of Data Processing Activities

### Article 30 Processing Register

| # | Processing Activity | Purpose | Legal Basis* | Categories | Recipients | Transfers | Retention |
|:---:|:---|:---|:---|:---|:---|:---|:---|
| 1 | User Registration | Account creation | Contract | Identity | Firebase | USA | Account life |
| 2 | Receipt Processing | Core service | Contract | Financial | Veryfi, Gemini | USA | Tier-based |
| 3 | Health Scoring | Dietary insights | Consent* | Health | Gemini | USA | Tier-based |
| 4 | AI Chat | Personal assistance | Consent* | All | Claude/Gemini | USA | Undefined |
| 5 | Analytics | Service improvement | Legit. Interest* | Behavioral | Firebase | USA | Undefined |
| 6 | Data Monetization | B2B revenue | Consent* | Anonymized | B2B clients | Various | 24 months |

*Legal basis not formally documented - requires immediate attention

---

## Appendix: Data Element Inventory

### Complete Personal Data Elements

| Element | Type | Source | Processing | Storage | Sharing |
|:---|:---|:---|:---|:---|:---|
| email | Identity | Google SSO | Auth | PostgreSQL | Firebase |
| display_name | Identity | Google SSO | Display | PostgreSQL | - |
| first_name | Identity | User input | Chat, Analytics | PostgreSQL | AI providers |
| last_name | Identity | User input | Chat, Analytics | PostgreSQL | AI providers |
| gender | Identity | User input | Personalization | PostgreSQL | AI providers |
| firebase_uid | Technical | Firebase | Primary key | PostgreSQL | - |
| receipt_image | Financial | User upload | OCR | Firebase Storage | Veryfi |
| store_name | Financial | OCR extraction | Analytics | PostgreSQL | Gemini, B2B |
| receipt_date | Financial | OCR extraction | Analytics | PostgreSQL | B2B |
| total_amount | Financial | OCR extraction | Analytics | PostgreSQL | B2B |
| item_name | Financial | OCR extraction | Categorization | PostgreSQL | Gemini, B2B |
| item_price | Financial | OCR extraction | Analytics | PostgreSQL | B2B |
| item_quantity | Financial | OCR extraction | Analytics | PostgreSQL | B2B |
| category | Derived | AI processing | Analytics | PostgreSQL | B2B |
| health_score | Health | AI processing | Insights | PostgreSQL | AI providers, B2B |
| chat_message | Communication | User input | AI response | PostgreSQL | AI providers |
| chat_response | Communication | AI output | Display | PostgreSQL | - |
| rate_limit_chat | Technical | System | Enforcement | PostgreSQL | - |
| rate_limit_receipt | Technical | System | Enforcement | PostgreSQL | - |

---

*Document prepared as part of GDPR Compliance Assessment for DeepmAInd/Milo Application*
