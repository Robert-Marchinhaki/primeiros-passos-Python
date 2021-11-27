import requests


def conectar():
    try:
        requests.get(url='http://pudim.com.br')
        print('Conseguimos acessar o site')
    except Exception as error:
        print('Não foi possível fazer a requisição')


conectar()
