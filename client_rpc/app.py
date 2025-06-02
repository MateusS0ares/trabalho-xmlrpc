# app.py
from flask import Flask, render_template, request
from rpc_client import get_previsao
from previsao_parser import preparar_previsao

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    cidade = request.form.get("cidade", "São Paulo")
    dados = get_previsao(cidade)
    previsao = preparar_previsao(dados)
    return render_template("index.html", previsao=previsao)

if __name__ == "__main__":
    app.run(debug=True)
