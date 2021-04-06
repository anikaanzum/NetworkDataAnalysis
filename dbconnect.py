import psycopg2
conn = psycopg2.connect(database='test', user='postgres', password='')
cur = conn.cursor()
#cur.execute('''select * from \"INC01B\" ''')
cur.execute('''create table course(id serial, name varchar(25));''')
conn.commit()
#cur.execute('''insert into student(id,name) values(1,'anika');''')
#cur.fetchall()
##for row in cur.fetchall():
#    print (row)

cur.close()
conn.close()