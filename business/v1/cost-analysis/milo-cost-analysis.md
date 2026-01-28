# Milo iOS App - Comprehensive Cost Analysis Report

**Document Version:** 1.0
**Date:** January 2026
**Prepared for:** DeepmAInd
**Application:** Milo - Receipt Scanning & Expense Tracking iOS App

---

## Table of Contents

1. Executive Summary
2. Infrastructure Overview
3. Fixed Costs Analysis
4. Variable Costs Analysis
5. Cost Projections by User Scale
6. Revenue & Break-Even Analysis
7. Cost Optimization Recommendations
8. Risk Assessment
9. Appendix: Pricing Sources

---

## 1. Executive Summary

### Total Monthly Cost Estimates

| User Scale | Monthly Cost | Per-User Cost |
|------------|--------------|---------------|
| 100 Users | <span style="color:#ef4444">$125 - $180</span> | $1.25 - $1.80 |
| 1,000 Users | <span style="color:#ef4444">$220 - $450</span> | $0.22 - $0.45 |
| 10,000 Users | <span style="color:#ef4444">$1,200 - $2,500</span> | $0.12 - $0.25 |
| 50,000 Users | <span style="color:#ef4444">$5,500 - $12,000</span> | $0.11 - $0.24 |

### Key Cost Drivers (in order of impact)

1. <span style="color:#ef4444">**Veryfi OCR API**</span> - Largest variable cost (~60% of variable costs)
2. <span style="color:#f59e0b">**Railway Hosting**</span> - Primary infrastructure cost
3. <span style="color:#f59e0b">**Anthropic Claude API**</span> - Chat feature (V1 only)
4. <span style="color:#16a34a">**Google Gemini API**</span> - Very cost-effective for categorization
5. <span style="color:#16a34a">**Firebase Authentication**</span> - Free up to 50K MAUs

### Critical Insights

<span style="background-color:#fee2e2; padding: 8px; display: block; border-left: 4px solid #ef4444; margin-bottom: 8px;">**Veryfi OCR is your #1 cost driver** - At ~<span style="color:#ef4444">$0.08/receipt</span>, this dominates variable costs</span>

<span style="background-color:#dbeafe; padding: 8px; display: block; border-left: 4px solid #3b82f6; margin-bottom: 8px;">**Rate limiting is crucial** - Your 15 receipts/30 days limit is essential for cost control</span>

<span style="background-color:#dcfce7; padding: 8px; display: block; border-left: 4px solid #22c55e; margin-bottom: 8px;">**Chat costs are manageable** - 100 messages/30 days limit helps control AI costs</span>

<span style="background-color:#dcfce7; padding: 8px; display: block; border-left: 4px solid #22c55e; margin-bottom: 8px;">**Firebase is essentially free** - Google Sign-In only means no SMS costs</span>

<span style="background-color:#fef3c7; padding: 8px; display: block; border-left: 4px solid #f59e0b;">**Apple takes 15-30%** - Factor App Store commission into subscription pricing</span>

---

## 2. Infrastructure Overview

### Architecture Summary

```
┌─────────────────────────────────────────────────────────────────────┐
│                        MILO iOS APPLICATION                         │
│                      (SwiftUI / StoreKit 2)                        │
└─────────────────────────┬───────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     RAILWAY INFRASTRUCTURE                          │
│  ┌─────────────────────┐    ┌─────────────────────────────────┐   │
│  │   FastAPI Backend   │────│   PostgreSQL Database          │   │
│  │   (Python 3.11)     │    │   (Managed by Railway)          │   │
│  └─────────┬───────────┘    └─────────────────────────────────┘   │
└────────────┼────────────────────────────────────────────────────────┘
             │
             ├──────────────────┬──────────────────┬─────────────────┐
             ▼                  ▼                  ▼                 ▼
┌────────────────────┐ ┌───────────────┐ ┌───────────────┐ ┌──────────────┐
│    Veryfi API      │ │ Google Gemini │ │ Claude API    │ │   Firebase   │
│   (OCR/Receipt)    │ │  (Categorize) │ │   (Chat V1)   │ │    (Auth)    │
│   ~$0.08/receipt   │ │ $0.10/$0.40/M │ │  $3/$15/M     │ │  Free <50K   │
└────────────────────┘ └───────────────┘ └───────────────┘ └──────────────┘
```

