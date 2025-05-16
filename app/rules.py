def apply_basic_rules(df):
    df['fraud_rule_flag'] = ((df['amount'] > 300) | (df['is_foreign'] == 1)).astype(int)
    return df
