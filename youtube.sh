#!/bin/sh

link=$1
if [$link = ""]
then
    echo "what do you want to search?"
    read name
    echo "searching $name"
    python /home/vanarp/Desktop/github/youtube_scrap.py "$name"
else
    echo "playing $2 in youtube"
    mpv $1
fi
