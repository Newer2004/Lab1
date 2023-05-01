import psycopg2

conn = psycopg2.connect("dbname=suppliers2 user=postgres password=kz999nsk")

# connect to the PostgreSQL server
        # create a cursor
cur = conn.cursor()
        
	# execute a statement
print('PostgreSQL database version:')
cur.execute('SELECT version()')

        # display the PostgreSQL database server version
db_version = cur.fetchone()
print(db_version)
       
	# close the communication with the PostgreSQL
cur.close()