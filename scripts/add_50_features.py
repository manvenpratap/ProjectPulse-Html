#!/usr/bin/env python3
import json

features_50 = [
    {"name": "Core Infrastructure", "screens": ["Database Schema", "Core Services", "API Gateway"], "desc": "Fundamental system services and architecture.", "release": "v1.0.0"},
    {"name": "User Management", "screens": ["Cash Accounts", "Security Accounts", "Authentication"], "desc": "User lifecycle and account security.", "release": "v1.0.0"},
    {"name": "Market Intelligence", "screens": ["Portfolio Valuations", "Market Data Feed", "Analytics Dashboard"], "desc": "Data processing and reporting.", "release": "v1.1.0"},
    {"name": "Order Entry & Execution", "screens": ["Order Entry", "Matching Engine", "Trade Confirmation"], "desc": "Trade order creation, routing, and instant validation.", "release": "v1.0.0"},
    {"name": "Portfolio Performance Analytics", "screens": ["Portfolio Overview", "Sunburst Chart", "Legend Details"], "desc": "Visual analytics and asset allocation sunburst breakdown.", "release": "v1.1.0"},
    {"name": "Governance & Compliance", "screens": ["Compliance Audit", "AML Integration", "Sanctions Checker"], "desc": "Regulatory tracking, AML verification workflows, and security auditing.", "release": "v1.1.0"},
    {"name": "Identity & Access Control (IAM)", "screens": ["Profile Edit", "MFA Settings", "Settings Panel"], "desc": "User profile editing, security settings including Multi-Factor Authentication (MFA), and system configurations.", "release": "v1.0.0"},
    {"name": "Realtime Market Data Feed", "screens": ["Ticker Stream", "Level-2 Orderbook", "Depth Chart"], "desc": "High-throughput WebSocket stream for live prices and orderbook depth.", "release": "v1.0.0"},
    {"name": "Risk Exposure & VaR Engine", "screens": ["Value-at-Risk Calculator", "Exposure Limits Panel", "Stress Testing Matrix"], "desc": "Monte Carlo simulation for portfolio risk exposure and regulatory reporting.", "release": "v1.2.0"},
    {"name": "Customer Onboarding & KYC", "screens": ["Document Upload", "ID Verification Portal", "Biometric Check"], "desc": "Automated KYC identity check and document verification pipeline.", "release": "v1.0.0"},
    {"name": "Payment Gateway Integration", "screens": ["Payment Methods", "Checkout Flow", "Transaction History"], "desc": "Multi-currency payment processing and instant settlement gateway.", "release": "v1.0.0"},
    {"name": "Automated Rebalancing Engine", "screens": ["Rebalance Parameters", "Model Portfolios", "Trade Generator"], "desc": "Algorithmic portfolio rebalancing against target asset allocations.", "release": "v1.2.0"},
    {"name": "Notification & Alert Hub", "screens": ["Alert Rule Builder", "Push Notification Channel", "Notification Center"], "desc": "Cross-channel real-time notifications for prices, trades, and system events.", "release": "v1.1.0"},
    {"name": "Corporate Actions & Dividends", "screens": ["Corporate Actions Feed", "Dividend Schedule", "Entitlement Calculator"], "desc": "Automated processing of stock splits, dividends, and corporate action events.", "release": "v1.2.0"},
    {"name": "FX Rates & Currency Conversion", "screens": ["FX Spot Rates", "Cross-Currency Matrix", "Currency Converter"], "desc": "Realtime foreign exchange rate feeds and multi-currency ledger conversions.", "release": "v1.0.0"},
    {"name": "Securities Lending & Borrowing", "screens": ["Borrow Availability", "Lending Rate Desk", "Collateral Manager"], "desc": "Securities lending pool management and collateral margin verification.", "release": "v2.0-Beta"},
    {"name": "Margin & Collateral Management", "screens": ["Margin Requirements", "Collateral Valuation", "Liquidation Monitor"], "desc": "Realtime margin calculation and automated collateral call triggers.", "release": "v1.2.0"},
    {"name": "Algorithmic Order Execution", "screens": ["Algo Strategy Config", "TWAP/VWAP Router", "Execution Analytics"], "desc": "Smart order routing using TWAP, VWAP, and Iceberg algorithmic strategies.", "release": "v2.0-Beta"},
    {"name": "Fixed Income & Bonds Desk", "screens": ["Bond Yield Curve", "Fixed Income Screener", "Duration Calculator"], "desc": "Government and corporate bond pricing, yield curves, and duration analytics.", "release": "v2.0-Beta"},
    {"name": "Derivatives & Options Pricing", "screens": ["Option Chain", "Greeks Calculator", "Implied Volatility Surface"], "desc": "Options pricing, Black-Scholes Greeks analysis, and volatility modeling.", "release": "v2.0-Beta"},
    {"name": "ESG Ratings & Sustainability", "screens": ["ESG Scorecard", "Carbon Footprint Tracker", "Sustainability Index"], "desc": "Environmental, Social, and Governance (ESG) scoring for portfolio assets.", "release": "v2.1.0"},
    {"name": "Crypto & Digital Asset Gateway", "screens": ["Wallet Integration", "Blockchain Explorer", "Staking Dashboard"], "desc": "Custodial crypto wallet integration, staking operations, and token tracking.", "release": "v2.1.0"},
    {"name": "Data Warehouse & BI ETL", "screens": ["Pipeline Monitor", "ETL Job Scheduler", "Data Quality Dashboard"], "desc": "Automated ETL pipelines processing raw telemetry into BI data marts.", "release": "v1.1.0"},
    {"name": "A/B Testing & Experimentation", "screens": ["Experiment Configurator", "Cohort Segmenter", "Conversion Funnel"], "desc": "Feature flag routing and statistical A/B test result evaluation.", "release": "v1.2.0"},
    {"name": "Audit Logging & Forensics", "screens": ["Audit Trail Viewer", "Log Search Engine", "Security Incident Log"], "desc": "Tamper-evident audit logging for all compliance and security interactions.", "release": "v1.0.0"},
    {"name": "Billing & Automated Invoicing", "screens": ["Subscription Plans", "Invoice Generator", "Billing History"], "desc": "Recurring SaaS billing, fee schedules, and automated PDF invoice delivery.", "release": "v1.0.0"},
    {"name": "Omnichannel Customer Support", "screens": ["Support Ticket Queue", "Live Chat Console", "Knowledge Base Index"], "desc": "Helpdesk ticket routing, live chat assistance, and self-serve knowledge base.", "release": "v1.1.0"},
    {"name": "Developer API Portal & SDKs", "screens": ["API Documentation", "Developer Dashboard", "Webhook Configurator"], "desc": "Public API portal, API key generation, webhooks, and client SDK downloads.", "release": "v1.1.0"},
    {"name": "Service Mesh & Traffic Routing", "screens": ["Ingress Controller", "Traffic Splitter", "Circuit Breaker Dashboard"], "desc": "Istio-based service mesh traffic management and dynamic load balancing.", "release": "v1.2.0"},
    {"name": "Secrets Rotator & Key Vault", "screens": ["Key Vault Console", "Secret Rotation Schedule", "Encryption Manager"], "desc": "Automated HSM-backed API key, database credential, and certificate rotation.", "release": "v1.0.0"},
    {"name": "Disaster Recovery & Backup", "screens": ["Snapshot Scheduler", "Failover Console", "Recovery Time Tester"], "desc": "Automated cross-region database replication and one-click failover.", "release": "v1.1.0"},
    {"name": "System Health & Telemetry", "screens": ["Metrics Dashboard", "APM Trace Viewer", "SLA Uptime Monitor"], "desc": "Prometheus metrics, distributed tracing, and real-time SLA monitor.", "release": "v1.0.0"},
    {"name": "Tax Calculation & Reporting", "screens": ["Capital Gains Calculator", "Tax Loss Harvesting", "Form 1099 Export"], "desc": "Realized capital gains calculation and tax report generation engine.", "release": "v1.2.0"},
    {"name": "Reconciliation & Settlement", "screens": ["Matching Engine Logs", "Bank Statement Reconciler", "Discrepancy Resolver"], "desc": "End-of-day cash and position reconciliation against custodian clearing houses.", "release": "v1.1.0"},
    {"name": "Fee Schedule & Commission Engine", "screens": ["Tiered Fee Structure", "Commission Breakdown", "Rebate Manager"], "desc": "Flexible fee tier calculation, commission splits, and broker rebates.", "release": "v1.0.0"},
    {"name": "Digital Signatures & E-Signing", "screens": ["Document Vault", "Signature Request Flow", "Audit Stamp Viewer"], "desc": "Legally binding digital contract signing and document vault storage.", "release": "v1.1.0"},
    {"name": "Liquidity Pools & Yield Aggregator", "screens": ["Pool Explorer", "Yield APY Tracker", "Liquidity Provider Portal"], "desc": "Automated market maker liquidity pool management and yield optimization.", "release": "v2.0-Beta"},
    {"name": "Cross-Border Remittance & Wire", "screens": ["SWIFT/SEPA Router", "Wire Transfer Form", "FX Rate Lock"], "desc": "International SWIFT and SEPA wire transfer execution with guaranteed FX rates.", "release": "v1.2.0"},
    {"name": "Credit Scoring & Underwriting", "screens": ["Scorecard Builder", "Credit Risk Assessor", "Application Decision Matrix"], "desc": "Automated credit score analysis and underwriting risk evaluation.", "release": "v2.0-Beta"},
    {"name": "Fraud Detection & Anomaly Screening", "screens": ["Anomaly Alert Console", "Behavioral Pattern Detector", "Fraud Rule Engine"], "desc": "ML-driven real-time fraud pattern detection on incoming transactions.", "release": "v1.1.0"},
    {"name": "Community Portal & Forums", "screens": ["Forum Feed", "User Reputation Badge", "Moderation Panel"], "desc": "Investor community discussion forum, peer insights, and moderation tools.", "release": "v2.1.0"},
    {"name": "GraphQL Federation Gateway", "screens": ["Schema Composer", "GraphQL Playground", "Query Performance Monitor"], "desc": "Unified GraphQL schema federation across microservices.", "release": "v1.2.0"},
    {"name": "Cache Management & Redis Routing", "screens": ["Cache Hit Ratio Monitor", "Invalidation Manager", "Redis Cluster Health"], "desc": "Distributed Redis cluster caching, key invalidation, and warm-up jobs.", "release": "v1.0.0"},
    {"name": "Vector Search & Semantic Index", "screens": ["Vector Embeddings Index", "Semantic Search Tester", "Similarity Engine"], "desc": "Vector database integration for AI-powered semantic search across documents.", "release": "v2.1.0"},
    {"name": "Time-Series Metric Collector", "screens": ["InfluxDB Monitor", "Metric Collector Config", "Retention Policy Editor"], "desc": "High-frequency time-series data collection and retention management.", "release": "v1.1.0"},
    {"name": "Config Sync Engine", "screens": ["Feature Flags Console", "Global Config Editor", "Version Rollback Utility"], "desc": "Dynamic runtime feature flag toggles and global configuration sync.", "release": "v1.0.0"},
    {"name": "Incident Response & Runbooks", "screens": ["PagerDuty Integration", "Runbook Automation", "Post-Mortem Logger"], "desc": "Incident escalation routing, automated remediation runbooks, and post-mortems.", "release": "v1.1.0"},
    {"name": "Asset Tokenization & Smart Contracts", "screens": ["Token Minting Portal", "Smart Contract Auditor", "Cap Table Manager"], "desc": "Real-world asset tokenization, smart contract auditing, and cap table tracking.", "release": "v2.1.0"},
    {"name": "Session Replay & UX Analytics", "screens": ["Heatmap Viewer", "Session Recording Console", "User Journey Analyzer"], "desc": "User session playback, DOM heatmaps, and drop-off funnel analytics.", "release": "v1.2.0"},
    {"name": "Partner API Sandbox", "screens": ["Sandbox Environment", "Mock Data Generator", "Partner Onboarding Guide"], "desc": "Isolated sandbox environment for third-party developer integration testing.", "release": "v1.2.0"}
]

