# servidor_rpc.py
from xmlrpc.server import SimpleXMLRPCServer
import random

def obter_previsao(cidade):
    print(f"📥 Requisição recebida para cidade: {cidade}")
    
    condicoes = ['Ensolarado', 'Nublado', 'Chuva', 'Tempestade', 'Neve']
    
    def gerar_dado():
        return {
            "temp": f"{random.randint(25, 35)}°C",
            "humidity": f"{random.randint(40, 80)}%",
            "wind": f"{round(random.uniform(0.5, 3.0), 2)} km/h",
            "condition": random.choice(condicoes)
        }
    
    previsao = {
        "city": cidade,
        "current": gerar_dado(),
        "next_days": [gerar_dado() for _ in range(3)]
    }
    
    print(f"📤 Previsão enviada: {previsao['current']['temp']} | {previsao['current']['condition']}")
    return previsao


server = SimpleXMLRPCServer(("localhost", 8000), allow_none=True)
print("Servidor XML-RPC disponível em http://localhost:8000")
server.register_function(obter_previsao, "obter_previsao")
server.serve_forever()
