import requests
import json

key = "5b455a407e7773f7059979cc45506617"
token = "194245b1524c580e3e27b57f770c2b4593dd7d1bb52a88a4b75dac2b9350b4b1"


idBoard = "5ce15796c6446b6afaebc2ce"
idPR = "5ce15797cacb3411ef188fc8"
idSE = "5ce15797b23dd08ee362c1fa"
idEM = "5ce15797d5d9b98bed9b4f12"
idRT = "5ce158b7b103cf26aa96a031"
idCO = "5ce158bf1bde4d62b0a835ff"

idsStatus = {"5ce15797cacb3411ef188fc8": "PR", "5ce15797b23dd08ee362c1fa": "SE", "5ce15797d5d9b98bed9b4f12": "EM", "5ce158b7b103cf26aa96a031": "RT", "5ce158bf1bde4d62b0a835ff": "CO"}

def adicionarPedido(nome, email, tel, PR, MR, DR, PV, GA, PM, FO):
    url = "https://api.trello.com/1/cards"
    querystring = {"name": "Pedido 02",
                   "desc": "Cliente: \n "+
                            "nome: "+str(nome)+"\n"+
                            "email: "+str(email)+"\n" +
                            "telefone: "+str(tel)+"\n\n"+
                            "Componentes: \n"+
                            "Processador: "+str(PR)+"\n"+
                            "Memoria Ram: " + str(MR) + "\n" +
                            "Disco Rigido/SSD: " + str(DR) + "\n" +
                            "Placa de Video: " + str(PV) + "\n" +
                            "Gabinete: " + str(GA) + "\n" +
                            "Placa Mae: " + str(PM) + "\n" +
                            "Fonte: " + str(FO),
                   "idList": idPR,
                   "keepFromSource": "all",
                   "key": key,
                   "token": token}
    response = requests.request("POST", url, params=querystring)

    print(response.text)

def atualizarStatus():
    url = "https://api.trello.com/1/boards/" + idBoard + "/actions"
    querystring = {"key": key,
                   "token": token}
    response = requests.request("GET", url, params=querystring)
    print(response.json())

def obterStatusPedidos():
    url = "https://api.trello.com/1/boards/" + idBoard + "/actions"
    querystring = {"fields":"data,type",
                    "key": key,
                    "token": token}
    jsonResponse = json.loads(json.dumps(requests.request("GET", url, params=querystring).json()))
    pedidos = []
    statusPedido = []
    for i in range(0,len(jsonResponse)):
        if(str(jsonResponse[i]["type"]) == "updateCard"):
            strPedido = str(jsonResponse[i]["data"]["card"]["name"])
            if(not strPedido in pedidos and "listAfter" in str(jsonResponse[i]["data"])):
                status = idsStatus[str(jsonResponse[i]["data"]["listAfter"]["id"])]
                pedidos.append(strPedido)
                statusPedido.append([strPedido, status])
    return statusPedido

print("Acoes: ")
# atualizarStatus()
print(obterStatusPedidos())

print("Foi so Texte")
