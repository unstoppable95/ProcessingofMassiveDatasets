import sqlite3
import os
from datetime import datetime

def insert_data(datafile):
    if os.path.isfile(datafile):  # sprawdzamy czy plik istnieje na dysku
        with open(datafile, "r", encoding='utf-8', errors='replace') as content:  # otwieramy plik do odczytu
            for line in content:
                cur.execute('INSERT INTO tracks VALUES(?,?, ?, ?);', (tuple(line.split("<SEP>"))))
    else:
        print("Plik z danymi", datafile, "nie istnieje!")

def insert_data2(datafile):
    if os.path.isfile(datafile):  # sprawdzamy czy plik istnieje na dysku
        with open(datafile, "r", encoding='utf-8', errors='replace') as content:  # otwieramy plik do odczytu
            for line in content:
                cur.execute('INSERT INTO dates (year,month,day) values (?,?,?);',  (tuple(datetime.utcfromtimestamp((int(line.split("<SEP>")[2]))).strftime('%Y-%m-%d').split("-"))))
                cur.execute('INSERT INTO samples VALUES(?,?,?);', ( line.split("<SEP>")[0],line.split("<SEP>")[1] ,cur.lastrowid))

    else:
        print("Plik z danymi", datafile, "nie istnieje!")

def query_small_file():
    """Funkcja pobiera i wyświetla dane z bazy."""
    cur.execute(
        """
        SELECT count(*) FROM tracks
        """)
    uczniowie = cur.fetchall()
    for row in uczniowie:
        print(row[0])

def query_large_file():
    """Funkcja pobiera i wyświetla dane z bazy."""
    cur.execute(
        """
        SELECT count(*) FROM samples
        """)
    uczniowie = cur.fetchall()
    for row in uczniowie:
        print(row[0])
def query_large_file2():
    """Funkcja pobiera i wyświetla dane z bazy."""
    cur.execute(
        """
        SELECT count(*) FROM dates
        """)
    uczniowie = cur.fetchall()
    for row in uczniowie:
        print(row[0])

start = datetime.now()
# utworzenie połączenia z bazą przechowywaną na dysku
# lub w pamięci (':memory:')
con = sqlite3.connect('lab3.db')

# utworzenie obiektu kursora
cur = con.cursor()

# tworzenie tabel
cur.execute("DROP TABLE IF EXISTS tracks;")
cur.execute("DROP TABLE IF EXISTS samples;")
cur.execute("DROP TABLE IF EXISTS dates;")

cur.execute("""
    CREATE TABLE tracks (
  track_id VARCHAR(18) PRIMARY KEY,
  song_id VARCHAR(18) NOT NULL,
  artist VARCHAR(256) DEFAULT NULL,
  title VARCHAR(256) DEFAULT NULL
)""")

cur.execute("""
    CREATE TABLE samples (
  user_id VARCHAR(40) NOT NULL,
  s_track_id VARCHAR(20) NOT NULL,
  date_id INTEGER NOT NULL,
  FOREIGN KEY(date_id) REFERENCES dates(id)
)""")

cur.execute("""
    CREATE TABLE dates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    year INTEGER NOT NULL,
    month INTEGER NOT NULL,
    day INTEGER NOT NULL
)""")


insert_data('unique_tracks.txt')
insert_data2('triplets_sample_20p.txt')


print("Dane unique tracks")
query_small_file()
print("Dane triplets sample")
query_large_file()
print("Dane triplets dates")
query_large_file2()

con.commit()
con.close()

end = datetime.now()
print ("Excecution_time: %s" % (end-start))
