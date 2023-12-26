import random

random.seed(42)  # for repeatability

from src.mock_models import CreditScoringModel, FraudDetectionModel

def get_reason_codes(score, thresholds, reason_codes):
    """
    Determines rean codes based on the score.

    :param score: The model's score.
    :param thresholds: A dictionary mapping score ranges to reason codes.
    :param reason_codes: A dictionary mapping reason codes to their explanations.
    :return: A list of reason codes.
    """
    for threshold, codes in thresholds.items():
        if threshold[0] <= score < threshold[1]:
            return [reason_codes[code] for code in codes]
    return ["No reason code available for this score range."]

credit_model = CreditScoringModel()
fraud_model = FraudDetectionModel()


reason_codes = {
    "credit": {
        "high_risk": "High risk for credit lending.",
        "low_credit": "Low credit score.",
        "low_risk": "Low risk for credit lending.",
        "high_credit": "High credit score.",
    },
    "fraud": {
        "low_risk_fraud": "Low risk of fraud.",
        "transaction_safe": "Transaction is safe.",
        "high_risk_fraud": "High risk of fraud.",
        "transaction_risky": "Transaction is risky.",
    }
}

thresholds = {
    "credit": {
        (300, 580): ["high_risk", "low_credit"],
        (580, 850): ["low_risk", "high_credit"],
    },
    "fraud": {
        (0, 0.5): ["low_risk_fraud", "transaction_safe"],
        (0.5, 1): ["high_risk_fraud", "transaction_risky"],
    }
}

credit_score = credit_model.predict({})
fraud_score = fraud_model.predict({})

credit_reasons = get_reason_codes(credit_model.predict({}), thresholds['credit'], reason_codes['credit'])
fraud_reasons = get_reason_codes(fraud_model.predict({}), thresholds['fraud'], reason_codes['fraud'])

# Output
print(f"Credit Score: {credit_score}, Reason Codes: {credit_reasons}")

print(f"Fraud Score: {fraud_score}, Reason Codes: {fraud_reasons}")
