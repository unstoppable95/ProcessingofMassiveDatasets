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
#wc -l tracks.txt
#head -n 3 tracks.txt
#wc -l samples.txt
#head -n 3 samples.txt
#wc -l dates.txt
#head -n 3 dates.txt

#delete temporary files
rm NEW_unique_tracks.txt
rm NEW_triplets_sample.txt

#task 1
awk -F ";" 'FNR==NR{A[$2]=$3t$4t$2;next} A[$2]{print A[$2]}' t=";" tracks.txt samples.txt | awk -F";" '{col[$1t$2t$3]++} END {for (i in col) print i ";" col[i]}' t=";" | sort -t";" -n -k4 -r | head -n 10 | cut -d ";" -f1,2,4 |tr ";" " "

#task 2
awk -F ";" '!seen[$1,$2]++' samples.txt | awk -F ';' ' { arr[$1]++ } END { for( no in arr) { print no , arr[no] } } ' |sort -k2 -r -n | head -n 10

#task 3
awk -F ";" 'FNR==NR{A[$2]=$3;next} A[$2]{print A[$2]t$2}' t=";" tracks.txt samples.txt | awk -F ";" '{col[$1]++} END {for (i in col) print i ";"col[i]}' | sort -n -t";" -k2 -r | head -n 1 |  tr ";" " "

#task 4
join -1 3 -2 1 samples.txt dates.txt -t";" -o'2.3'| sort  | uniq -c  | awk '{print $2,$1}'

#task 5
#select song_id of 3 Queen's most popular songs
awk -F ";" 'FNR==NR{A[$2]=$3;next} A[$2]{print $2 t A[$2]}' t=";" tracks.txt samples.txt | awk -F ";" '{if ($2 == "Queen") print $0;}' | awk -F ";" '{col[$1]++} END {for (i in col) print i ";"col[i]}' | sort -n -t";" -k2 -r | head -n 3 | cut -d ";" -f1 | awk '{print $1";"}'> Queens_3_songs.txt

#select 10 users,which listen all of 3 most popular Queen's songs
awk -F ";" 'NR==FNR{ a[$1]=$1; next }$2 in a{ print $1t$2 }' t=";" Queens_3_songs.txt samples.txt | sort -u -t";" | awk -F ";" '{col[$1]++} END {for (i in col) print i ";"col[i]}' | grep ';3' |cut -d ";" -f1 | sort | head -n 10

rm Queens_3_songs.txt

#if you want only console result and save some space on disk
#rm dates.txt tracks.txt samples.txt