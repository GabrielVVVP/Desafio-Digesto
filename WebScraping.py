#! /usr/bin/env python3
# -*- coding:utf-8 -*-

# Importando as Bibliotecas
from bs4 import BeautifulSoup
import urllib.request 
import os
import time
import re
import json
import csv

class SmartWatcher(): # Classe com o Robô Web Crawler
    def __init__(self):
        while True: # Chamada da função principal, que apenas irá terminar o loop de chamada quando o usuário digitar 1 na etapa final do menu
            resposta = self.main()
            if resposta == "1":
                break

    def main(self): # Função principal do menu interativo do robô Web Crawler
        url1 = 'https://www.vultr.com/products/cloud-compute/#pricing/' # Link de leitura da primeira parte do desafio
        url2 = 'https://www.digitalocean.com/pricing/' # Link de leitura da segunda parte do desafio

        print("Olá, este é o robô SmartWatcher, que extrai informações das páginas alvo.")
        print("O SmartWatcher pode adquirir informações de dois links diferentes. Selecione o link desejado.")
        print("Link 1: {}".format(url1))
        print("Link 2: {}".format(url2))
        opcao = input(("Selecione a opção desejada (1 ou 2): ")) # Seleção do link de leitura desejado
        if int(opcao)==1 or int(opcao)==2:
            if int(opcao)==1: # O link selecionado irá para o procedimento do BeautifulSoup
                url = url1
                value_check = 10
            else: 
                url = url2  
                value_check = 6
            print("Certo! Agora, de forma deseja mostrar os dados obtidos?")
            print("Opção 1: --print") # Seleção do modo print na tela
            print("Opção 2: --save_json") # Seleção do modo salvar em arquivo json
            print("Opção 3: --save_csv") # Seleção do modo salvar em arquivo csv
            modo = input(("Selecione a opção desejada (1, 2 ou 3): "))
            if int(modo)==1 or int(modo)==2 or int(modo)==3: # Casting da variável de opção de string para inteiro
                if int(modo)==1:
                    print("Certo! Os dados serão mostrados no terminal.")
                    self.print_tela(url,value_check)
                elif int(modo)==2:
                    print("Certo! Os dados serão salvados no formato JSON.")
                    self.save_json(url,value_check)
                else:
                    print("Certo! Os dados serão salvados no formato CSV.")
                    self.save_csv(url,value_check)            
                resposta = input(("Deseja finalizar a rotina (1), ou realizar novas leituras(2)? ")) # Opção de terminar o programa ou de voltar ao início do menu
                if int(resposta)==1 or int(resposta)==2:
                    os.system('clear')
                    return resposta
                else:
                    print("Opção inválida, reiniciando o sistema.") # Qualquer valor inválido no input do terminal irá fazer o programa retornar ao início do loop
                    time.sleep(1.5)
                    os.system('clear')
                    return resposta           
            else:
                print("Opção inválida, reiniciando o sistema.") # Qualquer valor inválido no input do terminal irá fazer o programa retornar ao início do loop  
                time.sleep(1.5)
                os.system('clear')
        else:
            print("Opção inválida, reiniciando o sistema.")  # Qualquer valor inválido no input do terminal irá fazer o programa retornar ao início do loop    
            time.sleep(1.5)
            os.system('clear')

    # Barra de progresso
    def printProgressBar (self,iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total))) # Percentual do progresso
        filledLength = int(length * iteration // total) # Tamanho da barra progresso
        bar = fill * filledLength + '-' * (length - filledLength) # Barra de progresso
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd) # Print completo
        # Gera uma nova linha quando completo
        if iteration == total: 
            print()

    def find_pattern(self,texts,pattern): # Função que aplica os filtros do Regex e retorna o resultado
        if re.search(pattern, texts.text) is not None: # Se a pesquisa não devolver None, o resultado é retornado
            for result in re.finditer(pattern, texts.text):
                return result[0]    

    def webscraper(self,url): # Função de extrair informações de sites da web

        cpu = [] # Lista com valores do CPU
        memory =[] # Lista com valores de Memory
        storage = [] # Lista com valores de SSD
        bandwidth = [] # Lista com valores de Bandwidth
        price = [] # Lista com valores de Preco

        user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7' # Parâmetros do cabeçalho da requisição
        headers={'User-Agent':user_agent,} # Cabeçalho da Requisição. 
        request=urllib.request.Request(url,None,headers) # Requisição com cabeçalho e endereço
        html = urllib.request.urlopen(request) # Leitura da url
        bs = BeautifulSoup(html, 'lxml') #Aplicando a biblioteca BeautifulSoup na url lida

        if url == "https://www.vultr.com/products/cloud-compute/#pricing/":
            
            results = bs.select('div strong') # Resultados do filtro da Biblioteca Beautiful Soup para a identificação dos parâmetros requisitados (Storage, CPU, Memory, Bandwidth, Price)
            
            counter = 0 # Contador de tipo de filtro aplicado
            count = False # Variável que quando acionada, irá incrementar o contador
            reset = False # Variável que quando acionada, irá reiniciar o contador
            for typing in results:
                if counter==0: # Quando o contador for 0, aplicar o padrão regex de busca por valores de Storage
                    pattern = re.compile(r'[0-9]{2,3}\b GB')
                    storage_data = self.find_pattern(typing,pattern)
                    if storage_data != None: 
                        storage.append(storage_data)
                        count = True
                elif counter==1: # Quando o contador for 1, aplicar o padrão regex de busca por valores de CPU
                    pattern = re.compile(r'[0-9]{1,2}\b CPU')
                    cpu_data = self.find_pattern(typing,pattern)
                    if cpu_data != None: 
                        cpu.append(cpu_data)
                        count = True
                elif counter==2: # Quando o contador for 2, aplicar o padrão regex de busca por valores de Memory
                    pattern= re.compile(r'[0-9]{1,4}\b ((\bMB\b)|(\bGB\b))')
                    memory_data = self.find_pattern(typing,pattern)
                    if memory_data != None: 
                        memory.append(memory_data)
                        count = True
                elif counter==3: # Quando o contador for 3, aplicar o padrão regex de busca por valores de Bandwidth
                    pattern = re.compile(r'([0-9]*[.])?[0-9]+\b TB')
                    bandwidth_data = self.find_pattern(typing,pattern)
                    if bandwidth_data != None: 
                        bandwidth.append(bandwidth_data)
                        count = True
                elif counter==4: # Quando o contador for 4, aplicar o padrão regex de busca por valores de Price
                    pattern = re.compile(r'[\$]([0-9]*[.])?[0-9]+')
                    price_data = self.find_pattern(typing,pattern)
                    if price_data != None: 
                        price.append(price_data)
                        reset = True          
                if count == True: # Quando a variável é acionada, o contador é incrementado
                    counter+=1
                    count = False
                if reset == True: # Quando a variável é acionada, o contador é reiniciado para 0
                    counter=0 
                    reset = False
            complete = [storage,cpu,memory,bandwidth,price] # Lista com todas as listas anteriores, que será retornada como resultado da função
            return complete

        else:

            results = bs.select('div span.largePrice') # Resultados do filtro da Biblioteca Beautiful Soup para a identificação dos parâmetros requisitados (Price)
            for typing in results:
                price.append("$"+typing.text)

            results2 = bs.select('div li.priceBoxItem div ul li') # Resultados do filtro da Biblioteca Beautiful Soup para a identificação dos parâmetros requisitados (Storage, CPU, Memory, Bandwidth)

            counter = 0 # Contador de tipo de filtro aplicado
            count = False # Variável que quando acionada, irá incrementar o contador
            reset = False # Variável que quando acionada, irá reiniciar o contador
            for typing2 in results2:
                if counter==0: # Quando o contador for 0, aplicar o padrão regex de busca por valores de Memory e depois de CPU
                    pattern= re.compile(r'[0-9]{1,4}\b GB')
                    memory_data = self.find_pattern(typing2,pattern)
                    if memory_data != None: 
                        memory.append(memory_data)
                    pattern = re.compile(r'[0-9]{1,2}\b ((\bCPU\b)|(\bCPUs\b))')
                    cpu_data = self.find_pattern(typing2,pattern)
                    if cpu_data != None: 
                        cpu.append(cpu_data)
                        count = True    
                elif counter==1: # Quando o contador for 1, aplicar o padrão regex de busca por valores de Storage
                    pattern = re.compile(r'[0-9]{2,3}\b GB SSD')
                    storage_data = self.find_pattern(typing2,pattern)
                    if storage_data != None: 
                        storage.append(storage_data)
                        count = True
                elif counter==2: # Quando o contador for 2, aplicar o padrão regex de busca por valores de Bandwidth
                    pattern = re.compile(r'[0-9]{1,4}\b ((\bGB\b)|(\bTB\b))')
                    bandwidth_data = self.find_pattern(typing2,pattern)
                    if bandwidth_data != None: 
                        bandwidth.append(bandwidth_data)
                        reset = True    
                if count == True: # Quando a variável é acionada, o contador é incrementado
                    counter+=1
                    count = False
                if reset == True: # Quando a variável é acionada, o contador é reiniciado para 0
                    counter=0 
                    reset = False     
            complete = [storage,cpu,memory,bandwidth,price] # Lista com todas as listas anteriores, que será retornada como resultado da função
            return complete
                
    def print_tela(self,url,value_check): # Função de demonstrar resultados no terminal

        self.printProgressBar(0, value_check, prefix = 'Progresso:', suffix = 'Completo', length = 50) # Chamada da barra de progresso com 0% completo     
        data = self.webscraper(url) # Recebe os dados do conteudo do site
        if (len(data[0])==value_check)and(len(data[1])==value_check)and(len(data[2])==value_check)and(len(data[3])==value_check)and(len(data[4])==value_check): # Verificação de leitura correta, para não executar erros            
            for item in range(value_check):
                time.sleep(0.1)   
                print("Instance {}: |Storage: {}|CPU: {}|Memory: {}| Bandwidth: {}| Price: {}".format(item+1,data[0][item],data[1][item],data[2][item],data[3][item],data[4][item])) # Valores da leitura do Site mostrados no terminal
                self.printProgressBar(item + 1, value_check, prefix = 'Progresso:', suffix = 'Completo', length = 50) # Update na barra de progresso
        else:
            print("Houve alguma falha na leitura, o sistema será reiniciado")                  

    def save_json(self,url,value_check): # Função de salvar resultados como arquivos JSON

        arquivo = input(("Digite o nome do arquivo JSON: "))+".json" # Selecionar o nome do arquivo
        results = self.webscraper(url) # Recebe os dados do conteudo do site
        data = {}

        self.printProgressBar(0, value_check, prefix = 'Progresso:', suffix = 'Completo', length = 50) # Chamada da barra de progresso com 0% completo     
        for item in range(value_check): # Organização dos dados em formato json
            instance = 'Instance {}'.format(item+1)
            data[instance] = {
                'Storage': results[0][item],
                'CPU': results[1][item],
                'Memory': results[2][item],
                'Bandwidth': results[3][item],
                'Price': results[4][item]
            }
            self.printProgressBar(item + 1, value_check, prefix = 'Progresso:', suffix = 'Completo', length = 50) # Update na barra de progresso
        with open(arquivo, "w") as outfile: # Salva no arquivo JSON
            json.dump(data, outfile)

    def save_csv(self,url,value_check): # Função de salvar resultados como arquivos JSON

        arquivo = input(("Digite o nome do arquivo CSV: "))+".csv" # Selecionar o nome do arquivo
        results = self.webscraper(url) # Recebe os dados do conteudo do site

        f = csv.writer(open(arquivo, 'w')) # Cria o arquivo csv
        f.writerow(['Instances','Storage', 'CPU', 'Memory', 'Bandwidth', 'Price']) 

        self.printProgressBar(0, value_check, prefix = 'Progresso:', suffix = 'Completo', length = 50) # Chamada da barra de progresso com 0% completo     
        for item in range(value_check): # Organização dos dados na tabela
            instance = 'Instance {}'.format(item+1)
            f.writerow([instance,results[0][item],results[1][item],results[2][item],results[3][item],results[4][item]]) # Escreve os dados nas linhas    
            self.printProgressBar(item + 1, value_check, prefix = 'Progresso:', suffix = 'Completo', length = 50) # Update na barra de progresso
    
runrobot = SmartWatcher()