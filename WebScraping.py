#! /usr/bin/env python3
# -*- coding:utf-8 -*-

# Importando as Bibliotecas
from bs4 import BeautifulSoup
import pandas as pd
from urllib.error import HTTPError
from urllib.error import URLError
import urllib.request 
import os
import time

def main(): # Função principal do menu interativo do robô Web Scraper
    url1 = 'https://www.vultr.com/products/cloud-compute/#pricing/' # Link de leitura da primeira parte do desafio
    url2 = 'https://www.digitalocean.com/pricing/' # Link de leitura da segunda parte do desafio

    print("Olá, este é o robô SmartWatcher, que extrai informações das páginas alvo.")
    print("O SmartWatcher pode adquirir informações de dois links diferentes. Selecione o link desejado.")
    print("Link 1: {}".format(url1))
    print("Link 2: {}".format(url2))
    opcao = input(("Selecione a opção desejada (1 ou 2): ")) # Seleção do link de leitura desejado.
    if int(opcao)==1 or int(opcao)==2:
        print("Certo! Agora, de forma deseja mostrar os dados obtidos?")
        print("Opção 1: Mostrar no Terminal")
        print("Opção 2: Salvar em JSON")
        print("Opção 3: Salvar em CSV")
        modo = input(("Selecione a opção desejada (1, 2 ou 3): "))
        if int(modo)==1 or int(modo)==2: # Casting da variável de opção de string para inteiro.
            print("Certo! Os dados serão mostrados no terminal.")
            if int(opcao)==1: # O link selecionado irá para o procedimento do BeautifulSoup.
                url = url1
            else: 
                url = url2   
            if int(modo)==1:
                user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7' # Parâmetros do cabeçalho da requisição.
                headers={'User-Agent':user_agent,} # Cabeçalho da Requisição. 
                request=urllib.request.Request(url,None,headers) # Requisição com cabeçalho e endereço.
                html = urllib.request.urlopen(request) # Leitura da url
                bs = BeautifulSoup(html, 'lxml') #Aplicando a biblioteca BeautifulSoup na url lida
                results = bs.select('div span') # Resultados do filtro da Biblioteca Beautiful Soup para a identificação dos parâmetros requisitados
                for item in results:
                    print(item.text)
            resposta = input(("Deseja finalizar a rotina (1), ou realizar novas leituras(2)? ")) # Opção de terminar o programa ou de voltar ao início do menu.
            if int(resposta)==1 or int(resposta)==2:
                return resposta
            else:
                print("Opção inválida, reiniciando o sistema.") # Qualquer valor inválido no input do terminal irá fazer o programa retornar ao início do loop. 
                time.sleep(1.5)
                os.system('clear')
                return resposta           
        else:
            print("Opção inválida, reiniciando o sistema.") # Qualquer valor inválido no input do terminal irá fazer o programa retornar ao início do loop.   
            time.sleep(1.5)
            os.system('clear')
    else:
        print("Opção inválida, reiniciando o sistema.")  # Qualquer valor inválido no input do terminal irá fazer o programa retornar ao início do loop.    
        time.sleep(1.5)
        os.system('clear')
    
while True: # Chamada da função principal, que apenas irá terminar o loop de chamada quando o usuário digitar 1 na etapa final do menu.
    resposta = main()
    if resposta == "1":
        break