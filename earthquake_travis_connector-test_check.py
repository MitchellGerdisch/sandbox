'''
Checks if the earthquake jdbc sink connector based pipeline completed successfully by seeing if the earthquakes table was created and has content
'''
import psycopg2
import os
import time

print("")
print("********************************************************************")
print("CHECKING EARTHQUAKE JDBC SINK CONNECTOR BASED PIPELINE DB")
print ("You should see a database dump that matches the producer records output seen above.")
print("********************************************************************")
print("")

# Connect to the DB
PG_HOST = os.getenv("PG_HOST")
PG_PORT = os.getenv("PG_PORT")
PG_USER = os.getenv("PG_USER")
PG_PASSWORD = os.getenv("PG_PASSWORD")

PG_DB = "defaultdb"
PG_TABLE = "earthquakes"

pg_connection = psycopg2.connect("dbname="+PG_DB+" user="+PG_USER+" host="+PG_HOST+" port="+PG_PORT+" password="+PG_PASSWORD)
pg_cursor = pg_connection.cursor()

# Sleep a bit to make sure the connector has time to get the data and create the table
time.sleep(5) 

# Now dump the data from the postgres table.
# If the table was not created, then it'll fail and throw an error.
# If the table exists but has no data even and the call above showed it found earthquakes, then we got trouble.
pg_cursor.execute("SELECT * FROM "+PG_TABLE+" ORDER BY time DESC;")
pg_records = pg_cursor.fetchall()
for pg_record in pg_records:
	mag = str(pg_record[0])
	id = str(pg_record[1])
	time = str(pg_record[2])
	place = str(pg_record[3])
	lat = str(pg_record[4])
	long = str(pg_record[5])
	print("id: "+id+" mag: "+mag+" time: "+time+"  lat: "+lat+" long: "+long+" place: "+place)
	
pg_connection.close()
