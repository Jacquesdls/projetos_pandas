import sqlite3
import pandas as pd

con = sqlite3.connect('agenda.db')

cur = con.cursor()


resultado = cur.execute("select * from CONTATO")


nomes =[]
enderecos = []
numeros = []

for linha in resultado.fetchall():
    nomes.append(linha[0])
    enderecos.append(linha[1])
    numeros.append(linha[2])
    
print(pd.Series(nomes))

dados = pd.DataFrame({'Nomes': nomes, 'Endereços': enderecos, 'Telefone': numeros})
print(dados)