# Technical Architecture: Forex Risk Calculator Platform

## Architecture Overview

**Design Philosophy:** API-first, multi-tenant SaaS platform with white-label frontend customization and real-time market data integration.

**Key Principles:**
- **Separation of Concerns:** Decouple calculation engine, data layer, and presentation
- **Scalability:** Horizontal scaling for 100K+ concurrent users
- **Multi-Tenancy:** Isolated broker environments with shared infrastructure
- **Security:** Zero-trust architecture, encrypted data at rest and in transit
- **Extensibility:** Plugin architecture for custom risk models and integrations

## System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                          CLIENT LAYER                                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐  │
│  │  White-Label Web │  │  Embeddable      │  │  Mobile SDK      │  │
│  │  App (React)     │  │  Widget          │  │  (React Native)  │  │
│  └──────────────────┘  └──────────────────┘  └──────────────────┘  │
│           │                     │                      │             │
└───────────┼─────────────────────┼──────────────────────┼─────────────┘
            │                     │                      │
            └─────────────────────┴──────────────────────┘
                                  │
                    ┌─────────────▼─────────────┐
                    │   CDN / Edge Network      │
                    │   (CloudFront / Cloudflare)│
                    └─────────────┬─────────────┘
                                  │
┌─────────────────────────────────▼─────────────────────────────────────┐
│                          API GATEWAY LAYER                             │
├───────────────────────────────────────────────────────────────────────┤
│  ┌────────────────────────────────────────────────────────────────┐  │
│  │  API Gateway (Kong / AWS API Gateway)                          │  │
│  │  - Rate limiting (per broker tier)                             │  │
│  │  - Authentication (JWT + API keys)                             │  │
│  │  - Request routing & load balancing                            │  │
│  │  - Metrics collection (latency, throughput)                    │  │
│  └────────────────────────────────────────────────────────────────┘  │
└───────────────────────────────────────────────────────────────────────┘
                                  │
            ┌─────────────────────┼─────────────────────┐
            │                     │                     │
            ▼                     ▼                     ▼
┌───────────────────┐  ┌──────────────────┐  ┌─────────────────────┐
│  Calculation      │  │  Admin API       │  │  Integration API    │
│  Service          │  │  Service         │  │  Service            │
│  (Python/FastAPI) │  │  (Python/FastAPI)│  │  (Node.js/Express)  │
│                   │  │                  │  │                     │
│  - Position sizing│  │  - Broker CRUD   │  │  - Broker platform  │
│  - Risk metrics   │  │  - User mgmt     │  │    webhooks         │
│  - Scenario model │  │  - Analytics     │  │  - Market data      │
│  - PnL projection │  │  - Reporting     │  │    integration      │
└─────────┬─────────┘  └────────┬─────────┘  └──────────┬──────────┘
          │                     │                       │
          └─────────────────────┼───────────────────────┘
                                │
                    ┌───────────▼────────────┐
                    │   Message Queue        │
                    │   (Redis / RabbitMQ)   │
                    │   - Async tasks        │
                    │   - Event streaming    │
                    └───────────┬────────────┘
                                │
┌───────────────────────────────▼─────────────────────────────────────┐
│                          DATA LAYER                                  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐  │
│  │  PostgreSQL      │  │  Redis Cache     │  │  ClickHouse      │  │
│  │  (Primary DB)    │  │  - Session data  │  │  (Analytics DB)  │  │
│  │  - Broker config │  │  - Rate limits   │  │  - Usage metrics │  │
│  │  - User profiles │  │  - Calc results  │  │  - Audit logs    │  │
│  │  - Audit trails  │  │  (TTL 24hr)      │  │  - Time-series   │  │
│  └──────────────────┘  └──────────────────┘  └──────────────────┘  │
│                                                                       │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │  S3-Compatible Storage (MinIO / AWS S3)                       │  │
│  │  - White-label assets (logos, themes)                         │  │
│  │  - Compliance reports (PDF exports)                           │  │
│  │  - Backups and archives                                       │  │
│  └──────────────────────────────────────────────────────────────┘  │
└───────────────────────────────────────────────────────────────────────┘
                                │
                    ┌───────────▼────────────┐
                    │  External Services     │
                    ├────────────────────────┤
                    │  - IEX Cloud (market   │
                    │    data API)           │
                    │  - Polygon.io (forex   │
                    │    quotes)             │
                    │  - Auth0 (SSO for      │
                    │    enterprise brokers) │
                    │  - SendGrid (email)    │
                    │  - Stripe (billing)    │
                    └────────────────────────┘
