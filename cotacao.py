import requests

resultado_requisicao = requests.get('https://api.hgbrasil.com/finance?key=1253b0bd')

r = resultado_requisicao.json()

resultados = r.get('results')
correncia = resultados.get('currencies')

moeda = correncia.get('source')

usd = correncia.get('USD')

nome_moeda = usd.get('name')
preco_compra = usd.get('buy')
preco_venda = usd.get('sell')
variacao = usd.get('variation')



def moeda_nome(moeda):
    moeda = nome_moeda
    return moeda

def compra(compra):
    compra = preco_compra
    return compra

def venda(venda):
    venda = preco_venda
    return venda

def variando(variando):
    variando = variacao
    return variando


print("---------------COTAÇÃO HOJE---------------")

print("\nMoeda: ", moeda_nome(moeda))
print("\nPreço de Compra em Reais: ", compra(compra))
print("\nPreço de Venda em Reais: ", venda(venda))
print("\nVariação da moeda no momento da consulta: ", variando(variando))
print("\n")

print("------------------------------------------")

