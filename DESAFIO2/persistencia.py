import json
import os

def salvar_dados(nome_arquivo, dados):
    pasta = os.path.dirname(os.path.abspath(__file__))
    caminho = os.path.join(pasta, 'dados', nome_arquivo)

    try:
        with open(caminho, 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
    except(ValueError, TypeError):
        print('ERRO AO SALVAR OS DADOS! ')
        return
    except FileNotFoundError:
        print('ARQUIVO NÃO ENCONTRADO! ')
        return
    except PermissionError:
        print('SEM PERMISSÃO PARA SALVAR OS DADOS! ')

def carregar_dados(nome_arquivo):
    pasta = os.path.dirname(os.path.abspath(__file__))
    caminho = os.path.join(pasta, 'dados', nome_arquivo)
    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            dados =json.load(arquivo)
        return dados
    except FileNotFoundError:
        print('ARQUIVO NÃO ENCONTRADO! ')
        return []
