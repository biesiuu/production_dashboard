import sqlite3
import os


print(f"Baza danych: {os.path.abspath('development.sqlite3')}")

conn = sqlite3.connect('development.sqlite3')
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tabele w bazie danych:")
for table in tables:
    print(table[0])

