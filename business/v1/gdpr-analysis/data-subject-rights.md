# GDPR Compliance Assessment
## Data Subject Rights Implementation Guide

---

| **Document** | 05 - Data Subject Rights Implementation |
|:---|:---|
| **Reference** | GDPR Articles 12-23 |
| **Status** | Implementation Required |

---

## 1. Overview

GDPR grants data subjects eight fundamental rights. Controllers must facilitate the exercise of these rights and respond to requests within one month (extendable by two months for complex requests).

### Current Implementation Status

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                    DATA SUBJECT RIGHTS - CURRENT STATUS                      ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  RIGHT                        │ ARTICLE │ STATUS    │ IMPLEMENTATION        ║
║  ────────────────────────────┼─────────┼───────────┼──────────────────────  ║
║  Right of Access              │   15    │ ❌ None   │ Export feature needed ║
║  Right to Rectification       │   16    │ ⚠️ Partial│ Profile edit exists   ║
║  Right to Erasure             │   17    │ ❌ None   │ Delete account needed ║
║  Right to Restriction         │   18    │ ❌ None   │ Pause feature needed  ║
║  Right to Portability         │   20    │ ❌ None   │ Export (JSON/CSV)     ║
║  Right to Object              │   21    │ ❌ None   │ Opt-out mechanism     ║
║  Automated Decision Rights    │   22    │ ❌ None   │ AI transparency       ║
║  Right to Withdraw Consent    │  7(3)   │ ❌ None   │ Consent management    ║
║                                                                              ║
║  OVERALL READINESS: 10%                                                      ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

---

## 2. Right of Access (Article 15)

### 2.1 Requirement

Data subjects have the right to:
- Confirm whether their data is being processed
- Access a copy of their personal data
- Receive supplementary information about processing

### 2.2 Information to Provide

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    ARTICLE 15 REQUIRED INFORMATION                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  (a) Purposes of processing                                                 │
│  (b) Categories of personal data                                            │
│  (c) Recipients or categories of recipients                                 │
│  (d) Retention periods or criteria                                          │
│  (e) Right to rectification, erasure, restriction, objection               │
│  (f) Right to lodge complaint with supervisory authority                   │
│  (g) Source of data (if not from data subject)                             │
│  (h) Existence of automated decision-making                                │
│                                                                             │
│  For international transfers:                                               │
│  - Appropriate safeguards (SCCs, etc.)                                     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2.3 Implementation Specification

#### API Endpoint

```
POST /api/v1/user/data-export
Authorization: Bearer <firebase_token>
Content-Type: application/json

Request Body:
{
  "format": "json" | "csv",
  "include_images": boolean,
  "date_range": {
    "start": "YYYY-MM-DD" | null,
    "end": "YYYY-MM-DD" | null
  }
}

Response:
{
  "export_id": "uuid",
  "status": "processing" | "ready",
  "download_url": "signed_url",  // valid 24 hours
  "expires_at": "ISO8601 timestamp"
}
```

#### Export Data Structure

```json
{
  "export_metadata": {
    "generated_at": "2026-01-28T12:00:00Z",
    "data_subject_id": "firebase_uid",
    "export_format": "json",
    "gdpr_article": "15"
  },

  "profile_data": {
    "email": "user@example.com",
    "display_name": "John Doe",
    "first_name": "John",
    "last_name": "Doe",
    "gender": "male",
    "created_at": "2025-06-15T10:30:00Z",
    "profile_completed": true
  },

  "transaction_data": [
    {
      "transaction_id": "uuid",
      "receipt_id": "uuid",
      "store_name": "grocery store",
      "item_name": "Organic Apples",
      "price": 4.99,
      "quantity": 1,
      "category": "Fruits & Vegetables",
      "health_score": 5,
      "date": "2026-01-15"
    }
  ],

  "receipt_data": [
    {
      "receipt_id": "uuid",
      "store_name": "grocery store",
      "total_amount": 45.67,
      "receipt_date": "2026-01-15",
      "status": "completed",
      "image_url": "signed_url (if requested)"
    }
  ],

  "chat_history": [
    {
      "message_id": "uuid",
      "timestamp": "2026-01-20T14:30:00Z",
      "role": "user",
      "content": "What did I spend on groceries last week?"
    }
  ],

  "consent_records": [
    {
      "consent_type": "health_features",
      "status": "granted",
      "timestamp": "2025-06-15T10:35:00Z",
      "version": "1.0"
    }
  ],

  "processing_information": {
    "purposes": ["Core service delivery", "Health insights", "AI assistance"],
    "legal_bases": ["Contract", "Consent", "Consent"],
    "recipients": ["Veryfi Inc.", "Google LLC", "Anthropic PBC"],
    "retention_periods": {
      "transactions": "Per subscription tier (3-unlimited months)",
      "receipts": "90 days after processing",
      "chat_history": "12 months"
    },
    "international_transfers": {
      "countries": ["USA"],
      "safeguards": "Standard Contractual Clauses"
    }
  }
}
```

