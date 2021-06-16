#!/bin/sh

link=$1
if [$link = ""]
then
    echo "what do you want to search?"
    read name
    echo "searching $name"
    python youtube.py "$name"
else
    echo "playing $2 in youtube"
    mpv $1
fi
