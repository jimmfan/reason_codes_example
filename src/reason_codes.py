import random

random.seed(42)  # for repeatability

class ReasonCodeGenerator:
    def __init__(self, model, thresholds, reason_codes):
        """
        Initializes the ReasonCodeGenerator.

        :param model: The predictive model.
        :param thresholds: A dictionary mapping score ranges to reason codes.
        :param reason_codes: A dictionary mapping reason codes to their explanations.
        """
        self.model = model
        self.thresholds = thresholds
        self.reason_codes = reason_codes

    def predict_and_explain(self, input_data):
        """
        Generates a prediction and corresponding reason codes.

        :param input_data: The input data for the model.
        :return: A tuple of the prediction score and a list of reason codes.
        """
        score = self.model.predict(input_data)
        reasons = self._get_reason_codes(score)
        return score, reasons

    def _get_reason_codes(self, score):
        """
        Determines reason codes based on the score.

        :param score: The model's score.
        :return: A list of reason codes.
        """
        for threshold, codes in self.thresholds.items():
            if threshold[0] <= score < threshold[1]:
                return [self.reason_codes[code] for code in codes]
        return ["No reason code available for this score range."]


# Create Mock Models
class CreditScoringModel:
    def predict(self, input_data):
        # Simulates a credit scoring model
        return random.randint(300, 850)

class FraudDetectionModel:
    def predict(self, input_data):
        # Simulates a fraud detection model
        return random.uniform(0, 1)  # Score between 0 and 1

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

credit_generator = ReasonCodeGenerator(credit_model, thresholds["credit"], reason_codes["credit"])

fraud_generator = ReasonCodeGenerator(fraud_model, thresholds["fraud"], reason_codes["fraud"])

# Example usage for credit scoring
credit_input_data = {}  # Replace with actual data
credit_score, credit_reasons = credit_generator.predict_and_explain(credit_input_data)

# Example usage for fraud detection
fraud_input_data = {}  # Replace with actual data
fraud_score, fraud_reasons = fraud_generator.predict_and_explain(fraud_input_data)

# Output
print(f"Credit Score: {credit_score}, Reason Codes: {credit_reasons}")
# Credit Score: 414, Reason Codes: ['High risk for credit lending.', 'Low credit score.']

print(f"Fraud Score: {fraud_score}, Reason Codes: {fraud_reasons}")
# Fraud Score: 0.025010755222666936, Reason Codes: ['Low risk of fraud.', 'Transaction is safe.']
