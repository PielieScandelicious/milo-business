# Scandalicious Data Product — Business Plan

## The Opportunity

Belgium has **3,979 food manufacturing companies**. 99% are SMEs. The vast majority have **zero access to consumer panel data** — the kind of data that tells them who buys their products, at which stores, how often, and at what price.

The only cross-retailer consumer panel in Belgium is **YouGov (ex-GfK)** — 6,000 households, six-figure annual contracts. Only the top 50-100 brands can afford it. The other 3,500+ food producers are flying blind.

Retailers like Colruyt, Delhaize, and Carrefour each sell their OWN shopper data — but only for their own stores. Colruyt Insights shows what happens at Colruyt. Delhaize Enlight+ shows what happens at Delhaize. **Nobody connects the dots across retailers** at an accessible price point.

**NielsenIQ's affordable product (Byzzer) is US-only.** There is no self-service consumer panel data tool available in Belgium or Europe for SMBs.

That's the gap.

---

## What We're Building

**The first affordable, cross-retailer consumer panel in Belgium.**

A mobile app where Belgian consumers scan their grocery receipts in exchange for small rewards. We extract item-level purchase data from every receipt using AI (Google Gemini). This data is aggregated into a **monthly datamart** that we sell to FMCG brands, food producers, and market research agencies.

---

## The Data Product

### What it is

A flat, pre-aggregated table (datamart) that clients receive monthly. One Excel/CSV file they can open, filter, and pivot to answer their business questions.

### The Grain

One row = **one brand, at one store, in one granular category, in one month**.

Example row:
```
month:              2026-01
group:              Fresh Food
parent_category:    Dairy, Eggs & Cheese
granular_category:  Yoghurt Fruit
store:              colruyt
retailer_group:     Colruyt Group
is_discounter:      yes
brand:              danone
is_private_label:   false
unique_buyers:      842
panel_size:         4,200
penetration_pct:    20.0%
purchase_frequency: 1.4
avg_spend_per_buyer: 5.01
total_spend:        4,218.50
total_units:        1,684
avg_unit_price:     2.49
category_share_pct: 18.2%
premium_spend_pct:  0%
discount_pct:       12.3%
avg_health_score:   3.2
```

### 4 Dimensions (what clients filter and pivot on)

**1. Time** — year > quarter > month

**2. Category** — 3-level hierarchy built into the app
- 8 Groups (Fresh Food, Pantry, Frozen, Drinks, Snacks, Household, Personal Care, Other)
- 31 Parent Categories (Dairy, Alcohol, Bakery, etc.)
- ~200 Granular Categories (Yoghurt Fruit, Beer Pils, Cheese Hard, etc.)

**3. Store** — retailer group > store chain > store type
- Colruyt Group (Colruyt, Okay, Bio-Planet)
- Ahold Delhaize (Delhaize, Albert Heijn)
- Aldi, Lidl, Carrefour, Spar, etc.
- Each store tagged: is_discounter, store_type

**4. Brand** — brand name + is_private_label flag
- National brands (Danone, Jupiler, Coca-Cola)
- Private label (Boni = Colruyt, 365 = Delhaize, Carrefour brand)

### 14 Metrics (the numbers clients care about)

| # | Metric | What it answers |
|---|---|---|
| 1 | unique_buyers | How many panelists buy this? |
| 2 | panel_size | Total active panelists that month |
| 3 | penetration_pct | What % of Belgians buy this? |
| 4 | purchase_frequency | How often do buyers come back? |
| 5 | avg_spend_per_buyer | How much does each buyer spend? |
| 6 | total_spend | Total euros spent |
| 7 | total_units | Total items purchased |
| 8 | avg_unit_price | Average price per unit |
| 9 | avg_price_per_unit_measure | Price per kg or liter |
| 10 | category_share_pct | Brand's share of category at this store |
| 11 | premium_spend_pct | % of spend on premium products |
| 12 | discount_pct | % of purchases bought on promo |
| 13 | avg_health_score | Average health score (0-5) |
| 14 | avg_basket_spend | Average receipt total when this category is present |

### How it's built

All metrics are aggregated from raw transaction data using a single SQL query. No complex pipelines. No product matching needed at this grain. The AI extraction gives us `normalized_brand` and `granular_category` per item — these map directly to the dimensions.

