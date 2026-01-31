<div align="center">

# **MILO**
## Business Executive Summary v4.0

### *AI-Powered Wellness Spending Intelligence Platform*

---

**DeepmAInd B.V.**

**Prepared:** January 31, 2026
**Document Version:** 4.0 (Technical Update)
**Classification:** Confidential - Investor Review

---

![Status](https://img.shields.io/badge/Status-MVP%20Complete-blue)
![Platform](https://img.shields.io/badge/Platform-iOS%20Native-green)
![AI](https://img.shields.io/badge/AI-Gemini%202.0-orange)
![Backend](https://img.shields.io/badge/Backend-FastAPI%20v2-red)

</div>

---

## Table of Contents

1. [Executive Overview](#1-executive-overview)
2. [The Opportunity](#2-the-opportunity)
3. [Product & Technology](#3-product--technology)
4. [Technical Architecture](#4-technical-architecture)
5. [Business Model](#5-business-model)
6. [Market Analysis](#6-market-analysis)
7. [Financial Projections](#7-financial-projections)
8. [Go-to-Market Strategy](#8-go-to-market-strategy)
9. [Competitive Positioning](#9-competitive-positioning)
10. [Risk Assessment](#10-risk-assessment)
11. [Compliance & Legal](#11-compliance--legal)
12. [Investment Thesis](#12-investment-thesis)
13. [Strategic Roadmap](#13-strategic-roadmap)
14. [Technical Appendix](#14-technical-appendix)

---

<div align="center">

## 1. Executive Overview

</div>

### Company Snapshot

| Attribute | Details |
|:----------|:--------|
| **Company** | DeepmAInd B.V. |
| **Product** | MILO - AI-Powered Personal Finance App |
| **Category** | Wellness-Aware Spending Analytics |
| **Stage** | MVP Complete, Pre-Launch |
| **Headquarters** | Netherlands (EU) |
| **Funding Sought** | $400K - $600K Seed |
| **Target Launch** | Q2 2026 |
| **Projection Model** | Conservative |

### Mission Statement

> *"Empower health-conscious consumers to understand not just **how much** they spend, but **whether they're spending on healthy choices** - while building an ethically-sourced, privacy-compliant consumer data platform."*

### Key Highlights

```
+------------------------------------------------------------------------------+
|                      INVESTMENT HIGHLIGHTS v4.0                              |
+------------------------------------------------------------------------------+
|                                                                              |
|  CATEGORY CREATOR     First wellness-aware spending analytics platform      |
|                                                                              |
|  $2.4M REVENUE        Year 3 projected annual revenue (conservative)        |
|                                                                              |
|  58% MARGINS          Operating margins at scale (Year 3)                   |
|                                                                              |
|  PRODUCTION READY     Fully functional iOS app + FastAPI backend            |
|                                                                              |
|  AI-NATIVE            Gemini 2.0 Flash + Veryfi OCR stack operational       |
|                                                                              |
|  6-10x RETURN         Conservative case investor return at Year 3 exit      |
|                                                                              |
+------------------------------------------------------------------------------+
```

### Three-Sentence Summary

**MILO** is a production-ready iOS application powered by a FastAPI backend that combines AI-driven receipt scanning (Veryfi OCR), proprietary health scoring (0-5 scale), and an intelligent chat assistant ("Milo" - powered by Gemini 2.0 Flash) into a unified wellness-aware spending platform. The technical stack is complete: native SwiftUI frontend with Firebase authentication, actor-based service architecture, SSE streaming chat, and a modular Python backend with 17-category classification and PostgreSQL persistence. With $400K-$600K in seed funding, MILO targets 25,000 monthly active users by Year 3 and a minimum $15M valuation at exit.

---

<div align="center">

## 2. The Opportunity

</div>

### Market Convergence

MILO sits at the intersection of three rapidly growing markets:

```
                    +-----------------------------------+
                    |      RECEIPT SCANNING             |
                    |     $2.5B -> $5.1B (2033)         |
                    |       CAGR: 11.1%                 |
                    +----------------+------------------+
                                     |
            +------------------------+------------------------+
            |                        |                        |
            v                        v                        v
+-----------------------+   +------------------+   +-----------------------+
|   PERSONAL FINANCE    |   |      MILO        |   |   CONSUMER DATA       |
|  $7.2B -> $14.4B      |<--|  UNIQUE POSITION |-->|      $12B+            |
|    CAGR: 12.3%        |   |                  |   |   CAGR: 22%           |
+-----------------------+   +------------------+   +-----------------------+
```

### Total Addressable Market

| Market Segment | 2025 Size | 2030 Projection | CAGR |
|:---------------|----------:|----------------:|-----:|
| Receipt Scanner Apps | $2.5B | $5.1B | 11.1% |
| Personal Finance Apps | $7.2B | $14.4B | 12.3% |
| Consumer Data Analytics | $12.0B | $26.5B | 22.0% |
| **Combined TAM** | **$21.7B** | **$46.0B** | **16.2%** |

### Why Now?

```
+-----------------------------------------------------------------------------+
|                      MARKET TIMING ASSESSMENT                                |
+-----------------------------------------------------------------------------+
|                                                                              |
|  FAVORABLE CONDITIONS:                                                       |
|  [x] Health-conscious spending is mainstream (not niche)                     |
|  [x] AI capabilities enable 95%+ categorization accuracy at low cost         |
|  [x] Privacy regulations create premium for compliant data providers         |
|  [x] Legacy competitors (Fetch, Ibotta) haven't innovated in years           |
|  [x] B2B demand for consented consumer data at all-time high                 |
|  [x] Gemini 2.0 Flash enables real-time AI chat at affordable rates          |
|                                                                              |
|  HEADWINDS TO CONSIDER:                                                      |
|  [ ] Subscription fatigue (41% of consumers affected)                        |
|  [ ] Economic uncertainty affecting discretionary spending                   |
|  [ ] App Store saturation increasing CAC                                     |
|  [ ] Privacy regulations increasing compliance costs                         |
|                                                                              |
|  NET ASSESSMENT: Favorable timing with manageable headwinds                  |
|                                                                              |
+-----------------------------------------------------------------------------+
```

---

<div align="center">

## 3. Product & Technology

</div>

### Core Product Features

```
+-----------------------------------------------------------------------------+
|                              MILO PLATFORM v4.0                              |
+---------------------------+----------------------------+--------------------+
|  RECEIPT SCAN             |  HEALTH SCORES             |  AI INTELLIGENCE   |
+---------------------------+----------------------------+--------------------+
| * Veryfi OCR API v8       | * 0-5 proprietary scale    | * Gemini 2.0 Flash |
| * 99%+ accuracy           | * 17 spending categories   | * 95%+ categorize  |
| * PDF + JPEG + PNG        | * Nutrition-based scoring  | * "Milo" chat bot  |
| * Duplicate detection     | * Per-item granularity     | * SSE streaming    |
| * Store auto-detection    | * Visual health display    | * Context-aware    |
| * 15 receipts/month       | * Food item focus          | * 100 msgs/month   |
+---------------------------+----------------------------+--------------------+
```

### Unique Value Proposition

| User Need | Current Solutions | MILO Advantage |
|:----------|:------------------|:---------------|
| Track spending | Bank apps show merchants only | **Item-level granularity (17 categories)** |
| Healthy choices | Separate nutrition apps | **Health scores 0-5 on every receipt** |
| AI insights | Generic chatbots | **Personalized spending coach with transaction context** |
| Data privacy | Sold without consent | **Tiered consent model, GDPR-ready architecture** |
| Modern UX | Legacy interfaces | **Native SwiftUI dark-mode experience** |

### Health Scoring System (Proprietary IP)

Our AI-powered health scoring algorithm rates every food item on a 0-5 scale:

| Score | Rating | Color | Description | Examples |
|:-----:|:-------|:------|:------------|:---------|
| 5 | Excellent | Green | Whole foods, minimal processing | Fresh vegetables, fruits, water |
| 4 | Good | Light Green | Healthy with minor concerns | Lean proteins, eggs, plain dairy |
| 3 | Moderate | Yellow | Balanced, some processed elements | Bread, pasta, cheese |
| 2 | Fair | Orange | Processed, limited nutrition | Processed meats, some snacks |
| 1 | Poor | Red | Highly processed, low nutrition | Chips, candy, cookies, sodas |
| 0 | Avoid | Dark Red | Ultra-processed, health concerns | Alcohol, energy drinks |
| null | Non-Food | Gray | Not applicable | Household, personal care |

### Subscription Tiers

| Tier | Price | Receipt Limit | Chat Limit | Key Features |
|:-----|------:|:--------------|:-----------|:-------------|
| **Free Trial** | $0 (14 days) | 10 total | 20 total | Try before buy |
| **Gold** | $5.99/mo | 25/month | 100/month | Full analytics, 6mo history |
| **Platinum** | $12.99/mo | 50/month | 200/month | Power features, 24mo history, API |

---

<div align="center">

## 4. Technical Architecture

</div>

### System Architecture Overview

```
+-----------------------------------------------------------------------------+
|                           MILO TECHNICAL STACK v4.0                          |
+-----------------------------------------------------------------------------+
|                                                                              |
|    iOS FRONTEND                     BACKEND API                              |
|    ============                     ===========                              |
|    SwiftUI (iOS 17+)                FastAPI 0.109.0 (Python 3.11)            |
|    Firebase Auth                    PostgreSQL + SQLAlchemy 2.0              |
|    StoreKit 2                       Async/Await Architecture                 |
|    Actor-based Services             Repository Pattern                       |
|                                                                              |
|    AI/ML SERVICES                   INFRASTRUCTURE                           |
|    ==============                   ==============                           |
|    Veryfi OCR v8                    Railway Hosting                          |
|    Gemini 2.0 Flash                 Firebase Storage                         |
|    17-Category Classification       End-to-End Encryption                    |
|    Health Score Algorithm           CORS + Rate Limiting                     |
|                                                                              |
+-----------------------------------------------------------------------------+
```

### Backend Architecture (FastAPI)

```
scandalicious-backend/
+-- app/
|   +-- main.py                 # FastAPI app, CORS, exception handlers
|   +-- config.py               # Pydantic settings, environment config
|   |
|   +-- api/                    # HTTP layer
|   |   +-- deps.py             # get_db(), get_current_db_user()
|   |   +-- v2/                 # Production API (Gemini-based)
|   |       +-- receipts.py     # Receipt upload & management
|   |       +-- chat.py         # AI chat with SSE streaming
|   |       +-- analytics.py    # Spending summaries & trends
|   |       +-- profile.py      # User profile management
|   |
|   +-- services/               # Business logic layer
|   |   +-- receipt_processor_v2.py      # OCR -> Categorize -> Save pipeline
|   |   +-- veryfi_service.py            # Veryfi OCR integration
|   |   +-- categorization_service_gemini.py  # AI categorization
|   |   +-- dobby_chat_service_gemini.py      # Chat assistant
|   |   +-- rate_limit_service.py        # Usage tracking
|   |
|   +-- models/                 # SQLAlchemy ORM
|   |   +-- user.py             # User with firebase_uid
|   |   +-- receipt.py          # Receipt with status enum
|   |   +-- transaction.py      # 17 categories, health scores
|   |
|   +-- db/repositories/        # Data access layer
|       +-- user_repo.py
|       +-- receipt_repo.py
|       +-- transaction_repo.py
```

### iOS Frontend Architecture (SwiftUI)

```
Scandalicious/
+-- App/
|   +-- DobbyApp.swift          # @main entry, Firebase init
|
+-- Views/
|   +-- Auth/
|   |   +-- LoginView.swift     # Firebase Auth + Google/Apple Sign-In
|   |   +-- OnboardingView.swift
|   +-- Main/
|   |   +-- ContentView.swift   # TabView navigation (View/Scan/Milo)
|   |   +-- OverviewView.swift  # Analytics dashboard (1800+ lines)
|   |   +-- MiloAIChatView.swift # SSE streaming chat
|
+-- ViewModels/
|   +-- AuthenticationManager.swift  # Firebase state, token sharing
|   +-- AnalyticsViewModel.swift     # Spending data state
|   +-- SubscriptionManager.swift    # StoreKit integration
|
+-- Services/
|   +-- AnalyticsAPIService.swift    # Actor-based API client
|   +-- ReceiptUploadService.swift   # Multipart form upload
|   +-- MiloAIChatService.swift      # AsyncThrowingStream for SSE
```

### Data Flow: Receipt Upload

```
+-----------------------------------------------------------------------------+
|                      RECEIPT PROCESSING PIPELINE                             |
+-----------------------------------------------------------------------------+
|                                                                              |
|  1. iOS App                         2. FastAPI                               |
|     +------------------+               +------------------+                  |
|     | Camera capture   |  HTTP POST    | Rate limit check |                  |
|     | JPEG at 1.0      |  =========>   | (15/month)       |                  |
|     | quality          |  multipart    +------------------+                  |
|     +------------------+  form-data              |                           |
|                                                  v                           |
|  3. Veryfi OCR API                  4. Gemini 2.0 Flash                      |
|     +------------------+               +------------------+                  |
|     | Base64 encode    |               | Categorize items |                  |
|     | POST to v8 API   |  =========>   | Assign health    |                  |
|     | Extract items    |               | scores (0-5)     |                  |
|     +------------------+               +------------------+                  |
|              |                                  |                           |
|              v                                  v                           |
|  5. PostgreSQL                      6. Response                              |
|     +------------------+               +------------------+                  |
|     | Create Receipt   |               | ReceiptUpload    |                  |
|     | Create Trans-    |  <=========   | Response with    |                  |
|     | actions (1:N)    |               | all items        |                  |
|     +------------------+               +------------------+                  |
|                                                                              |
+-----------------------------------------------------------------------------+
```

### Data Flow: AI Chat (SSE Streaming)

```
+-----------------------------------------------------------------------------+
|                         STREAMING CHAT ARCHITECTURE                          |
+-----------------------------------------------------------------------------+
|                                                                              |
|  iOS Client                         FastAPI Backend                          |
|  ==========                         ===============                          |
|                                                                              |
|  MiloAIChatService                  POST /api/v2/chat/stream                 |
|       |                                    |                                 |
|       | URLSession.bytes(for:)             | Validate token                  |
|       |                                    | Check rate limit (100/mo)       |
|       v                                    v                                 |
|  AsyncThrowingStream              StreamingResponse                          |
|       |                                    |                                 |
|       |                                    | DobbyChatServiceGemini          |
|       |                                    |   * Fetch user profile          |
|       |                                    |   * Build transaction context   |
|       |                                    |   * Query last 365 days         |
|       |                                    v                                 |
|       |                            Gemini 2.0 Flash                          |
|       |                            generate_content_stream()                 |
|       |                                    |                                 |
|       | <-- SSE: {"type":"text","content":"..."} --|                         |
|       | <-- SSE: {"type":"text","content":"..."} --|                         |
|       | <-- SSE: {"type":"done"} --------------------|                        |
|       v                                    |                                 |
|  Update UI in real-time            Increment rate limit                      |
|                                    Commit session                            |
|                                                                              |
+-----------------------------------------------------------------------------+
```

### Database Schema

```
+-----------------------------------------------------------------------------+
|                         POSTGRESQL SCHEMA                                    |
+-----------------------------------------------------------------------------+
|                                                                              |
|  users                              receipts                                 |
|  ------                             --------                                 |
|  id (UUID, PK)                      id (UUID, PK)                            |
|  firebase_uid (UNIQUE, INDEX)       user_id (FK -> users.id, INDEX)          |
|  email (UNIQUE)                     store_name                               |
|  display_name                       receipt_date                             |
|  is_active                          total_amount                             |
|  created_at                         status (pending/processing/completed)    |
|                                     created_at, processed_at                 |
|                                                                              |
|  transactions                       user_rate_limits                         |
|  ------------                       ----------------                         |
|  id (UUID, PK)                      firebase_uid (UNIQUE, INDEX)             |
|  user_id (FK, INDEX)                messages_used (default 0)                |
|  receipt_id (FK, INDEX)             receipts_used (default 0)                |
|  store_name (INDEX)                 period_start_date                        |
|  item_name                          period_end_date (30 days rolling)        |
|  item_price                                                                  |
|  category (17 ENUM, INDEX)          user_profiles                            |
|  health_score (0-5, nullable)       -------------                            |
|  date (INDEX)                       user_id (FK -> users.firebase_uid)       |
|                                     first_name, last_name                    |
|  COMPOSITE INDICES:                 gender (male/female/prefer_not_to_say)   |
|  * ix_transactions_user_date        profile_completed (boolean)              |
|  * ix_transactions_user_store                                                |
|  * ix_transactions_user_category                                             |
|                                                                              |
+-----------------------------------------------------------------------------+
```

### 17 Spending Categories

| # | Category | Examples | Health Scores |
|:-:|:---------|:---------|:--------------|
| 1 | Meat & Fish | Chicken, salmon, beef | 3-4 |
| 2 | Alcohol | Beer, wine, spirits | 0 |
| 3 | Drinks (Soft/Soda) | Cola, energy drinks | 0-1 |
| 4 | Drinks (Water) | Water, sparkling water | 5 |
| 5 | Household | Cleaning, paper products | null |
| 6 | Snacks & Sweets | Chips, candy, cookies | 1-2 |
| 7 | Fresh Produce | Fruits, vegetables | 5 |
| 8 | Dairy & Eggs | Milk, cheese, yogurt | 3-4 |
| 9 | Ready Meals | Prepared foods, pizza | 2-3 |
| 10 | Bakery | Bread, pastries | 2-3 |
| 11 | Pantry | Pasta, rice, canned goods | 3 |
| 12 | Personal Care | Shampoo, dental | null |
| 13 | Frozen | Frozen foods | 2-3 |
| 14 | Baby & Kids | Diapers, baby food | null |
| 15 | Pet Supplies | Pet food, accessories | null |
| 16 | Tobacco | Cigarettes, vapes | 0 |
| 17 | Other | Uncategorized items | varies |

### API Endpoints (v2)

| Method | Endpoint | Description | Rate Limit |
|:-------|:---------|:------------|:-----------|
| POST | /receipts/upload | Upload receipt image | 15/month |
| GET | /receipts | List grouped receipts | - |
| DELETE | /receipts/{id} | Delete receipt + transactions | - |
| GET | /transactions | List with filters | - |
| PUT | /transactions/{id} | Update transaction | - |
| POST | /chat/ | Send message to Milo | 100/month |
| POST | /chat/stream | Streaming chat (SSE) | 100/month |
| GET | /analytics/summary | Period spending summary | - |
| GET | /analytics/categories | Category breakdown | - |
| GET | /analytics/trends | Spending trends | - |
| GET | /profile | Get user profile | - |
| POST | /profile | Create/update profile | - |

---

<div align="center">

## 5. Business Model

</div>

### Three-Pillar Revenue Architecture

```
                          YEAR 3 REVENUE MIX (CONSERVATIVE)
                                  $2.4M ARR

                    +----------------------------------+
                    |                                  |
                    |      B2B DATA MONETIZATION       |
                    |            $1.25M                |
                    |             52%                  |
                    |                                  |
    +---------------+----------------------------------+---------------+
    |               |                                  |               |
    |  B2C SUBS     |                                  |   ANALYTICS   |
    |   $834K       |                                  |    $315K      |
    |    35%        |                                  |     13%       |
    |               |                                  |               |
    +---------------+----------------------------------+---------------+
```

### Pillar 1: B2C Subscriptions (35% of Revenue)

| Tier | Monthly | Annual | Receipt Limit | Chat Limit | Target Users |
|:-----|--------:|-------:|:--------------|:-----------|:-------------|
| **Trial** | FREE | - | 10 total | 20 total | New users |
| **Gold** | $5.99 | $59.99 | 25/mo | 100/mo | Regular shoppers |
| **Platinum** | $12.99 | $129.99 | 50/mo | 200/mo | Power users |

### Pillar 2: B2B Data Monetization (52% of Revenue)

| Product | Description | Pricing | Margin |
|:--------|:------------|--------:|-------:|
| **DaaS** | Per-panelist data feeds | $25-50/user/yr | 70-80% |
| **Syndicated Reports** | Quarterly trend reports | $2K-25K each | 85-90% |
| **Custom Research** | Bespoke analysis | $5K-50K | 60-70% |

### Pillar 3: Analytics Reports (13% of Revenue)

| Report Type | Price Range | Target Buyer |
|:------------|------------:|:-------------|
| Quarterly Trend Reports | $1,000-$3,000 | Strategy teams |
| Category Deep Dives | $3,000-$10,000 | Brand managers |
| Custom Market Studies | $10,000-$25,000 | C-suite executives |

### Cost Structure (Per-User Economics)

| Cost Component | Per Receipt | Per Chat | Technology |
|:---------------|------------:|---------:|:-----------|
| Veryfi OCR | $0.08 | - | API v8 |
| Gemini 2.0 Flash | ~$0.001 | ~$0.002 | Categorization + Chat |
| Firebase | - | - | $8K/year fixed |
| Railway | - | - | $20K/year fixed |
| **Total Variable** | $0.081 | $0.002 | - |

---

<div align="center">

## 6. Market Analysis

</div>

### Target Customer Segments

| Segment | Addressable Size | Realistic Capture | Priority |
|:--------|----------------:|------------------:|:---------|
| **Health Optimizers** | 5M (US mobile) | 0.3% | HIGH |
| **Ex-Mint Users** | 3M (still seeking) | 0.2% | HIGH |
| **Wellness Families** | 3M (tech-savvy) | 0.1% | MEDIUM |
| **Financial Optimizers** | 2M (premium) | 0.1% | MEDIUM |

### Primary Persona: "Healthy Hannah"

```
+-----------------------------------------------------------------------------+
|                            TARGET PERSONA                                    |
+-----------------------------------------------------------------------------+
|                                                                              |
|  NAME:        Hannah Chen                AGE:    32                          |
|  OCCUPATION:  Marketing Manager          INCOME: $85,000                     |
|  LOCATION:    Urban/Suburban             TECH:   iPhone 15, Apple Watch      |
|                                                                              |
|  CURRENT APPS:  Yuka, Apple Health, MyFitnessPal                             |
|  PAIN POINTS:   Can't connect health choices to spending patterns            |
|  WILLINGNESS:   Pays for wellness apps, values data privacy                  |
|                                                                              |
|  QUOTE:         "I want to see if my grocery budget is actually              |
|                  supporting my health goals"                                 |
|                                                                              |
|  MILO FIT:      Perfect alignment - health-conscious, budget-aware,          |
|                 tech-savvy, willing to pay for quality tools                 |
|                                                                              |
+-----------------------------------------------------------------------------+
```

### Market Sizing (Conservative)

```
                           MARKET FUNNEL (CONSERVATIVE)

        +-----------------------------------------------------+
        |                     TAM: $21.7B                      |
        |         Combined Receipt + Finance + Data            |
        +--------------------------+--------------------------+
                                   |
                    +--------------v--------------+
                    |      SAM: $1.8B             |
                    |   US Health-Conscious       |
                    |   Finance App Users         |
                    +--------------+--------------+
                                   |
                        +----------v----------+
                        |    SOM: $24M        |
                        |    Year 3 Target    |
                        |     (25K MAU)       |
                        +---------------------+
```

---

<div align="center">

## 7. Financial Projections

</div>

### 3-Year Revenue Forecast (Conservative)

| Metric | Year 1 | Year 2 | Year 3 |
|:-------|-------:|-------:|-------:|
| **Trial Signups** | 12,500 | 35,000 | 60,000 |
| **Conversion Rate** | 15% | 17% | 18% |
| **Ending Paid Users** | 1,688 | 5,355 | 9,720 |
| **B2C Revenue** | $128K | $460K | $835K |
| **B2B Revenue** | $80K | $500K | $1,250K |
| **Analytics Revenue** | $20K | $140K | $315K |
| **Total Revenue** | **$228K** | **$1.1M** | **$2.4M** |
| **Operating Profit** | ($72K) | $418K | $1.39M |
| **Operating Margin** | -31.6% | 38.0% | **58.0%** |

### Unit Economics (Conservative)

| Metric | Gold Tier | Platinum Tier | B2B Panel |
|:-------|----------:|--------------:|----------:|
| **Customer LTV (Net)** | $50.92 | $121.48 | $80.00 |
| **Customer CAC** | $17.00 | $17.00 | $30.00 |
| **LTV:CAC Ratio** | 3.0:1 | 7.1:1 | 2.7:1 |
| **Payback Period** | 4.5 mo | 2.6 mo | 6-8 mo |

### Cost Structure (Year 3)

```
                          COST BREAKDOWN (YEAR 3)

    +-------------------------------------------------------------+
    |                     VARIABLE COSTS                           |
    |                        $255K (11%)                           |
    +-------------------------------------------------------------+
    | Veryfi OCR Processing     $194K    ######################### |
    | Gemini API                $3K      #                         |
    | Firebase Storage          $8K      #                         |
    | Payment Processing        $50K     #####                     |
    +-------------------------------------------------------------+

    +-------------------------------------------------------------+
    |                      FIXED COSTS                             |
    |                       $755K (31%)                            |
    +-------------------------------------------------------------+
    | Engineering               $300K    ######################### |
    | Sales & Marketing         $200K    #################         |
    | B2B Sales Team            $120K    ##########                |
    | Legal & Compliance        $75K     ######                    |
    | Customer Support          $40K     ###                       |
    | Infrastructure            $20K     ##                        |
    +-------------------------------------------------------------+
```

### Profitability Milestones

| Milestone | Timeline | Revenue Run-Rate |
|:----------|:---------|:-----------------|
| Break-Even (Monthly) | Month 10 | $50K MRR |
| Cash Flow Positive | Month 14 | $80K MRR |
| Sustained Profitability | Month 24 | $150K MRR |

---

<div align="center">

## 8. Go-to-Market Strategy

</div>

### Launch Timeline

```
                         GO-TO-MARKET PHASES (CONSERVATIVE)

    PRE-LAUNCH          LAUNCH            SCALE              EXPAND
    (M-3 to M0)         (M1-M6)           (M7-M18)           (M19-36)
    ==========          ======            =====              ======

    * ASO Setup         * Soft Launch      * CAC < $20        * Android
    * Beta Program      * PR Push          * 2 B2B Pilots     * UK Market
    * Waitlist (500)    * Paid Ads         * 25% Organic      * Enterprise
    * Content           * Influencers      * 5K MAU           * 15K MAU

    Target: 300 Beta    Target: 1.5K MAU   Target: 7K MAU     Target: 25K MAU
```

### Marketing Budget Allocation (Year 1: $75K)

| Channel | Allocation | Budget | Focus |
|:--------|:----------:|-------:|:------|
| Paid Acquisition | 35% | $26,250 | App installs, retargeting |
| Influencer Marketing | 20% | $15,000 | Micro partnerships |
| Content & SEO | 20% | $15,000 | Organic growth engine |
| B2B Marketing | 15% | $11,250 | ABM, thought leadership |
| Brand & Creative | 10% | $7,500 | Assets, video production |

---

<div align="center">

## 9. Competitive Positioning

</div>

### Competitive Landscape

| Competitor | Users | Focus | Health Features | AI Chat | Threat |
|:-----------|------:|:------|:---------------:|:-------:|:------:|
| **Fetch Rewards** | 12.5M | Rewards/Points | No | No | Medium |
| **Ibotta** | 14.7M | Cashback | No | No | Medium |
| **Receipt Hog** | 10M+ | Gamified Rewards | No | No | Low |
| **Copilot** | N/A | AI Budgeting | No | Yes | Medium |
| **Monarch Money** | Growing | Household Finance | No | No | Medium |
| **MILO** | Pre-launch | Wellness + Finance | **Yes** | **Yes** | - |

### Feature Comparison

```
                         FEATURE COMPARISON

                        Item-Level   Health    AI Chat    Privacy
                        Granularity  Scoring   Assistant  Premium
                        ===========  =======   =========  =======
    MILO                    [X]        [X]        [X]        [X]
    Fetch Rewards           [ ]        [ ]        [ ]        [ ]
    Ibotta                  [ ]        [ ]        [ ]        [ ]
    Copilot                 [ ]        [ ]        [X]        [?]
    Monarch                 [ ]        [ ]        [ ]        [?]
```

### SWOT Analysis

```
+----------------------------------+----------------------------------+
|           STRENGTHS              |           WEAKNESSES             |
+----------------------------------+----------------------------------+
| [+] Unique health scoring IP     | [-] No existing user base        |
| [+] Modern AI tech (Gemini 2.0)  | [-] iOS-only (57% addressable)   |
| [+] Privacy-first architecture   | [-] No rewards/cashback          |
| [+] Dual B2C + B2B revenue       | [-] Limited brand awareness      |
| [+] Production-ready codebase    | [-] Requires external funding    |
| [+] 17-category granularity      | [-] Small team capacity          |
+----------------------------------+----------------------------------+
|          OPPORTUNITIES           |             THREATS              |
+----------------------------------+----------------------------------+
| [^] Health-conscious trend (71%) | [v] Big Tech entry risk (Apple)  |
| [^] B2B data demand growing      | [v] Economic downturn impact     |
| [^] AI normalization (73%)       | [v] Privacy regulation changes   |
| [^] GLP-1 awareness (16% HH)     | [v] Subscription fatigue (41%)   |
| [^] Post-Mint user migration     | [v] CAC inflation trend          |
+----------------------------------+----------------------------------+
```

---

<div align="center">

## 10. Risk Assessment

</div>

### Risk Summary

| Category | Critical | High | Medium | Low |
|:---------|:--------:|:----:|:------:|:---:|
| Market | 0 | 2 | 2 | 1 |
| Technical | 0 | 1 | 2 | 1 |
| Financial | 1 | 1 | 1 | 0 |
| Regulatory | 1 | 1 | 1 | 0 |
| **Total** | **2** | **5** | **6** | **2** |

### Critical Risks

**Risk 1: GDPR Non-Compliance at Launch**
| Attribute | Assessment |
|:----------|:-----------|
| Impact | CRITICAL (Cannot launch in EU, 52% of revenue blocked) |
| Probability | MEDIUM (If timeline slips) |
| Mitigation | Dedicated budget, 12-week remediation plan |
| Residual Risk | LOW after mitigation |

**Risk 2: Insufficient Seed Funding**
| Attribute | Assessment |
|:----------|:-----------|
| Impact | CRITICAL (Operations cease) |
| Probability | MEDIUM |
| Mitigation | Conservative projections, multiple investor outreach |
| Residual Risk | MEDIUM |

### Technical Risk Mitigations

| Risk | Impact | Mitigation |
|:-----|:------:|:-----------|
| Veryfi API cost increase | HIGH | Volume contracts, alternative OCR exploration |
| Gemini API reliability | MEDIUM | Fallback to Claude API (already integrated in V1) |
| Firebase Auth issues | LOW | Token caching, App Group sharing for extension |
| Database scaling | LOW | PostgreSQL with proper indexing, connection pooling |

---

<div align="center">

## 11. Compliance & Legal

</div>

### GDPR Compliance Status

```
+------------------------------------------------------------------------------+
|                        GDPR READINESS ASSESSMENT                              |
+------------------------------------------------------------------------------+
|                                                                               |
|  Current Status:     NON-COMPLIANT (pre-launch expected)                      |
|  Readiness Score:    25/100                                                   |
|  Required Investment: 75K-115K EUR                                            |
|  Timeline to Compliance: 12 weeks                                             |
|                                                                               |
|  CRITICAL: Cannot launch or monetize data without GDPR compliance             |
|                                                                               |
+------------------------------------------------------------------------------+
```

### Compliance Priorities

| Priority | Requirement | Status | Investment |
|:---------|:------------|:------:|:-----------|
| Critical | Privacy Policy | Pending | 5-10K EUR |
| Critical | Data Processing Agreements | Pending | 15-25K EUR |
| Critical | Consent Management System | Pending | 10-15K EUR |
| High | Data Subject Rights Portal | Pending | 15-20K EUR |
| High | International Transfer Docs | Pending | 10-15K EUR |
| High | DPIA for AI Processing | Pending | 10-15K EUR |

### Data Architecture (Privacy-Ready)

```
+-----------------------------------------------------------------------------+
|                         DATA PRIVACY ARCHITECTURE                            |
+-----------------------------------------------------------------------------+
|                                                                              |
|  USER CONSENT TIERS:                                                         |
|  ==================                                                          |
|  Tier 1: Essential Only    - Core app functionality                          |
|  Tier 2: Analytics         - Aggregated usage patterns                       |
|  Tier 3: B2B Data Sharing  - Anonymized panel participation                  |
|                                                                              |
|  DATA STORAGE:                                                               |
|  =============                                                               |
|  * PostgreSQL (EU region via Railway)                                        |
|  * Firebase Storage (configurable region)                                    |
|  * User data isolated by firebase_uid                                        |
|  * Soft delete support for GDPR right to erasure                             |
|                                                                              |
|  THIRD-PARTY PROCESSORS:                                                     |
|  =======================                                                     |
|  * Veryfi (US) - Receipt OCR, 60s retention                                  |
|  * Google Gemini - AI processing, no training on user data                   |
|  * Firebase - Authentication, EU region available                            |
|                                                                              |
+-----------------------------------------------------------------------------+
```

---

<div align="center">

## 12. Investment Thesis

</div>

### Investment Summary

```
+------------------------------------------------------------------------------+
|                      INVESTMENT OPPORTUNITY (CONSERVATIVE)                    |
+------------------------------------------------------------------------------+
|                                                                               |
|  AMOUNT SOUGHT:        $400,000 - $600,000                                    |
|  ROUND:                Seed                                                   |
|  USE:                  Product, Compliance, Growth, Operations                |
|  RUNWAY:               18-24 months                                           |
|  TARGET RETURN:        6-10x at Year 3 exit (conservative)                    |
|                                                                               |
+------------------------------------------------------------------------------+
```

### Use of Funds ($500K Mid-Point)

| Category | % | Amount | Purpose |
|:---------|--:|-------:|:--------|
| Product Development | 30% | $150K | Subscriptions, B2B features, Android |
| Legal & Compliance | 20% | $100K | GDPR, privacy, data agreements |
| User Acquisition | 20% | $100K | Marketing, influencers, paid channels |
| B2B Sales | 15% | $75K | Sales capability, partnerships |
| Operations | 15% | $75K | Finance, HR, admin, contingency |

### Investment Highlights

| Factor | Details |
|:-------|:--------|
| **Category Creation** | First wellness-aware spending analytics platform |
| **Production Ready** | Complete iOS + FastAPI stack, not just prototype |
| **AI-Native** | Gemini 2.0 Flash at $0.002/interaction |
| **Sustainable Economics** | 58% operating margins, 3:1+ LTV:CAC |
| **Diversified Revenue** | Three pillars reduce concentration risk |
| **Capital Efficiency** | Profitable by Month 14, 18-24mo runway |

### Exit Valuation Range (Year 3)

| Scenario | Multiple | Valuation | Seed Return |
|:---------|:--------:|----------:|:-----------:|
| **Conservative** | 5x | $12M | 3-4x |
| **Base Case** | 6x | $14.4M | **6-8x** |
| Moderate | 8x | $19.2M | 10-12x |
| Optimistic | 10x | $24M | 12-15x |

### Potential Acquirers

```
+-----------------------------------------------------------------------------+
|                          ACQUIRER UNIVERSE                                   |
+-----------------------------------------------------------------------------+
|                                                                              |
|  CPG & CONSUMER (Most Likely)        DATA & ANALYTICS                        |
|  ========================            ================                        |
|  Nestle * P&G * Unilever             NielsenIQ * Circana (IRI)               |
|  PepsiCo * Kraft Heinz               Dun & Bradstreet                        |
|                                                                              |
|  FINTECH & PAYMENTS                  RETAIL & ECOMMERCE                      |
|  ==================                  ==================                      |
|  Plaid * Yodlee * MX                 Instacart * Walmart Labs                |
|  Block (Square)                      Kroger Technology                       |
|                                                                              |
+-----------------------------------------------------------------------------+
```

---

<div align="center">

## 13. Strategic Roadmap

</div>

### Milestone Timeline

```
================================================================================

    2026 Q2-Q3                    2026 Q4 - 2027 Q2          2027 Q3 - 2028
    ==========                    ================           ==============

    FOUNDATION                    VALIDATION                  SCALE

    [x] Close Seed Round          [ ] Achieve 5K MAU          [ ] Android Launch
    [ ] GDPR Compliance           [ ] First B2B Revenue       [ ] UK Expansion
    [ ] App Store Launch          [ ] $30K MRR                [ ] 15K MAU
    [ ] 1K-1.5K MAU               [ ] 2+ Enterprise Pilots    [ ] Series A Prep
    [ ] Beta Validation           [ ] Prove Unit Economics    [ ] Team Growth

================================================================================

    2028-2029
    =========

    PROFITABILITY & EXIT OPTIONALITY

    [ ] 25K MAU
    [ ] $2.4M ARR
    [ ] 58% Operating Margin
    [ ] Strategic Acquisition or Series A

================================================================================
```

### Critical Success Factors

```
+-----------------------------------------------------------------------------+
|                       CRITICAL SUCCESS FACTORS                               |
+-----------------------------------------------------------------------------+
|                                                                              |
|  1. GDPR COMPLIANCE (Non-Negotiable)                                         |
|     Must achieve before launch - blocks 52% of revenue otherwise             |
|                                                                              |
|  2. TRIAL CONVERSION                                                         |
|     Achieving 15%+ trial-to-paid - drives all B2C revenue                    |
|                                                                              |
|  3. DATA CONSENT                                                             |
|     Achieving 40%+ opt-in - enables B2B revenue stream                       |
|                                                                              |
|  4. UNIT ECONOMICS                                                           |
|     Maintaining CAC < $20 and LTV:CAC > 3:1 - validates scalability          |
|                                                                              |
|  5. B2B CAPABILITY                                                           |
|     Building sales function - 52% of revenue depends on this                 |
|                                                                              |
+-----------------------------------------------------------------------------+
```

---

<div align="center">

## 14. Technical Appendix

</div>

### A. Technology Stack Details

| Layer | Technology | Version | Purpose |
|:------|:-----------|:--------|:--------|
| **iOS** | SwiftUI | iOS 17+ | Native UI framework |
| **iOS** | Firebase SDK | Latest | Auth, Analytics, Storage |
| **iOS** | StoreKit 2 | Native | Subscriptions |
| **Backend** | FastAPI | 0.109.0 | Async REST API |
| **Backend** | Python | 3.11 | Runtime |
| **Backend** | SQLAlchemy | 2.0.25 | ORM with async |
| **Database** | PostgreSQL | Latest | Primary datastore |
| **AI** | Gemini 2.0 Flash | google-genai 1.0+ | Categorization + Chat |
| **OCR** | Veryfi | v8 API | Receipt extraction |
| **Auth** | Firebase Admin | 6.4.0 | Token verification |
| **Hosting** | Railway | - | Backend deployment |

### B. API Response Examples

**Receipt Upload Response:**
```json
{
  "receipt_id": "uuid",
  "status": "completed",
  "store_name": "Albert Heijn",
  "receipt_date": "2026-01-31",
  "total_amount": 45.67,
  "items_count": 12,
  "is_duplicate": false,
  "transactions": [
    {
      "id": "uuid",
      "item_name": "Organic Bananas",
      "item_price": 2.49,
      "category": "Fresh Produce",
      "health_score": 5
    }
  ]
}
```

**Chat Stream SSE Events:**
```
data: {"type": "text", "content": "Based on your spending..."}
data: {"type": "text", "content": " this month, you've spent..."}
data: {"type": "done"}
```

### C. Key Metrics Definitions

| Metric | Definition |
|:-------|:-----------|
| MAU | Monthly Active Users with at least 1 session |
| Paid Users | Users with active Gold or Platinum subscription |
| Trial Conversion | % of trial users converting to paid within 14 days |
| Data Consent Rate | % of users opting into B2B data sharing |
| Monthly Churn | % of paid users canceling in a given month |
| LTV | Lifetime Value = ARPU / Monthly Churn Rate |
| CAC | Customer Acquisition Cost = Marketing Spend / New Customers |

---

<div align="center">

## Conclusion

</div>

```
+------------------------------------------------------------------------------+
|                                                                               |
|                      INVESTMENT RECOMMENDATION                                |
|                                                                               |
|                           ##################                                  |
|                           #                #                                  |
|                           #    CAUTIOUS    #                                  |
|                           #      BUY       #                                  |
|                           #                #                                  |
|                           ##################                                  |
|                                                                               |
|  MILO represents a category-creating opportunity with meaningful upside       |
|  potential, tempered by execution risks that warrant conservative             |
|  expectations.                                                                |
|                                                                               |
|  STRENGTHS:                                                                   |
|  [+] Unique value proposition in growing markets                              |
|  [+] Production-ready iOS + FastAPI technology stack                          |
|  [+] Viable unit economics (3:1+ LTV:CAC)                                     |
|  [+] Diversified revenue reduces single-point-of-failure risk                 |
|  [+] AI-native architecture with Gemini 2.0 at low cost                       |
|                                                                               |
|  RISKS:                                                                       |
|  [-] GDPR compliance required before launch (12-week delay possible)          |
|  [-] B2B revenue (52%) depends on data consent rates                          |
|  [-] No existing user base requires acquisition spending                      |
|  [-] Subscription fatigue trend may impact conversion                         |
|                                                                               |
|  The $400K-$600K seed investment offers 6-10x return potential under          |
|  conservative assumptions, with meaningful downside protection through        |
|  early profitability focus and diversified revenue streams.                   |
|                                                                               |
|  RECOMMENDATION: Invest with clear milestones and capital tranches            |
|                                                                               |
+------------------------------------------------------------------------------+
```

---

<div align="center">

### Contact

**DeepmAInd B.V.**

*Building the future of wellness-aware spending intelligence*

---

*This document is confidential and intended for authorized recipients only.*
*Forward-looking statements are based on current expectations and assumptions.*
*Actual results may vary materially. All projections use conservative assumptions.*

---

**Document Version:** 4.0 (Technical Update)
**Last Updated:** January 31, 2026
**Prepared for:** Investor Review

</div>
