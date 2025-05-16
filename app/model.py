from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

_model = None

def train_model(df):
    global _model
    X = df[['amount','num_failed_logins','is_foreign','hour']]
    y = df['fraud_rule_flag']
    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)
    clf = LogisticRegression()
    clf.fit(X_train, y_train)
    _model = clf

def predict(df):
    if _model is None:
        train_model(df)
    X = df[['amount','num_failed_logins','is_foreign','hour']]
    df['ml_pred'] = _model.predict(X)
    return df
