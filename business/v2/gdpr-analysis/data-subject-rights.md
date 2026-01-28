<div align="center">

# **MILO**
## Data Subject Rights Implementation v2.0

---

**DeepmAInd B.V.** | January 28, 2026

</div>

---

## Rights Overview

| Right | GDPR Article | Current Status | Priority |
|:------|:-------------|:--------------:|:--------:|
| **Access** | Art. 15 | ❌ Not implemented | 🔴 Critical |
| **Rectification** | Art. 16 | ⚠️ Partial (profile only) | 🟡 High |
| **Erasure** | Art. 17 | ❌ Not implemented | 🔴 Critical |
| **Restriction** | Art. 18 | ❌ Not implemented | 🟡 High |
| **Portability** | Art. 20 | ❌ Not implemented | 🔴 Critical |
| **Object** | Art. 21 | ❌ Not implemented | 🟡 High |
| **Automated decisions** | Art. 22 | ⚠️ Partial | 🟡 High |

---

## Right of Access (Art. 15)

### Requirements

| Requirement | Implementation |
|:------------|:---------------|
| Confirm processing | Account exists = yes |
| Purposes | Documented in privacy policy |
| Categories | Defined in data mapping |
| Recipients | Processor list |
| Retention periods | Policy document |
| Copy of data | Export function required |

### Implementation Plan

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                         ACCESS REQUEST WORKFLOW                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   User Request                                                                ║
║        │                                                                      ║
║        ▼                                                                      ║
║   ┌─────────────┐     ┌─────────────┐     ┌─────────────┐                    ║
║   │  Identity   │────▶│   Compile   │────▶│   Deliver   │                    ║
║   │ Verification│     │    Data     │     │    Data     │                    ║
║   └─────────────┘     └─────────────┘     └─────────────┘                    ║
║        │                    │                    │                            ║
║        │                    │                    │                            ║
║   App login or          All user data       Secure download                  ║
║   email verification    in JSON format      within 30 days                   ║
║                                                                               ║
║   DEADLINE: 30 days from request                                             ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

### Data Export Format

```json
{
  "export_date": "2026-01-28T12:00:00Z",
  "user": {
    "email": "user@example.com",
    "name": "Display Name",
    "created_at": "2025-06-01T10:00:00Z"
  },
  "receipts": [
    {
      "id": "rec_123",
      "date": "2026-01-15",
      "merchant": "Grocery Store",
      "total": 45.67,
      "items": [...]
    }
  ],
  "health_scores": [...],
  "consent_records": [...],
  "analytics_summary": {...}
}
```

**Implementation Cost:** €5,000 | **Timeline:** Week 5

---

## Right to Rectification (Art. 16)

### Current State

| Data Type | Editable | Location |
|:----------|:--------:|:---------|
| Display name | ✅ Yes | Profile settings |
| Email | ⚠️ Requires verification | Account settings |
| Profile photo | ✅ Yes | Profile settings |
| Receipt data | ❌ No | Locked after import |
| Health scores | ❌ No | System-generated |

### Required Improvements

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                      RECTIFICATION REQUIREMENTS                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   Current:                                                                    ║
║   ✅ Users can edit profile information                                      ║
║                                                                               ║
║   Needed:                                                                     ║
║   ⬜ Receipt correction mechanism (flag incorrect OCR)                       ║
║   ⬜ Support email for complex corrections                                   ║
║   ⬜ Audit trail for all corrections                                         ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

**Implementation Cost:** €2,000 | **Timeline:** Week 6

---

## Right to Erasure (Art. 17)

### Erasure Scope

| Data Type | Erasure Action | Exceptions |
|:----------|:---------------|:-----------|
| User account | Full deletion | None |
| Receipt data | Full deletion | Legal retention |
| Health scores | Full deletion | None |
| Profile image | Full deletion | None |
| Analytics | Anonymization | Aggregate stats |
| Processor data | Deletion request | Verify completion |

### Implementation Plan

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                          DELETION WORKFLOW                                    ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   User initiates deletion                                                    ║
║        │                                                                      ║
║        ▼                                                                      ║
║   ┌─────────────────────────────────────────────────────────────────────┐    ║
║   │                    CONFIRMATION SCREEN                               │    ║
║   │                                                                      │    ║
║   │   ⚠️ Delete Your Account                                             │    ║
║   │                                                                      │    ║
║   │   This will permanently delete:                                      │    ║
║   │   • Your account and profile                                         │    ║
║   │   • All receipt data (X receipts)                                   │    ║
║   │   • All health scores and insights                                  │    ║
║   │   • Your subscription (no refund)                                   │    ║
║   │                                                                      │    ║
║   │   This action cannot be undone.                                      │    ║
║   │                                                                      │    ║
║   │   [Cancel]                    [Delete My Account]                   │    ║
║   │                                                                      │    ║
║   └─────────────────────────────────────────────────────────────────────┘    ║
║        │                                                                      ║
║        ▼                                                                      ║
║   30-day grace period (can recover account)                                  ║
║        │                                                                      ║
║        ▼                                                                      ║
║   Permanent deletion from all systems                                        ║
║        │                                                                      ║
║        ├──▶ PostgreSQL: CASCADE DELETE                                       ║
║        ├──▶ Firebase Auth: Delete user                                       ║
║        ├──▶ Firebase Storage: Delete files                                   ║
║        ├──▶ Veryfi: No action (transient)                                    ║
║        └──▶ Analytics: Anonymize user ID                                     ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

**Implementation Cost:** €5,000 | **Timeline:** Week 5

---

## Right to Restriction (Art. 18)