Three small lookup tables are maintained manually:
- `dim_store` (~15 rows — store chain metadata)
- `dim_category` (~200 rows — generated from the app's category hierarchy)
- `dim_brand` (~50-100 rows — top brands, private label flags)

---

## Why It's Valuable

### The USP

**We are the only affordable cross-retailer full-basket consumer panel in Belgium.**

- **YouGov (ex-GfK)**: Cross-retailer but costs six figures. 99.9% of Belgian companies priced out.
- **Colruyt Insights**: Affordable but only shows Colruyt stores. Blind to 74% of the market.
- **Delhaize Enlight+**: Only Delhaize. Blind to 77% of the market.
- **Carrefour Links**: Only Carrefour. Blind to 82% of the market.
- **Shopmium**: Cross-retailer but biased data — only promo-triggered scans.
- **PingPrice**: Cross-retailer but shelf prices only, not purchase behavior.
- **Us**: Cross-retailer. Full basket. Affordable. The only option in this position.

Retailers will **never** share cross-retailer data with each other. Colruyt will never tell a brand what happens at Delhaize. This competitive dynamic is permanent. Our position in the gap is structurally defensible.

### What makes our data unique

1. **Actual prices paid** — not shelf prices, not list prices. What consumers actually handed over money for, including discounts.
2. **Cross-retailer promo tracking** — see if a Colruyt promo cannibalized the brand's sales at Delhaize.
3. **Price per unit measure** — normalized to price per kg/L for true cross-brand comparison.
4. **Health scoring** — every item scored 0-5. No panel provider does this. Unique angle.
5. **Full-basket context** — what's bought together (basket affinity).
6. **Time-of-day patterns** — shopping occasions from receipt timestamps.

### What business decisions clients can make

| Decision | Example |
|---|---|
| Retailer sell-in | "My penetration at Colruyt is 16% but only 4% at Delhaize — give me shelf space" |
| Pricing strategy | "My avg price at Delhaize is €2.69 vs €2.49 at Colruyt — am I priced too high?" |
| Promo effectiveness | "My discount_pct jumped to 22% but penetration only grew 1pt — promo attracted deal-seekers, not loyal buyers" |
| Private label monitoring | "Private label grew from 35% to 41% at Colruyt but stayed flat at Delhaize" |
| Category opportunity | "Plant-based dairy penetration grew from 6.9% to 8.4% in 6 months with 85% premium mix" |
| Competitive intel | "Competitor X gained 3pt share at Aldi — they have better distribution there" |

### Example Q&A the data product answers

**A Belgian beer brand director asks: "Are we losing share to private label?"**

> Based on our panel of 5,000 Belgian households: **Yes, but only at Aldi.** Jupiler holds 38% value share at Colruyt (stable), 34% at Delhaize (stable), but dropped from 22% to 16% at Aldi. Cara Pils grew from 31% to 39% at Aldi in the same period. The shift is price-driven: Jupiler's avg price at Aldi is €14.99/crate vs Cara Pils at €9.99.

**A Colruyt private label director asks: "Do Boni buyers also buy competitor private label?"**

> 67% of Boni buyers also shop at Delhaize, and 54% of those buy 365 products there. Your private label shoppers are price-tier loyal, not Boni loyal — they systematically choose the cheapest option at whatever store they're in.

**An SMB pasta sauce maker asks: "I want to get listed at Colruyt. What should I know?"**

> Premium pasta sauce (>€3.50/jar) is only 14% of sauce purchases at Colruyt — but growing +2pt/quarter. Private label holds 39%, Barilla 21%. There's a gap for a Belgian artisanal brand at €4-5. Without our data, this producer walks into Colruyt with nothing but a product sample and hope.

---

## The App — What's Important

### Core principle: Reward the scanning, never reward the shopping

The app's incentive structure must be **completely indifferent** to what users buy, where they shop, or how much they spend. If we reward saving money or deal-hunting, we attract bargain hunters and bias the panel. The data becomes worthless.

### What the app does

1. **Receipt scanning** — user takes a photo of any grocery receipt
2. **Points per receipt** — €0.05-0.10 per receipt, regardless of contents
3. **Spending overview** — "You spent €423 this month, here are your categories"
4. **Receipt archive** — searchable history of all purchases
5. **Streak rewards** — "7 days in a row, bonus points"
6. **Monthly lottery** — all users with 10+ receipts enter a draw

### What the app does NOT do

- No savings leaderboards (biases toward deal-hunters)
- No "save money" challenges (changes shopping behavior)
- No price comparison between stores (makes users switch stores)
- No "cheaper alternative" suggestions (biases toward budget products)
- No cashback on specific products (Shopmium's mistake — biased data)

### Positioning

> **"Scan your receipts. Earn rewards. See where your money goes."**

Not "shop smarter." Not "save money." Just: scan, earn, track.

### Demographics to collect

Three fields during onboarding (optional but critical for data value):
1. **Age range** (18-24 / 25-34 / 35-44 / 45-54 / 55-64 / 65+)
2. **Household size** (1 / 2 / 3-4 / 5+)
3. **Postcode** (4 digits — maps to province/municipality)

This enables panel weighting and demographic breakdowns for clients.

---

## Competitive Landscape (Belgium)

| Data source | Cross-retailer? | Purchase data? | Affordable? | Self-service? |
|---|---|---|---|---|
| YouGov (ex-GfK) | Yes | Yes | No (€100K+) | No |
| Colruyt Insights | No (Colruyt only) | Yes | Unknown | Semi |
| Delhaize Enlight+ | No (Delhaize only) | Yes | No (enterprise) | Yes |
| Carrefour Links | No (Carrefour only) | Yes | No (enterprise) | No |
| Shopmium | Yes | Biased (promo only) | N/A | N/A |
| PingPrice | Yes | No (prices only) | Partial | N/A |
| Daltix | Yes | No (shelf data) | No (enterprise) | No |
| **Us** | **Yes** | **Yes** | **Yes** | **Yes** |

---

## Cost Analysis

### Year 1: Reaching 5,000 panelists

| Cost | Amount |
|---|---|
| User rewards (€0.07/receipt, ramping up) | €20,000-25,000 |
| User acquisition (ads, referrals, content) | €25,000-50,000 |
| Infrastructure (Gemini API, hosting, DB) | €4,000-6,000 |
| **Total Year 1** | **€49,000-81,000** |

### Year 2: Maintaining 5,000 panelists

| Cost | Amount |
|---|---|
| User rewards (5,000 users × 12 receipts/mo × €0.07) | €50,000-56,000 |
| User acquisition (replacing churn + growth) | €15,000-25,000 |
| Infrastructure | €5,000-7,000 |
| **Total Year 2** | **€70,000-88,000** |

### Revenue timeline

| Milestone | When | Revenue |
|---|---|---|
| 1,000 users | Month 5-6 | First sample reports, show to potential buyers |
| 2,000 users | Month 7-9 | First paying clients: 3-5 at €300-500/mo = €900-2,500/mo |
| 3,500 users | Month 10-12 | Growing: 5-10 clients = €1,500-5,000/mo |
| 5,000 users | Month 13-18 | Full product: 15-25 clients at €300-600/mo = €4,500-15,000/mo |

**Year 1 revenue: €5,000-15,000** (last few months only)
**Year 2 revenue: €50,000-150,000**

### The funding gap

Year 1 needs €50-80K in costs with only €5-15K in revenue. The gap is **€35-75K**.

By mid-Year 2, the data revenue covers reward costs and the business is self-sustaining.

### How to finance it

**Recommended: Belgian grants + pre-sales**

1. **Vlaio (Flanders)** or **Innoviris (Brussels)** — €25,000-50,000 in non-dilutive grants for data/AI innovation projects
2. **Pre-sell** the data product: build a sample report, show it to 10 food producers, get letters of intent
3. **Personal investment**: €5-10K to bridge months 1-4 before grant approval

Alternative options:
- **Angel investment** (BeAngels, BAN Vlaanderen): €50-100K for 5-15% equity
- **FMCG brand partnership**: one mid-size brand funds rewards in exchange for exclusive early data access
- **Bootstrap**: grow purely organic at ~€1,000/month rewards budget, slower but no external funding needed

---

## Target Clients

| Segment | Who | Price | Volume |
|---|---|---|---|
| **Belgian SMB food producers** | Artisanal cheese, local breweries, sauce makers | €200-600/mo | 1,000s of potential clients |
| **Mid-size Belgian brands** | Lotus, Devos-Lemmens, La William, Imperial | €1,000-4,000/mo | 50-100 companies |
| **Private label manufacturers** | Contract manufacturers supplying Boni, 365, etc. | €1,000-3,000/mo | 20-50 companies |
| **Market research agencies** | Belgian/EU research firms advising FMCG brands | €800-2,500/mo | 20-30 firms |
| **Retailer private label teams** | Colruyt (Boni), Delhaize (365) wanting cross-retailer view | €2,500-8,000/mo | 3-5 retailers |

---

## The Pitch (for friends, investors, partners)

### 30-second version

> Belgium has 4,000 food companies. 99% have zero data about who buys their products and where. The only consumer panel (YouGov) costs six figures per year. Retailers like Colruyt and Delhaize sell their own data, but only for their own stores — a cheese maker can never see the full picture.
>
> We're building an app where Belgians scan grocery receipts in exchange for small rewards. We extract every item, brand, price, and store using AI. We aggregate this into a monthly data product and sell it to food brands for €200-600/month — giving them cross-retailer market intelligence that didn't exist before at this price.
>
> We need 5,000 consistent users and ~€50-75K to get there. The data product becomes self-sustaining at ~15 paying clients.

### 2-minute version

> **The problem:** FMCG brands in Belgium are flying blind. They sell through Colruyt, Delhaize, Carrefour, Aldi — but they have no idea who buys their products, how often, or what happens at the competition. The only data source that shows this (YouGov, formerly GfK) costs €100,000+ per year. 99% of Belgian food brands can't afford it.
>
> Meanwhile, each retailer sells their own shopper data — but only for their own stores. Colruyt Insights shows you Colruyt. Delhaize Enlight+ shows you Delhaize. Nobody connects the dots. And they never will, because retailers are competitors.
>
> **Our solution:** An app where Belgian consumers scan their grocery receipts and earn small rewards (€0.05-0.10 per receipt). We use AI to extract every item, brand, price, category, and store from each receipt. We aggregate this across thousands of households into a monthly data product that shows:
>
> - Which brands are winning at which stores
> - How private label competes against national brands across retailers
> - What prices consumers actually pay (including discounts)
> - How purchase patterns change over time
>
> **Why it works:** We're not asking people to change how they shop. We just ask them to scan a receipt for 7 cents. The data is unbiased because rewards are per receipt, not per product. And because we see ALL stores, we can show things no single retailer will ever reveal.
>
> **The business model:** 5,000 panelists cost ~€55K/year in rewards. 15-25 clients paying €300-600/month = €54,000-180,000/year. Self-sustaining from year 2. The data gets more valuable every month as history compounds.
>
> **What we need:** €50-75K to fund rewards and user acquisition for year 1. We're applying for Vlaio/Innoviris grants (non-dilutive) and pre-selling to Belgian food producers to validate demand.

---

## Technical Architecture (Summary)

```
USER SCANS RECEIPT
       │
       ▼
AI EXTRACTION (Google Gemini)
  → store_name, item_name, normalized_brand, granular_category,
    item_price, quantity, unit_price, is_premium, is_discount,
    health_score, unit_of_measure, weight_or_volume
       │
       ▼
TRANSACTION DATABASE (operational — one row per item)
       │
       ▼
NIGHTLY ETL (aggregation query)
       │
       ▼
DATAMART (analytical — one row per brand × store × category × month)
       │
       ├──→ PDF Reports (SMB tier, €200-600/mo)
       ├──→ Dashboard (mid tier, €1,000-4,000/mo)
       └──→ API + CSV export (enterprise, €2,500-8,000/mo)
```

No complex infrastructure needed. The AI extraction already exists in the app. The datamart is one SQL query. The lookup tables are ~15 + ~200 + ~100 rows maintained manually.

---

## Key Risks

| Risk | Mitigation |
|---|---|
| Not enough users sign up | Pre-validate with sample report before investing in acquisition |
| Users stop scanning after a few months | Streak rewards + lottery + consistent small payments |
| Panel is not representative (skews young/urban) | Collect demographics, apply weighting, be transparent with clients |
| Gemini extraction quality degrades | Monitor brand/category consistency, maintain alias tables |
| YouGov drops their price | Unlikely (60 years without doing so), and you'd still be 10-20x cheaper |
| Another receipt app enters Belgium | First-mover advantage — historical data compounds in value |
| GDPR concerns from clients | Data is aggregated and anonymized. No individual user data ever leaves the system |

---

*Last updated: February 2026*
