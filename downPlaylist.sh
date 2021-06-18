#!/bin/bash

while true
do
echo "Inter URL For Video:"
read url

youtube-dl -F $url

notify-send "Program Get All Formats" \

echo "Do You audio or video (a or v):"
read av

echo "Inter Quality:"
read q

if [[ ! -d pwd/AudioList ]] && [[ $av == 'a' ]]
then
    mkdir AudioList
    cd AudioList
    youtube-dl -f $q --no-warnings $url
fi

if [[ ! -d pwd/VideoList ]] && [[ $av == 'v' ]]
then
    mkdir VideoList
    cd VideoList
    youtube-dl -f $q --no-warnings $url
fi

cd ..

notify-send "Video Downloaded!!" \

youtube-dl -e $url

notify-send "Program End!!" \

done
