#! /bin/bash

rm /bin/mouse
rm /usr/local/bin/mouse
cd
rm -r mouse

if [[ -d /System/Library/CoreServices/SpringBoard.app ]]
then
uicache -r
fi
