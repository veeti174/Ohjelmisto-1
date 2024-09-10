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
sql = "SELECT name, iso_country FROM country"
sql2 = "SELECT name, iso_country FROM country WHERE name='ä'"
cursor.execute(sql)
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
#Tulostetaan toisen tulosrivin maakoodi (2. monikon alkio)
#print(result[1][1])
# käsitellään koko tulosjoukko (lista) toistorakenteella
for row in result:
    print(f"Maan {row[0]} maakoodi {row[1]}.")
print(f"Maita yhteensä: {cursor.rowcount}")
if cursor.rowcount == 0:
    print("Ei yhtään maata.")