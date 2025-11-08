# User Personas: Forex Risk Calculator Platform

## Persona Overview

This platform serves a **dual customer model**:
1. **Primary Customer:** Forex brokers (B2B) - They pay for the platform
2. **End User:** Retail traders (B2B2C) - They use the platform via brokers

Understanding both personas is critical for product development and marketing.

---

## Primary Customer Personas (Brokers)

### Persona 1: Mid-Tier Broker Owner

**Name:** Michael Rodriguez
**Role:** CEO / Founder, Apex Forex Trading
**Company Size:** 2,500 active clients, $18M annual revenue
**Location:** London, UK
**Age:** 42

#### Background
- **Industry Experience:** 15 years in forex (former trader → IB → launched broker in 2018)
- **Education:** BSc Economics, CFA Level II
- **Technical Savvy:** Moderate (uses trading platforms, basic Excel, relies on CTO for deep tech)
- **Team:** 25 employees (sales, support, compliance, operations, tech)

#### Goals & Motivations
1. **Reduce Client Churn**
   - Current 90-day retention: 35% (industry avg: 30-40%)
   - Target: 50% retention (top-quartile brokers)
   - Why: Client acquisition costs $600 per client (Google Ads, affiliate fees)

2. **Differentiate from Competitors**
   - Market saturated with 850+ retail brokers
   - Competing on spreads = race to bottom (5% margins)
   - Needs value-added service to justify premium positioning

3. **Regulatory Compliance**
   - FCA (UK) requires demonstrable client education
   - Annual compliance audit costs £80K
   - Risk of £500K+ fines for inadequate risk disclosure

4. **Scalable Client Education**
   - 40% of support tickets are "How much should I risk?" questions
   - Support team (5 people) overwhelmed during market volatility
   - Needs self-service tool to reduce support burden

#### Pain Points
- **High churn:** "We spend £350K/year acquiring clients, then 65% quit in 3 months because they blow their accounts. It's a leaky bucket."
- **Compliance burden:** "Our compliance officer spends 20 hours/week manually documenting risk disclosures. We need automation."
- **Commoditization:** "We're just another MT4 broker with tight spreads. Traders see us as interchangeable. How do we stand out?"
- **Scale limitations:** "We can't afford a dedicated educator for every new client. We need a tool that educates at scale."