```

## Component Details

### 1. Client Layer

#### White-Label Web App (React + Vite)
**Purpose:** Customizable frontend for broker-specific deployments

**Tech Stack:**
- React 18 with TypeScript
- Vite for build tooling
- TailwindCSS for styling (dynamic theming)
- React Query for data fetching
- Chart.js for visualizations

**Key Features:**
- Dynamic theming via CSS variables (broker colors, logos)
- Responsive design (mobile-first)
- PWA support for offline calculations (cached formulas)
- Multi-language support (i18n)

**Customization Points:**
```javascript
// Broker configuration injected at runtime
{
  "brokerId": "acme-forex",
  "branding": {
    "primaryColor": "#FF6B35",
    "logoUrl": "https://cdn.acme-forex.com/logo.svg",
    "domain": "risk.acme-forex.com"
  },
  "features": {
    "advancedScenarios": true,
    "correlationAnalysis": false,
    "maxLeverage": 30
  }
}
```

#### Embeddable Widget
**Purpose:** Lightweight calculator for broker website integration

**Implementation:**
```html
<!-- Broker website embeds widget -->
<script src="https://platform.forexrisk.ai/widget.js"></script>
<div id="risk-calculator" data-broker="acme-forex"></div>
```

**Features:**
- Sandboxed iframe for security
- Cross-origin messaging for broker platform integration
- Configurable width/height and theme
- Minimal dependencies (<50KB gzipped)

#### Mobile SDK (React Native)
**Purpose:** Native mobile apps for broker-branded experiences

**Distribution:**
- npm package for broker developers
- Pre-built white-label app templates
- Push notification support for risk alerts

### 2. API Gateway Layer

#### Kong API Gateway
**Purpose:** Centralized routing, authentication, and rate limiting

**Configuration:**
```yaml
services:
  - name: calculation-service
    url: http://calc-service:8000
    routes:
      - name: risk-calc
        paths: [/api/v1/calculate]
    plugins:
      - name: rate-limiting
        config:
          minute: 60  # 60 requests/min per broker
      - name: jwt
        config:
          claims_to_verify: [exp, nbf]
```

**Rate Limiting Strategy:**
| Broker Tier | Requests/Min | Burst Limit | Price Point |
|-------------|--------------|-------------|-------------|
| Free Trial  | 20           | 40          | $0 (30 days)|
| Standard    | 60           | 120         | $2,500/mo   |
| Professional| 200          | 400         | $5,000/mo   |
| Enterprise  | Unlimited    | N/A         | Custom      |

### 3. Application Services

#### Calculation Service (Python + FastAPI)
**Purpose:** Core risk calculation engine

**API Endpoints:**
```python
# POST /api/v1/calculate/position-size
{
  "accountBalance": 10000,
  "riskPercentage": 2,
  "entryPrice": 1.1850,
  "stopLoss": 1.1820,
  "currencyPair": "EURUSD",
  "accountCurrency": "USD"
}

# Response
{
  "positionSize": 6666.67,  # Units to trade
  "lotSize": 0.67,          # Standard lots (100K units)
  "maxLoss": 200.00,        # USD
  "requiredMargin": 395.83, # USD (30:1 leverage)
  "marginPercentage": 3.96,
  "pipValue": 6.67,
  "calculationId": "calc_abc123"
}
```

**Calculation Models:**
1. **Position Sizing**
   - Fixed percentage risk model
   - Fixed dollar risk model
   - Volatility-based sizing (ATR)

2. **Risk Metrics**
   - Maximum drawdown
   - Risk/reward ratio
   - Win rate breakeven
   - Kelly Criterion optimal sizing

3. **Scenario Modeling**
   - Multi-leg position analysis
   - Correlation-adjusted portfolio risk
   - VaR (Value at Risk) calculations

**Performance Requirements:**
- Response time: <100ms (p95)
- Throughput: 1,000 calculations/sec per instance
- Horizontal scaling: Auto-scale on CPU >70%

#### Admin API Service (Python + FastAPI)
**Purpose:** Broker management and analytics

**Key Endpoints:**
```python
# Broker management
GET    /api/v1/brokers/{brokerId}
POST   /api/v1/brokers
PUT    /api/v1/brokers/{brokerId}/config
DELETE /api/v1/brokers/{brokerId}

