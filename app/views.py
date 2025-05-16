from flask import Blueprint, jsonify, request
from .simulate   import generate_transactions
from .rules      import apply_basic_rules
from .model      import predict
from .forensic   import prepare_case_register
from .config     import RISK_APPETITE
from . import db
from .models     import Transaction, FraudCase

bp = Blueprint('fraud', __name__, url_prefix='/fraud')

@bp.route('/run', methods=['POST'])
def run_pipeline():
    n = request.json.get('n', 500) if request.is_json else 500

    df = generate_transactions(n)
    df = apply_basic_rules(df)
    df = predict(df)
    cases = prepare_case_register(df)

    total_tx       = len(df)
    rule_flags     = int(df['fraud_rule_flag'].sum())
    ml_flags       = int(df['ml_pred'].sum())
    fraud_rate_pct = round(100.0 * ml_flags / total_tx, 2) if total_tx else 0
    detection_rate = round(100.0 * ml_flags / rule_flags, 2) if rule_flags else 0
    false_pos_rate = round(100.0 * (rule_flags - ml_flags) / total_tx, 2)
    high_risk_volume = rule_flags
    under_appetite = fraud_rate_pct <= RISK_APPETITE['max_fraud_rate_pct']

    db.session.bulk_insert_mappings(
        Transaction,
        df.to_dict(orient='records')
    )
    db.session.commit()

    db.session.bulk_insert_mappings(
        FraudCase,
        cases[['transaction_id']].to_dict(orient='records')
    )
    db.session.commit()

    return jsonify({
        'total_transactions': total_tx,
        'fraud_cases_count': ml_flags,
        'metrics': {
            'fraud_rate_pct': fraud_rate_pct,
            'detection_rate_pct': detection_rate,
            'false_positive_rate_pct': false_pos_rate,
            'high_risk_volume': high_risk_volume,
        },
        'risk_appetite': {
            'max_fraud_rate_pct': RISK_APPETITE['max_fraud_rate_pct'],
            'current_fraud_rate_pct': fraud_rate_pct,
            'within_appetite': under_appetite,
        },
        'fraud_cases': cases.to_dict(orient='records'),
    })
