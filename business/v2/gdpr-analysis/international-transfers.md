<div align="center">

# **MILO**
## International Data Transfers Analysis v2.0

---

**DeepmAInd B.V.** | January 28, 2026

</div>

---

## Transfer Overview

| Transfer Route | Data Type | Mechanism | Status |
|:---------------|:----------|:----------|:------:|
| EU → USA (Veryfi) | Receipt images | SCCs required | ❌ Missing |
| EU → USA (Google) | AI prompts | SCCs required | ❌ Missing |
| EU → USA (Firebase) | Auth, analytics | SCCs required | ❌ Missing |
| EU → EU (Railway) | All core data | No transfer | ✅ OK |

---

## Legal Framework

### Post-Schrems II Requirements

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                    INTERNATIONAL TRANSFER REQUIREMENTS                        ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   Since Schrems II (July 2020), transfers to USA require:                    ║
║                                                                               ║
║   1. VALID TRANSFER MECHANISM                                                ║
║      • Standard Contractual Clauses (SCCs) - 2021 version                   ║
║      • Or Binding Corporate Rules (not applicable)                          ║
║                                                                               ║
║   2. TRANSFER IMPACT ASSESSMENT (TIA)                                        ║
║      • Assess US surveillance laws                                           ║
║      • Evaluate supplementary measures needed                                ║
║                                                                               ║
║   3. SUPPLEMENTARY MEASURES                                                   ║
║      • Technical: Encryption, pseudonymization                               ║
║      • Organizational: Access controls, policies                             ║
║      • Contractual: Additional commitments                                   ║
║                                                                               ║
║   EU-US Data Privacy Framework (2023):                                       ║
║   • Provides adequacy for certified US companies                             ║
║   • Google LLC is certified                                                  ║
║   • Veryfi Inc: Status unknown - verify                                      ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

## Transfer 1: Veryfi (OCR Processing)

### Transfer Details

| Attribute | Value |
|:----------|:------|
| **Exporter** | DeepmAInd B.V. (Netherlands) |
| **Importer** | Veryfi Inc. (USA) |
| **Data** | Receipt images (financial data) |
| **Purpose** | OCR text extraction |
| **Volume** | ~75,000 receipts/month (Y3) |
| **Retention** | Transient (<24 hours claimed) |

### Transfer Impact Assessment

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                     VERYFI TRANSFER IMPACT ASSESSMENT                         ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   US LEGAL FRAMEWORK ASSESSMENT                                               ║
║   ─────────────────────────────                                               ║
║   FISA 702: Potentially applicable (cloud provider)                          ║
║   EO 12333: Potential bulk collection risk                                   ║
║                                                                               ║
║   DATA SENSITIVITY ASSESSMENT                                                 ║
║   ───────────────────────────                                                 ║
║   • Financial data (moderate sensitivity)                                    ║
║   • No direct identifiers in images                                          ║
║   • Merchant/location could enable identification                            ║
║   Risk Level: MEDIUM                                                         ║
║                                                                               ║
║   SUPPLEMENTARY MEASURES REQUIRED                                             ║
║   ───────────────────────────────                                             ║
║   ✅ TLS 1.3 in transit                                                      ║
║   ✅ Transient processing (no storage)                                       ║
║   ⬜ Verify DPF certification                                                ║
║   ⬜ SCCs required if not DPF certified                                      ║
║                                                                               ║
║   CONCLUSION: Transfer permissible with SCCs or DPF verification             ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

### Required Actions

| Action | Timeline | Cost |
|:-------|:---------|-----:|
| Verify Veryfi DPF status | Week 1 | - |
| Execute SCCs (if needed) | Week 2 | €3,000 |
| Document supplementary measures | Week 2 | €1,000 |

---

## Transfer 2: Google Gemini (AI Processing)

### Transfer Details

| Attribute | Value |
|:----------|:------|
| **Exporter** | DeepmAInd B.V. (Netherlands) |
| **Importer** | Google LLC (USA) |
| **Data** | Line items text (anonymized) |
| **Purpose** | Health scoring AI |
| **Volume** | ~500,000 API calls/month (Y3) |
| **Retention** | Not retained (API policy) |

### Transfer Impact Assessment

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                     GOOGLE TRANSFER IMPACT ASSESSMENT                         ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   US LEGAL FRAMEWORK ASSESSMENT                                               ║
║   ─────────────────────────────                                               ║
║   FISA 702: Google subject to FISA                                           ║
║   BUT: Google participates in DPF (certified)                                ║
║                                                                               ║
║   DATA SENSITIVITY ASSESSMENT                                                 ║
║   ───────────────────────────                                                 ║
║   • Line items only (no user ID)                                             ║
║   • Pseudonymized before transfer                                            ║
║   • Cannot identify individual users                                         ║
║   Risk Level: LOW                                                            ║
║                                                                               ║
║   DPF CERTIFICATION STATUS                                                    ║
║   ────────────────────────                                                    ║
║   Google LLC: ✅ CERTIFIED                                                   ║
║   https://www.dataprivacyframework.gov/s/participant-search                  ║
║                                                                               ║
║   CONCLUSION: Transfer permissible under DPF adequacy                        ║
║               SCCs recommended as supplementary                              ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

### Required Actions

