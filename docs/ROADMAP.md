# Product Roadmap: Forex Risk Calculator Platform

## Roadmap Overview

**Vision:** Evolve from standalone risk calculator to comprehensive **broker enablement platform** with compliance, education, and analytics capabilities.

**Timeline:** 24-month roadmap with quarterly releases
**Methodology:** Agile development with 2-week sprints

---

## Phase 1: MVP & Pilot Program (Months 1-6)

### Q1 2025: Core Platform Development

**Theme:** Build foundational risk calculator with white-label capability

#### Sprint 1-2: Calculation Engine
**Status:** ✅ Completed
- [x] Position sizing calculator (fixed % risk, fixed $ risk)
- [x] Multi-currency support (USD, EUR, GBP base accounts)
- [x] Major forex pairs (28 pairs: EUR/USD, GBP/USD, USD/JPY, etc.)
- [x] Pip value calculations with proper decimal handling
- [x] Margin requirement calculations (configurable leverage)

**Technical Deliverables:**
- Python calculation library with 95%+ test coverage
- REST API with <100ms response time
- Input validation and error handling

#### Sprint 3-4: White-Label Frontend
**Status:** 🔄 In Progress
- [x] Responsive React app with mobile-first design
- [x] Dynamic theming system (CSS variables)
- [ ] Multi-language support (EN, ES, DE, FR, ZH)
- [ ] Embeddable widget (iframe + postMessage API)
- [ ] Accessibility compliance (WCAG 2.1 AA)

**User Stories:**
- As a **broker**, I can customize primary/secondary colors and upload my logo
- As a **broker**, I can deploy the calculator on my custom domain (risk.mybroker.com)
- As a **trader**, I can use the calculator on mobile without installing an app

#### Sprint 5-6: Broker Admin Dashboard
**Status:** 📋 Planned
- [ ] Broker registration and onboarding flow
- [ ] Configuration panel (branding, leverage limits, feature flags)
- [ ] Basic usage analytics (calculations per day, unique users)
- [ ] User management (invite broker staff, role assignment)
- [ ] API key generation and management

**Success Metrics:**
- 5 pilot brokers onboarded
- <2 hours broker setup time (from signup to live calculator)
- 90% configuration accuracy (no support tickets for theming issues)

### Q2 2025: Pilot Launch & Iteration

**Theme:** Deploy with pilot brokers and gather feedback

#### Sprint 7-8: Educational Content Integration
- [ ] Interactive tutorials (leverage basics, risk management rules)
- [ ] Contextual tooltips and help text
- [ ] Video library integration (YouTube embed)
- [ ] Progress tracking (user completes risk education modules)

**Content Strategy:**
- 10 core lessons (5-10 minutes each)
- Topics: Leverage, pip values, position sizing, correlation, drawdown management
- Gamification: Badges for completing lessons

#### Sprint 9-10: Compliance & Audit Trail
- [ ] Automatic logging of all risk warnings shown to users
- [ ] Compliance report generation (PDF export for regulators)
- [ ] Configurable risk disclaimers per jurisdiction (ESMA, NFA, ASIC)
- [ ] User acknowledgment tracking (checkbox + timestamp)

**Regulatory Requirements:**
- ESMA: Leverage limits (30:1 majors, 20:1 minors, 10:1 exotics)
- NFA: Risk disclosure on every calculation
- ASIC: Position size warnings for >2% account risk

#### Sprint 11-12: Pilot Optimization
- [ ] Performance optimization (target <50ms calc response)
- [ ] Bug fixes from pilot broker feedback
- [ ] Mobile app optimization (PWA install prompt)
- [ ] Analytics dashboard enhancements (churn correlation, engagement heatmaps)

