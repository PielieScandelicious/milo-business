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
| **Receipt Upload** | <span style="color:#ef4444">$0.0802 per receipt</span> | Veryfi OCR: <span style="color:#ef4444">$0.0800</span> + Gemini: $0.0002 |
| **Chat Message** | <span style="color:#16a34a">$0.0003 per message</span> | Gemini 2.0 Flash Processing |

<span style="background-color:#dbeafe; padding: 8px; display: block; border-left: 4px solid #3b82f6;">**KEY INSIGHT:** Veryfi OCR represents <span style="color:#ef4444">**99.75%**</span> of variable costs. Receipt upload limits are the critical lever for cost management.</span>

---

## Recommended Tier Structure

### <span style="color:#6b7280">SILVER TIER</span> (Entry Level)

| Attribute | Value |
|-----------|-------|
| Monthly Limits | 10 receipts \| 50 chat messages |
| Variable Cost | <span style="color:#ef4444">$0.82 per user/month</span> |
| Recommended Price | <span style="color:#6b7280">**FREE**</span> (Ad-supported or freemium) |
| Strategic Purpose | User acquisition and conversion funnel |

### <span style="color:#f59e0b">GOLD TIER</span> (Standard)

| Attribute | Value |
|-----------|-------|
| Monthly Limits | 40 receipts \| 200 chat messages |
| Variable Cost | <span style="color:#ef4444">$3.26 per user/month</span> |
| Recommended Price | <span style="color:#f59e0b">**$5.99 - $6.99/month**</span> |
| Gross Margin | <span style="color:#16a34a">46% - 54%</span> |
| Strategic Purpose | Core revenue generation |

### <span style="color:#a855f7">PLATINUM TIER</span> (Premium)

| Attribute | Value |
|-----------|-------|
| Monthly Limits | 150 receipts \| 500 chat messages |
| Variable Cost | <span style="color:#ef4444">$12.15 per user/month</span> |
| Recommended Price | <span style="color:#a855f7">**$14.99 - $19.99/month**</span> |
| Gross Margin | <span style="color:#f59e0b">19% - 39%</span> |
| Strategic Purpose | Power user retention and premium positioning |

---

## Infrastructure Costs

### Fixed Monthly Costs (Baseline)

| Service | Cost |
|---------|------|
| Railway Hosting (Hobby) | <span style="color:#ef4444">$5.00/month</span> |
| Firebase Authentication | <span style="color:#16a34a">$0.00</span> (Free tier covers <50K MAUs) |
| PostgreSQL Database | Included in Railway |
| Firebase Storage (~20GB) | <span style="color:#ef4444">$0.52/month</span> |
| **Total Fixed Infrastructure** | <span style="color:#ef4444">**$5.52/month**</span> |

<span style="background-color:#fef3c7; padding: 8px; display: block; border-left: 4px solid #f59e0b;">**IMPORTANT:** These costs scale with user growth. At 10,000+ MAU, expect infrastructure costs of <span style="color:#ef4444">$50-150/month</span>.</span>

---

## Profitability Projections

### Scenario: 1,000 Active Users

**Distribution Assumption:**
- 700 <span style="color:#6b7280">Silver</span> (70%)
- 250 <span style="color:#f59e0b">Gold</span> (25%)
- 50 <span style="color:#a855f7">Platinum</span> (5%)

**Monthly Revenue:**

| Tier | Users | Price | Revenue |
|------|-------|-------|---------|
| <span style="color:#6b7280">Silver</span> | 700 | $0 | $0 |
| <span style="color:#f59e0b">Gold</span> | 250 | $6.49 | <span style="color:#16a34a">$1,622.50</span> |
| <span style="color:#a855f7">Platinum</span> | 50 | $17.49 | <span style="color:#16a34a">$874.50</span> |
| **Total** | | | <span style="color:#16a34a">**$2,497.00**</span> |

**Monthly Variable Costs:**

| Tier | Users | Cost/User | Total |
|------|-------|-----------|-------|
| <span style="color:#6b7280">Silver</span> | 700 | $0.82 | <span style="color:#ef4444">$574.00</span> |
| <span style="color:#f59e0b">Gold</span> | 250 | $3.26 | <span style="color:#ef4444">$815.00</span> |
| <span style="color:#a855f7">Platinum</span> | 50 | $12.15 | <span style="color:#ef4444">$607.50</span> |
| **Total** | | | <span style="color:#ef4444">**$1,996.50**</span> |

**Monthly Fixed Costs:** <span style="color:#ef4444">~$15.00</span> (scaled infrastructure)

### <span style="color:#16a34a">**Net Monthly Profit: $485.50**</span>
### <span style="color:#16a34a">**Net Margin: 19.4%**</span>

---

## Strategic Recommendations

### 1. <span style="color:#3b82f6">PRIORITIZE GOLD TIER CONVERSIONS</span>
The <span style="color:#f59e0b">Gold</span> tier offers the best margin-to-value ratio. Focus marketing efforts on converting <span style="color:#6b7280">Silver</span> users to <span style="color:#f59e0b">Gold</span>.

### 2. <span style="color:#3b82f6">IMPLEMENT USAGE-BASED OVERAGE CHARGES</span>
Consider allowing users to purchase additional receipts at $0.15-0.20 each (<span style="color:#16a34a">88-150% margin</span>) rather than forcing tier upgrades.

### 3. <span style="color:#3b82f6">NEGOTIATE VERYFI VOLUME PRICING</span>
At 10,000+ monthly documents, contact Veryfi for volume discounts. A 20% reduction in OCR costs would increase <span style="color:#f59e0b">Gold</span> tier margins by <span style="color:#16a34a">12 percentage points</span>.

### 4. <span style="color:#3b82f6">MONITOR SILVER TIER CAREFULLY</span>
Free users generate costs without revenue. Implement engagement-based features (ads, referral incentives) to offset costs or drive conversions.

### 5. <span style="color:#3b82f6">ANNUAL SUBSCRIPTION INCENTIVES</span>
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
