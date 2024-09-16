

import numpy as np
import mysql.connector
airports =[]

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

def fetch_airport_by_IATA(code):
    connection = get_db_connection()
    sql = f"SELECT name, municipality, type FROM airport WHERE iso_country='{code}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    result_row = cursor.fetchall()
    #print(result_row)
    print(cursor.rowcount)
    return result_row


# pääohjelma kysyy syötteen, ja käyttää sitä funktiokutsun parametrina
user_input = input("Anna IATA koodi.: ")
# muutetaan kaikki merkkijonon kirjaimet isoiksi (varmmuden vuoksi)
user_input = user_input.upper()
result = fetch_airport_by_IATA(user_input)
# Jos result muuttujan arvo on jotain muuta kuin None (tai False)
sort(result)
if result: # sama kuin vertailu: result != None
    print(*result, sep ="\n")
sorted_indices = np.argsort(-arr[:,1])
sorted_arr = arr[sorted_indices]


print(sorted_arr)

print(np.sort(result).tolist())

#else:
    #print(f"Eipä löydy.")