import sqlite3, csv, io #import der lib

conn = sqlite3.connect("Chinook_Sqlite_AutoIncrementPKs.sqlite")

cur = conn.cursor()
# Ansprechen der lokalen sqlite Datenbank
cur.execute("SELECT * \
                    FROM \
                    Customer \
            ;")

data_csv = "data.csv"

list_data = cur.fetchall()
with open(data_csv, 'w', encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=";", lineterminator="\n", quoting=csv.QUOTE_NONNUMERIC)
    writer.writerows(list_data)
conn.close() 
