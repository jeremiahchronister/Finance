# Product Metrics & KPIs: Forex Risk Calculator Platform

## Metrics Framework Overview

**Measurement Philosophy:** Track metrics across three dimensions:
1. **Business Health:** Revenue, retention, growth
2. **Product Engagement:** Usage, adoption, feature utilization
3. **Customer Success:** Churn reduction, compliance, trader outcomes

**Reporting Cadence:**
- **Daily:** Operational metrics (uptime, API errors)
- **Weekly:** Engagement metrics (MAU, calculations/day)
- **Monthly:** Business metrics (MRR, churn, NPS)
- **Quarterly:** Strategic metrics (market share, product-market fit)

---

## North Star Metric

### Primary North Star: Monthly Active Brokers (MAB)

**Definition:** Number of broker accounts with ≥1 active end user in the past 30 days

**Why This Metric:**
- ✅ Leading indicator of revenue (active brokers → paying brokers)
- ✅ Measures platform value (brokers only stay active if traders use it)
- ✅ Easy to communicate to investors/board
- ✅ Balances growth and retention

**Target Trajectory:**
| Milestone | Month | MAB Target | Status |
|-----------|-------|------------|--------|
| Pilot Launch | Month 6 | 5 | 📋 Planned |
| Limited Launch | Month 12 | 25 | 📋 Planned |
| Scale Phase | Month 18 | 60 | 📋 Planned |
| Series A | Month 24 | 100 | 📋 Planned |

**Complementary North Star:** Monthly Active Users (MAU) - Total traders using platform across all brokers

---

## Business Metrics (SaaS Fundamentals)

### 1. Revenue Metrics

#### Monthly Recurring Revenue (MRR)
**Formula:** `Sum of all active broker subscriptions`
**Target:** $290K by Month 24 (100 brokers × $2,900 avg)

**Calculation:**
```
MRR = (Standard Tier Brokers × $2,500) +
      (Standard Tier MAU × $0.50) +
      (Professional Tier Brokers × $5,000) +
      (Professional Tier MAU × $0.40) +
      (Enterprise Custom Contracts)
```

**Breakdown by Tier (Month 24 Target):**
| Tier | Brokers | Base MRR | MAU | Usage MRR | Total MRR |
|------|---------|----------|-----|-----------|-----------|
| Standard | 70 | $175K | 56,000 | $28K | $203K |
| Professional | 25 | $125K | 20,000 | $8K | $133K |
| Enterprise | 5 | $50K | 4,000 | $1.2K | $51.2K |
| **Total** | **100** | **$350K** | **80,000** | **$37.2K** | **$387.2K** |

**MRR Growth Rate (Month-over-Month):**
- Pilot Phase (Months 1-6): N/A (no revenue)
- Launch Phase (Months 7-12): 15-25% MoM
- Scale Phase (Months 13-24): 8-12% MoM

#### Annual Recurring Revenue (ARR)
**Formula:** `MRR × 12`
**Target:**
- Month 12: $870K ARR
- Month 24: $4.6M ARR

#### Net Revenue Retention (NRR)
**Formula:** `(Starting MRR + Expansion - Churn) / Starting MRR × 100`
**Target:** 110% (10% expansion from existing brokers offsets churn)

**Expansion Sources:**
- Broker upgrades from Standard → Professional tier
- Broker client base growth (more MAU = more usage fees)
- Upsells (mobile SDK, custom integrations)

**Example Calculation (Month 18):**
```
Starting MRR (Month 17): $180K
Expansion (3 brokers upgraded): +$7.5K
Churn (1 broker left): -$2.9K
Ending MRR (Month 18): $184.6K
NRR = ($184.6K / $180K) × 100 = 102.6%
```

#### Customer Lifetime Value (LTV)
**Formula:** `Avg MRR per Broker × Gross Margin × (1 / Monthly Churn Rate)`
**Target:** $60,000 (24-month avg retention)

**Calculation:**
```
Avg MRR per Broker: $2,900
Gross Margin: 85%
Monthly Churn Rate: 3% (36-month retention)
LTV = $2,900 × 0.85 × (1 / 0.03) = $82,150

Conservative Estimate (24-month retention):
LTV = $2,900 × 0.85 × 24 = $59,160
```

