import datetime
import json
import csv

def pergunta():
    print("Qual operação deseja realizar:")

    operacao = int(input("( 1 ) Adicionar \n "
                     "( 2 ) Listar \n "
                     "( 3 ) Excluir"))
    return operacao

def adiciona(funcionario):

    resp = "S"
    while resp == "S":

        chave = input("Id do funcionario: ")
        nome = input("Nome do funcionario: ")
        cargo = input("Cargo: ")
        salario = input("Salario: ")

        funcionario[chave] = [nome, cargo, salario]

        with open("funcionario.json", "w") as func_json:
            json.dump(funcionario, func_json)

        with open("funcionario.csv", "w", newline='') as inv:
            for chave, valor in funcionario.items():
                inv.write(chave + ";" + valor[0] + ";" + valor[1] + ";" + valor[2] + "\n")

        resp = input("Digite < S > Para continuar: ").upper()


def listar():

    with open("funcionario.csv", "r") as csv:
        lista = csv.readlines()
        return lista
