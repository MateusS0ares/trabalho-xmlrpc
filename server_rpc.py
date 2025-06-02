# servidor_rpc.py
from xmlrpc.server import SimpleXMLRPCServer
import random

def obter_previsao(cidade):
    print(f"📥 Requisição recebida para cidade: {cidade}")
    
    def gerar_dado():
        # Define faixas de temperatura para cada condição
        condicoes = {
            'Ensolarado': (20, 35),
            'Nublado': (10, 25),
            'Chuva': (5, 20),
            'Tempestade': (0, 15),
            'Neve': (-10, 0)
        }
        
        # Escolhe uma condição aleatória
        condicao = random.choice(list(condicoes.keys()))
        temp_min, temp_max = condicoes[condicao]
        
        return {
            "temp": f"{random.randint(temp_min, temp_max)}°C",
            "humidity": f"{random.randint(40, 80)}%",
            "wind": f"{round(random.uniform(0.5, 3.0), 2)} km/h",
            "condition": condicao
        }
    
    previsao = {
        "city": cidade,
        "current": gerar_dado(),
        "next_days": [gerar_dado() for _ in range(7)]
    }
    
    print(f"📤 Previsão enviada: {previsao['current']['temp']} | {previsao['current']['condition']}")
    return previsao


server = SimpleXMLRPCServer(("localhost", 8000), allow_none=True)
print("Servidor XML-RPC disponível em http://localhost:8000")
server.register_function(obter_previsao, "obter_previsao")
server.serve_forever()