**Pilot Success Criteria:**
- ✅ 20% reduction in 90-day trader churn
- ✅ 40% monthly active usage (% of broker's clients)
- ✅ NPS ≥50 from broker admins
- ✅ 10,000+ calculations performed

**Go/No-Go Decision:** End of Q2 - Proceed to limited launch if 3+ of 4 criteria met

---

## Phase 2: Limited Launch & Growth (Months 7-12)

### Q3 2025: Productionization & Scale

**Theme:** Prepare platform for 25+ paying brokers

#### Sprint 13-14: Real-Time Market Data Integration
- [ ] IEX Cloud API integration for live forex quotes
- [ ] Polygon.io backup data feed
- [ ] Automatic spread/slippage adjustments in calculations
- [ ] Volatility-based position sizing (ATR indicators)

**Value Proposition:**
- Calculations reflect **real market conditions**, not static assumptions
- Traders see accurate margin requirements based on current spreads
- Dynamic risk warnings during high volatility (NFP, FOMC events)

**Technical Requirements:**
- WebSocket connections for real-time price updates
- Fallback to broker-provided data if external API down
- Cost optimization: Cache quotes for 5 seconds, shared across users

#### Sprint 15-16: Advanced Risk Scenarios
- [ ] Multi-leg position analysis (hedging strategies)
- [ ] Portfolio risk calculator (correlation-adjusted)
- [ ] Drawdown simulator (Monte Carlo scenarios)
- [ ] Risk/reward optimizer (optimal SL/TP placement)

**Target Users:**
- Intermediate/advanced traders (20% of user base)
- Prop firm traders with multi-pair strategies
- Brokers targeting institutional clients

#### Sprint 17-18: Billing & Payment System
- [ ] Stripe integration for subscription billing
- [ ] Tiered pricing model (Standard, Professional, Enterprise)
- [ ] Usage-based billing ($0.50 per MAU)
- [ ] Invoicing and payment history for brokers

**Pricing Tiers:**
| Tier | Base Fee | MAU Fee | Max Users | Features |
|------|----------|---------|-----------|----------|
| Standard | $2,500/mo | $0.50 | 5,000 | White-label, basic analytics |
| Professional | $5,000/mo | $0.40 | 20,000 | + Real-time data, advanced scenarios |
| Enterprise | Custom | $0.30 | Unlimited | + SSO, custom integrations, SLA |

#### Sprint 19-20: Mobile SDK (React Native)
- [ ] npm package for broker mobile app integration
- [ ] Pre-built UI components (calculator widget, charts)
- [ ] Push notifications (risk alerts, education reminders)
- [ ] Offline mode (cached calculations for common scenarios)

**Distribution:**
- Public npm package: `@forexrisk/mobile-sdk`
- Documentation site with integration guides
- Sample app for broker developers

### Q4 2025: Market Expansion

**Theme:** Acquire 25 paying brokers, expand feature set

#### Sprint 21-22: Broker Platform Integrations
- [ ] MetaTrader 4/5 plugin (display risk calc in MT terminal)
- [ ] cTrader integration (embedded widget)
- [ ] TradingView widget (partner integration)
- [ ] Generic REST API for proprietary platforms

**Integration Benefits:**
- Traders see risk warnings **before** executing trades in their platform
- Automatic position sizing based on current account balance (pulled from broker API)
- Frictionless UX (no separate tool to open)

#### Sprint 23-24: CRM & Marketing Automation
- [ ] Salesforce AppExchange app (broker lead tracking)
- [ ] HubSpot integration (marketing campaign sync)
- [ ] Intercom integration (client support chat)
- [ ] Webhook system for custom integrations

**Use Cases:**
- Broker marks lead as "risk-aware" in Salesforce after completing education
- HubSpot sends automated email series based on calculator usage
- Intercom support team sees user's calculation history during support chat

**Q4 Goals:**
- 25 paying broker clients ($750K ARR)
- 50,000 Monthly Active Users across all brokers
- 2 strategic partnerships (MT4/MT5 plugin distributor, CRM vendor)
- NPS ≥60

---

## Phase 3: Platform Expansion (Months 13-24)

### Q1 2026: Enterprise Features

**Theme:** Target large brokers (10K+ clients) and prop firms

#### Sprint 25-26: SSO & Enterprise Security
- [ ] OAuth 2.0 / OIDC integration (Auth0, Okta)
- [ ] SAML 2.0 for enterprise SSO
- [ ] SCIM for user provisioning
- [ ] SOC 2 Type II compliance audit

**Enterprise Sales Enablement:**
- Security questionnaire responses (standard RFP template)
- Compliance documentation (GDPR, SOC 2, ISO 27001 roadmap)
- SLA guarantees (99.95% uptime, 4-hour support response)

#### Sprint 27-28: Custom Risk Models
- [ ] Broker-defined risk rules (e.g., max 5% total portfolio risk)
- [ ] Algorithmic trading risk limits (max positions per hour, drawdown circuit breakers)
- [ ] Regulatory rule engine (auto-enforce ESMA/NFA limits by jurisdiction)

**Target Customers:**
- Prop firms: Enforce strict risk rules on funded traders
- Large brokers: Differentiate with proprietary risk models
- Institutional brokers: Custom VaR calculations for hedge fund clients

#### Sprint 29-30: AI-Powered Risk Recommendations
- [ ] Machine learning model: Predict optimal position size based on user history
- [ ] Sentiment analysis: Adjust risk based on market news (FinBERT integration)
- [ ] Anomaly detection: Flag unusual risk behavior (potential fraud)

**AI Features:**
- "Traders similar to you risk 1.5% on this pair" (collaborative filtering)
- "Market volatility is 2x normal - consider reducing position size" (real-time alerts)
- "Your win rate on EUR/USD is 65% - you can risk up to 2.5% (Kelly Criterion)"

**Ethical Considerations:**
- Transparent AI explanations (no black box recommendations)
- User opt-in for AI features (privacy-first)
- Regular model audits for bias

### Q2-Q3 2026: Horizontal Expansion

**Theme:** Expand beyond forex to crypto, CFDs, options

#### Sprint 31-36: Multi-Asset Support
- [ ] Crypto risk calculator (BTC, ETH, top 50 coins)
- [ ] CFD risk calculator (indices, commodities, stocks)
- [ ] Options risk calculator (Greeks, probability of profit)
- [ ] Futures position sizing (contract size variations)

**Market Opportunity:**
- Crypto brokers: $5B market (Coinbase, Kraken, Binance)
- CFD brokers: $12B market (Plus500, IG Group, CMC Markets)
- Options platforms: $3B market (Robinhood, tastytrade, TD Ameritrade)

**Go-to-Market:**
- Reposition as "Trading Risk Platform" (not just forex)
- Partner with crypto exchanges for embedded calculator
- White-label for multi-asset brokers (FX + crypto + CFDs)

#### Sprint 37-40: Social Trading Integration
- [ ] Copy trading risk analysis (evaluate signal providers)
- [ ] Portfolio copier risk calculator (allocate % to multiple traders)
- [ ] Social proof features (show avg. risk % of profitable traders)

**Partnerships:**
- eToro: Embed calculator in copy trader selection flow
- ZuluTrade: Risk score for signal providers
- Myfxbook: Integration with autotrade analytics

### Q4 2026: Full Compliance Suite

**Theme:** Evolve into end-to-end broker compliance platform

#### Sprint 41-44: KYC/AML Module
- [ ] Identity verification (Onfido, Jumio integration)
- [ ] PEP screening and sanctions lists (Dow Jones, Refinitiv)
- [ ] Transaction monitoring (unusual deposit/withdrawal patterns)
- [ ] Case management dashboard (compliance officer workflow)

**Value Proposition:**
- Brokers need KYC/AML regardless - bundled with risk education = unique offering
- Compliance data informs risk models (e.g., flag high-risk jurisdictions)
- Single platform for all compliance needs (lower total cost of ownership)

#### Sprint 45-48: Regulatory Reporting Automation
- [ ] FCA reporting (UK transaction reporting)
- [ ] MiFID II compliance (best execution, order records)
- [ ] CFTC reporting (US futures/forex reporting)
- [ ] Automated report generation and submission

**Competitive Moat:**
- No direct competitor offers risk education + compliance + reporting
- Switching costs: Brokers won't rip out compliance system
- Regulatory expertise becomes core differentiator

**End of Year 2 Goals:**
- 100+ broker clients
- $3M ARR
- 150,000 MAU
- Product suite: Risk + Education + Compliance + Reporting
- Series A funding ($3M-$5M raised)

---

## Feature Prioritization Framework

### MoSCoW Method

**Must Have (Core MVP):**
- Position sizing calculator
- White-label branding
- Broker admin dashboard
- Compliance audit trail

**Should Have (Competitive Differentiation):**
- Real-time market data
- Advanced risk scenarios
- Mobile SDK
- Broker platform integrations

**Could Have (Nice to Have):**
- AI-powered recommendations
- Social trading integration
- Multi-asset support

**Won't Have (Future Consideration):**
- Automated trading (trade execution)
- Direct trader signup (B2C model)
- Broker comparison marketplace

### Prioritization Scoring

| Feature | Business Value (1-10) | Dev Effort (1-10) | Priority Score |
|---------|----------------------|------------------|----------------|
| Real-time data | 9 | 6 | 1.5 (9/6) |
| Mobile SDK | 8 | 7 | 1.14 |
| MT4/MT5 integration | 10 | 5 | 2.0 ⭐ |
| AI recommendations | 7 | 9 | 0.78 |
| Multi-asset support | 9 | 8 | 1.13 |
| KYC/AML module | 10 | 10 | 1.0 |

**Decision:** Prioritize MT4/MT5 integration (highest score) for Q3 2025

---

## Success Metrics by Phase

### Phase 1: Pilot (Months 1-6)
- ✅ 5 pilot brokers live
- ✅ 10,000+ calculations
- ✅ 20% churn reduction
- ✅ NPS ≥50

### Phase 2: Launch (Months 7-12)
- ✅ 25 paying brokers
- ✅ $750K ARR
- ✅ 50,000 MAU
- ✅ 2 strategic partnerships

### Phase 3: Scale (Months 13-24)
- ✅ 100+ brokers
- ✅ $3M ARR
- ✅ 150,000 MAU
- ✅ Series A funding closed
- ✅ Top 3 broker tech ranking (Finance Magnates survey)

---

## Risk Mitigation & Contingency Plans

### Technical Risks

**Risk:** MVP development takes longer than 6 months
- **Mitigation:** Hire additional contractor for Q1; cut non-essential features (multi-language support delayed to Q3)
- **Contingency:** Extend pilot program to 9 months; delay limited launch to Q4

**Risk:** Real-time market data costs exceed projections
- **Mitigation:** Negotiate volume discounts with IEX/Polygon; implement aggressive caching (5-sec TTL)
- **Contingency:** Offer tiered pricing (real-time data only in Professional tier)

### Market Risks

**Risk:** Pilot brokers don't see 20% churn reduction
- **Mitigation:** A/B test different educational content; optimize calculator UX based on user feedback
- **Contingency:** Pivot value prop to compliance automation (still valuable even without churn improvement)

**Risk:** Sales cycle longer than projected (pilot to paid conversion)
- **Mitigation:** Offer 3-month free trial; create self-service signup for smaller brokers
- **Contingency:** Extend cash runway with bridge funding; reduce burn rate (smaller team)

---

## Dependencies & Blockers

### External Dependencies
- **Market data providers:** IEX Cloud contract (30-day notice)
- **Broker partnerships:** MT4/MT5 plugin approval (MetaQuotes vetting process ~6 weeks)
- **Compliance audits:** SOC 2 certification (6-12 months with auditor)

### Internal Dependencies
- **Hiring:** Lead engineer hired by end of Month 1 (critical path for MVP)
- **Pilot broker recruitment:** 5 brokers committed by Month 2 (enables parallel dev + feedback)
- **Funding:** Seed round closed by Month 9 (required for team expansion in Phase 2)

---

## Roadmap Review & Updates

**Review Cadence:**
- **Weekly:** Sprint planning and retrospectives (engineering team)
- **Monthly:** Roadmap adjustments based on pilot feedback (product + leadership)
- **Quarterly:** Strategic roadmap review with investors/advisors

**Update Process:**
1. Gather feedback from brokers, users, and team
2. Re-prioritize features using scoring framework
3. Update roadmap document (this file)
4. Communicate changes to stakeholders (email + all-hands meeting)

**Version History:**
- v1.0 (Nov 2024): Initial 24-month roadmap
- v1.1 (Q1 2025): Post-pilot adjustments [Planned]
- v2.0 (Q3 2025): Phase 3 detailed planning [Planned]

---

**Document Owner:** Product Management
**Last Updated:** November 2024
**Next Review:** January 2025 (post-pilot kickoff)
