import sqlite3 
conn =   sqlite3.connect('db/database.db')#cursor
cur = conn.cursor()
cur.execute(""" CREATE TABLE IF NOT EXISTS  AREAAREA ( id INTEGER PRIMARY KEY ,  id1 TEXT, id2 TEXT  )""")
conn.commit()
idarea1 = int(input('Введите id первой области :'))
idarea2 = int(input('Введите id второй области :'))

def addarea ():
 cur.execute("INSERT INTO AREAAREA VALUES( NULL, ?, ?)", ( idarea1,idarea2))
 conn.commit()

def deleteare ():
     cur.execute("""DELETE FROM AREAAREA WHERE  id1 = ?, id2 = ?""", (idarea1,idarea2))
     conn.commit()


deleteare()



conn.commit()







