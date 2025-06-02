# previsao_parser.py
from datetime import datetime, timedelta
import locale

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')  # Configura o locale para português do Brasil

def formatar_data(dias=0):
    data = datetime.now() + timedelta(days=dias)
    # Formata a data com "de" entre os elementos e capitaliza o nome do dia
    return data.strftime("%A").capitalize() + data.strftime(", %d de %B de %Y")

def obter_dias_da_semana():
    dias_da_semana = []
    for i in range(1, 8):  # Próximos 7 dias
        dia = (datetime.now() + timedelta(days=i)).strftime("%A").capitalize()
        dias_da_semana.append(dia)
    return dias_da_semana

def preparar_previsao(raw_data):
    dias_da_semana = obter_dias_da_semana()
    return {
        "city": raw_data["city"],
        "date": formatar_data(),
        "current": raw_data["current"],
        "next_days": [
            {**dia, "day_name": dias_da_semana[i]} for i, dia in enumerate(raw_data["next_days"])
        ]
    }