### Services Used

| Service | Purpose | Billing Model |
|---------|---------|---------------|
| Railway | Backend hosting + PostgreSQL | Usage-based (CPU, RAM, Storage) |
| Veryfi | Receipt OCR extraction | Per document |
| Google Gemini | Item categorization | Per token |
| Anthropic Claude | Chat assistant (V1 only) | Per token |
| Firebase | User authentication | Per MAU (free <50K) |
| Apple | App distribution + payments | Annual fee + commission |

---

## 3. Fixed Costs Analysis

### Annual Fixed Costs

| Item | Cost | Notes |
|------|------|-------|
| Apple Developer Program | $99/year | Required for App Store distribution |
| Domain Name (optional) | $12-50/year | For custom API domain |
| SSL Certificate | $0 | Railway includes free SSL |
| **Total Annual Fixed** | **$99 - $149** | |
| **Monthly Equivalent** | **$8.25 - $12.42** | |

### Railway Base Costs

| Plan | Monthly Fee | Included Credits | Best For |
|------|-------------|------------------|----------|
| Hobby | $5/month | $5 | Development/Testing |
| Pro | $20/month | $20 | Production apps |
| Team | $20/seat | $20/seat | Multiple developers |

**Recommendation:** Start with Pro Plan ($20/month) for production deployment.

---

## 4. Variable Costs Analysis

### 4.1 Veryfi OCR API (Primary Cost Driver)

**Pricing Structure:**
- Free tier: 50-100 documents total (not monthly)
- Paid: ~$0.08 per receipt
- Volume discount: Available at 10,000+ documents

**Cost Calculation per User:**
| Metric | Value |
|--------|-------|
| User Rate Limit | 15 receipts per 30 days |
| Cost per Receipt | $0.08 |
| Maximum Cost per Active User | 15 × $0.08 = $1.20/month |
| Average Cost (50% utilization) | $0.60/month per active user |

**Monthly Veryfi Costs by Scale:**

| Active Users | Receipts (50%) | Receipts (100%) | Monthly Cost Range |
|--------------|----------------|-----------------|-------------------|
| 100 | 750 | 1,500 | $60 - $120 |
| 1,000 | 7,500 | 15,000 | $600 - $1,200 |
| 10,000 | 75,000 | 150,000 | $6,000 - $12,000 |
| 50,000 | 375,000 | 750,000 | Contact for volume |

### 4.2 Google Gemini 2.0 Flash API (Categorization)

**Pricing:**
- Input: $0.10 per million tokens
- Output: $0.40 per million tokens

**Usage Estimate per Receipt:**
- Input: ~500 tokens (store name + items list)
- Output: ~300 tokens (categorized items + health scores)
- Cost per receipt: ~$0.00017 (essentially negligible)

**Insight:** Gemini costs are negligible - excellent choice for categorization!

### 4.3 Anthropic Claude Sonnet 4 API (Chat - V1 Only)

**Pricing:**
- Input: $3.00 per million tokens
- Output: $15.00 per million tokens

**Usage Estimate per Chat Message:**
- Input (system prompt + context): ~2,000 tokens
- Output (response): ~500 tokens
- Cost per message: ~$0.0135

**Note:** V2 API uses Gemini instead of Claude, which is ~100x cheaper for chat!

### 4.4 Firebase Authentication

**Pricing:**
- Free: Up to 50,000 MAUs
- Paid: $0.0025 - $0.0055 per MAU (above 50K)
- Google Sign-In: No SMS costs

**Insight:** Firebase is free until you reach significant scale!

