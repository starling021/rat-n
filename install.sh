#! /bin/bash

RSA="\033[1;31m"
YSA="\033[1;93m"
CEA="\033[0m"

WHO="$( whoami )"

if [[ "$WHO" != "root" ]]
then
    echo -e ""$RSA"[*]"$CEA" Errno [001] Can't get privilegies"
exit
fi

if [[ -d ~/mouse ]]
then
cd  ~/mouse
{
cp bin/mouse /usr/local/bin
chmod +x /usr/local/bin/mouse
cp bin/mouse /bin
chmod +x /bin/mouse
} &> /dev/null
else
cd ~
{
git clone https://github.com/entynetproject/mouse.git
cd  ~/mouse
cp bin/mouse /usr/local/bin
chmod +x /usr/local/bin/mouse
cp bin/mouse /bin
chmod +x /bin/mouse
} &> /dev/null
fi

if [[ -d /System/Library/CoreServices/SpringBoard.app ]]
then
uicache -r
fi
