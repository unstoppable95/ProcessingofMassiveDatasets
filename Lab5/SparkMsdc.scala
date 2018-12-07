//Read data
val songs = spark.read.option("delimiter",";").csv("tracks.txt").
toDF("track_id","song_id", "artist","song")

val facts = spark.read.option("delimiter",";").csv("samples.txt").
toDF( "user_id","song_id","date_id")

val dates = spark.read.option("delimiter",";").csv("dates.txt").
toDF( "date_id","day","month", "day")

//query 1 The most popular songs
facts.groupBy("song_id").
count.join(songs,facts("song_id")===songs("song_id")).
select("song","artist","count").
orderBy(desc("count")).
show(10)


//query 3 The most popular artist 

//query 4 The most popular songs for each month
facts.join(dates, "date_id").
groupBy("month").
count().
select("month","count").
orderBy("month").
show(12)