### 4.5 Railway Usage Costs (Beyond Base Plan)

**Usage Rates (approximate):**
- Compute: $0.000463/min (~$20/month for always-on service)
- Memory: $0.000231/GB-min
- Network: Included in most cases
- PostgreSQL: Counts against usage credits

---

## 5. Cost Projections by User Scale

### Scenario A: 100 Monthly Active Users (Launch Phase)

| Cost Category | Low Estimate | High Estimate |
|---------------|--------------|---------------|
| Railway (Pro) | <span style="color:#ef4444">$20</span> | <span style="color:#ef4444">$30</span> |
| Veryfi OCR | <span style="color:#ef4444">$60</span> | <span style="color:#ef4444">$120</span> |
| Gemini API | <span style="color:#16a34a">$0.13</span> | <span style="color:#16a34a">$0.25</span> |
| Claude API (V1 chat) | <span style="color:#ef4444">$34</span> | <span style="color:#ef4444">$68</span> |
| Firebase | <span style="color:#16a34a">$0</span> | <span style="color:#16a34a">$0</span> |
| Apple Developer (monthly) | $8.25 | $8.25 |
| <span style="color:#ef4444">**TOTAL**</span> | <span style="color:#ef4444">**$122.38**</span> | <span style="color:#ef4444">**$226.50**</span> |
| **Per User** | **$1.22** | **$2.27** |

### Scenario B: 1,000 Monthly Active Users (Growth Phase)

| Cost Category | Low Estimate | High Estimate |
|---------------|--------------|---------------|
| Railway (Pro) | $30 | $50 |
| Veryfi OCR | $600 | $1,200 |
| Gemini API | $1.28 | $2.50 |
| Claude API (V1 chat) | $338 | $675 |
| Firebase | $0 | $0 |
| Apple Developer (monthly) | $8.25 | $8.25 |
| **TOTAL** | **$977.53** | **$1,935.75** |
| **Per User** | **$0.98** | **$1.94** |

### Scenario C: 10,000 Monthly Active Users (Scale Phase)

| Cost Category | Low Estimate | High Estimate |
|---------------|--------------|---------------|
| Railway (Pro) | $50 | $150 |
| Veryfi OCR | $6,000 | $12,000 |
| Gemini API | $12.75 | $25 |
| Claude API (V1 chat) | $3,375 | $6,750 |
| Firebase | $0 | $0 |
| Apple Developer (monthly) | $8.25 | $8.25 |
| **TOTAL** | **$9,446** | **$18,933** |
| **Per User** | **$0.94** | **$1.89** |

---

## 6. Revenue & Break-Even Analysis

### Subscription Pricing Strategy

| Plan | Monthly Price | Annual Price | Annual Savings |
|------|---------------|--------------|----------------|
| Milo Basic (Free) | $0 | $0 | - |
| Milo Premium | $4.99 | $39.99 | 33% |
| Milo Pro | $9.99 | $79.99 | 33% |

### Apple Commission Impact

| Revenue Tier | Commission Rate | Effective Rate |
|--------------|-----------------|----------------|
| < $1M/year (Small Business) | 15% | You keep 85% |
| > $1M/year | 30% | You keep 70% |
| Subscription after Year 1 | 15% | You keep 85% |

### Break-Even Analysis

**Assumptions:**
- All users on Premium Monthly ($4.99)
- Small Business Program (15% commission)
- Net revenue per user: $4.24/month
- Average cost per user: $1.50/month (mid-range estimate)

| Scenario | Monthly Cost | Break-Even Users | At 1,000 Users |
|----------|--------------|------------------|----------------|
| Low Cost | $0.98/user | 303 paying users | +$3,260 profit |
| Mid Cost | $1.50/user | 546 paying users | +$2,740 profit |
| High Cost | $2.00/user | 893 paying users | +$2,240 profit |