### Restriction Triggers

| Trigger | Action | Duration |
|:--------|:-------|:---------|
| Accuracy contested | Pause processing | Until verified |
| Processing unlawful | Store only | User decision |
| No longer needed | Store only | User request |
| Objection pending | Pause processing | Until resolved |

### Implementation

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                        RESTRICTION MECHANISM                                  ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   Database flag: user.processing_restricted = true                           ║
║                                                                               ║
║   When restricted:                                                            ║
║   ✅ Data stored but not processed                                           ║
║   ✅ No health scoring                                                       ║
║   ✅ No analytics collection                                                 ║
║   ✅ No B2B data sharing                                                     ║
║   ✅ Basic app access maintained                                             ║
║                                                                               ║
║   Lift restriction: User request via settings or support                     ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

**Implementation Cost:** €2,000 | **Timeline:** Week 6

---

## Right to Portability (Art. 20)

### Portable Data

| Data Type | Format | Included |
|:----------|:-------|:--------:|
| Account info | JSON | ✅ |
| Receipt data | JSON/CSV | ✅ |
| Health scores | JSON/CSV | ✅ |
| Consent records | JSON | ✅ |
| Analytics | Not applicable | ❌ |

### Export Formats

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                         DATA PORTABILITY OPTIONS                              ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   Settings → Privacy → Export My Data                                        ║
║                                                                               ║
║   ┌─────────────────────────────────────────────────────────────────────┐    ║
║   │                                                                     │    ║
║   │   Export Format:                                                    │    ║
║   │   ○ JSON (machine-readable, complete)                              │    ║
║   │   ○ CSV (spreadsheet-compatible, receipts only)                    │    ║
║   │                                                                     │    ║
║   │   Include:                                                          │    ║
║   │   ☑ Account information                                            │    ║
║   │   ☑ All receipts                                                   │    ║
║   │   ☑ Health scores                                                  │    ║
║   │   ☐ Consent history                                                │    ║
║   │                                                                     │    ║
║   │   [Request Export]                                                 │    ║
║   │                                                                     │    ║
║   │   Note: Export will be ready within 24 hours.                      │    ║
║   │   You'll receive a notification when it's ready.                   │    ║
║   │                                                                     │    ║
║   └─────────────────────────────────────────────────────────────────────┘    ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

**Implementation Cost:** €5,000 | **Timeline:** Week 5

---

## Right to Object (Art. 21)

### Objection Scenarios

| Processing Type | Legal Basis | Objection Right |
|:----------------|:------------|:---------------:|
| B2B data sharing | Consent | Withdraw consent |
| Marketing | Consent | Unsubscribe |
| Analytics | Legitimate interest | ✅ Can object |
| Core service | Contract | ❌ Cannot object |

### Implementation

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                          OBJECTION MECHANISM                                  ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   Settings → Privacy → Processing Preferences                                ║
║                                                                               ║
║   ┌─────────────────────────────────────────────────────────────────────┐    ║
║   │                                                                     │    ║
║   │   Control how we use your data:                                    │    ║
║   │                                                                     │    ║
║   │   Analytics                                             [ON|off]   │    ║
║   │   Help us improve MILO with usage patterns                         │    ║
║   │                                                                     │    ║
║   │   Marketing Communications                              [on|OFF]   │    ║
║   │   Receive emails about new features                                │    ║
║   │                                                                     │    ║
║   │   Data Contribution                                     [on|OFF]   │    ║
║   │   Share anonymized data for research                               │    ║
║   │                                                                     │    ║
║   └─────────────────────────────────────────────────────────────────────┘    ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

**Implementation Cost:** €2,000 | **Timeline:** Week 6

---

## Automated Decision-Making (Art. 22)

### AI Processing in MILO

| Process | Type | Human Oversight |
|:--------|:-----|:----------------|
| Health scoring | Profiling | User can contest |
| Category assignment | Automated | User can edit |
| Insights generation | Automated | Informational only |

### Safeguards Required

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                        ART. 22 SAFEGUARDS                                     ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   MILO's AI processing:                                                       ║
║   • Does NOT make legally binding decisions                                  ║
║   • Does NOT affect access to services                                       ║
║   • Provides informational insights only                                     ║
║                                                                               ║
║   Nevertheless, we provide:                                                   ║
║   ✅ Transparency: "AI-generated" labels on all scores                       ║
║   ✅ Explanation: How scores are calculated                                  ║
║   ✅ Contest: Flag incorrect scores for review                               ║
║   ✅ Opt-out: Disable health scoring entirely                                ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

## Response Timelines

| Request Type | Standard | Extension | Total Max |
|:-------------|:--------:|:---------:|:---------:|
| Access | 30 days | +60 days | 90 days |
| Rectification | 30 days | +60 days | 90 days |
| Erasure | 30 days | +60 days | 90 days |
| Restriction | 30 days | +60 days | 90 days |
| Portability | 30 days | +60 days | 90 days |
| Objection | Immediate | N/A | N/A |

---

## Implementation Summary

| Right | Cost | Timeline | Priority |
|:------|-----:|:---------|:--------:|
| Access | €5,000 | Week 5 | 🔴 |
| Rectification | €2,000 | Week 6 | 🟡 |
| Erasure | €5,000 | Week 5 | 🔴 |
| Restriction | €2,000 | Week 6 | 🟡 |
| Portability | €5,000 | Week 5 | 🔴 |
| Object | €2,000 | Week 6 | 🟡 |
| **Total** | **€21,000** | **Week 5-6** | |

---

<div align="center">

**Document Version:** 2.0 | January 28, 2026

</div>
