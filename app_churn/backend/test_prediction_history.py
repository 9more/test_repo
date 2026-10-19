from services.prediction_history_service import get_prediction_history

history = get_prediction_history(limit=10)

for item in history:
    print(item)
