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
| 100 Users | $125 - $180 | $1.25 - $1.80 |
| 1,000 Users | $220 - $450 | $0.22 - $0.45 |
| 10,000 Users | $1,200 - $2,500 | $0.12 - $0.25 |
| 50,000 Users | $5,500 - $12,000 | $0.11 - $0.24 |

### Key Cost Drivers (in order of impact)

1. **Veryfi OCR API** - Largest variable cost (~60% of variable costs)
2. **Railway Hosting** - Primary infrastructure cost
3. **Anthropic Claude API** - Chat feature (V1 only)
4. **Google Gemini API** - Very cost-effective for categorization
5. **Firebase Authentication** - Free up to 50K MAUs

### Critical Insights

- **Veryfi OCR is your #1 cost driver** - At ~$0.08/receipt, this dominates variable costs
- **Rate limiting is crucial** - Your 15 receipts/30 days limit is essential for cost control
- **Chat costs are manageable** - 100 messages/30 days limit helps control AI costs
- **Firebase is essentially free** - Google Sign-In only means no SMS costs
- **Apple takes 15-30%** - Factor App Store commission into subscription pricing

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
| Railway (Pro) | $20 | $30 |
| Veryfi OCR | $60 | $120 |
| Gemini API | $0.13 | $0.25 |
| Claude API (V1 chat) | $34 | $68 |
| Firebase | $0 | $0 |
| Apple Developer (monthly) | $8.25 | $8.25 |
| **TOTAL** | **$122.38** | **$226.50** |
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

**Key Insight:** With a 35-50% conversion rate, the app becomes profitable at 1,000 total users.

---

## 7. Cost Optimization Recommendations

### 7.1 High Impact Optimizations

#### Migrate V1 Chat to V2 (Gemini)
- **Current:** Claude Sonnet 4 at $3/$15 per million tokens
- **Proposed:** Gemini 2.0 Flash at $0.10/$0.40 per million tokens
- **Savings:** ~97% reduction in chat costs
- **Impact at 10K users:** Save $3,000-$6,500/month

#### Negotiate Veryfi Volume Pricing
- Contact Veryfi for enterprise pricing at 10K+ documents
- Expected discount: 20-40% at scale
- **Impact at 10K users:** Save $1,200-$4,800/month

#### Implement Receipt Caching
- Cache extracted receipt data to avoid re-processing
- Prevent duplicate API calls for identical receipts
- **Impact:** 5-15% reduction in Veryfi costs

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
| Veryfi price increase | Medium | High | Negotiate long-term contract |
| Viral growth spike | Low | High | Set hard rate limits |
| API outages | Low | Medium | Implement retry logic |
| Apple commission increase | Low | Medium | Diversify revenue |

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
