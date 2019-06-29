#! /bin/bash

RSA="\033[1;91m"
YSA="\033[1;93m"
CEA="\033[0m"

WHO="$( whoami )"

if [[ "$WHO" != "root" ]]
then
    echo -e ""$RSA"[*]"$CEA" Errno [001] Can't get privilegies"
exit
fi

{
rm /bin/mouse
rm /usr/local/bin/mouse
cd
rm -r mouse
} &> /dev/null

if [[ -d /System/Library/CoreServices/SpringBoard.app ]]
then
    uicache -r
fi
