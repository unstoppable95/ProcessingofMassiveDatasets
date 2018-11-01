import sqlite3
import os


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
                cur.execute('INSERT INTO samples VALUES(?,?, ?);', (tuple(line.split("<SEP>"))))
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



# utworzenie połączenia z bazą przechowywaną na dysku
# lub w pamięci (':memory:')
con = sqlite3.connect('lab3.db')

# utworzenie obiektu kursora
cur = con.cursor()
# tworzenie tabel
cur.execute("DROP TABLE IF EXISTS tracks;")
cur.execute("DROP TABLE IF EXISTS samples;")

cur.execute("""
    CREATE TABLE tracks (
  track_id varchar(18) NOT NULL,
  song_id varchar(18) NOT NULL,
  artist varchar(256) DEFAULT NULL,
  title varchar(256) DEFAULT NULL,
  PRIMARY KEY (track_id)
)""")

cur.execute("""
    CREATE TABLE samples (
  user_id varchar(40) NOT NULL,
  s_track_id varchar(20) NOT NULL,
  hear_date varchar(20) DEFAULT NULL
)""")

insert_data('unique_tracks.txt')
insert_data2('triplets_sample_20p.txt')

print("Dane unique tracks")
query_small_file()
print("Dane triplets dample")
query_large_file()
con.commit()
con.close()

