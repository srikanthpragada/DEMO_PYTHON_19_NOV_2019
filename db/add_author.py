import sqlite3

con = sqlite3.connect(r"e:\classroom\python\nov19\catalog.db")
cur = con.cursor()
name = input("Enter Fullname :")
email = input("Enter Email    :")
mobile = input("Enter mobile   :")
cur.execute("insert into authors(fullname,email,mobile) values(?,?,?)",
            (name,email,mobile))
print("No. of rows inserted : ", cur.rowcount)
con.commit()
con.close()
