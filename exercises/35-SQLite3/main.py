import sqlite3
con = sqlite3.connect("nome_do_banco.db")
cur = con.cursor()
cur.execute("CREATE TABLE contato(nome, endereco, telefone)")
res = cur.execute("SELECT name FROM sqlite_master")
res.fetchone()
('contato',)

cur.execute("INSERT INTO contato VALUES ('Rodrigo', 'Tóquio', '123456789')")
con.commit()

for linha in cur.execute("SELECT name FROM sqlite_master WHERE type='table'"):
    print(linha)

