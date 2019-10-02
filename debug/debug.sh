#! /bin/bash

if [[ -d ~/mouse ]]
then
    sleep 0
    exit
    else
        cd ~
        {
        git clone https://github.com/entynetproject/mouse.git
        } &> /dev/null
        exit
        fi
