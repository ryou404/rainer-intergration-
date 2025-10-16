import sqlite3

#connect to sql and get the permission
conn=sqlite3.connect('product_info.db')
cursor=conn.cursor()

#using permission to execute sql instruction
#cursor.execute('SELECT * FROM product_info')
sqlsel="""
SELECT id, name FROM product_info
WHERE id='2'
"""

#grab execute result and save to python variable, print variable
records=cursor.fetchall()
print (records)

sqlins="""
INSERT INTO "main"."product_info" 
("name", "version", "remark") 
VALUES ('laptop', 'asus', 'vivobook');
"""
cursor.execute(sqlins)
records=cursor.fetchall()
conn.commit()

print (records)

#execute sqlctrl.py
#1: in terminal: python sqlctrl.py
#2: in terminal: python3 sqlctrl.py
#3: in VScode: click 'Run Python File'