#change separator 
sed 's/<SEP>/;/g' triplets_sample_20p.txt > NEW_triplets_sample.txt
sed 's/<SEP>/;/g' unique_tracks.txt > NEW_unique_tracks.txt

#eliminate duplicates/ create result file tracks.txt (track_id;song_id;artist;title)
awk -F ';' '!NF || !seen[$2]++' NEW_unique_tracks.txt > tracks.txt

#create result file samples.txt (user_id;song_id;date_id)
awk -F ';' '{OFS=";"; print $1,$2,NR}' NEW_triplets_sample.txt >samples.txt

#create result file dates.txt (id;year;month;day)
awk -F ";" '{OFS=";"; x=strftime("%Y;%m;%d", $3); print NR ";" x}' NEW_triplets_sample.txt >dates.txt

#check files content
wc -l tracks.txt
head -n 3 tracks.txt
wc -l samples.txt
head -n 3 samples.txt
wc -l dates.txt
head -n 3 dates.txt


#delete temporary files
rm NEW_unique_tracks.txt
rm NEW_triplets_sample.txt