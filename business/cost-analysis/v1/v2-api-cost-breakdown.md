# MILO APP - V2 API Detailed Cost Breakdown

**Comprehensive Analysis of Per-Transaction Costs**

Analysis Date: January 28, 2026

---

## Section 1: V2 API Architecture Overview

The Milo V2 API utilizes the following external services for receipt processing and AI-powered insights:

### Primary Services
- **Veryfi API v8** - OCR and receipt data extraction
- **Google Gemini 2.0 Flash** - AI categorization and health scoring
- **Firebase Authentication** - User identity management
- **Firebase Cloud Storage** - File storage
- **Railway** - Backend hosting infrastructure
- **PostgreSQL** - Database (included with Railway)

### V2 vs V1 Comparison
The V2 API was specifically designed for cost optimization by replacing Claude Sonnet 4 (used in V1) with Gemini 2.0 Flash for categorization tasks, resulting in approximately **95% cost reduction** for AI processing.

---

## Section 2: Receipt Upload Cost Analysis

Each receipt upload triggers the following API calls:

### Step 1: Veryfi OCR Processing
- **Endpoint:** `https://api.veryfi.com/api/v8/partner/documents`
- **Cost:** $0.0800 per document
- **What it does:** Extracts vendor name, date, total amount, and line items from receipt images

### Step 2: Gemini 2.0 Flash Categorization
- **Model:** gemini-2.0-flash
- **Input tokens (typical):** ~500 tokens
- **Output tokens (typical):** ~300 tokens
- **Cost calculation:**
  - Input: 500 tokens × ($0.10 / 1,000,000) = $0.00005
  - Output: 300 tokens × ($0.40 / 1,000,000) = $0.00012
  - **Total:** $0.00017 per categorization

### Step 3: Database Operations
- **Cost:** Included in Railway hosting
- **Operations:** Receipt record creation, transaction records, status updates

### **TOTAL COST PER RECEIPT UPLOAD: $0.0802**

---

## Cost Breakdown by Component

| Component | Cost per Receipt | % of Total |
|-----------|------------------|------------|
| Veryfi OCR | $0.0800 | 99.75% |
| Gemini Categorization | $0.0002 | 0.25% |
| Database Operations | $0.0000 | 0.00% |
| **TOTAL** | **$0.0802** | **100.00%** |

**CRITICAL INSIGHT:** Veryfi OCR dominates the cost structure. Any cost optimization strategy must focus on reducing OCR calls or negotiating volume pricing with Veryfi.

---

## Section 3: Chat Message Cost Analysis

Each chat message in the V2 API uses Gemini 2.0 Flash:

### Chat Request Processing
- **Model:** gemini-2.0-flash
- **Typical input context:** ~1,000 tokens (includes user history and spending data)
- **Typical output response:** ~500 tokens

### Cost Calculation
- Input: 1,000 tokens × ($0.10 / 1,000,000) = $0.0001
- Output: 500 tokens × ($0.40 / 1,000,000) = $0.0002
- **Total:** $0.0003 per message

### **TOTAL COST PER CHAT MESSAGE: $0.0003**

### V1 vs V2 Comparison
| API Version | Model | Cost per Message |
|-------------|-------|------------------|
| V1 API | Claude Sonnet 4 | ~$0.0045 |
| V2 API | Gemini 2.0 Flash | ~$0.0003 |
| **SAVINGS** | | **93% reduction** |

---

## Section 4: Infrastructure Costs

### Railway Hosting

**Plan:** Hobby ($5/month base)
**Included:** $5 resource credit

**Resource Rates:**
| Resource | Rate |
|----------|------|
| Memory | $10/GB/month |
| vCPU | $20/vCPU/month |
| Network Egress | $0.05/GB |
| Volume Storage | $0.15/GB/month |

**Estimated Usage (1,000 users):**
| Resource | Usage | Cost |
|----------|-------|------|
| Memory | 0.5GB | $5.00/month |
| vCPU | 0.25 | $5.00/month |
| Egress | 10GB | $0.50/month |
| **Total** | | **$10.50/month** |

### Firebase Authentication

**Pricing Model:** Free up to 50,000 MAUs

| MAU Range | Cost |
|-----------|------|
| <50,000 MAUs | $0.00/month |
| 50,000-100,000 MAUs | ~$275/month |
| 100,000+ MAUs | Contact for enterprise pricing |

### Firebase Cloud Storage

| Usage | Rate |
|-------|------|
| Storage | $0.026/GB/month |
| Download | $0.12/GB transferred |

**Estimated Usage:**
- Profile data (~20GB): $0.52/month
- Downloads (~50GB): $6.00/month
- **Total:** ~$6.52/month

### PostgreSQL Database
Included with Railway hosting - No additional cost

---

## Section 5: Veryfi Pricing Deep Dive

### Current Pricing Tiers

**Free Tier:**
- 100 documents total OR 50 documents/month
- Suitable for development/testing only

**Starter Plan:**
- $500/month minimum
- Includes 6,250 receipts
- Per-receipt cost: $0.08
- 12-month commitment: $0.07/receipt

### Volume Discounts

| Monthly Receipts | Standard Cost | With Volume Discount* |
|------------------|---------------|----------------------|
| 1,000 | $80.00 | $80.00 |
| 5,000 | $400.00 | $400.00 |
| 10,000 | $800.00 | ~$640.00 (20% off) |
| 25,000 | $2,000.00 | ~$1,500.00 (25% off) |
| 50,000 | $4,000.00 | ~$2,800.00 (30% off) |
| 100,000 | $8,000.00 | ~$5,200.00 (35% off) |