| Action | Timeline | Cost |
|:-------|:---------|-----:|
| Verify DPF certification | Week 1 | - |
| Execute Google DPA with SCCs | Week 2 | €2,000 |
| Document pseudonymization | Week 2 | €500 |

---

## Transfer 3: Firebase (Auth, Storage, Analytics)

### Transfer Details

| Attribute | Value |
|:----------|:------|
| **Exporter** | DeepmAInd B.V. (Netherlands) |
| **Importer** | Google LLC (USA) - Firebase |
| **Data** | Auth tokens, profile images, analytics |
| **Purpose** | Authentication, storage, analytics |
| **Volume** | All active users |
| **Retention** | Account lifetime |

### Transfer Impact Assessment

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                    FIREBASE TRANSFER IMPACT ASSESSMENT                        ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   US LEGAL FRAMEWORK ASSESSMENT                                               ║
║   ─────────────────────────────                                               ║
║   FISA 702: Google subject to FISA                                           ║
║   BUT: Google participates in DPF (certified)                                ║
║                                                                               ║
║   DATA SENSITIVITY ASSESSMENT                                                 ║
║   ───────────────────────────                                                 ║
║   Authentication:                                                             ║
║   • Tokens (technical data)                                                  ║
║   • Email addresses (personal data)                                          ║
║   Risk Level: MEDIUM                                                         ║
║                                                                               ║
║   Storage:                                                                    ║
║   • Profile images (personal data)                                           ║
║   Risk Level: LOW                                                            ║
║                                                                               ║
║   Analytics:                                                                  ║
║   • Usage patterns (pseudonymized)                                           ║
║   Risk Level: LOW                                                            ║
║                                                                               ║
║   SUPPLEMENTARY MEASURES                                                      ║
║   ─────────────────────                                                       ║
║   ✅ Firebase encryption at rest                                             ║
║   ✅ TLS in transit                                                          ║
║   ⬜ Configure EU data residency where available                             ║
║                                                                               ║
║   CONCLUSION: Transfer permissible under DPF + standard DPA                  ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

### Required Actions

| Action | Timeline | Cost |
|:-------|:---------|-----:|
| Accept Firebase/Google DPA | Week 2 | - |
| Configure EU data residency | Week 2 | - |
| Document transfer safeguards | Week 2 | €500 |

---

## Transfer 4: Railway (Backend Hosting)

### Transfer Details

| Attribute | Value |
|:----------|:------|
| **Exporter** | DeepmAInd B.V. (Netherlands) |
| **Importer** | Railway Corp. |
| **Data** | All core user data |
| **Location** | EU region configurable |

### Assessment

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                     RAILWAY TRANSFER ASSESSMENT                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   RAILWAY EU DEPLOYMENT                                                       ║
║   ─────────────────────                                                       ║
║   Railway offers EU region deployment                                        ║
║   Data remains within EU jurisdiction                                        ║
║                                                                               ║
║   CONFIGURATION REQUIRED                                                      ║
║   ─────────────────────                                                       ║
║   ✅ Select EU region for all services                                       ║
║   ✅ PostgreSQL in EU                                                        ║
║   ✅ FastAPI backend in EU                                                   ║
║                                                                               ║
║   TRANSFER STATUS: NO INTERNATIONAL TRANSFER                                 ║
║                                                                               ║
║   DPA still required for processor relationship                              ║
║   SCCs NOT required (no third country transfer)                              ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

### Required Actions

| Action | Timeline | Cost |
|:-------|:---------|-----:|
| Verify EU deployment | Week 1 | - |
| Execute DPA | Week 3 | €3,000 |

---

## Standard Contractual Clauses

### SCC Implementation

| Processor | SCC Module | Status |
|:----------|:-----------|:------:|
| Veryfi | Module 2 (C→P) | ⬜ Required |
| Google (Gemini) | Module 2 (C→P) | ⬜ Via DPA |
| Firebase | Module 2 (C→P) | ⬜ Via DPA |
| Railway | Not required | N/A |

### SCC Documentation Checklist

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                         SCC DOCUMENTATION                                     ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   For each transfer requiring SCCs:                                          ║
║                                                                               ║
║   ⬜ Annex I.A: List of parties                                              ║
║   ⬜ Annex I.B: Description of transfer                                      ║
║   ⬜ Annex I.C: Competent supervisory authority                              ║
║   ⬜ Annex II: Technical/organizational measures                             ║
║   ⬜ Annex III: List of sub-processors (if applicable)                       ║
║   ⬜ Transfer Impact Assessment                                              ║
║   ⬜ Supplementary measures documentation                                    ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

## Implementation Timeline

| Week | Activity | Deliverable |
|:----:|:---------|:------------|
| 1 | Verify DPF certifications | Status report |
| 2 | Initiate SCC negotiations | Draft agreements |
| 3 | Execute SCCs with Veryfi | Signed SCCs |
| 4 | Execute Google DPA | Signed DPA |
| 5 | Complete TIA documentation | TIA reports |
| 6 | Final transfer documentation | Complete package |

---

## Budget Summary

| Item | Cost |
|:-----|-----:|
| Veryfi SCCs | €3,000 |
| Google DPA review | €2,000 |
| TIA documentation | €2,000 |
| Supplementary measures docs | €1,000 |
| **Total** | **€8,000** |

---

<div align="center">

**Document Version:** 2.0 | January 28, 2026

</div>