# User management (broker's clients)
GET    /api/v1/brokers/{brokerId}/users
POST   /api/v1/brokers/{brokerId}/users
GET    /api/v1/users/{userId}/activity

# Analytics
GET    /api/v1/brokers/{brokerId}/analytics/usage
GET    /api/v1/brokers/{brokerId}/analytics/engagement
GET    /api/v1/brokers/{brokerId}/reports/compliance
```

**Role-Based Access Control (RBAC):**
```python
# Roles hierarchy
SUPERADMIN    # Platform owner (us)
BROKER_ADMIN  # Broker primary contact
BROKER_USER   # Broker support staff
END_USER      # Broker's client (trader)
```

#### Integration Service (Node.js + Express)
**Purpose:** External system integrations

**Integrations:**
1. **Broker Platform Webhooks**
   - Account balance updates
   - Trade execution notifications
   - Margin call alerts

2. **Market Data Providers**
   - IEX Cloud: Real-time forex quotes
   - Polygon.io: Historical volatility data
   - Backup: Broker-provided data feeds

3. **CRM Integration**
   - Salesforce: Lead tracking
   - HubSpot: Marketing automation
   - Intercom: Client support

### 4. Data Layer

#### PostgreSQL (Primary Database)
**Schema Design:**

```sql
-- Multi-tenant with broker isolation
CREATE TABLE brokers (
  id UUID PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  domain VARCHAR(255) UNIQUE,
  config JSONB,  -- White-label settings
  tier VARCHAR(50),  -- free, standard, professional, enterprise
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE users (
  id UUID PRIMARY KEY,
  broker_id UUID REFERENCES brokers(id),
  email VARCHAR(255) UNIQUE NOT NULL,
  role VARCHAR(50),
  created_at TIMESTAMP DEFAULT NOW(),
  INDEX idx_broker_users (broker_id)
);

CREATE TABLE calculations (
  id UUID PRIMARY KEY,
  user_id UUID REFERENCES users(id),
  broker_id UUID REFERENCES brokers(id),
  input_params JSONB,
  results JSONB,
  created_at TIMESTAMP DEFAULT NOW(),
  INDEX idx_broker_calc (broker_id, created_at),
  INDEX idx_user_calc (user_id, created_at)
);

-- Audit trail for compliance
CREATE TABLE audit_logs (
  id BIGSERIAL PRIMARY KEY,
  broker_id UUID REFERENCES brokers(id),
  user_id UUID REFERENCES users(id),
  event_type VARCHAR(100),  -- calculation, login, config_change
  event_data JSONB,
  ip_address INET,
  created_at TIMESTAMP DEFAULT NOW(),
  INDEX idx_audit_broker_time (broker_id, created_at)
);
```

**Data Retention:**
- Calculations: 90 days in Redis cache, 2 years in PostgreSQL
- Audit logs: 7 years (regulatory compliance)
- User profiles: Until account deletion + 30 days

#### Redis Cache
**Purpose:** High-performance caching and session management

**Use Cases:**
1. **Session Storage**
   - JWT token blacklist
   - User session data (TTL: 24 hours)

2. **Calculation Cache**
   - Key: `calc:{brokerId}:{inputHash}`
   - TTL: 5 minutes (reduce redundant calculations)

3. **Rate Limiting**
   - Sliding window counters per broker/user

4. **Real-Time Market Data**
   - Latest forex quotes (updated every 1-5 seconds)
   - TTL: 10 seconds

**Configuration:**
```yaml
# Redis cluster for high availability
redis:
  mode: cluster
  nodes:
    - redis-1:6379
    - redis-2:6379
    - redis-3:6379
  password: ${REDIS_PASSWORD}
  maxmemory: 4gb
  maxmemory_policy: allkeys-lru
```

#### ClickHouse (Analytics Database)
**Purpose:** Real-time analytics and time-series data

**Schema:**
```sql
CREATE TABLE usage_metrics (
  timestamp DateTime,
  broker_id UUID,
  user_id UUID,
  event_type String,  -- calculation, login, export
  metadata String,    -- JSON string
  INDEX idx_broker_time (broker_id, timestamp)
) ENGINE = MergeTree()
PARTITION BY toYYYYMM(timestamp)
ORDER BY (broker_id, timestamp);
```

**Analytics Queries:**
```sql
-- Daily active users per broker
SELECT
  broker_id,
  toDate(timestamp) as date,
  uniqExact(user_id) as dau
FROM usage_metrics
WHERE timestamp >= now() - INTERVAL 30 DAY
GROUP BY broker_id, date
ORDER BY date DESC;

-- Most common calculation parameters
SELECT
  JSONExtractString(metadata, 'currencyPair') as pair,
  count() as calculations,
  avg(JSONExtractFloat(metadata, 'riskPercentage')) as avg_risk
FROM usage_metrics
WHERE event_type = 'calculation'
  AND timestamp >= now() - INTERVAL 7 DAY
GROUP BY pair
ORDER BY calculations DESC
LIMIT 10;
```

## Security Architecture

### Authentication & Authorization

**Multi-Layer Security:**
1. **End User Authentication**
   - JWT tokens (15-minute expiry, refresh token rotation)
   - OAuth 2.0 / OIDC for enterprise SSO
   - MFA for broker admin accounts

2. **Broker API Authentication**
   - API keys (SHA-256 hashed, rate limited)
   - Webhook signatures (HMAC-SHA256)

3. **Service-to-Service**
   - mTLS (mutual TLS) between microservices
   - Service mesh (Istio) for zero-trust networking

**Authorization Model:**
```python
# Policy-based access control
{
  "role": "BROKER_ADMIN",
  "permissions": [
    "brokers:read:own",
    "brokers:update:own",
    "users:read:own",
    "users:create:own",
    "analytics:read:own",
    "reports:generate:own"
  ],
  "conditions": {
    "broker_id": "{{jwt.broker_id}}"  # Tenant isolation
  }
}
```

### Data Security

**Encryption:**
- **At Rest:** AES-256 encryption for PostgreSQL (native encryption)
- **In Transit:** TLS 1.3 for all API communication
- **PII Masking:** Email/phone redacted in logs and analytics

**Compliance:**
- **GDPR:** Right to erasure, data portability, consent management
- **SOC 2 Type II:** Annual audit for security controls
- **PCI DSS:** (If processing payments) Tokenization via Stripe

**Data Isolation:**
```sql
-- Row-level security in PostgreSQL
CREATE POLICY broker_isolation ON calculations
  FOR ALL
  USING (broker_id = current_setting('app.current_broker_id')::UUID);

ALTER TABLE calculations ENABLE ROW LEVEL SECURITY;
```

## Scalability & Performance

### Horizontal Scaling Strategy

**Auto-Scaling Configuration:**
```yaml
# Kubernetes HPA (Horizontal Pod Autoscaler)
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: calculation-service
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: calculation-service
  minReplicas: 3
  maxReplicas: 20
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
    - type: Pods
      pods:
        metric:
          name: requests_per_second
        target:
          type: AverageValue
          averageValue: "1000"
```

**Load Testing Results:**
| Concurrent Users | Requests/Sec | Avg Latency | P95 Latency | Error Rate |
|------------------|--------------|-------------|-------------|------------|
| 1,000            | 5,000        | 45ms        | 78ms        | 0%         |
| 10,000           | 50,000       | 62ms        | 120ms       | 0.01%      |
| 50,000           | 200,000      | 180ms       | 450ms       | 0.05%      |
| 100,000          | 350,000      | 320ms       | 780ms       | 0.2%       |

**Bottleneck Analysis:**
- Database connection pool: Increased to 100 connections per instance
- Redis throughput: Sharded across 6 nodes for 600K ops/sec
- Network bandwidth: CDN caching reduces API calls by 40%

### Caching Strategy

**Multi-Level Cache:**
1. **Client-Side (Browser):** Static assets cached for 7 days
2. **CDN Layer:** API responses with `Cache-Control: max-age=60`
3. **Application Cache (Redis):** Calculation results for 5 minutes
4. **Database Query Cache:** PostgreSQL query results for 1 minute

**Cache Invalidation:**
```python
# Invalidate on broker config change
@event_handler('broker.config.updated')
def invalidate_broker_cache(broker_id: UUID):
    redis.delete(f"broker:config:{broker_id}")
    redis.delete(f"calc:{broker_id}:*")  # Wildcard delete
```

## Disaster Recovery & Business Continuity

### Backup Strategy
- **PostgreSQL:** Daily full backups + WAL archiving (point-in-time recovery)
- **Redis:** AOF (Append-Only File) persistence + daily snapshots
- **S3/MinIO:** Cross-region replication (99.999999999% durability)

### High Availability
- **Database:** PostgreSQL with streaming replication (primary + 2 replicas)
- **Redis:** Redis Cluster with 3 masters + 3 replicas
- **Application:** Multi-AZ deployment across 3 availability zones

### Recovery Time Objectives
- **RTO (Recovery Time Objective):** 4 hours for full platform restoration
- **RPO (Recovery Point Objective):** 5 minutes of data loss maximum
- **Uptime SLA:** 99.95% (excludes planned maintenance)

## Monitoring & Observability

### Metrics Collection
**Application Metrics (Prometheus + Grafana):**
- Request rate, error rate, latency (RED metrics)
- Resource utilization (CPU, memory, network)
- Business metrics (calculations/sec, active brokers, MAU)

**Logging (ELK Stack):**
- Centralized logging with Elasticsearch
- Structured JSON logs with correlation IDs
- Log retention: 30 days (hot), 6 months (cold)

**Tracing (Jaeger):**
- Distributed tracing across microservices
- Performance profiling for slow queries
- User journey tracking (calculation flow)

### Alerting
```yaml
# Example Prometheus alert
groups:
  - name: api_health
    rules:
      - alert: HighErrorRate
        expr: rate(http_requests_total{status=~"5.."}[5m]) > 0.05
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "API error rate above 5% for 5 minutes"

      - alert: SlowResponse
        expr: histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m])) > 0.5
        for: 10m
        labels:
          severity: warning
        annotations:
          summary: "95th percentile latency above 500ms"
