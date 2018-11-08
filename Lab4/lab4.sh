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

#concat files
#awk -F ";" 'FNR==NR{A[$2]=$2;next} A[$2]{print $1 t A[$2]}' t=";" tracks.txt samples.txt 
#delete repeates
#awk -F ";" '!seen[$1,$2]++' 

#task 1
awk -F ";" 'FNR==NR{A[$2]=$3t$4t$2;next} A[$2]{print A[$2]}' t=";" tracks.txt samples.txt | awk -F";" '{col[$1t$2t$3]++} END {for (i in col) print i ";" col[i]}' t=";" | sort -t";" -n -k4 -r | head -n 10 | cut -d ";" -f1,2,4 |tr ";" " "


#task 2
awk -F ";" '!seen[$1,$2]++' samples.txt | awk -F ';' ' { arr[$1]++ } END { for( no in arr) { print no , arr[no] } } ' |sort -k2 -r -n | head -n 10

#task 4
join -1 3 -2 1 samples.txt dates.txt -t";" -o'2.3'| sort  | uniq -c  | awk '{print $2,$1}'