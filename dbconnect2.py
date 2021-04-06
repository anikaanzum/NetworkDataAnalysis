hostname = 'localhost'
username = 'postgres'
password = ''
database = 'test'

# Simple routine to run a query on a database and print the results:
def doQuery( conn ) :
    cur = conn.cursor()

    cur.execute( "SELECT * FROM \"INC01B\";" )

print ("Using psycopg2…")
import psycopg2
myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
print(doQuery( myConnection ))
myConnection.close()
'''
print ("Using PyGreSQL…")
import pgdb
myConnection = pgdb.connect( host=hostname, user=username, password=password, database=database )
doQuery( myConnection )
myConnection.close()
'''