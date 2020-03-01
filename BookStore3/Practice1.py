#import psycopg2
import psycopg2

# conn = psycopg2.connect("data1.db")
# c =conn.cursor()
# c.execute("INSERT into resto VALUES(?,?)",(3,'sunil'))
# conn.commit()
# conn.close()

def create():
    con = psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    c =con.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS family (item TEXT,qunatity INTEGER,price REAL)")
    con.commit()
    con.close()

def insert(item,quantity,price):
    con = psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    c = con.cursor()
    c.execute("INSERT INTO family VALUES ('%s','%s','%s')" % (item,quantity,price))
    con.commit()
    con.close()

def view():
    con = psycopg2.connect("data1.db")
    c = con.cursor()
    c.execute("SELECT * FROM family")
    rows = c.fetchall()
    con.close()
    return rows

def delete(item):
    con = psycopg2.connect("data1.db")
    c = con.cursor()
    c.execute("DELETE FROM family WHERE item=?",(item,))
    con.commit()
    con.close()

def update(item,quantity,price):
    con = psycopg2.connect("data1.db")
    c = con.cursor()
    c.execute("UPDATE family SET WHERE item=?,quantity=?, price=?",(item,quantity,price))
    con.commit()
    con.close()

create()
insert("Shoes",1,1000)
# update(?,?,?)
# delete('Shirt')
# print(view())