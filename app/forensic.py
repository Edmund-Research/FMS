def prepare_case_register(df):
    fraud = df[df['ml_pred']==1].copy()
    fraud['case_register_id'] = range(1, len(fraud)+1)
    return fraud
