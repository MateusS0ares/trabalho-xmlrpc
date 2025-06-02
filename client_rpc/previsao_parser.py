# previsao_parser.py
from datetime import datetime, timedelta

def formatar_data(dias=0):
    return (datetime.now() + timedelta(days=dias)).strftime("%A, %d %B %Y")

def preparar_previsao(raw_data):
    return {
        "city": raw_data["city"],
        "date": formatar_data(),
        "current": raw_data["current"],
        "next_days": raw_data["next_days"]
    }
