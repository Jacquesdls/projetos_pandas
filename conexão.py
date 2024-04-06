import sqlite3
import pandas as pd

con = sqlite3.connect('agenda.db')

cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS CONTATO " +
    " ( nome varchar(100), endereco varchar(100), telefone varchar(20)) ")

resultado = cur.execute("INSERT INTO CONTATO (nome, endereco, telefone) values " +
                        " ('Monica', 'monica@gmail.com', '11998552410')")

con.commit()

con.close()


