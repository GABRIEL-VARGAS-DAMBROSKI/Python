# -*- coding: utf-8 -*-

from lib.scrapy_table import Scrapy_Table

url = "https://pt.wikipedia.org/wiki/C%C3%A2mara_Municipal_de_S%C3%A3o_Paulo"
site_connect = Scrapy_Table(url)
tables = site_connect.get_tables(5)
login = []
vereadoresDict = {
        "Nome",
        "Partido",
        "Votos"
        }

for linha in tables[1:]:
    login.append(linha[0])
    #pegar os partidos
    #pegar a somatória dos votos
    #pegar vereadores com mais de 40 mil votos
    
for caracter in login:
    print(caracter[:8])