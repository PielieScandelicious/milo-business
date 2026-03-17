# Scandalicious iOS App — Business Context Document

> **Purpose**: Complete context document for business plan writing. Covers all features, user experience, monetization, technical capabilities, and competitive differentiators of the Scandalicious iOS app.

---

## 1. Product Overview

**App Name**: Scandalicious
**Platform**: iOS (iPhone)
**Tech Stack**: SwiftUI, Firebase Auth, FastAPI backend on Railway, PostgreSQL
**Target Market**: Belgium (primary), with expansion potential to Netherlands and France
**Languages**: English, Dutch (Nederlands), French (Français)
**Supported Stores**: 13 Belgian/Dutch grocery chains — Colruyt, Delhaize, Carrefour, Lidl, Aldi, Albert Heijn, Okay, Intermarché, Spar, Bio-Planet, Action, Kruidvat, Jumbo

**One-liner**: Scandalicious turns grocery receipts into actionable financial and nutritional insights through AI, while rewarding users with real euro cashback for every scan.

---

## 2. Core Value Proposition

Unlike traditional expense trackers that rely on manual entry or bank API connections (which only show "€45 at Colruyt"), Scandalicious uses AI-powered receipt scanning to extract **item-level data** — every product, its price, quantity, category, and even a health/nutrition score. This enables:

- **Granular spending analytics** (not just totals, but what you actually bought)
- **Nutritional tracking** without a separate diet app
- **Personalized deal recommendations** based on what you actually buy
- **AI financial coaching** with full purchase history context
- **Gamified engagement** that turns a mundane task into a rewarding habit

---

## 3. User Journey

### 3.1 Onboarding
1. **Authentication** — Sign up via Email, Google, or Apple Sign-In
2. **Profile setup** — Nickname, age, gender, language preference
3. **Store selection** — Pick preferred grocery stores from a visual 3-column grid of 13 Belgian chains (with logos and brand colors)
4. **Ready to scan** — Immediately taken to the main app

### 3.2 Daily Use Loop
1. **Scan a receipt** → In-app camera or Share Extension (from Photos/Files/any app)
2. **AI processes it** → Store identified, items extracted, categorized, health-scored
3. **Earn rewards** → Cash (€0.50+ per receipt), spin wheel tickets, streak progress
4. **Spin the wheel** → Win €0.20 to €1,000 jackpot
5. **Track spending** → Dashboard shows budgets, categories, store breakdowns, trends
6. **Get insights** → AI chat answers questions about spending, cooking suggestions, health patterns
7. **Browse deals** → Personalized weekly promotions at their stores
8. **Redeem rewards** → Spend wallet balance on real store coupons

---

## 4. Feature Inventory

### 4.1 Receipt Scanning
- **Custom camera interface** with image quality validation (rejects blurry/dark photos)
- **Multi-image stacking** for long receipts
- **Share Extension** — Upload receipts directly from Photos, Files, Safari, or email without opening the app
- **AI-powered OCR** extracts: store name, date, all line items, quantities, unit prices
- **Smart categorization** — 34 categories across 8 groups (Fresh Food, Pantry, Frozen, Drinks, Snacks, Household, Personal Care, Other)
- **Duplicate detection** with confidence scoring to prevent double-counting
- **Async processing** with real-time status polling and push notification on completion
- **Item normalization** — Standardizes brand names and product names across receipts

### 4.2 Spending Analytics & Budget Management
- **Monthly spending dashboard** with total spend, receipt count, and interactive charts
- **Interactive donut/pie charts** — Category and store breakdowns with tap-to-drill-down
- **Budget setting** — Monthly budget with per-category allocation (smart or manual)
- **Budget tracking** — Real-time pace indicators (Well Under / On Track / Slightly Over / Over Budget)
- **Projected end-of-month spend** based on current pace
- **Store breakdown** — Spending per supermarket with visit frequency
- **Category breakdown** — Expandable to individual transaction items
- **Period navigation** — Browse any historical month with swipe gestures
- **Year-in-Review** — Annual summary with monthly trends, top categories, top stores
- **All-time statistics** — Lifetime spending totals and patterns
- **Pull-to-refresh** data sync

### 4.3 Food Health Scoring
- **Nutri-Score-style rating** (0–5 scale) for every scanned grocery item
- **Per-item scores** visible on transaction details
- **Aggregate health scores** per receipt, per category, per month, and all-time
- **Health score distribution** — Percentage breakdown of very healthy to very unhealthy purchases
- **Trend tracking** — Monitor if dietary habits improve over time
- **AI health insights** — Chat with Milo about nutritional patterns