### 2. Customer Acquisition Metrics

#### Customer Acquisition Cost (CAC)
**Formula:** `(Sales + Marketing Spend) / New Brokers Acquired`
**Target:** $8,000 per broker (LTV:CAC = 7.5:1)

**Breakdown by Channel:**
| Channel | Spend/Month | Brokers Acquired | CAC |
|---------|-------------|------------------|-----|
| Industry Events (iFX EXPO) | $10K | 2 | $5,000 |
| LinkedIn Ads | $5K | 0.5 | $10,000 |
| Referrals | $0 | 1 | $0 |
| Inbound (SEO/Content) | $3K | 0.5 | $6,000 |
| **Total** | **$18K** | **4** | **$4,500** |

**CAC Payback Period:**
**Formula:** `CAC / (MRR × Gross Margin)`
**Target:** 8 months
```
$8,000 / ($2,900 × 0.85) = 3.2 months ✅ (Excellent)
```

#### LTV:CAC Ratio
**Formula:** `LTV / CAC`
**Target:** 7.5:1 (healthy SaaS benchmark: 3:1)
```
$60,000 / $8,000 = 7.5 ✅
```

### 3. Churn & Retention Metrics

#### Monthly Broker Churn Rate
**Formula:** `Brokers Lost in Month / Total Brokers at Start of Month × 100`
**Target:** <3% monthly (80%+ annual retention)

