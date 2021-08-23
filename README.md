# Desafio-Digesto

### Desenvolvedor(a) Backend - Versão 1.5 - 20/01/2021

Este repositório descreve o desenvolvimento do desafio de Desenvolvedor Backend proposto pela Digesto.

O desafio possui alguns objetivos, que serão descritos à seguir.

## OBJETIVOS
1. Desenvolver um web crawler em Python que extrai das páginas-alvo e salva em disco
os dados especificados.
2. Manter em sistema git hospedado de sua preferência (github, gitlab, etc.) o progresso
do seu código de acordo com as melhores práticas que regem o uso de tal sistema. Ao
término do desafio, compartilhar conosco o endereço público do repositório.
3. Refletir sobre o código conforme ele cresce e propor abstrações. Tais abstrações só
devem ser usadas caso ajudem a manter esta pequena aplicação mais coesa, concisa
e com baixo nível de acoplamento entre seus componentes internos.

## ESPECIFICAÇÃO
Dadas as opções de máquinas nas páginas-alvo, o crawler deve extrair os seguintes
atributos de cada opção de máquina:
* CPU / VCPU
* MEMORY
* STORAGE / SSD DISK
* BANDWIDTH / TRANSFER
* PRICE [ $/mo ]

Páginas-alvo:
1. https://www.vultr.com/products/cloud-compute/#pricing (apenas SSD Cloud
Instances)
2. https://www.digitalocean.com/pricing/ (apenas tabela Basic droplets)
Ao executar um crawler, devem ser disponíveis as seguintes opções independentes entre si:
* --print
(Imprime resultados na tela)
* --save_csv
(Salva dados em arquivo csv)
* --save_json
(Salva dados em arquivo json)

Não deve ser usado o framework Scrapy, Selenium ou semelhante alto-nível, mas sinta-se
livre para usar alguns conceitos como inspiração, bem como bibliotecas menores utilizadas
pelo mesmo (requests, xpath, regex, parsel, etc.).

## ETAPAS
### 1 página-alvo, imprime na tela
A primeira etapa exige que o seu crawler funcione para a página alvo 1, capturando as
informações e sendo capaz de imprimi-las na linha de comando em formato arbitrário.
### 1 página-alvo, imprime na tela, salva em json
A segunda etapa exige que o seu crawler funcione para a mesma página-alvo da etapa
anterior, tendo as mesmas funcionalidades da etapa anterior, mas também sendo capaz de
salvar os dados em um arquivo em formato json.
### 1 página-alvo, imprime na tela, salva em json, salva em csv
A terceira etapa exige que o seu crawler funcione para a mesma página-alvo da etapa
anterior, tendo as mesmas funcionalidades da etapa anterior, mas também sendo capaz de
salvar os dados em um arquivo em formato csv.
### 2 páginas-alvo
A quarta etapa exige que você extraia as informações também da página-alvo 2, tendo as
mesmas funcionalidades da etapa anterior.

## PRAZO
O prazo de entrega é de 6 dias corridos a partir da apresentação do enunciado. Sinta-se livre
para nos fazer perguntas caso não tenha entendido completamente o enunciado.

## DESENVOLVIMENTO

### Descrição
O robô Web Crawler desenvolvido neste desafio foi chamado de SmartWatcher e possui um menu interativo no terminal na qual o usuário pode escolher a funcionalidade desejada.

<p align="center">
  <img src="https://user-images.githubusercontent.com/60860861/130505287-f1fc41c4-5bb6-432c-84fb-c18eed535140.png" width="1000" height="150"></img>
</p>

Primeiramente, o usuário poderá selecionar entre os dois sites alvos, através das opções (1) e (2) digitadas no terminal. Qualquer outro valor irá levantar uma mensagem de erro e reiniciará o menu.

<p align="center">
  <img src="https://user-images.githubusercontent.com/60860861/130507022-0e9dd528-8688-4340-981a-255dce7e07da.png" width="1000" height="250"></img>
</p>

Depois, o usuário poderá selecionar entre as três opções descritas nos objetivos do desafio, através das opções:
* --print : Que é selecionada digitando 1.
* --save_csv : Que é selecionada digitando 2.
* --save_json : Que é selecionada digitando 3.

Após selecionar uma das opções, o menu irá executar a tarefa e depois irá perguntar se deseja terminar o programa digitando 1, ou se deseja utilizá-lo novamente digitando 2.

<p align="center">
  <img src="https://user-images.githubusercontent.com/60860861/130507553-05b06b17-66d7-4e71-8f66-9e28a8612f51.png" width="1000" height="400"></img>
</p>

Caso seja selecionado um dos modos save_csv ou save_json, antes de salvar o resultado no formato CSV ou JSON desejado, o usuário terá a oportunidade de selecionar um nome para o arquivo.

<p align="center">
  <img src="https://user-images.githubusercontent.com/60860861/130507891-35ea6934-0e60-419a-b4fd-9d3bda50ef1d.png" width="1000" height="300"></img>
</p>


### Entrega

Os commits foram feitos primeiramente em uma branch denominada dev, que recebe todas as implementações do projeto.

Caso as implementações estejam em pleno funcionamento e possam ser integradas ao código principal da branch main, elas são integradas em um pull request da branch de desenvolvimento dev para a branch main.

Assim, em cada uma das 4 etapas de desenvolvimento, os pull requests associados ao progresso do desenvolvimento do desafio possuem comentários demonstrando os avanços de uma etapa para outra.

O código também possui comentários para explicar o seu funcionamento.

Após o termino do desafio e das suas 4 etapas, um commit adicional foi implementado para melhorar a abstração do projeto e manter o nível baixo de acoplamento entre suas partes.

O desafio foi entregue na quinta-feira dia (19/08).
A data do último commit de desenvolvimento é da segunda-feira dia (23/08) com 5 dias.
