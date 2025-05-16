-- Daily fraud rate
SELECT DATE(flagged_at) AS day,
       COUNT(*) FILTER (WHERE ml_pred)       AS fraud_count,
       COUNT(*)                              AS total_tx,
       ROUND(100.0 * fraud_count / total_tx, 2) AS fraud_rate_pct
FROM transactions t
LEFT JOIN fraud_cases f USING (transaction_id)
GROUP BY day
ORDER BY day;
