import sys
import json
import random
from datetime import datetime, timezone

def generate_predictions():
    """
    Mock prediction function to siimulate the AI model output.
    Take JSON input and output
    """

    time_offsets = [
        {"value": 0, "unit": "minute"},
        {"value": 15, "unit": "minute"},
        {"value": 30, "unit": "minute"},
        {"value": 45, "unit": "minute"},
        {"value": 1, "unit": "hour"},
        {"value": 2, "unit": "hour"},
        {"value": 3, "unit": "hour"},
        {"value": 5, "unit": "hour"},
        {"value": 8, "unit": "hour"},
        {"value": 13, "unit": "hour"},
        {"value": 21, "unit": "hour"}
    ]

    predictions = []
    for offset in time_offsets:
        predictions.append({
            "offset": offset,
            "gas_fee": {
                "value": round(random.uniform(20,50), 2), 
                "unit": "gwei"
            },
            "confidence": random.choice(["low", "medium", "high"])
        })

    best_option = min(
        predictions,
        key=lambda p: (p["gas_fee"]["value"], {"low": 3, "medium": 2, "high" :1}[p["confidence"]])
    )

    best_option_with_reasons = {
        "offset": best_option["offset"],
        "gas_fee": best_option["gas_fee"],
        "confidence": best_option["confidence"],
        "reason": "Lowest gas fee with the best confidence level in the next 24 hours"
    }

    # Metadata
    metadata = {
        "currency_unit": "gwei",
        "prediction_time": datetime.now(timezone.utc).isoformat() + "Z",
        "model_version": "v1.0.0"
    }
    
    response = {
        "predictions": predictions,
        "best_option": best_option_with_reasons,
        "metadata": metadata
    }

    print(json.dumps(response, indent=2))

if __name__ == "__main__":
    # Run the predictions
    generate_predictions()