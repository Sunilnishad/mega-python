import sqlite3

class Database:

    def __init__(self,db):
        conn = sqlite3.connect(db)
        c= conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY,title TEXT,year TEXT,author TEXT,isbn INTEGER)")
        conn.commit()
        conn.close()

    def insert(self,title,year,author,isbn):
        conn = sqlite3.connect("bookStore.db")
        c = conn.cursor()
        c.execute("INSERT INTO books VALUES(NULL,?,?,?,?)",(title,year,author,isbn))
        conn.commit()
        conn.close()

    def delete(self,id):
        conn = sqlite3.connect("bookStore.db")
        c= conn.cursor()
        c.execute("DELETE FROM books WHERE id=?",(id,))
        conn.commit()
        conn.close()

    def view(self):
        conn = sqlite3.connect("bookStore.db")
        c = conn.cursor()
        c.execute("SELECT * FROM books")
        rows = c.fetchall()
        conn.close()
        return rows

    # In this parameter which is possed it is init. because when the func. is called all value is checked.
    def search(self,title="",year="",author="",isbn=""):
        conn = sqlite3.connect("bookStore.db")
        c = conn.cursor()
        c.execute("SELECT * FROM books WHERE title=? OR year=? OR author =? OR isbn=?",(title,year,author,isbn))
        rows = c.fetchall()
        conn.close()
        return rows

    def update(self,id,title,year,author,isbn):
        conn = sqlite3.connect("bookStore.db")
        c= conn.cursor()
        c.execute("UPDATE books SET title=?,year=?,author=?,isbn=? WHERE id=?",(title,year,author,isbn,id))
        conn.commit()
        conn.close()

#create_table()
#insert("Knight Rider",1995,"Bhushan",125723489)
#print(view())
#print(search(year=1996))
#print(update(2,"Knight Rider",2000,"Bhusan",12678000))