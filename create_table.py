import sqlite3

con = sqlite3.connect('recipes.db')
cur = con.cursor()

cur.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='recipes' ''')

if cur.fetchone()[0]==1 : 
    print('Table exists.')
else :
    print('Table does not exist.')
    cur.execute('''create table recipes
               (id integer primary key, name text, ingredients text, steps text, type character(20))''')      
    con.commit()