*Volume discounts are estimates based on industry standards. Contact Veryfi for actual rates.

---

## Section 6: Gemini 2.0 Flash Pricing Deep Dive

### Current Pricing (January 2026)

| Token Type | Price |
|------------|-------|
| Input Tokens | $0.10 per 1 million tokens |
| Output Tokens | $0.40 per 1 million tokens |

### Free Tier Available
- Rate limited
- Google may use data for model improvement
- Suitable for development and low-volume production

### Cost Projection by Message Volume

| Monthly Messages | Input Tokens | Output Tokens | Total Cost |
|------------------|--------------|---------------|------------|
| 1,000 | 1M | 0.5M | $0.30 |
| 10,000 | 10M | 5M | $3.00 |
| 50,000 | 50M | 25M | $15.00 |
| 100,000 | 100M | 50M | $30.00 |
| 500,000 | 500M | 250M | $150.00 |

**KEY INSIGHT:** Gemini costs are negligible compared to Veryfi. Even at massive scale (500K messages/month), the cost is only $150 - less than 200 receipt uploads.

---

## Section 7: Total Cost Modeling

### Scenario A: 1,000 Monthly Active Users

**Assumptions:**
- Silver (70%): 700 users × 8 receipts × 40 messages avg usage
- Gold (25%): 250 users × 30 receipts × 150 messages avg usage
- Platinum (5%): 50 users × 100 receipts × 400 messages avg usage

**Receipt Costs:**
| Tier | Calculation | Cost |
|------|-------------|------|
| Silver | 700 × 8 × $0.0802 | $449.12 |
| Gold | 250 × 30 × $0.0802 | $601.50 |
| Platinum | 50 × 100 × $0.0802 | $401.00 |
| **Total** | 18,100 receipts | **$1,451.62** |

**Chat Costs:**
| Tier | Calculation | Cost |
|------|-------------|------|
| Silver | 700 × 40 × $0.0003 | $8.40 |
| Gold | 250 × 150 × $0.0003 | $11.25 |
| Platinum | 50 × 400 × $0.0003 | $6.00 |
| **Total** | 74,500 messages | **$25.65** |

**Infrastructure:**
| Service | Cost |
|---------|------|
| Railway | $15.00 |
| Firebase Auth | $0.00 |
| Firebase Storage | $10.00 |
| **Total** | **$25.00** |

### **TOTAL MONTHLY COST (1K users): $1,502.27**

---

### Scenario B: 10,000 Monthly Active Users

**Receipt Costs (with 20% volume discount):**
- Total Receipts: ~181,000 receipts
- Standard cost: $14,516.20
- **With discount: $11,612.96**

**Chat Costs:**
- Total Messages: ~745,000 messages
- **Cost: $223.50**

**Infrastructure:**
| Service | Cost |
|---------|------|
| Railway (Pro) | $50.00 |
| Firebase Auth | $0.00 |
| Firebase Storage | $50.00 |
| **Total** | **$100.00** |

### **TOTAL MONTHLY COST (10K users): $11,936.46**
### **Cost per user: $1.19/month**

---

### Scenario C: 100,000 Monthly Active Users

**Receipt Costs (with 35% volume discount):**
- Total Receipts: ~1,810,000 receipts
- Standard cost: $145,162.00
- **With discount: $94,355.30**

**Chat Costs:**
- Total Messages: ~7,450,000 messages
- **Cost: $2,235.00**

**Infrastructure:**
| Service | Cost |
|---------|------|
| Railway (Enterprise) | $500.00 |
| Firebase Auth | $275.00 |
| Firebase Storage | $500.00 |
| **Total** | **$1,275.00** |

### **TOTAL MONTHLY COST (100K users): $97,865.30**
### **Cost per user: $0.98/month**

**ECONOMIES OF SCALE:** Cost per user decreases from $1.50 at 1K users to $0.98 at 100K users - a 35% reduction driven primarily by Veryfi volume discounts.

---

## Section 8: Cost Optimization Strategies

### 1. VERYFI VOLUME NEGOTIATION
- **Potential Savings:** 20-35% on largest cost component
- **Action:** Contact Veryfi at api@veryfi.com for enterprise pricing

### 2. RECEIPT CACHING/DEDUPLICATION
- **Current:** Duplicate detection already implemented
- **Enhancement:** Add fuzzy matching to catch near-duplicates
- **Potential Savings:** 5-10% reduction in OCR calls

### 3. TIERED RATE LIMITS
- **Current:** Flat 15 receipts/month for all users
- **Proposed:** 10/40/150 by tier
- **Impact:** Better cost allocation to revenue-generating users

### 4. GEMINI FREE TIER UTILIZATION
- **Strategy:** Use free tier for low-priority requests
- **Limitation:** Rate limits and data usage policies apply

### 5. ANNUAL COMMITMENT DISCOUNTS
- **Veryfi:** 12-month commit saves $0.01/document
- **At 100K docs/month:** $1,000/month savings

---

## Appendix: API Pricing Sources

| Service | Source | Verified |
|---------|--------|----------|
| Veryfi OCR API | veryfi.com/pricing | January 2026 |
| Google Gemini 2.0 Flash | ai.google.dev/gemini-api/docs/pricing | January 2026 |
| Railway Hosting | railway.com/pricing | January 2026 |
| Firebase | firebase.google.com/pricing | January 2026 |

---

*Document prepared by: AI Business Analysis*
*For: DeepmAInd / Milo App*
*Version: 2.0 (V2 API Focus)*
