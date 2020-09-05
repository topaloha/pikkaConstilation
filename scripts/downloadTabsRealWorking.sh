#!/bin/bash

youtube-dl -o "./%(id)s.%(ext)s" --no-warnings --rm-cache-dir --skip-download --sub-lang en  --sub-format vtt --write-sub --write-auto-sub -i --no-call-home --external-downloader aria2c --external-downloader-args '-c -j 3 -x 3 -s 3 -k 1M'  https://www.youtube.com/c/joerogan/videos 