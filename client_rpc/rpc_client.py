# rpc_client.py
import xmlrpc.client

client = xmlrpc.client.ServerProxy("http://localhost:8000/", allow_none=True)

def get_previsao(cidade):
    return client.obter_previsao(cidade)
