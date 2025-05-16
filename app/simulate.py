import pandas as pd, numpy as np

def generate_transactions(n=500):
    np.random.seed(42)
    df = pd.DataFrame({
        'transaction_id': range(1, n+1),
        'amount': np.random.exponential(scale=100, size=n),
        'num_failed_logins': np.random.poisson(lam=0.1, size=n),
        'is_foreign': np.random.binomial(1, 0.05, n),
        'hour': np.random.randint(0, 24, n),
    })
    return df
