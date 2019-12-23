import sqlite3

con = sqlite3.connect(r"e:\classroom\python\nov19\catalog.db")
cur = con.cursor()
cur.execute("select * from authors")
for row in cur.fetchall():
    print(f"{row[0]:5} {row[1]:20} {row[2]:30} {row[3]}")

cur.execute("select * from authors order by fullname")
for id,name,email,mobile in cur.fetchall():
    print(f"{id:5} {name:20} {email:30} {mobile}")


con.close()
