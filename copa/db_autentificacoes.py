from tinydb import TinyDB,Query
from datetime import datetime
import requests


db = TinyDB("autentificacoes.json")
url = ""

def inserir_autentificacao(nome):
    agora = datetime.now()

    autentificacao = {
    "Nome": nome,
    "Data": agora.strftime("%d/%m/%Y"),
    "Hora": agora.strftime("%H:%M:%S")
    }


    db.insert(autentificacao)


def backup():
    hora = datetime.now().strftime("%H:%M")

    if hora == "16:30" or hora == "16:50":
        todos_registros = db.all()

        if len(todos_registros) > 0 :
            valores_dos_registros = [list(registros.values()) for registros in todos_registros ]
            resposta = requests.post(url, json={"dados":valores_dos_registros})
            while resposta.status_code != 200:
                resposta = requests.post(url, json={"dados":valores_dos_registros})

            db.truncate()

db.truncate()
