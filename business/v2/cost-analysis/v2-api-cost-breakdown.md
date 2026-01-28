<div align="center">

# **MILO**
## API Cost Breakdown v2.0

### *Detailed API & Infrastructure Costs*

---

**DeepmAInd B.V.**

**Document Version:** 2.0 | January 28, 2026

</div>

---

## API Cost Summary

| API/Service | Cost Model | Per-Unit | Monthly (10K Users) |
|:------------|:-----------|:--------:|--------------------:|
| **Veryfi OCR** | Per receipt | $0.08 | $16,000 |
| **Gemini 2.0 Flash** | Per token | ~$0.0003/msg | $240 |
| **Firebase Auth** | Per MAU | Free <50K | $0 |
| **Firebase Storage** | Per GB | $0.026/GB | $67 |
| **Railway Hosting** | Per resource | Variable | $150-300 |
| **Total** | - | - | **~$16,500** |

---

## 1. Veryfi OCR API

### Pricing Structure

| Tier | Volume | Price/Receipt |
|:-----|-------:|--------------:|
| Starter | 0-1,000 | $0.10 |
| Growth | 1,001-10,000 | $0.08 |
| Scale | 10,001-100,000 | $0.06-0.08 |
| Enterprise | 100,000+ | Negotiated |

### Cost Projection by User Base

| Users | Receipts/Mo* | Monthly Cost | Annual Cost |
|------:|-------------:|-------------:|------------:|
| 1,000 | 20,000 | $1,600 | $19,200 |
| 5,000 | 100,000 | $8,000 | $96,000 |
| 10,000 | 200,000 | $16,000 | $192,000 |
| 25,000 | 500,000 | $35,000** | $420,000 |

*Assuming average 20 receipts/user/month
**With volume discount

### Cost Per Tier

| Tier | Receipt Limit | Veryfi Cost | As % of Price |
|:-----|:-------------:|------------:|--------------:|
| Trial | 10 total | $0.80 | N/A |
| Gold | 25/month | $2.00 | 33.4% |
| Platinum | 50/month | $4.00 | 30.8% |

---

## 2. Google Gemini 2.0 Flash

### Pricing

| Type | Price |
|:-----|------:|
| Input tokens | $0.10/million |
| Output tokens | $0.40/million |

### Usage Per Function

| Function | Input Tokens | Output Tokens | Cost |
|:---------|-------------:|--------------:|-----:|
| **Categorization** | ~500 | ~300 | $0.00017 |
| **Chat Message** | ~2,000 | ~500 | $0.00040 |
| **Health Score** | ~200 | ~100 | $0.00006 |

### Monthly Cost Projection

| Users | Messages/Mo | Categorizations | Monthly Cost |
|------:|------------:|----------------:|-------------:|
| 1,000 | 50,000 | 20,000 | $24 |
| 5,000 | 250,000 | 100,000 | $120 |
| 10,000 | 500,000 | 200,000 | $240 |

> **Assessment:** Gemini costs are negligible (<1% of variable costs)

---

## 3. Firebase Services

### Authentication

| MAU Range | Price |
|:----------|------:|
| 0-50,000 | Free |
| 50,001+ | $0.0025-0.0055/MAU |

**MILO Status:** Free tier covers Year 1-2 projections

### Storage

| Component | Price |
|:----------|------:|
| Storage | $0.026/GB/month |
| Downloads | $0.12/GB |
| Uploads | Free |

### Storage Projection

| Users | Storage/User | Total Storage | Monthly Cost |
|------:|-------------:|--------------:|-------------:|
| 1,000 | 50MB | 50GB | $1.30 |
| 5,000 | 50MB | 250GB | $6.50 |
| 10,000 | 50MB | 500GB | $13.00 |

---

## 4. Railway Hosting

### Pricing Components

| Resource | Price |
|:---------|------:|
| Compute | ~$0.000463/min |
| Memory | ~$0.000231/GB-min |
| PostgreSQL | Included in usage |

### Monthly Projection

| Users | CPU Hours | Memory GB-hr | Monthly Cost |
|------:|----------:|-------------:|-------------:|
| 1,000 | 720 | 1,440 | $50-80 |
| 5,000 | 720 | 2,880 | $100-150 |
| 10,000 | 1,440 | 5,760 | $200-300 |

---

## 5. Payment Processing

### Apple App Store

| Program | Commission |
|:--------|:----------:|
| Standard | 30% |
| Small Business (<$1M) | 15% |
| After Year 1 subscription | 15% |

### Stripe (B2B)

| Fee Type | Rate |
|:---------|-----:|
| Transaction | 2.9% + $0.30 |
| International | +1.5% |

### Payment Cost Projection

| Revenue | B2C (15%) | B2B (3%) | Total |
|--------:|----------:|---------:|------:|
| $228K | $19K | $2K | $21K |
| $1.1M | $69K | $12K | $81K |
| $2.4M | $125K | $25K | $150K |

---

## Total API Cost Summary

### Year 3 Projection (10K Paid Users)

| Service | Monthly | Annual | % of Total |
|:--------|--------:|-------:|:----------:|
| **Veryfi OCR** | $16,167 | $194,000 | 76.1% |
| **Gemini API** | $250 | $3,000 | 1.2% |
| **Firebase** | $667 | $8,000 | 3.1% |
| **Railway** | $250 | $3,000 | 1.2% |
| **Payments** | $4,167 | $50,000 | 19.6% |
| **Total** | **$21,250** | **$255,000** | 100% |

---

## Cost Optimization Recommendations

### High Priority

| Action | Savings | Effort |
|:-------|:-------:|:------:|
| Negotiate Veryfi volume | 15-25% | Medium |
| Optimize Gemini prompts | 10-20% | Low |
| Annual Railway contract | 10-15% | Low |

### Alternative Providers

| Service | Alternative | Price | Trade-off |
|:--------|:------------|------:|:----------|
| Veryfi | Google Doc AI | $0.01-0.05 | Less receipt-specific |
| Veryfi | Amazon Textract | $0.015 | More dev work |
| Gemini | Claude Haiku | ~$0.0003 | Similar cost |

---

<div align="center">

**Document Version:** 2.0
**Last Updated:** January 28, 2026

</div>
