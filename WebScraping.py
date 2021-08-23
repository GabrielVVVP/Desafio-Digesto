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
import re

def find_pattern(texts,pattern): # Função que aplica os filtros do Regex e retorna o resultado
    if re.search(pattern, texts.text) is not None: # Se a pesquisa não devolver None, o resultado é retornado
        for result in re.finditer(pattern, texts.text):
            return result[0]        

def showterminal(url): # Função de demonstrar resultados no terminal

    cpu = [] # Lista com valores do CPU
    memory =[] # Lista com valores de Memory
    storage = [] # Lista com valores de SSD
    bandwidth = [] # Lista com valores de Bandwidth
    price = [] # Lista com valores de Preco
   
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7' # Parâmetros do cabeçalho da requisição.
    headers={'User-Agent':user_agent,} # Cabeçalho da Requisição. 
    request=urllib.request.Request(url,None,headers) # Requisição com cabeçalho e endereço.
    html = urllib.request.urlopen(request) # Leitura da url
    bs = BeautifulSoup(html, 'lxml') #Aplicando a biblioteca BeautifulSoup na url lida
    results = bs.select('div strong') # Resultados do filtro da Biblioteca Beautiful Soup para a identificação dos parâmetros requisitados (Storage, CPU, Memory, Bandwidth, Price)
    
    counter = 0 # Contador de tipo de filtro aplicado
    count = False # Variável que quando acionada, irá incrementar o contador
    reset = False # Variável que quando acionada, irá reiniciar o contador
    for typing in results:
        if counter==0: # Quando o contador for 0, aplicar o padrão regex de busca por valores de Storage
            pattern = re.compile(r'[0-9]{2,3}\b GB')
            storage_data = find_pattern(typing,pattern)
            if storage_data != None: 
                storage.append(storage_data)
                count = True
        elif counter==1: # Quando o contador for 1, aplicar o padrão regex de busca por valores de CPU
            pattern = re.compile(r'[0-9]{1,2}\b CPU')
            cpu_data = find_pattern(typing,pattern)
            if cpu_data != None: 
                cpu.append(cpu_data)
                count = True
        elif counter==2: # Quando o contador for 2, aplicar o padrão regex de busca por valores de Memory
            pattern= re.compile(r'[0-9]{1,4}\b ((\bMB\b)|(\bGB\b))')
            memory_data = find_pattern(typing,pattern)
            if memory_data != None: 
                memory.append(memory_data)
                count = True
        elif counter==3: # Quando o contador for 3, aplicar o padrão regex de busca por valores de Bandwidth
            pattern = re.compile(r'([0-9]*[.])?[0-9]+\b TB')
            bandwidth_data = find_pattern(typing,pattern)
            if bandwidth_data != None: 
                bandwidth.append(bandwidth_data)
                count = True
        elif counter==4: # Quando o contador for 4, aplicar o padrão regex de busca por valores de Price
            pattern = re.compile(r'[\$]([0-9]*[.])?[0-9]+')
            price_data = find_pattern(typing,pattern)
            if price_data != None: 
                price.append(price_data)
                reset = True          
        if count == True: # Quando a variável é acionada, o contador é incrementado
            counter+=1
            count = False
        if reset == True: # Quando a variável é acionada, o contador é reiniciado para 0
            counter=0 
            reset = False

    if (len(storage)==10)and(len(cpu)==10)and(len(memory)==10)and(len(bandwidth)==10)and(len(price)==10): # Verificação de leitura correta, para não executar erros            
        for item in range(10):
            print("Instance {}: |Storage: {}|CPU: {}|Memory: {}| Bandwidth: {}| Price: {}".format(item+1,storage[item],cpu[item],memory[item],bandwidth[item],price[item])) # Valores da leitura do Site mostrados no terminal
    else:
        print("Houve alguma falha na leitura, o sistema será reiniciado")                  

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
                showterminal(url)
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