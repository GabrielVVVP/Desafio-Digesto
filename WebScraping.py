#! /usr/bin/env python3
# -*- coding:utf-8 -*-

# Importando as Bibliotecas
from bs4 import BeautifulSoup
import pandas as pd
from urllib.error import HTTPError
from urllib.error import URLError
import urllib.request

url = 'https://www.vultr.com/products/cloud-compute/#pricing/'
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7' # Parâmetros do cabeçalho da requisição.
headers={'User-Agent':user_agent,} # Cabeçalho da Requisição. 
request=urllib.request.Request(url,None,headers) # Requisição com cabeçalho e endereço.
html = urllib.request.urlopen(request) # Leitura da url
bs = BeautifulSoup(html, 'lxml') #Aplicando a biblioteca BeautifulSoup na url lida
results = bs.select('div span') # Resultados do filtro da Biblioteca Beautiful Soup para a identificação dos parâmetros requisitados
for item in results:
    print(item.text)
