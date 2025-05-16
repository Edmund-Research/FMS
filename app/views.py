from flask import Blueprint, jsonify, request
from .simulate import generate_transactions
from .rules import apply_basic_rules
from .model import predict
from .forensic import prepare_case_register
import pandas as pd

bp = Blueprint('fraud', __name__, url_prefix='/fraud')

@bp.route('/run', methods=['POST'])
def run_pipeline():
    n = request.json.get('n', 500) if request.is_json else 500

    df = generate_transactions(n)
    df = apply_basic_rules(df)
    df = predict(df)
    cases = prepare_case_register(df)

    return jsonify({
        'total_transactions': len(df),
        'fraud_cases': cases.to_dict(orient='records'),
    })