<span style="background-color:#dcfce7; padding: 8px; display: block; border-left: 4px solid #22c55e;">**Key Insight:** With a 35-50% conversion rate, the app becomes <span style="color:#16a34a">profitable at 1,000 total users</span>.</span>

---

## 7. Cost Optimization Recommendations

### 7.1 High Impact Optimizations

#### <span style="color:#3b82f6">Migrate V1 Chat to V2 (Gemini)</span>
- **Current:** Claude Sonnet 4 at <span style="color:#ef4444">$3/$15 per million tokens</span>
- **Proposed:** Gemini 2.0 Flash at <span style="color:#16a34a">$0.10/$0.40 per million tokens</span>
- **Savings:** <span style="color:#16a34a">~97% reduction in chat costs</span>
- **Impact at 10K users:** Save <span style="color:#16a34a">$3,000-$6,500/month</span>

#### <span style="color:#3b82f6">Negotiate Veryfi Volume Pricing</span>
- Contact Veryfi for enterprise pricing at 10K+ documents
- Expected discount: 20-40% at scale
- **Impact at 10K users:** Save <span style="color:#16a34a">$1,200-$4,800/month</span>

#### <span style="color:#3b82f6">Implement Receipt Caching</span>
- Cache extracted receipt data to avoid re-processing
- Prevent duplicate API calls for identical receipts
- **Impact:** <span style="color:#16a34a">5-15% reduction in Veryfi costs</span>

### 7.2 Medium Impact Optimizations

#### Use Claude Batch API
- 50% discount for non-real-time processing
- Implement for analytics summaries, not real-time chat
- **Savings:** Up to 50% on batch-eligible requests

#### Implement Prompt Caching
- Claude's 5-minute cache: 90% discount on cached reads
- Cache the system prompt and transaction context
- **Savings:** 30-50% on Claude costs

---

## 8. Risk Assessment

### Cost Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Veryfi price increase | <span style="color:#f59e0b">Medium</span> | <span style="color:#ef4444">High</span> | Negotiate long-term contract |
| Viral growth spike | <span style="color:#16a34a">Low</span> | <span style="color:#ef4444">High</span> | Set hard rate limits |
| API outages | <span style="color:#16a34a">Low</span> | <span style="color:#f59e0b">Medium</span> | Implement retry logic |
| Apple commission increase | <span style="color:#16a34a">Low</span> | <span style="color:#f59e0b">Medium</span> | Diversify revenue |

### API Alternatives (Risk Mitigation)

**Veryfi Alternatives:**
- Google Document AI - ~$0.01-0.05/page
- Amazon Textract - ~$0.015/page
- Microsoft Form Recognizer - ~$0.01/page

*Note: Veryfi's receipt-specific extraction may justify premium pricing.*

### Scaling Considerations

| Users | Key Actions Required |
|-------|---------------------|
| 1,000 | Establish Veryfi relationship; monitor costs |
| 5,000 | Negotiate volume discounts; optimize queries |
| 10,000 | Consider Railway Pro+; negotiate all API contracts |
| 50,000 | Migrate to enterprise pricing; consider dedicated infra |

---

## 9. Appendix: Pricing Sources

| Service | URL |
|---------|-----|
| Railway | https://railway.com/pricing |
| Veryfi | https://www.veryfi.com/pricing/ |
| Google Gemini | https://ai.google.dev/gemini-api/docs/pricing |
| Anthropic Claude | https://platform.claude.com/docs/en/about-claude/pricing |
| Firebase | https://firebase.google.com/pricing |
| Apple | https://developer.apple.com/app-store/small-business-program/ |

---

## Document Information

| Field | Value |
|-------|-------|
| Report Generated | January 2026 |
| Application | Milo iOS App (Bundle: com.deepmaind.Milo) |
| Backend | Railway + FastAPI + PostgreSQL |
| Prepared By | DeepmAInd Cost Analysis |

*This cost analysis is based on publicly available pricing information as of January 2026. Actual costs may vary based on usage patterns, negotiated rates, and pricing changes.*
