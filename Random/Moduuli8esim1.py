import mysql.connector

# "tallennetaan" connect.funktionpaluttama yhteys muuttujaan
# jatkokäyttöä varten
connection = mysql.connector.connect(
         host='localhost', # localhost
         #port=3306,
         database='flightgame',
         user='',
         password='',
         autocommit=True,
        # tarvitaan uudelle 9.0 versiolle ajurista:
         collation='utf8mb4_general_ci'
         )
#print(connection)
cursor = connection.cursor()
result = cursor.execute("SELECT name, iso_country FROM country")
#result = cursor.fetchone()
#print(result[0])
# fetchmany palauttaa n seuraavaa osoittiminen kohdalta
#result = cursor.fetchmany(3)
#print(result)
#fetchall() palauttaa kaikki (loput)
result = cursor.fetchall()
# tulosrivien lukumäärä
print(cursor.rowcount)
print(result)
#result = cursor.fetchall()
#print(*result, sep = "\n")