### 4.4 AI Chat Assistant ("Milo")
- **Conversational AI** powered by streaming Server-Sent Events (SSE) for real-time responses
- **Full purchase history context** — Milo knows everything the user has bought
- **Capabilities**:
  - "What can I cook with what I bought this week?" — Recipe suggestions from scanned groceries
  - "Predict my spending this month" — Spending forecasts
  - "Track price of [product]" — Price history analysis
  - "How healthy are my purchases?" — Nutrition insights
  - General financial advice and spending pattern analysis
- **Markdown support** including formatted tables in responses
- **Animated dachshund mascot** (Milo) as chat avatar, drawn in real-time with SwiftUI Canvas
- **Rate limited** — Monthly message cap (100/month) as freemium gate

### 4.5 AI-Powered Deals & Promotions
- **Weekly personalized deal recommendations** based on user's actual purchase history
- **Weekly savings estimate** prominently displayed
- **"Top Picks"** — Specific products on sale at the user's preferred stores with price, discount %, and calculated savings
- **"Smart Switch"** — AI identifies when switching brands on the same product saves money
- **Direct links** to store promotional folders
- **Store-specific branding** — Each store's deals shown with their brand colors
- **Animated loading state** — Custom dachshund "sniffing for deals" animation at 30fps

### 4.6 Gamification System

#### Wallet (Virtual Euro Balance)
- Euro-denominated virtual wallet (stored in cents for precision)
- Earned through receipt rewards, spin wheel wins, streak bonuses, mystery bonuses
- Spent on real store coupons in the Coupon Store

#### Receipt Rewards
- **Base reward**: €0.50 per receipt scan
- **Tier multiplier**: Up to 1.5x at Diamond tier (€0.75 per receipt)
- **Mystery bonus** on every scan: 25% chance of extra cash, 10% chance of free spin, revealed via animated 3D card flip

#### Spin Wheel
- 8-segment prize wheel with physics-based spin animation (4.5s deceleration curve)
- Prizes: €0.20 (35%), €0.50 (25%), €1 (18%), €2 (10%), €5 (6%), €10 (3%), €50 (2%), **€1,000 jackpot (1%)**
- Haptic tick feedback during spin (graduated frequency)
- Confetti animation on jackpot or wins ≥ €10
- Spins earned per receipt based on tier level (1 to 5 spins)

#### Tier System (Monthly)

| Tier | Receipts/Month | Cash Multiplier | Spins/Receipt |
|------|---------------|-----------------|---------------|
| Bronze | 0–4 | 1.0x (€0.50) | 1 |
| Silver | 5–7 | 1.1x (€0.55) | 2 |
| Gold | 8–11 | 1.25x (€0.625) | 3 |
| Diamond | 12+ | 1.5x (€0.75) | 5 |

#### Streak System
- Weekly scan streak — count of consecutive weeks with at least one scan
- "At Risk" warning at 5+ days without scanning
- Streak shield item protects against losing a streak
- 4-week reward cycle: 3 spin-reward weeks + 1 cash-bonus week (escalating: €0.50 → €1 → €1.50+)

#### Badges (12 Achievements)
- First Scan, Streak milestones (2/4/8 weeks), Tier milestones (Silver/Gold)
- Big Spender, Lucky Spin (≥€10 win), Jackpot, Night Owl, Collector, Coupon Buyer

#### Coupon Store
- Spend wallet balance on real store discount coupons
- Store-specific coupons (Lidl, Colruyt, Delhaize, Aldi, Carrefour, Albert Heijn)
- QR code payload for in-store redemption
- "My Coupons" section tracks owned and redeemed coupons

### 4.7 Expense Splitting
- Split any receipt among multiple people (up to 8 color-coded participants)
- Equal split or custom per-item assignment
- "Is Me" flag for the user's own share
- Recent friends list for quick reuse
- Shareable text summary for messaging friends
- Full calculation breakdown per participant

### 4.8 Apple Wallet Integration
- Create digital loyalty/membership cards for any grocery store
- Barcode scanning (camera) or photo import to capture existing loyalty cards
- Custom card colors and store logo upload
- Cards saved directly to Apple Wallet via PassKit

### 4.9 Profile & Settings
- Editable: nickname, gender, age, language, preferred stores
- Subscription management (StoreKit 2 native sheet)
- Sign out with cache clearing

---

## 5. UI/UX Design Philosophy

