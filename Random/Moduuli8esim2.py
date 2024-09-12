import mysql.connector

# tietokantayhteyden luominen funktion avulla
def get_db_connection():
    return mysql.connector.connect(
        host='localhost', # localhost
        #port=3306,
        database='flightgame',
        user='',
        password='',
        autocommit=True,
        # tarvitaan uudelle 9.0 versiolle ajurista:
        collation='utf8mb4_general_ci'
        )

def fetch_airport_by_icao(code):
    connection = get_db_connection()
    sql = f"SELECT name, municipality FROM airport WHERE ident='{code}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    result_row = cursor.fetchone()
    #print(result_row)
    return result_row

# pääohjelma kysyy syötteen, ja käyttää sitä funktiokutsun parametrina
user_input = input("Anna icao koodi.: ")
# muutetaan kaikki merkkijonon kirjaimet isoiksi (varmmuden vuoksi)
user_input = user_input.upper()
result = fetch_airport_by_icao(user_input)
# Jos result muuttujan arvo on jotain muuta kuin None (tai False)
if result: # sama kuin vertailu: result != None
    print(f"Haettu kenttä: {result[0]}, {result[1]}")
else:
    print(f"Eipä löydy.")