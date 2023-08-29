import requests
from bs4 import BeautifulSoup
from tinydb import TinyDB, Query

def acessar_pagina(url):
    pagina = requests.get(url)
    bs = BeautifulSoup(pagina.text, "html.parser")
    #print(bs)
    return bs

def construir_url():
    links_notas_de_imprensa= "https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa?b_start:int="
    links =[]
    contador = 300
    while contador >=0:
        url_completa = links_notas_de_imprensa + str(contador)
        if contador == 0:
            url_completa = "https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa"
        links.append(url_completa)
        contador -= 30
        print(url_completa)
    return links

def main():
    url = "https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa"
    #pagina_web = acessar_pagina(url)
    #print(pagina_web)
    lista_url = construir_url()
    i=1
    for link in construir_url():
        print(str(i) + " " + link)
        i+=1
if __name__== "__main__":
    main()