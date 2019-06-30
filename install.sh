#! /bin/bash

RSA="\033[31m"
YSA="\033[1;93m"
CEA="\033[0m"
WHS="\033[0;97m"

WHO="$( whoami )"

if [[ "$WHO" != "root" ]]
then
    echo -e ""$RSA"[-]"$WHS" [Errno 1] Can't get privilegies"$CEA""
    exit
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
