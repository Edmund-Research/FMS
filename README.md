### Fraud Pipeline Metrics

Every time you call `POST /fraud/run`, the response includes:

- `total_transactions`: Number of simulated transactions  
- `fraud_cases_count`: How many were classified as fraud  
- **Metrics**:
  - `fraud_rate_pct`: (fraud_cases / total_transactions) × 100  
  - `detection_rate_pct`: (ML-flagged / rule-flagged) × 100  
  - `false_positive_rate_pct`: ((rule-flagged − ML-flagged) / total_transactions) × 100  
  - `high_risk_volume`: Number of transactions hitting the rule-based flags
- **Risk Appetite**:
  - `max_fraud_rate_pct`: defined tolerance (e.g. 1%)  
  - `current_fraud_rate_pct`: The measured rate  
  - `within_appetite`: Boolean – is `current_fraud_rate_pct` ≤ `max_fraud_rate_pct`?  

These metrics highlight the KPIs (fraud rate, detection rate, false positives), KRIs (high-risk volume), and ensure values stay within your risk appetite.

## 1. Key Performance Indicators (KPIs)
KPIs measure how well fraud-management processes are working against your operational goals.

## 2. Key Risk Indicators (KRIs)
KRIs are early-warning metrics that signal an increasing risk of fraud.

## 3. Risk Appetite
Risk Appetite is the level of fraud loss/rate the organization is willing to accept in pursuit of business objectives.
