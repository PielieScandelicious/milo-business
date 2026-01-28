# MILO APP - V2 API Cost Analysis Executive Summary

**Tier-Based Receipt Upload Rate Limiting**

Analysis Date: January 28, 2026

---

## Executive Overview

This document presents a comprehensive cost analysis for implementing a three-tier subscription model (Silver, Gold, Platinum) for the Milo iOS personal finance app. The analysis focuses exclusively on V2 API endpoints, which utilize Google Gemini 2.0 Flash for AI processing—a strategic choice that significantly reduces operational costs compared to V1 endpoints.

---

## Key Findings

### Cost Structure Summary

The V2 API architecture generates the following primary costs per user action:

| Action | Cost | Breakdown |
|--------|------|-----------|
| **Receipt Upload** | $0.0802 per receipt | Veryfi OCR: $0.0800 + Gemini: $0.0002 |
| **Chat Message** | $0.0003 per message | Gemini 2.0 Flash Processing |

**KEY INSIGHT:** Veryfi OCR represents 99.75% of variable costs. Receipt upload limits are the critical lever for cost management.

---

## Recommended Tier Structure

### SILVER TIER (Entry Level)

| Attribute | Value |
|-----------|-------|
| Monthly Limits | 10 receipts \| 50 chat messages |
| Variable Cost | $0.82 per user/month |
| Recommended Price | FREE (Ad-supported or freemium) |
| Strategic Purpose | User acquisition and conversion funnel |

### GOLD TIER (Standard)

| Attribute | Value |
|-----------|-------|
| Monthly Limits | 40 receipts \| 200 chat messages |
| Variable Cost | $3.26 per user/month |
| Recommended Price | $5.99 - $6.99/month |
| Gross Margin | 46% - 54% |
| Strategic Purpose | Core revenue generation |

### PLATINUM TIER (Premium)

| Attribute | Value |
|-----------|-------|
| Monthly Limits | 150 receipts \| 500 chat messages |
| Variable Cost | $12.15 per user/month |
| Recommended Price | $14.99 - $19.99/month |
| Gross Margin | 19% - 39% |
| Strategic Purpose | Power user retention and premium positioning |

---

## Infrastructure Costs

### Fixed Monthly Costs (Baseline)

| Service | Cost |
|---------|------|
| Railway Hosting (Hobby) | $5.00/month |
| Firebase Authentication | $0.00 (Free tier covers <50K MAUs) |
| PostgreSQL Database | Included in Railway |
| Firebase Storage (~20GB) | $0.52/month |
| **Total Fixed Infrastructure** | **$5.52/month** |

**IMPORTANT:** These costs scale with user growth. At 10,000+ MAU, expect infrastructure costs of $50-150/month.

---

## Profitability Projections

### Scenario: 1,000 Active Users

**Distribution Assumption:**
- 700 Silver (70%)
- 250 Gold (25%)
- 50 Platinum (5%)

**Monthly Revenue:**

| Tier | Users | Price | Revenue |
|------|-------|-------|---------|
| Silver | 700 | $0 | $0 |
| Gold | 250 | $6.49 | $1,622.50 |
| Platinum | 50 | $17.49 | $874.50 |
| **Total** | | | **$2,497.00** |

**Monthly Variable Costs:**

| Tier | Users | Cost/User | Total |
|------|-------|-----------|-------|
| Silver | 700 | $0.82 | $574.00 |
| Gold | 250 | $3.26 | $815.00 |
| Platinum | 50 | $12.15 | $607.50 |
| **Total** | | | **$1,996.50** |

**Monthly Fixed Costs:** ~$15.00 (scaled infrastructure)

### **Net Monthly Profit: $485.50**
### **Net Margin: 19.4%**

---

## Strategic Recommendations

### 1. PRIORITIZE GOLD TIER CONVERSIONS
The Gold tier offers the best margin-to-value ratio. Focus marketing efforts on converting Silver users to Gold.

### 2. IMPLEMENT USAGE-BASED OVERAGE CHARGES
Consider allowing users to purchase additional receipts at $0.15-0.20 each (88-150% margin) rather than forcing tier upgrades.

### 3. NEGOTIATE VERYFI VOLUME PRICING
At 10,000+ monthly documents, contact Veryfi for volume discounts. A 20% reduction in OCR costs would increase Gold tier margins by 12 percentage points.

### 4. MONITOR SILVER TIER CAREFULLY
Free users generate costs without revenue. Implement engagement-based features (ads, referral incentives) to offset costs or drive conversions.

### 5. ANNUAL SUBSCRIPTION INCENTIVES
Offer 15-20% discounts for annual commitments to improve cash flow predictability and reduce churn.

---

## Conclusion

The proposed three-tier structure provides a sustainable business model with clear upgrade paths. The V2 API's use of Gemini 2.0 Flash delivers substantial cost savings over V1, making the tier limits both generous for users and profitable for the business.

### Next Steps
1. Review detailed cost breakdown document
2. Finalize tier pricing based on competitive analysis
3. Implement rate limiting infrastructure
4. Design upgrade prompts and paywall UX

---

*Document prepared by: AI Business Analysis*
*For: DeepmAInd / Milo App*
*Version: 2.0 (V2 API Focus)*
