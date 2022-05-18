import os
import json
import csv
from funcoes import *

if os.path.exists("funcionario.json"):
    with open("funcionario.json", "r") as func_json:
        funcionario = json.load(func_json)
else:
    funcionario = {}


resp = "S"
while resp == "S":

    operacao = pergunta()

    if operacao == 1:
        adiciona(funcionario)

    elif operacao == 2:
        lista = listar()

        for linha in lista:
            lista = linha.split(";")
            print("Nome: ", lista[1])
            print("Cargo: ", lista[2])
            print(f"Salario: R$ {lista[3]}")

    resp = input("Deseja continuar?").upper()

print("Obrigado por usar o cadastro de funcionarios")

