import sqlite3

con = sqlite3.connect(r"e:\classroom\python\nov19\catalog.db")
cur = con.cursor()
id = input("Enter id :")
email = input("Enter Email    :")
try:
    cur.execute("update authors set email = ? where id = ?", (email,id))
    if cur.rowcount == 1:
        con.commit()
        print("Updated details successfully")
    else:
        print("Author id is not found!")
except Exception as ex:
    print("Sorry! Could not update details due to error -> ", ex)


con.close()
