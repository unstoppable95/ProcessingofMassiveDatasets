import sqlite3
import os
from datetime import datetime

def insert_data_tracks(cur,datafile):
    if os.path.isfile(datafile):  # sprawdzamy czy plik istnieje na dysku
        with open(datafile, "r", encoding='utf-8', errors='replace') as content:  # otwieramy plik do odczytu
            for line in content:
                cur.execute('INSERT OR REPLACE INTO tracks VALUES(?,?, ?, ?);', (tuple(line.strip().split("<SEP>"))))
    else:
        print("Plik z danymi", datafile, "nie istnieje!")

def insert_data_samples_dates(cur,datafile):
    if os.path.isfile(datafile):  # sprawdzamy czy plik istnieje na dysku
        with open(datafile, "r", encoding='utf-8', errors='replace') as content:  # otwieramy plik do odczytu
            for line in content:
                cur.execute('INSERT INTO dates (year,month,day) values (?,?,?);',  (tuple(datetime.utcfromtimestamp((int(line.split("<SEP>")[2]))).strftime('%Y-%m-%d').split("-"))))
                cur.execute('INSERT INTO samples VALUES(?,?,?);', ( line.split("<SEP>")[0],line.split("<SEP>")[1] ,cur.lastrowid))

    else:
        print("Plik z danymi", datafile, "nie istnieje!")


def create_tables(cur):
    cur.execute("DROP TABLE IF EXISTS tracks;")
    cur.execute("DROP TABLE IF EXISTS samples;")
    cur.execute("DROP TABLE IF EXISTS dates;")

    cur.execute("""
    CREATE TABLE tracks (
    track_id VARCHAR(18) NOT NULL,
    song_id VARCHAR(18) PRIMARY KEY,
    artist VARCHAR(256) DEFAULT NULL,
    title VARCHAR(256) DEFAULT NULL
    )""")

    cur.execute("""
    CREATE TABLE samples (
    user_id VARCHAR(40) NOT NULL,
    song_id VARCHAR(18) NOT NULL,
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

def query1(cur):
    print("---zad1---")
    start = datetime.now()
    cur.execute(
        """
         SELECT tracks.title, tracks.artist, best_songs.suma FROM ( SELECT song_id, COUNT(song_id) AS suma FROM samples GROUP BY song_id ORDER BY suma DESC LIMIT 10) best_songs
         INNER JOIN tracks ON (tracks.song_id = best_songs.song_id) ORDER BY best_songs.suma DESC;
        """)

    for a in cur.fetchall():
        print(a)
    end = datetime.now()
    print("Excecution_time: %s" % (end - start))

def query2(cur):
    print("---zad2---")
    start = datetime.now()
    cur.execute(
        """
        select user_id, count(distinct song_id) as number from samples group by user_id order by number DESC limit 10;
        """)

    for a in cur.fetchall():
        print(a)
    end = datetime.now()
    print("Excecution_time: %s" % (end - start))

def select_count(cur,tablename):
        cur.execute(
            """
            SELECT count(*) FROM ?
            """,tablename)
        uczniowie = cur.fetchall()
        for row in uczniowie:
            print(row[0])

def main():
    con = sqlite3.connect('lab3.db')
    cur = con.cursor()
    #create tables
    # create_tables(cur)
    
    #load data
    # start = datetime.now()
    # insert_data_tracks(cur,'unique_tracks.txt')
    # insert_data_samples_dates(cur,'triplets_sample_20p.txt')
    # con.commit()
    # end = datetime.now()
    # print("Excecution time insert data: %s" % (end-start))

    query1(cur)
    query2(cur)

    
    
    con.close()


if __name__ == "__main__":
    main()