# app/config.py
RISK_APPETITE = {
    'max_fraud_rate_pct': 1.0,   # e.g. we accept up to 1% of transactions being fraudulent
    'mttd_threshold_min': 30,    # target mean time to detect ≤ 30 minutes
}
