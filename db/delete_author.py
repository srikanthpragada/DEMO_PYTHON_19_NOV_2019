import sqlite3

con = sqlite3.connect(r"e:\classroom\python\nov19\catalog.db")
cur = con.cursor()
email = input("Enter Email :")
try:
    cur.execute("delete from authors where email = ?", (email,))
    if cur.rowcount == 1:
        con.commit()
        print("Deleted author successfully")
    else:
        print("Author with given email not found!")
except Exception as ex:
    print("Sorry! Could not delete author due to error -> ", ex)


con.close()
