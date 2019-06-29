#! /bin/bash

RSA="\033[1;31m"
YSA="\033[1;93m"

WHO="$( whoami )"

if [[ "$WHO" != "root" ]]
then
    echo -e ""$RSA"[*]"$CEA" Errno [001] Can't get privilegies"
exit
fi

rm /bin/mouse
rm /usr/local/bin/mouse
cd
rm -r mouse

if [[ -d /System/Library/CoreServices/SpringBoard.app ]]
then
    uicache -r
fi