#### iOS Implementation

```
Settings Screen:
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│  Privacy & Data                                                             │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  📥 Download My Data                                                │   │
│  │     Export all your personal data                                   │   │
│  │                                                     [Request Export]│   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  Export Options:                                                            │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Format:  ○ JSON  ● CSV                                             │   │
│  │  Include receipt images: [Toggle OFF]                               │   │
│  │  Date range: [All Time ▼]                                           │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  Note: Your export will be ready within 24 hours.                          │
│  You'll receive a notification when it's ready to download.                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Right to Rectification (Article 16)

### 3.1 Requirement

Data subjects have the right to rectify inaccurate personal data and complete incomplete data.

### 3.2 Current State

| Data Element | Editable | Location |
|:---|:---:|:---|
| First name | ✅ Yes | Profile screen |
| Last name | ✅ Yes | Profile screen |
| Gender | ✅ Yes | Profile screen |
| Email | ❌ No | Linked to Google account |
| Transactions | ✅ Yes | Manual edit available |
| Categories | ✅ Yes | Manual override available |
| Health scores | ❌ No | AI-generated, no override |

### 3.3 Required Improvements

- [ ] Add ability to correct health scores (user override)
- [ ] Add ability to correct store names
- [ ] Add ability to correct item categorizations
- [ ] Implement "request correction" for AI-assigned data
- [ ] Log all corrections for audit trail

---

## 4. Right to Erasure (Article 17)

### 4.1 Requirement

Data subjects have the right to erasure ("right to be forgotten") when:
- Data no longer necessary for original purpose
- Consent is withdrawn
- Data subject objects and no overriding legitimate grounds
- Data processed unlawfully
- Legal obligation to erase
- Data collected from children

### 4.2 Exceptions

Erasure may be refused for:
- Exercise of freedom of expression
- Legal obligations
- Public health purposes
- Archiving/research (with safeguards)
- Legal claims

### 4.3 Implementation Specification

#### API Endpoint

```
POST /api/v1/user/delete-account
Authorization: Bearer <firebase_token>
Content-Type: application/json

Request Body:
{
  "confirmation": "DELETE MY ACCOUNT",
  "reason": "string (optional)",
  "keep_anonymized_data": boolean  // for research panel
}

Response:
{
  "deletion_id": "uuid",
  "status": "scheduled",
  "scheduled_for": "ISO8601 timestamp",  // 30 days from now
  "can_cancel_until": "ISO8601 timestamp"
}
```

#### Deletion Workflow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          ACCOUNT DELETION WORKFLOW                          │
└─────────────────────────────────────────────────────────────────────────────┘

    User Request                   30-Day Cooling Off              Final Deletion
         │                               │                               │
         ▼                               ▼                               ▼
    ┌─────────┐                    ┌─────────┐                    ┌─────────┐
    │ Request │───────────────────▶│ Pending │───────────────────▶│ Execute │
    │ Delete  │                    │ Delete  │                    │ Delete  │
    └─────────┘                    └─────────┘                    └─────────┘
         │                               │                               │
         │                               │ User can cancel               │
         │                               │ during this period            │
         │                               │                               │
         ▼                               ▼                               ▼
    ┌─────────────────────────────────────────────────────────────────────────┐
    │                                                                         │
    │  Actions at each stage:                                                 │
    │                                                                         │
    │  REQUEST:                                                               │
    │  • Log deletion request                                                 │
    │  • Send confirmation email                                              │
    │  • Mark account as "pending deletion"                                   │
    │  • Disable new data collection                                          │
    │                                                                         │
    │  PENDING (30 days):                                                     │
    │  • User can still cancel                                                │
    │  • Account remains functional (read-only)                               │
    │  • Reminder email at day 25                                             │
    │                                                                         │
    │  EXECUTE:                                                               │
    │  • Delete all personal data from PostgreSQL                             │
    │  • Delete all images from Firebase Storage                              │
    │  • Delete Firebase Auth account                                         │
    │  • Send deletion confirmation to processors                             │
    │  • Retain anonymized data only if consented                             │
    │  • Generate deletion certificate                                        │
    │                                                                         │
    └─────────────────────────────────────────────────────────────────────────┘
```

#### Data to Delete

| Data Store | Data | Action |
|:---|:---|:---|
| PostgreSQL/users | User record | Hard delete |
| PostgreSQL/user_profiles | Profile data | Hard delete |
| PostgreSQL/receipts | All receipts | Hard delete |
| PostgreSQL/transactions | All transactions | Hard delete* |
| PostgreSQL/user_rate_limits | Rate limit data | Hard delete |
| Firebase Auth | Auth account | Delete account |
| Firebase Storage | Receipt images | Delete all files |