**Churn Reasons (Tracked via Exit Surveys):**
- Broker went out of business (market consolidation)
- Insufficient ROI (didn't reduce churn as expected)
- Budget cuts (market downturn)
- Switched to in-house solution
- Acquired by larger broker (merged platforms)

**Churn Mitigation Tactics:**
- Quarterly Business Reviews (QBRs) with at-risk brokers
- Success coaching (optimize usage, share best practices)
- Feature requests (prioritize high-value broker needs)
- Price adjustments (offer discounts for annual contracts)

#### Annual Broker Retention Rate
**Formula:** `(Brokers at End of Year / Brokers at Start of Year) × 100`
**Target:** 80%+

**Cohort Retention Analysis:**
| Cohort | Month 3 | Month 6 | Month 12 | Month 24 |
|--------|---------|---------|----------|----------|
| Pilot (Month 6) | 100% | 100% | 90% | 80% |
| Q3 2025 (Month 9) | 100% | 95% | 85% | - |
| Q4 2025 (Month 12) | 95% | 90% | - | - |

### 4. Gross Margin
**Formula:** `(Revenue - COGS) / Revenue × 100`
**Target:** 85% (SaaS benchmark: 70-80%)

**COGS Breakdown (Month 24):**
| Cost Category | Monthly Cost | % of Revenue |
|---------------|--------------|--------------|
| Infrastructure (AWS) | $8,000 | 2% |
| Market Data (IEX, Polygon) | $5,000 | 1.3% |
| Third-Party SaaS (Auth0, Stripe) | $3,000 | 0.8% |
| Customer Support (dedicated CSM) | $15,000 | 3.9% |
| **Total COGS** | **$31,000** | **8%** |
| **Gross Margin** | | **92%** ✅ |

**Note:** Target 85% to be conservative (actual may be higher)

---

## Product Engagement Metrics

### 1. User Activation Metrics

#### New Broker Onboarding Time
**Definition:** Time from signup to first calculation performed by broker's end user
**Target:** <7 days (ideal: <2 days)

**Onboarding Funnel:**
| Step | % Complete | Time to Next Step |
|------|------------|-------------------|
| Broker signs up | 100% | - |
| Completes branding config | 90% | 1 day |
| Publishes to custom domain | 80% | 2 days |
| First end user visits | 60% | 4 days |
| First calculation performed | 50% | 7 days |

**Optimization:** Reduce drop-off at "First end user visits" (broker promotion issue)

#### Trader Activation Rate
**Definition:** % of broker's clients who use calculator within 30 days of broker launch
**Target:** 40% (benchmark: 30-50% for embedded tools)

**Calculation:**
```
Broker has 2,000 active clients
800 clients use calculator in first 30 days
Activation Rate = 800 / 2,000 = 40% ✅
```

### 2. Engagement Metrics

#### Monthly Active Users (MAU)
**Definition:** Unique end users who perform ≥1 calculation in past 30 days
**Target:** 80,000 by Month 24

**MAU by Broker Size:**
| Broker Size | Avg Clients | Activation % | MAU per Broker |
|-------------|-------------|--------------|----------------|
| Small (500) | 500 | 35% | 175 |
| Medium (2,000) | 2,000 | 40% | 800 |
| Large (5,000) | 5,000 | 45% | 2,250 |

#### Weekly Active Users (WAU)
**Definition:** Unique end users who perform ≥1 calculation in past 7 days
**Target:** 30,000 by Month 24 (WAU/MAU ratio = 37.5%)

#### Daily Active Users (DAU)
**Definition:** Unique end users who perform ≥1 calculation in past 24 hours
**Target:** 12,000 by Month 24 (DAU/MAU ratio = 15%)

**Stickiness Ratio:**
```
DAU/MAU = 12,000 / 80,000 = 15%
Benchmark: 10-20% for utility tools (calculator is not daily use)
```

#### Calculations Per User (CPU)
**Definition:** Avg number of calculations per active user per month
**Target:** 8-12 calculations/month

**Segmentation:**
| User Type | Calculations/Month | % of Users |
|-----------|-------------------|------------|
| Novice traders | 15-20 | 60% |
| Intermediate traders | 8-12 | 30% |
| Advanced traders | 3-5 | 10% |

**Why Novices Calculate More:** Uncertainty drives frequent checks; experts internalize position sizing

### 3. Feature Adoption Metrics

#### Education Module Completion Rate
**Definition:** % of users who complete ≥1 education module
**Target:** 50% (benchmark: 30-40% for optional content)

**Most Popular Modules (by completion rate):**
1. "Leverage Basics" - 45% completion
2. "Position Sizing 101" - 38% completion
3. "Stop Loss Strategies" - 32% completion
4. "Risk/Reward Ratio" - 28% completion
5. "Correlation Analysis" - 15% completion (advanced topic)

#### Advanced Feature Usage
**Definition:** % of users who use advanced calculators (portfolio risk, scenario modeling)
**Target:** 20% (serves intermediate/advanced traders)

**Feature Usage Breakdown:**
| Feature | % of Users | Avg Uses/Month |
|---------|------------|----------------|
| Basic Position Size Calc | 100% | 10 |
| Education Modules | 50% | 2 modules |
| Risk/Reward Scenarios | 30% | 4 |
| Portfolio Risk Calc | 20% | 3 |
| VaR Calculator | 8% | 2 |

#### Mobile vs. Desktop Usage
**Target:** 40% mobile, 60% desktop (traders prefer desktop for serious analysis)

**Current Split:**
- Mobile Web: 35%
- Desktop Web: 60%
- Embeddable Widget: 5%

---

## Customer Success Metrics

### 1. Broker Impact Metrics

#### Client Churn Reduction (Primary Value Metric)
**Definition:** % reduction in broker's 90-day trader churn after deploying platform
**Target:** 20-30% reduction

**Measurement:**
```
Broker baseline churn: 65% (industry avg)
Post-deployment churn: 48%
Reduction: (65% - 48%) / 65% = 26% ✅
```

**Case Study Tracking:**
- Track 5 pilot brokers (control group data from pre-deployment period)
- Quarterly surveys with brokers (self-reported churn reduction)
- Access to broker analytics (if permitted)

#### Support Ticket Reduction
**Definition:** % reduction in broker's risk management support tickets
**Target:** 30% reduction

**Measurement:**
```
Baseline: 600 tickets/month (40% risk-related = 240 tickets)
Post-deployment: 420 tickets/month (25% risk-related = 105 tickets)
Reduction: (240 - 105) / 240 = 56% ✅
```

#### Broker Net Promoter Score (NPS)
**Definition:** "How likely are you to recommend this platform to another broker?" (0-10)
**Target:** ≥50 (industry benchmark: 30-50)

**Calculation:**
```
Promoters (9-10): 60%
Passives (7-8): 30%
Detractors (0-6): 10%
NPS = 60% - 10% = 50 ✅
```

**Survey Cadence:** Quarterly (post-QBR)

### 2. Trader Outcome Metrics

#### Trader Survival Rate (90-Day)
**Definition:** % of new traders still active after 90 days (across all brokers using platform)
**Target:** 50% (vs. industry baseline 30-35%)

**Correlation with Calculator Usage:**
| User Segment | Calc Usage | 90-Day Survival |
|--------------|------------|----------------|
| Never used calculator | 0 | 32% (baseline) |
| Used 1-5 times | Low | 42% |
| Used 6-15 times | Medium | 55% |
| Used 16+ times | High | 68% |

**Insight:** Education correlates with survival (causation requires A/B test)

#### Average Account Balance Growth
**Definition:** % change in trader account balance after 90 days (for surviving traders)
**Target:** +5% (vs. baseline -10% for traders who quit)

**Measurement Challenge:** Brokers may not share account balance data (privacy)
**Proxy Metric:** Self-reported trader satisfaction survey

#### Risk Compliance Rate
**Definition:** % of calculations where trader selected ≤2% account risk
**Target:** 60% (benchmark: healthy risk management)

**Current Distribution:**
- <1% risk: 20%
- 1-2% risk: 40% ✅
- 2-5% risk: 30% ⚠️
- >5% risk: 10% 🔴 (high-risk behavior)

---

## Operational Metrics

### 1. Platform Performance

#### API Response Time (p95)
**Definition:** 95th percentile response time for calculation API
**Target:** <200ms

**Current Performance:**
| Endpoint | p50 | p95 | p99 |
|----------|-----|-----|-----|
| /calculate/position-size | 45ms | 120ms ✅ | 280ms |
| /calculate/portfolio-risk | 120ms | 350ms ⚠️ | 650ms |
| /education/module | 200ms | 450ms ⚠️ | 800ms |

**Action Item:** Optimize portfolio-risk endpoint (database query bottleneck)

#### Platform Uptime
**Definition:** % of time platform is available (excluding planned maintenance)
**Target:** 99.9% (8.76 hours downtime/year)

**Current:** 99.93% (6 hours downtime in past 12 months) ✅

**Incident Tracker:**
| Date | Duration | Root Cause | Impact |
|------|----------|------------|--------|
| Oct 2024 | 2 hours | Database failover | 500 users affected |
| Aug 2024 | 1 hour | AWS region outage | 200 users affected |
| Jun 2024 | 3 hours | Code deployment bug | 1,000 users affected |

#### Error Rate
**Definition:** % of API requests resulting in 5xx errors
**Target:** <0.1%

**Current:** 0.05% ✅

### 2. Data Quality Metrics

#### Calculation Accuracy Rate
**Definition:** % of calculations that pass automated QA checks
**Target:** 99.99% (1 error per 10,000 calculations)

**QA Process:**
- Unit tests (95% code coverage)
- Integration tests (end-to-end scenarios)
- Manual spot checks (100 random calculations/week)

**Known Edge Cases:**
- Exotic currency pairs (low liquidity → wider spreads)
- Extremely high leverage (>500:1) → margin calculation edge cases

#### Audit Trail Completeness
**Definition:** % of calculations with complete compliance metadata (user ID, timestamp, inputs, disclaimers shown)
**Target:** 100% (regulatory requirement)

**Current:** 100% ✅ (enforced at application layer)

---

## Strategic Metrics (Quarterly Review)

### 1. Market Penetration

#### Market Share (Total Addressable Market)
**Definition:** % of retail forex brokers using our platform
**TAM:** 850 brokers globally
**Target:**
- Month 12: 25 / 850 = 2.9%
- Month 24: 100 / 850 = 11.8%

#### Brand Awareness (Broker Survey)
**Definition:** % of brokers who have heard of our platform
**Target:**
- Month 12: 20% awareness
- Month 24: 50% awareness

**Measurement:** Annual survey by Finance Magnates or similar industry publication

### 2. Product-Market Fit Metrics

#### Retention Curve Flattening
**Definition:** Cohort retention curve flattens after 6-12 months (indicates PMF)
**Target:** 80%+ retention at Month 12

**Visual Check:**
```
Retention %
100% ├──┐
     │    ╲
 80% │      ──────────  ← Flattens (good = PMF)
     │
 60% │
     │
 40% │
     │
 20% │
     │
  0% └─────────────────────────
     0   3   6   9  12  18  24 Months
```

#### Organic Growth Rate
**Definition:** % of new brokers acquired through referrals (vs. paid marketing)
**Target:** 30% by Month 24 (indicates strong word-of-mouth)

**Current Breakdown (Month 18):**
- Paid marketing: 60%
- Referrals: 25% ✅
- Inbound (SEO): 15%

### 3. Competitive Metrics

#### Feature Parity Score
**Definition:** % of competitor features we also offer
**Target:** 80% parity with MetaTrader/cTrader calculators

**Comparison:**
| Feature | MT4/MT5 | cTrader | Us | Parity |
|---------|---------|---------|----|----|
| Basic calculator | ✅ | ✅ | ✅ | 100% |
| Multi-currency | ✅ | ✅ | ✅ | 100% |
| Real-time data | ✅ | ✅ | ⚠️ Planned Q3 | 0% |
| Mobile app | ✅ | ✅ | ⚠️ SDK in Q4 | 0% |
| White-label | ⚠️ Full platform | ⚠️ Full platform | ✅ Standalone | **Advantage** |
| Compliance | ❌ | ❌ | ✅ | **Advantage** |

**Overall Parity:** 75% (excluding our unique advantages)

#### Customer Satisfaction vs. Competitors
**Definition:** Broker NPS for our platform vs. MetaTrader/cTrader
**Target:** Higher NPS than MT4/MT5 (industry NPS ~30)

**Current:**
- Our Platform: NPS 50 ✅
- MetaTrader 4/5: NPS 28 (source: Finance Magnates Survey 2023)
- cTrader: NPS 42 (source: Finance Magnates Survey 2023)

---

## Metrics Dashboard (Executive Summary)

### Monthly Board Report (One-Page)

| Metric | Current | Target | Trend | Status |
|--------|---------|--------|-------|--------|
| **Business** |
| MRR | $184K | $200K | ↗️ +12% MoM | 🟡 |
| ARR | $2.2M | $2.4M | ↗️ +8% MoM | 🟡 |
| Broker Churn | 2.5% | <3% | → Stable | 🟢 |
| LTV:CAC | 7.2:1 | 7.5:1 | → Stable | 🟢 |
| **Engagement** |
| MAU | 65,000 | 70,000 | ↗️ +5% MoM | 🟡 |
| Calculations/Day | 18,000 | 20,000 | ↗️ +3% MoM | 🟡 |
| Broker NPS | 52 | ≥50 | ↗️ +2 pts | 🟢 |
| **Customer Success** |
| Broker Churn Reduction | 24% | 20-30% | → Stable | 🟢 |
| Trader 90-Day Survival | 48% | 50% | ↗️ +2% | 🟡 |
| **Operations** |
| API Response (p95) | 185ms | <200ms | → Stable | 🟢 |
| Platform Uptime | 99.94% | 99.9% | → Stable | 🟢 |

**Legend:** 🟢 On track | 🟡 Needs attention | 🔴 At risk

---

## Metrics Instrumentation

### Data Collection Tools
- **Product Analytics:** Mixpanel (user events, funnels, retention)
- **Business Metrics:** Stripe (MRR, churn), ChartMogul (SaaS analytics)
- **Application Monitoring:** Datadog (performance, errors, uptime)
- **Customer Feedback:** Delighted (NPS surveys), Intercom (support tickets)

### Event Tracking Schema
```javascript
// Example event: Calculation performed
{
  "event": "calculation_performed",
  "user_id": "usr_abc123",
  "broker_id": "brk_xyz789",
  "timestamp": "2024-11-07T14:32:00Z",
  "properties": {
    "calculation_type": "position_size",
    "account_balance": 10000,
    "risk_percentage": 2,
    "currency_pair": "EURUSD",
    "result_lot_size": 0.67,
    "device": "mobile_web",
    "session_id": "sess_def456"
  }
}
```

### Automated Reporting
- **Daily:** Slack alert if uptime <99.9% or error rate >0.1%
- **Weekly:** Email to product team (MAU, calculations/day, feature usage)
- **Monthly:** Executive dashboard (revenue, churn, NPS)
- **Quarterly:** Board deck (strategic metrics, cohort analysis)

---

**Document Owner:** Product Analytics / Data Team
**Last Updated:** November 2024
**Review Cycle:** Monthly (adjust targets based on actuals)