#### Buying Behavior
- **Decision Criteria:**
  1. Proven ROI (will it reduce churn by 20%?)
  2. Easy integration (can't disrupt existing MT4 setup)
  3. White-label (must look like our brand, not a third-party tool)
  4. Compliance proof (audit trail for FCA inspections)

- **Budget:** £2K-£5K/month for client retention tools
- **Decision Timeline:** 3-6 months (pilot → full deployment)
- **Stakeholders Involved:** CEO (final approval), CTO (technical eval), Compliance Officer (regulatory sign-off), Head of Retention (user testing)

#### Use Cases
1. **Onboarding New Clients:** New trader completes risk education module + uses calculator before first trade (compliance requirement met)
2. **Reducing Support Tickets:** Embed calculator widget on broker website + MT4 terminal (self-service risk questions)
3. **Compliance Reporting:** Export quarterly report showing all risk warnings delivered to clients (FCA audit evidence)
4. **Marketing Differentiation:** Promote "Apex Risk Academy" in Google Ads and affiliate materials (competitive advantage)

#### Success Metrics
- 20% reduction in 90-day churn (from 65% to 52%)
- 30% reduction in support tickets (from 600/mo to 420/mo)
- Zero FCA compliance findings in annual audit
- 10% increase in client acquisition (due to differentiation)

#### Quote
> "I don't need another trading platform. I need a tool that keeps my clients alive long enough to become profitable. That's what grows my business."

---

### Persona 2: Broker Compliance Officer

**Name:** Sarah Chen
**Role:** Head of Compliance, Global Markets FX
**Company Size:** 8,500 active clients, $45M annual revenue
**Location:** Sydney, Australia
**Age:** 38

#### Background
- **Industry Experience:** 12 years in financial services compliance (banking → broker compliance)
- **Education:** LLB (Law), Grad Dip in Applied Finance, FINSIA certified
- **Technical Savvy:** High (comfortable with databases, audit tools, RegTech platforms)
- **Team:** 4 compliance analysts

#### Goals & Motivations
1. **Regulatory Compliance**
   - ASIC (Australian regulator) requires strict risk disclosure
   - Must prove clients understand leverage and margin before trading
   - Needs audit trail for all risk warnings

2. **Risk Mitigation**
   - Prevent regulatory penalties (ASIC fines: AUD $500K-$5M)
   - Reduce risk of client complaints (AFCA disputes)
   - Maintain broker's reputation

3. **Operational Efficiency**
   - Currently: Manual review of client onboarding docs (20 hours/week)
   - Target: Automated risk disclosure with zero manual review
   - Free up time for higher-value compliance work (AML investigations)

#### Pain Points
- **Manual processes:** "I spend half my week reviewing PDFs of risk disclosures that clients allegedly read. I have no proof they understood it."
- **Regulatory changes:** "ASIC changed leverage limits twice this year. We had to update 50+ documents and retrain support staff. It's chaos."
- **Audit anxiety:** "During our last ASIC audit, we couldn't produce evidence that 300+ clients saw our risk warnings. We got a warning letter."
- **Lack of data:** "I can't tell you which clients are high-risk because we don't track their risk behavior systematically."

#### Buying Behavior
- **Decision Criteria:**
  1. Regulatory alignment (must meet ASIC/FCA/NFA requirements)
  2. Audit trail (tamper-proof logs with timestamps)
  3. Flexibility (easy to update disclaimers when regulations change)
  4. Reporting (one-click export of compliance evidence)

- **Budget:** Not the budget holder (CEO decides), but strong influencer
- **Decision Timeline:** 6-12 months (RFP process for RegTech tools)
- **Stakeholders Involved:** Compliance team (requirements gathering), Legal (contract review), IT (security assessment), CEO (budget approval)

#### Use Cases
1. **Automated Risk Disclosure:** New client must complete risk calculator + education module before account activation (logged in database)
2. **Regulatory Reporting:** Generate quarterly report for ASIC showing % of clients who completed risk education (regulatory KPI)
3. **Risk Monitoring:** Dashboard showing clients who consistently over-leverage (trigger manual review)
4. **Audit Response:** Export all risk warnings shown to specific client during AFCA dispute (legal defense)

#### Success Metrics
- 100% of new clients complete risk education (vs. 70% currently)
- Zero ASIC audit findings related to risk disclosure
- 50% reduction in time spent on manual compliance reviews
- 90% reduction in client complaint escalations (AFCA)

#### Quote
> "I need a system I can show to ASIC and say, 'Here's timestamped proof that every single client saw a risk warning and understood it before trading.' That's my job security."

---

### Persona 3: Prop Trading Firm Risk Manager

**Name:** David Kim
**Role:** Chief Risk Officer, Velocity Capital (Prop Firm)
**Company Size:** 400 funded traders, $25M AUM
**Location:** Chicago, USA
**Age:** 45

#### Background
- **Industry Experience:** 20 years (trader → risk manager at hedge fund → prop firm CRO)
- **Education:** MS Financial Engineering, CFA Charter holder
- **Technical Savvy:** Very high (Python, VBA, SQL, quantitative modeling)
- **Team:** 3 risk analysts

#### Goals & Motivations
1. **Protect Capital**
   - Fund traders with $10K-$100K accounts
   - One rogue trader can blow $500K+ in minutes
   - Need automated risk controls to enforce max loss limits

2. **Scale Trader Education**
   - Evaluate 500+ applicants monthly
   - Only 10% pass risk management test
   - Need standardized education to improve pass rate

3. **Data-Driven Decision Making**
   - Track which risk behaviors correlate with profitability
   - Identify high-potential traders early
   - Optimize capital allocation

#### Pain Points
- **Manual monitoring:** "We have 400 traders. I can't watch every position in real-time. I need automated alerts when someone violates risk rules."
- **Inconsistent education:** "Every trader interprets our risk rules differently. Some think '2% max risk' means per trade, others think per day. We need clarity."
- **High failure rate:** "70% of funded traders fail within 6 months. It's expensive to fund and monitor them. We need better risk education upfront."
- **Lack of benchmarks:** "I don't know if our traders are taking appropriate risk compared to industry standards. We're flying blind."

#### Buying Behavior
- **Decision Criteria:**
  1. Customization (must support our proprietary risk rules: max 2% per trade, max 6% daily drawdown, max 10 positions)
  2. API integration (pull real-time position data from our trading platform)
  3. Alerting (real-time notifications when trader violates rules)
  4. Analytics (dashboard showing risk behavior by trader cohort)

- **Budget:** $10K-$25K one-time setup + $5K/month ongoing
- **Decision Timeline:** 2-3 months (faster than brokers; less bureaucracy)
- **Stakeholders Involved:** CRO (decision maker), CTO (technical eval), CEO (budget approval)

#### Use Cases
1. **Trader Evaluation:** Applicants complete risk education + quiz before funded account approval (filter out high-risk applicants)
2. **Automated Risk Enforcement:** API integration with trading platform → automatically close positions if trader exceeds 2% risk rule
3. **Performance Analytics:** Dashboard showing correlation between risk behavior and profitability (optimize funding decisions)
4. **Trader Coaching:** Identify traders who struggle with risk management → assign targeted education modules

#### Success Metrics
- 30% improvement in funded trader pass rate (from 30% to 40%)
- 50% reduction in risk rule violations (automated enforcement)
- 20% reduction in capital drawdown (better risk management)
- $200K+ annual savings (fewer blown accounts)

#### Quote
> "I'll pay good money for a system that prevents my traders from blowing up their accounts. Risk management is my entire business model."

---

## End User Personas (Traders)

### Persona 4: Novice Forex Trader

**Name:** Jessica Martinez
**Role:** Marketing Manager (day job), Aspiring Forex Trader (side hustle)
**Age:** 29
**Location:** Miami, USA
**Trading Experience:** 3 months

#### Background
- **Income:** $75K/year salary
- **Trading Capital:** $2,500 (started with $1K, deposited $1.5K more after initial losses)
- **Education:** BA Marketing, no finance background
- **Trading Knowledge:** Learned from YouTube videos and broker webinars
- **Platform:** MetaTrader 4 (broker default)

#### Goals & Motivations
1. **Supplement Income**
   - Target: $500-$1,000/month extra income
   - Long-term: Quit day job and trade full-time (aspirational)

2. **Learn Proper Trading**
   - Wants to "do it right" (not gamble)
   - Intimidated by technical jargon
   - Needs simple, actionable education

3. **Avoid Losing Account**
   - Already lost $800 in first 2 months (32% drawdown)
   - Scared to deposit more money
   - Doesn't understand why she's losing

#### Pain Points
- **Information overload:** "Every YouTube video says something different. I don't know who to trust."
- **Overtrading:** "I make 10-15 trades per day because I get bored. I think that's why I'm losing."
- **Poor risk management:** "I didn't know what a stop loss was until I blew my account. I just picked random lot sizes."
- **Emotional trading:** "When I'm down $200, I double my position size to 'win it back.' It usually makes things worse."

#### Behavior & Needs
- **Learning Style:** Visual learner, prefers videos and interactive tools over text
- **Time Commitment:** 1-2 hours/day (evenings after work, weekends)
- **Mobile vs Desktop:** 60% mobile (checks positions during lunch break), 40% desktop (evenings)
- **Trust Signals:** Testimonials, certifications, broker endorsement

#### Use Cases
1. **Pre-Trade Risk Check:** Before entering trade, uses calculator to see max loss → decides if she's comfortable with that amount
2. **Position Sizing:** Inputs 2% risk rule (learned from education module) → calculator tells her exact lot size
3. **Education:** Watches 5-minute video on "Why stop losses matter" → takes quiz → earns "Risk Management Basics" badge
4. **Confidence Building:** Sees that "Profitable traders risk 1-2% per trade" → feels validated in her approach

#### Success Metrics (From Broker's Perspective)
- Completes risk education module (compliance metric)
- Uses calculator 3+ times/week (engagement metric)
- 90-day survival rate improves from 35% to 50%
- Deposits additional funds after 6 months (LTV increase)

#### Quote
> "I just want someone to tell me exactly how much to risk. All the YouTube videos say 'risk 1-2%' but they don't show me how to calculate that."

---

### Persona 5: Experienced Trader (Intermediate)

**Name:** Robert Thompson
**Role:** Software Engineer (day job), Part-Time Forex Trader
**Age:** 34
**Location:** Toronto, Canada
**Trading Experience:** 4 years

#### Background
- **Income:** $120K/year salary
- **Trading Capital:** $25,000 (built from initial $5K deposit over 3 years)
- **Education:** BS Computer Science
- **Trading Knowledge:** Self-taught (books: "Trading in the Zone," "Market Wizards"; online courses)
- **Platform:** cTrader (prefers algo trading features)

#### Goals & Motivations
1. **Consistent Profitability**
   - Currently: Break-even over 4 years (some winning months, some losing months)
   - Target: 10-15% annual return (realistic goal)

2. **Systematic Trading**
   - Moving away from discretionary trading → algorithmic strategies
   - Wants data-driven risk management (not gut feel)

3. **Portfolio Diversification**
   - Trades 5-6 currency pairs simultaneously
   - Needs portfolio-level risk management (correlation analysis)

#### Pain Points
- **Correlation risk:** "I thought I was diversified trading EUR/USD, GBP/USD, and AUD/USD, but they all moved in the same direction. I lost 8% in one day."
- **Scaling challenges:** "When I increase my account size, I struggle with position sizing. 2% of $5K is easy, but 2% of $25K with multiple positions is complex."
- **Lack of tools:** "MT4/cTrader have basic calculators, but they don't show me portfolio-wide risk or optimal position sizing across multiple trades."
- **Overconfidence:** "I had a winning streak and increased my risk to 5% per trade. Then I had a losing streak and lost 3 years of gains in 2 months."

#### Behavior & Needs
- **Learning Style:** Analytical, prefers data/charts over anecdotes
- **Time Commitment:** 10-15 hours/week (evenings + weekends)
- **Mobile vs Desktop:** 90% desktop (serious analysis), 10% mobile (monitoring)
- **Tech Affinity:** Comfortable with APIs, scripting, advanced tools

#### Use Cases
1. **Portfolio Risk Analysis:** Inputs all 6 open positions → calculator shows correlation-adjusted total risk (12% not 2% × 6)
2. **Algorithmic Integration:** Uses API to automatically calculate position size before algo places trade
3. **Scenario Modeling:** "What if EUR/USD drops 2% and GBP/USD drops 1.5% simultaneously?" → calculator shows projected loss
4. **Optimization:** "What's the optimal position size for 15% annual return with max 20% drawdown?" (Kelly Criterion)

#### Success Metrics (From Broker's Perspective)
- High engagement (uses calculator daily)
- Long-term retention (4+ years with broker)
- High account value ($25K → target $50K+ in 2 years)
- Referral potential (tells other traders about tool)

#### Quote
> "I don't need a basic calculator. I need a tool that understands correlation, portfolio risk, and can integrate with my algo trading system."

---

### Persona 6: Professional Trader (Prop Firm)

**Name:** Alex Okafor
**Role:** Full-Time Prop Trader, Velocity Capital
**Age:** 27
**Location:** Lagos, Nigeria → Remote
**Trading Experience:** 6 years

#### Background
- **Income:** $0 salary (100% profit-share: keeps 80% of profits after hitting $10K target)
- **Trading Capital:** $50,000 funded account (prop firm capital, not his own money)
- **Education:** BS Finance
- **Trading Knowledge:** Professional (mentored by senior trader, passed prop firm evaluation)
- **Platform:** cTrader + custom Python scripts

#### Goals & Motivations
1. **Maximize Profit Share**
   - Monthly target: $10K profit → keeps $8K (80% split)
   - Stretch goal: $20K profit → $16K take-home

2. **Avoid Account Termination**
   - Firm rules: Max 2% risk per trade, max 6% daily drawdown, max 10% monthly drawdown
   - Violation = account termination (lose funding)

3. **Build Track Record**
   - Long-term: Launch own hedge fund or become fund manager
   - Needs consistent performance metrics to show investors

#### Pain Points
- **Strict risk limits:** "I have great trade ideas, but the firm's risk rules force me to take smaller positions than I'd like. I need to optimize within constraints."
- **Monitoring burden:** "I trade London and NY sessions (12 hours/day). I can't manually track my daily drawdown in real-time. I need automated alerts."
- **Opportunity cost:** "I waste 30 minutes/day calculating position sizes manually. That's time I could spend analyzing markets."
- **Performance pressure:** "If I violate risk rules twice, I'm out. I can't afford mistakes. I need a system that prevents me from fucking up."

#### Behavior & Needs
- **Learning Style:** Experiential (learns by doing, iterates quickly)
- **Time Commitment:** 60-80 hours/week (full-time professional)
- **Mobile vs Desktop:** 95% desktop (trading desk setup), 5% mobile (emergency monitoring)
- **Precision Requirements:** Needs exact calculations (no rounding errors)

#### Use Cases
1. **Real-Time Risk Monitoring:** Dashboard shows current daily drawdown (4.2% of 6% max) → green/yellow/red alerts
2. **Automated Enforcement:** API integration with cTrader → prevents opening position if it would violate 2% rule
3. **Performance Attribution:** "How much of my profit came from EUR/USD vs GBP/JPY?" → optimize strategy allocation
4. **Compliance Proof:** Export monthly report showing zero risk rule violations → submit to prop firm for performance review

#### Success Metrics (From Prop Firm's Perspective)
- Zero risk rule violations (automated compliance)
- Consistent profitability (12-month track record)
- High profit factor (gross profit / gross loss >1.5)
- Referral potential (tells other prop traders about firm)

#### Quote
> "Risk management isn't optional for me. It's the difference between a $100K/year income and being unemployed. I need automation I can trust."

---

## Persona Prioritization

### Primary Target (MVP Phase)
1. **Mid-Tier Broker Owner (Michael)** - Decision maker, budget holder, clear ROI case
2. **Novice Trader (Jessica)** - Largest user segment (60% of broker clients), biggest churn problem

### Secondary Target (Post-MVP)
3. **Compliance Officer (Sarah)** - Strong influencer, regulatory compliance = must-have feature
4. **Experienced Trader (Robert)** - Power users, drive engagement metrics

### Tertiary Target (Phase 3 Expansion)
5. **Prop Firm Risk Manager (David)** - Different sales motion, but high ACV ($50K+)
6. **Professional Trader (Alex)** - End user of prop firm product, informs feature requirements

---

## Persona-Driven Feature Mapping

| Feature | Michael (Broker) | Sarah (Compliance) | Jessica (Novice) | Robert (Intermediate) | David (Prop Firm) |
|---------|-----------------|-------------------|------------------|----------------------|------------------|
| White-label branding | ✅ Critical | ⚠️ Nice-to-have | ❌ Doesn't care | ❌ Doesn't care | ✅ Critical |
| Education modules | ✅ High value | ✅ High value | ✅ Critical | ⚠️ Nice-to-have | ✅ High value |
| Audit trail | ⚠️ Important | ✅ Critical | ❌ Doesn't know | ❌ Doesn't care | ✅ High value |
| Portfolio risk calc | ❌ Low priority | ❌ Low priority | ❌ Too advanced | ✅ Critical | ✅ High value |
| Mobile app | ⚠️ Important | ❌ Low priority | ✅ High value | ⚠️ Nice-to-have | ⚠️ Important |
| API integration | ⚠️ Important | ⚠️ Important | ❌ Doesn't know | ✅ High value | ✅ Critical |
| Real-time alerts | ❌ Low priority | ⚠️ Important | ⚠️ Nice-to-have | ⚠️ Nice-to-have | ✅ Critical |

**MVP Focus (Bolded):**
- **White-label branding** (Michael, David)
- **Education modules** (Michael, Sarah, Jessica, David)
- **Audit trail** (Sarah, David)
- **Basic calculator** (All personas)

---

## Using Personas in Product Development

### User Story Template
```
As [persona name/role],
I want to [action],
So that I can [benefit].

Acceptance Criteria:
- [Testable requirement 1]
- [Testable requirement 2]

Priority: [High/Medium/Low based on persona prioritization]
```

### Example User Stories

**For Michael (Broker Owner):**
> As Michael (broker owner), I want to deploy a white-labeled risk calculator on my domain (risk.apexforex.com) with my logo and colors, so that I can differentiate my brand and reduce client churn without sending traffic to a third-party site.
>
> Acceptance Criteria:
> - Custom domain (CNAME setup)
> - Logo upload (SVG/PNG, max 200KB)
> - Primary/secondary color picker
> - Preview mode before publishing
>
> Priority: **High** (Core value proposition for brokers)

**For Jessica (Novice Trader):**
> As Jessica (novice trader), I want to see a visual warning if my position size is too large for my account, so that I don't accidentally blow up my account like I did last month.
>
> Acceptance Criteria:
> - Red warning if risk >5% of account
> - Yellow warning if risk 2-5%
> - Green confirmation if risk <2%
> - Plain-English explanation ("This trade risks $125, which is 5% of your $2,500 account. Most profitable traders risk 1-2%.")
>
> Priority: **High** (Prevents churn, improves trader outcomes)

---

**Document Owner:** Product Management
**Last Updated:** November 2024
**Next Review:** Post-pilot (Q2 2025) - Update with real user feedback