### Visual Identity
- **Dark mode exclusive** — Premium, modern feel with near-black (#0D0D0D) background
- **Per-tab color gradients** — Each section has a distinctive color identity that fades on scroll:
  - Budget: Purple
  - Home: Deep ocean blue
  - Deals: Emerald green
  - Milo AI: Indigo
  - Rewards: Gold/amber
- **Gold accent** (RGB: 255, 214, 0) used throughout rewards and gamification
- **Glass-morphism cards** — Semi-transparent white (7% opacity) rounded rectangles

### Brand Mascot
- **Milo** — A dachshund (wiener dog) rendered in real-time with SwiftUI Canvas
- Appears as: tab bar icon, AI chat avatar, loading animation (sniffing for deals), onboarding welcome
- Full character design with fur gradients, eye shines, eyebrows, tongue, and floppy ears
- Custom walking/sniffing animation at 30fps in the Deals tab loading state

### Animation & Polish
- **Spring physics** on nearly every interaction
- **3D card flips** (mystery bonus reveal, stats cards, pie charts)
- **Confetti particle system** for celebration moments
- **Animated number transitions** — Currency amounts animate digit-by-digit on change
- **Haptic feedback** throughout — ticks during spin, success/error notifications
- **Skeleton loading views** with shimmer effect during data load
- **Staggered entrance animations** on each tab visit
- **Rubber-band bounce** on period navigation boundaries
- **Capture success overlay** — Expanding rings with 24 shimmer particles on receipt capture

### Accessibility & Localization
- SF Symbols throughout for system consistency
- Full localization system with `L("key")` wrapper for all user-facing strings
- Three languages with flag emoji indicators (🇬🇧 🇳🇱 🇫🇷)

---

## 6. Monetization Model

### Current State: Beta / User Acquisition Phase
The paywall is **intentionally disabled** — all users receive full premium access. This indicates a growth-first strategy to build the user base before monetizing.

### Implemented Monetization (Ready to Activate)
- **Freemium subscription** via StoreKit 2 (Apple native):
  - `com.deepmaind.scandalicious.premium.monthly`
  - `com.deepmaind.scandalicious.premium.yearly`
- **Full paywall UI built** with free trial flow, feature comparison, and restore purchases

### Freemium Gates (Built into the App)
- **AI message limit**: 100 messages/month (Milo AI chat)
- **Receipt upload limit**: 15 receipts/month
- These limits are tracked in the UI (gear menu shows usage like "8/20 receipts") but currently not enforced

### Potential Additional Revenue Streams (Infrastructure Exists)
- **Coupon store** — Could partner with retailers for sponsored coupons
- **Promoted deals** — The Deals tab could feature paid store promotions
- **Data insights** — Aggregated, anonymized purchase data is valuable to FMCG brands and retailers

---

## 7. Technical Architecture Summary

### Frontend (iOS)
- **SwiftUI** with MVVM architecture
- **@MainActor ViewModels** for thread-safe UI updates
- **Actor-based services** for concurrent API access
- **Disk-backed caching** — 12 months of data cached locally for instant navigation
- **Multi-phase data preloading** on app launch (4 parallel phases)
- **Share Extension** with App Group data sharing
- **StoreKit 2** for native subscription handling
- **PassKit** for Apple Wallet integration
- **AVFoundation** for custom camera

### Backend (FastAPI)
- **Python 3.11** with FastAPI framework
- **PostgreSQL** database with Alembic migrations
- **Railway** hosting with separate non-prod and production environments
- **Firebase Auth** token verification
- **AI/ML pipeline**: OCR → item extraction → categorization → health scoring
- **SSE streaming** for real-time AI chat responses
- **Pinecone** vector search for promo matching
- **Gemini** for promo description generation

### Third-Party Dependencies
| Dependency | Purpose |
|-----------|---------|
| Firebase iOS SDK | Auth, Analytics, App Check |
| GoogleSignIn-iOS | Google authentication |
| PhosphorSwift | Icon library (34 category icons) |

---

## 8. Competitive Differentiators

### 1. Receipt-First, Not Bank-First
Most expense trackers connect to bank accounts (Plaid/Open Banking) and show merchant-level data ("€45 at Colruyt"). Scandalicious scans physical receipts to get **item-level data** — which products, at what price, in what quantity. This is fundamentally richer data.

### 2. Health Scoring on Groceries
No comparable grocery tracking app scores the nutritional quality of purchases. Users can track whether their diet is improving month-over-month, bridging the gap between financial and health apps.

### 3. Conversational AI with Purchase Context
"Milo" isn't a generic chatbot — it has access to the user's entire purchase history. It can answer questions like "What can I cook with what I bought this week?" or "Am I spending more on meat than last month?" — combining financial advisor and nutritionist.

### 4. Real Promotional Data Integration
The Deals tab fetches actual current weekly promotions from Belgian supermarkets and cross-references them with the user's purchase history. The "Smart Switch" feature identifies brand-switching savings opportunities that are personally relevant.

### 5. Gamified Financial Behavior Change
The combination of cashback (€0.50+/receipt), spin wheel (up to €1,000 jackpot), streaks, tiers, badges, and a virtual wallet creates strong behavioral reinforcement. Unlike points-based systems, prizes are in actual euros redeemable for real store coupons.

### 6. Share Extension (Friction Removal)
Users can upload receipts directly from the iOS Photos app, Files app, or any share sheet — without opening Scandalicious. This eliminates the biggest friction point in receipt-scanning apps.

### 7. Belgium-Specific Focus
Hard-coded support for 13 Belgian/Dutch grocery chains with brand colors, logos, and promotional data. This is a focused market entry rather than a generic global play.

### 8. Multilingual from Day One
English, Dutch, and French support covers the Belgian linguistic divide (Flanders, Wallonia, Brussels), a critical requirement for any Belgian consumer product.

---

## 9. Data Assets & Moats

### Proprietary Data
- **Item-level purchase history** — Granular product-by-product data per user, per store, per period
- **Health score database** — Nutritional classification of grocery products
- **Price history** — Product pricing over time across multiple retailers
- **Brand normalization** — Mapping of OCR text to standardized brand/product names

### Engagement Moats
- **Wallet balance** — Users have earned money they don't want to abandon
- **Streak history** — Losing a long streak is psychologically costly
- **Badge collection** — Sunk-cost effect from earned achievements
- **Purchase history** — Months/years of spending data that can't be rebuilt elsewhere
- **AI context** — Milo's value increases with more data (network effect within user)

### Scalability
- Architecture supports expansion to Netherlands (Albert Heijn, Jumbo already in store list) and France (Carrefour, Intermarché already present)
- Adding new markets requires: store database additions, OCR training on new receipt formats, promotional data feeds

---

## 10. Key Metrics the App Tracks

The app is instrumented to measure (via Firebase Analytics + internal tracking):

| Metric | Source |
|--------|--------|
| Receipts scanned / month | Receipt upload counter |
| Items parsed / month | Transaction count |
| AI messages sent / month | Rate limit counter |
| Active streak length | Streak system |
| Tier distribution | Tier progression |
| Wallet balance / spend | Gamification wallet |
| Spins used / won | Spin wheel |
| Coupons purchased / redeemed | Coupon store |
| Budget adherence | Budget progress |
| Health score trends | Health analytics |
| Store visit frequency | Store breakdown |
| Category spending distribution | Category analytics |

---

## 11. Current Maturity & Gaps

### Production-Ready
- Full auth flow (Email, Google, Apple)
- Receipt scanning with async processing
- Spending analytics with 12-month cache
- AI chat with streaming responses
- Budget management with pace tracking
- Gamification (wallet, spins, streaks, tiers, badges, coupons)
- Expense splitting
- Share Extension
- Apple Wallet pass creation
- Multi-language support
- Paywall UI (ready to enable)

### Known Gaps
- **Gamification not synced to backend** — Wallet, streaks, badges stored only in local UserDefaults. Reinstalling the app loses this data. Backend sync is the most critical missing piece for production launch.
- **Paywall disabled** — Subscriptions built but not enforced (intentional for beta)
- **Push notifications** — Infrastructure exists but remote push for re-engagement (e.g., streak at risk) not yet implemented
- **Social features** — Expense splitting exists, but no friend system, sharing, or leaderboards beyond local split

---

## 12. App Store Positioning

### Primary Category
Finance / Personal Finance

### Secondary Category
Health & Fitness (due to health scoring)

### Keywords
Receipt scanner, grocery tracker, spending analytics, budget planner, grocery health score, AI financial assistant, cashback rewards, Belgian supermarkets, Colruyt, Delhaize, Carrefour, Lidl

### Value Props for App Store Listing
1. Scan receipts, earn real money (€0.50+ per scan)
2. Know exactly where your grocery money goes
3. Track the health quality of your purchases
4. AI assistant that knows your shopping habits
5. Weekly personalized deals at your favorite stores
6. Win up to €1,000 on the spin wheel
7. Split grocery bills with friends in seconds