print(f"Total features created: {len(features_50)}")
formatted_json = json.dumps(features_50, indent=10)

with open('projectpulse.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace P.features = [...]
old_p_features = """        P.features = [
          { name: 'Core Infrastructure', screens: ['Database Schema', 'Core Services', 'API Gateway'], desc: 'Fundamental system services and architecture.', release: 'v1.0.0' },
          { name: 'User Management', screens: ['Cash Accounts', 'Security Accounts', 'Authentication'], desc: 'User lifecycle and account security.', release: 'v1.0.0' },
          { name: 'Market Intelligence', screens: ['Portfolio Valuations', 'Market Data Feed', 'Analytics Dashboard'], desc: 'Data processing and reporting.', release: 'v1.1.0' }
        ];"""

new_p_features = "        P.features = " + formatted_json + ";"

if old_p_features in content:
    content = content.replace(old_p_features, new_p_features)
    print("Successfully replaced P.features in sample initialization!")
else:
    print("WARNING: Could not find exact old_p_features string!")

# Replace stateP.features default template
old_state_features = """        features: [
          { name: 'Core Infrastructure', screens: ['Database Schema', 'Core Services', 'API Gateway'], desc: 'Fundamental system services and architecture.' },
          { name: 'User Management', screens: ['Cash Accounts', 'Security Accounts', 'Authentication'], desc: 'User lifecycle and account security.' },
          { name: 'Market Intelligence', screens: ['Portfolio Valuations', 'Market Data Feed', 'Analytics Dashboard'], desc: 'Data processing and reporting.' }
        ],"""

features_50_no_release = [
    {"name": f["name"], "screens": f["screens"], "desc": f["desc"]} for f in features_50
]
new_state_features = "        features: " + json.dumps(features_50_no_release, indent=10) + ","

if old_state_features in content:
    content = content.replace(old_state_features, new_state_features)
    print("Successfully replaced stateP.features default template!")
else:
    print("WARNING: Could not find exact old_state_features string!")

with open('projectpulse.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Finished updating projectpulse.html!")