*If user consented to research panel, transactions may be retained in fully anonymized form with no link to original user.

#### iOS Implementation

```
Settings Screen:
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│  Privacy & Data                                                             │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  🗑️ Delete My Account                                               │   │
│  │     Permanently delete your account and all data                    │   │
│  │                                                     [Delete Account]│   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘

Delete Confirmation:
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│  ⚠️ Delete Your Account?                                                   │
│                                                                             │
│  This will permanently delete:                                              │
│  • Your profile information                                                 │
│  • All uploaded receipts                                                    │
│  • All transaction history                                                  │
│  • All chat conversations                                                   │
│                                                                             │
│  Your account will be scheduled for deletion in 30 days.                   │
│  You can cancel during this period.                                        │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Type "DELETE MY ACCOUNT" to confirm:                               │   │
│  │  [                                                              ]   │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  [ ] Keep my anonymized data for research (helps improve products)         │
│                                                                             │
│  [Cancel]                                      [Delete Account]             │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 5. Right to Restriction (Article 18)

### 5.1 Requirement

Data subjects can request restriction of processing when:
- Accuracy is contested (during verification)
- Processing is unlawful but erasure is not desired
- Controller no longer needs data but data subject needs it for legal claims
- Objection is pending verification

### 5.2 Implementation

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       RESTRICTION IMPLEMENTATION                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Database Schema Addition:                                                  │
│                                                                             │
│  ALTER TABLE users ADD COLUMN processing_restricted BOOLEAN DEFAULT FALSE; │
│  ALTER TABLE users ADD COLUMN restriction_reason TEXT;                     │
│  ALTER TABLE users ADD COLUMN restriction_date TIMESTAMP;                  │
│                                                                             │
│  When restricted = TRUE:                                                    │
│  • Store data but do not process                                           │
│  • Exclude from analytics                                                   │
│  • Exclude from data monetization                                           │
│  • Disable AI features                                                      │
│  • Allow read-only access to user                                           │
│                                                                             │
│  Allowed processing when restricted:                                        │
│  • Storage only                                                             │
│  • With data subject consent                                                │
│  • For legal claims                                                         │
│  • For protection of another person's rights                                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 6. Right to Data Portability (Article 20)

### 6.1 Requirement

Data subjects have the right to:
- Receive their data in structured, machine-readable format
- Transmit data to another controller
- Have data transmitted directly where technically feasible

### 6.2 Scope

Portability applies to:
- Data provided by data subject
- Data processed based on consent or contract
- Data processed by automated means

### 6.3 Export Formats

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       PORTABILITY EXPORT FORMATS                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  FORMAT 1: JSON (Recommended)                                               │
│  • Structured, machine-readable                                             │
│  • Preserves data relationships                                             │
│  • Standard format for APIs                                                 │
│                                                                             │
│  FORMAT 2: CSV (Alternative)                                                │
│  • Multiple files (profile.csv, transactions.csv, etc.)                    │
│  • Easily importable to spreadsheets                                        │
│  • Loses some relational structure                                          │
│                                                                             │
│  IMAGES:                                                                    │
│  • Included as separate files in ZIP archive                               │
│  • Original format preserved (JPG, PNG, PDF)                               │
│  • Filenames reference transaction IDs                                      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 7. Right to Object (Article 21)

### 7.1 Requirement

Data subjects can object to processing based on:
- Legitimate interests (controller must demonstrate compelling grounds)
- Direct marketing (absolute right, must stop immediately)
- Research/statistics (unless necessary for public interest)

### 7.2 Implementation

```
Settings Screen:
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│  Data Processing Preferences                                                │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Analytics & Improvement                                            │   │
│  │  Help us improve Milo with anonymized usage data                    │   │
│  │                                                          [Toggle ON]│   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Research Panel                                                     │   │
│  │  Contribute anonymized data to consumer research                    │   │
│  │                                                         [Toggle OFF]│   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Marketing Communications                                           │   │
│  │  Receive tips, updates, and offers                                  │   │
│  │                                                         [Toggle OFF]│   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 8. Automated Decision-Making Rights (Article 22)

### 8.1 Requirement

Data subjects have the right not to be subject to decisions based solely on automated processing that produce legal or similarly significant effects, unless:
- Necessary for contract
- Authorized by law
- Based on explicit consent

Where automated decisions are made, data subjects have rights to:
- Human intervention
- Express their point of view
- Contest the decision

### 8.2 Automated Processing in Milo

