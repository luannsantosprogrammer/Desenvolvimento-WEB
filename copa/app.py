from flask import Flask,render_template,jsonify,request
from db_autentificacoes import inserir_autentificacao,backup
from ativando_bipe import bipe
import webbrowser

app = Flask(__name__)


nome= {"nome": ""}
webbrowser.open("http://127.0.0.1:5000/")
webbrowser.open("http://127.0.0.1:5000/relogio")

@app.route("/")
def copa():

    return render_template("copa.html")


@app.route("/relogio")
def relogio():
    return render_template("relogio.html")


@app.route("/envio", methods=["POST"])
def envio():
    dado = request.get_json()
    nome["nome"] = dado.get("nome","")
    if nome["nome"] != "":
        inserir_autentificacao(nome["nome"])
    return jsonify(nome)

@app.route("/bipe",methods=["POST"])
def rota_bipe():
    dado = request.get_json()
    som_bipe = dado.get("bipe")
    if som_bipe == "bipe":
        bipe()

@app.route("/recebendo",methods=["GET"])
def recebendo():
    backup()
    return jsonify(nome)



if __name__=="__main__":
    app.run()