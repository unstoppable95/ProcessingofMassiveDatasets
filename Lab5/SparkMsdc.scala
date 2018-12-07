//Read data
val songs = spark.read.option("delimiter",";").csv("tracks.txt").
toDF("track_id","song_id", "artist","song")

val facts = spark.read.option("delimiter",";").csv("samples.txt").
toDF( "user_id","song_id","date_id")

val dates = spark.read.option("delimiter",";").csv("dates.txt").
toDF( "date_id","day","month", "day")

//query 1 -> The most popular songs
facts.groupBy("song_id").
count.join(songs,facts("song_id")===songs("song_id")).
select("song","artist","count").
orderBy(desc("count")).
show(10)

//query 2 -> Top 10 users which listened the biggest number of unique songs 
facts.select("user_id","song_id").
distinct().
groupBy("user_id").
count().
select("user_id","count").
orderBy(desc("count")).
show(10,false)

//query 3 -> The most popular artist 
facts.select("song_id").
join(songs, "song_id").
groupBy("artist").
count().
select("artist","count").
orderBy(desc("count")).
show(1)

//query 4 -> The most popular songs for each month
facts.join(dates, "date_id").
groupBy("month").
count().
select("month","count").
orderBy("month").
show(12)

//query 5 -> 10 users who listened all 3 most popular songs prepared by Queen 
val Queens3Popular = songs.select("song_id","artist").
filter($"artist".isin("Queen")).
join(facts, "song_id").
groupBy("song_id").
count().
orderBy(desc("count")).
select("song_id").limit(3)

facts.select("user_id","song_id").
join(Queens3Popular,"song_id").
distinct().
groupBy("user_id").
count().
filter($"count">=3).
orderBy("user_id").
select("user_id").
show(10,false)