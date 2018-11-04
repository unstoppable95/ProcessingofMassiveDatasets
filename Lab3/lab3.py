import sqlite3
import os
from datetime import datetime

def insert_data_tracks(cur,datafile):
    if os.path.isfile(datafile):
        with open(datafile, "r", encoding='iso-8859-2', errors='replace') as content:
            for line in content:
                cur.execute('INSERT OR REPLACE INTO tracks VALUES(?,?, ?, ?);', (tuple(line.strip().split("<SEP>"))))
    else:
        print("Plik z danymi", datafile, "nie istnieje!")


def insert_data_samples_dates(cur,datafile):
    if os.path.isfile(datafile):
        with open(datafile, "r", encoding='iso-8859-2', errors='replace') as content:
            for line in content:
               cur.execute('INSERT INTO dates (year,month,day) values (?,?,?);',  (tuple(datetime.utcfromtimestamp((int(line.split("<SEP>")[2]))).strftime('%Y-%m-%d').split("-"))))
               cur.execute('INSERT INTO samples VALUES(?,?,?);', ( line.split("<SEP>")[0],line.split("<SEP>")[1] ,cur.lastrowid))
    else:
        print("Plik z danymi", datafile, "nie istnieje!")

def select_count(cur, tablename):
    cur.execute(
        """
        SELECT count(*) FROM ?
        """, tablename)
    uczniowie = cur.fetchall()
    for row in uczniowie:
        print(row[0])

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
    FOREIGN KEY(date_id) REFERENCES dates(id),
    FOREIGN KEY(song_id) REFERENCES tracks(song_id)
    )""")

    cur.execute("""
    CREATE TABLE dates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    year INTEGER NOT NULL,
    month INTEGER NOT NULL,
    day INTEGER NOT NULL
    )""")

def create_index(con):
    con.execute('DROP INDEX IF EXISTS song_id_idx')
    con.execute('CREATE INDEX song_id_idx ON samples(song_id)')
    con.execute('DROP INDEX IF EXISTS tracks_artist_idx')
    con.execute('CREATE INDEX tracks_artist_idx ON tracks(artist)')

def task_1(cur):
    cur.execute(
        """
         SELECT t.title, t.artist, songs.sum FROM ( SELECT song_id, COUNT(song_id) AS sum FROM samples GROUP BY song_id ORDER BY sum DESC LIMIT 10) songs
        JOIN tracks t ON t.song_id = songs.song_id ORDER BY songs.sum DESC;
        """)

    for tuple in cur.fetchall():
        print(" ".join(map(str, tuple)))

def task_2(cur):
    cur.execute(
        """
        select user_id, count(distinct song_id) as number from samples group by user_id order by number DESC limit 10;
        """)

    for tuple in cur.fetchall():
        print(" ".join(map(str, tuple)))

def task_3(cur):
    cur.execute(
        """
        select t.artist, count(*) as counter from tracks t join samples s on t.song_id=s.song_id group by t.artist order by counter desc limit 1;
        """)

    for tuple in cur.fetchall():
        print(" ".join(map(str, tuple)))

def task_4(cur):
    cur.execute(
        """
        select d.month, count(s.song_id) from dates d join samples s on s.date_id = d.id group by d.month order by d.month;
        """)

    for a in cur.fetchall():
        print(" ".join(map(str, a)))

def task_5(cur):
    cur.execute(
        """
        SELECT user_id FROM samples WHERE song_id IN (SELECT samples.song_id FROM samples JOIN tracks on samples.song_id = tracks.song_id AND tracks.artist LIKE 'Queen'
        GROUP BY samples.song_id ORDER BY COUNT(samples.song_id) DESC LIMIT 3) GROUP BY user_id HAVING COUNT(DISTINCT samples.song_id) >= 3 ORDER BY user_id LIMIT 10;
        """)

    for tuple in cur.fetchall():
        print(" ".join(map(str, tuple)))



def main():
    con = sqlite3.connect('lab3.db')
    cur = con.cursor()
    #create tables
    create_tables(cur)

    #load data
    # start = datetime.now()
    insert_data_tracks(cur,'unique_tracks.txt')
    insert_data_samples_dates(cur,'triplets_sample_20p.txt')
    create_index(con)
    con.commit()

    #tasks
    task_1(cur)
    task_2(cur)
    task_3(cur)
    task_4(cur)
    task_5(cur)


    # end = datetime.now()
    # print("Excecution time total : %s" % (end-start))
    con.close()


if __name__ == "__main__":
    main()