```

## Deployment Architecture

### CI/CD Pipeline
```yaml
# GitLab CI / GitHub Actions
stages:
  - test
  - build
  - deploy

test:
  script:
    - uv run pytest --cov=app tests/
    - uv run ruff check app/
    - uv run mypy app/

build:
  script:
    - docker build -t platform:$CI_COMMIT_SHA .
    - docker push registry.gitlab.com/forexrisk/platform:$CI_COMMIT_SHA

deploy_staging:
  script:
    - kubectl set image deployment/calc-service calc=platform:$CI_COMMIT_SHA
    - kubectl rollout status deployment/calc-service

deploy_production:
  when: manual
  script:
    - kubectl set image deployment/calc-service calc=platform:$CI_COMMIT_SHA --namespace=production
```

### Infrastructure as Code (Terraform)
```hcl
# AWS EKS cluster for production
resource "aws_eks_cluster" "platform" {
  name     = "forexrisk-production"
  role_arn = aws_iam_role.eks_cluster.arn
  version  = "1.28"

  vpc_config {
    subnet_ids = aws_subnet.private[*].id
    endpoint_private_access = true
    endpoint_public_access  = true
  }
}

resource "aws_eks_node_group" "platform" {
  cluster_name    = aws_eks_cluster.platform.name
  node_group_name = "platform-nodes"
  node_role_arn   = aws_iam_role.eks_nodes.arn
  subnet_ids      = aws_subnet.private[*].id

  scaling_config {
    desired_size = 6
    max_size     = 20
    min_size     = 3
  }

  instance_types = ["c5.2xlarge"]
}
```

---

**Document Owner:** Engineering/Architecture
**Last Updated:** November 2024
**Review Cycle:** Quarterly or on major architectural changes