| Process | Automated | Significant Effect | Action Required |
|:---|:---:|:---|:---|
| Health scoring | Yes | Potentially | Disclose algorithm, allow override |
| Category assignment | Yes | No | Inform, allow manual correction |
| Duplicate detection | Yes | Yes (blocks upload) | Provide appeal mechanism |
| Rate limiting | Yes | Yes (blocks features) | Transparent limits, clear messaging |

### 8.3 Implementation

```
AI Transparency Feature:
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│  How Milo Uses AI                                                           │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  🏥 Health Scores                                                   │   │
│  │                                                                      │   │
│  │  We assign health scores (0-5) to food items based on:              │   │
│  │  • Nutritional guidelines                                           │   │
│  │  • Ingredient analysis                                              │   │
│  │  • AI-powered assessment                                            │   │
│  │                                                                      │   │
│  │  You can:                                                           │   │
│  │  • Override any health score manually                               │   │
│  │  • Disable health scoring entirely                                  │   │
│  │  • Request human review of scores                                   │   │
│  │                                                                      │   │
│  │  [Manage Health Scores]                                             │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  📦 Category Assignment                                             │   │
│  │                                                                      │   │
│  │  Items are automatically categorized into 16 categories.            │   │
│  │  You can change any category assignment.                            │   │
│  │                                                                      │   │
│  │  [View Categories]                                                  │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 9. Right to Withdraw Consent (Article 7(3))

### 9.1 Requirement

- Consent must be as easy to withdraw as to give
- Data subject must be informed of right before consent
- Withdrawal does not affect lawfulness of prior processing

### 9.2 Implementation

```
Consent Management:
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│  Your Consents                                                              │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  ✅ Health Insights                          Granted Jun 15, 2025   │   │
│  │     Health scoring and dietary analysis                             │   │
│  │                                                   [Withdraw Consent]│   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  ✅ AI Personalization                       Granted Jun 15, 2025   │   │
│  │     Share transaction history with AI assistant                     │   │
│  │                                                   [Withdraw Consent]│   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  ❌ Research Panel                                                  │   │
│  │     Contribute anonymized data to research                          │   │
│  │                                                       [Give Consent]│   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  Withdrawing consent will:                                                  │
│  • Stop future processing for that purpose                                 │
│  • Not affect data already processed                                       │
│  • Not affect processing based on other legal bases                        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 10. Request Handling Procedures

### 10.1 Response Timeline

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        REQUEST RESPONSE TIMELINE                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Day 0          Day 30                              Day 90                  │
│    │              │                                   │                     │
│    ▼              ▼                                   ▼                     │
│    ●──────────────●───────────────────────────────────●                    │
│    │              │                                   │                     │
│ Request      Standard                            Extended                   │
│ Received     Deadline                            Deadline                   │
│                                                  (if complex)               │
│                                                                             │
│  ACTIONS:                                                                   │
│  • Day 0-3: Verify identity, acknowledge receipt                           │
│  • Day 3-7: Gather data from all systems                                   │
│  • Day 7-14: Prepare response                                              │
│  • Day 14-21: Internal review                                              │
│  • Day 21-30: Deliver response                                             │
│                                                                             │
│  If complex (extending to 90 days):                                        │
│  • Notify data subject by Day 30                                           │
│  • Explain reasons for extension                                           │
│  • Provide interim update if possible                                      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 10.2 Identity Verification

Before responding to any request:

1. Verify request comes from authenticated user (Firebase token)
2. For email/support requests, verify email matches account
3. For sensitive requests (deletion), require additional confirmation
4. Log all verification steps

### 10.3 Request Logging

```sql
CREATE TABLE data_subject_requests (
  id UUID PRIMARY KEY,
  user_id VARCHAR(255) NOT NULL,
  request_type VARCHAR(50) NOT NULL,  -- access, rectification, erasure, etc.
  request_date TIMESTAMP NOT NULL,
  status VARCHAR(20) NOT NULL,  -- received, processing, completed, refused
  response_date TIMESTAMP,
  response_notes TEXT,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);
```

---

## 11. Implementation Priority

| Priority | Right | Effort | Timeline |
|:---:|:---|:---:|:---|
| 1 | Erasure (Delete Account) | High | Week 1-2 |
| 2 | Withdraw Consent | Medium | Week 2-3 |
| 3 | Access (Data Export) | High | Week 3-4 |
| 4 | Object (Opt-out) | Medium | Week 4-5 |
| 5 | Portability | Medium | Week 5-6 |
| 6 | Automated Decisions | Medium | Week 6-7 |
| 7 | Restriction | Low | Week 7-8 |
| 8 | Rectification (enhance) | Low | Week 8 |

---

*Document prepared as part of GDPR Compliance Assessment for DeepmAInd/Milo Application*
