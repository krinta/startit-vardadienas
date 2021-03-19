import sqlite3
import csv

DATUBAZE = "vardi.db"


def jauna_db():
  print("Veidojam jaunu DB")
  conn = sqlite3.connect(DATUBAZE)
  c = conn.cursor()
  c.execute('''CREATE TABLE IF NOT EXISTS vardadienas 
              (vards text PRIMARY KEY, diena int NOT NULL, menesis int NOT NULL)''')
  c.execute('''CREATE INDEX IF NOT EXISTS d1 ON vardadienas(diena);''')
  c.execute('''CREATE INDEX IF NOT EXISTS m1 ON vardadienas(menesis);''')
  conn.commit()
  print("Izveidojām jaunu DB")


def importejam_datus():
  vd = []
  with open('vardi.txt', 'r') as f:
    reader = csv.reader(f)
    for varda_dati in reader:
      vd.append(varda_dati)

  conn = sqlite3.connect(DATUBAZE)
  c = conn.cursor()
  print(" importējam datus")
  c.executemany('INSERT INTO vardadienas VALUES (?,?,?)', vd)
  conn.commit()
  print("imports pabeigts")
  conn.close()


def parbauda_db():
  conn = sqlite3.connect(DATUBAZE)
  c = conn.cursor()
  c.execute('SELECT * FROM vardadienas LIMIT 1')
  print(c.fetchone())

importejam_datus()
parbauda_db()