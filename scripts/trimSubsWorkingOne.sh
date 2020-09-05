#!/bin/bash

# $ chmod u+x scriptname  to make it executable and ./scriptname to run

# this makes subs look fine

for f in /home/d/pikkerConstilation/autoSubs/JowRogan/*

do
	sed '1,/^$/d' <"$f" | sed 's/<[^>]*>//g' | awk -F. 'NR%8==1{printf"%s ",$1}NR%8==3' > "${f%.e*}"

	rm -f $f
	
done

youtube-dl -o "./%(id)s.%(ext)s" --no-warnings --rm-cache-dir --skip-download --sub-lang en  --sub-format vtt --write-sub --write-auto-sub -i --no-call-home --external-downloader aria2c --external-downloader-args '-c -j 3 -x 3 -s 3 -k 1M'  https://www.youtube.com/c/joerogan/videos