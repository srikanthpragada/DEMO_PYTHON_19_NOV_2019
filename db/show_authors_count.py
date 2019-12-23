import sqlite3

con = sqlite3.connect(r"e:\classroom\python\nov19\catalog.db")
cur = con.cursor()
cur.execute("select count(*) from authors")
row = cur.fetchone()
print("No. of authors : ",row[0])


con.close()
