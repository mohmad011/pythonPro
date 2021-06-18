#!/bin/bash

while true
do
echo "Inter URL For Video:"
read url

youtube-dl -F --no-playlist $url

notify-send "Program Get All Formats" \

echo "Do You audio or video (a or v):"
read av

echo "Inter Quality:"
read q

if [[ ! -d pwd/Audio ]] && [[ $av == 'a' ]]
then
    mkdir Audio
    cd Audio
    youtube-dl -f $q --no-playlist --no-warnings $url
fi

if [[ ! -d pwd/Video ]] && [[ $av == 'v' ]]
then
    mkdir Video
    cd Video
    youtube-dl -f $q --no-playlist --no-warnings $url
fi

cd ..

notify-send "Video Downloaded!!" \

youtube-dl -e --no-playlist $url

notify-send "Program End!!" \


done
