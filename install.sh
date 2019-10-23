#! /bin/bash

# 
#            --------------------------------------------------
#                           Mouse Payload Loader                
#            --------------------------------------------------
#          Copyright (C) <2015>  <Entynetproject (Ivan Nikolsky)>
#
#        This program is free software: you can redistribute it and/or modify
#        it under the terms of the GNU General Public License as published by
#        the Free Software Foundation, either version 3 of the License, or
#        any later version.
#
#        This program is distributed in the hope that it will be useful,
#        but WITHOUT ANY WARRANTY; without even the implied warranty of
#        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#        GNU General Public License for more details.
#
#        You should have received a copy of the GNU General Public License
#        along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
#    About Author :   
#    Founder   : Entynetproject (Ivan Nikolsky)
#    Site      : http://entynetproject.simplesite.com/
#    Instagram : @entynetproject 
#    Twitter   : @entynetproject
#    Email     : entynetproject@gmail.com
#

RS="\033[1;31m"
YS="\033[1;33m"
CE="\033[0m"

if [[ $EUID -ne 0 ]]
then
   sleep 1
   echo -e "["$RS"*"$CE"] "$RS"This script must be run as "$YS"root"$C"" 1>&2
   sleep 1
   exit
fi

if [[ -d ~/geospy ]]
then
cd ~/geospy/bin
{
cp geospy /usr/local/bin
chmod +x /usr/local/bin/geospy
cp geospy /bin
chmod +x /bin/geospy
} &> /dev/null
else
cd ~
{
git clone https://github.com/entynetproject/geospy.git
cd ~/geospy/bin
cp geospy /usr/local/bin
chmod +x /usr/local/bin/geospy
cp geospy /bin
chmod +x /bin/geospy
} &> /dev/null
fi
sleep 0.5
cd ~/geospy
python banner.py

if [[ -f /etc/geospy.conf ]]
then

CONF="$( cat /etc/geospy.conf )"
sleep 1

if [[ "$CONF" = "arm" ]]
then
if [[ -d /System/Library/CoreServices/SpringBoard.app ]]
then
echo ""$GNS"Installing dependencies..."$CE""
else 
echo ""$GNS"Installing dependencies..."$CE""
pkg update
pkg install python
pkg install python-pip
fi
fi

if [[ "$CONF" = "amd" ]]
then
if [[ -d /System/Library/CoreServices/Finder.app ]]
then
echo ""$GNS"Installing dependencies..."$CE""
else
echo ""$GNS"Installing dependencies..."$CE""
apt-get update
apt-get install python
apt-get install python-pip
fi
fi

if [[ "$CONF" = "intel" ]]
then
if [[ -d /System/Library/CoreServices/Finder.app ]]
then
echo ""$GNS"Installing dependencies..."$CE""
else
echo ""$GNS"Installing dependencies..."$CE""
apt-get update
apt-get install python
apt-get install python-pip
fi
fi

else
read -e -p $'\033[1;34m- \033[0mSelect your architecture (amd/intel/arm) \033[33m~> \033[0m' CONF
if [[ "$CONF" = "" ]]
then
exit
else
if [[ "$CONF" = "arm" ]]
then
read -e -p $'\033[1;34m- \033[0mIs this a single board computer (yes/no)? \033[33m~> \033[0m' PI
if [[ "$PI" = "yes" ]]
then
echo "amd" >> /etc/geospy.conf
CONF="amd"
else
echo "$CONF" >> /etc/geospy.conf
fi
fi
fi
sleep 1

if [[ "$CONF" = "arm" ]]
then
if [[ -d /System/Library/CoreServices/SpringBoard.app ]]
then
echo ""$GNS"Installing dependencies..."$CE""
else 
echo ""$GNS"Installing dependencies..."$CE""
pkg update
pkg install python
pkg install python-pip
fi
fi

if [[ "$CONF" = "amd" ]]
then
if [[ -d /System/Library/CoreServices/Finder.app ]]
then
echo ""$GNS"Installing dependencies..."$CE""
else
echo ""$GNS"Installing dependencies..."$CE""
apt-get update
apt-get install python
apt-get install python-pip
fi
fi

if [[ "$CONF" = "intel" ]]
then
if [[ -d /System/Library/CoreServices/Finder.app ]]
then
echo ""$GNS"Installing dependencies..."$CE""
else
echo ""$GNS"Installing dependencies..."$CE""
apt-get update
apt-get install python
apt-get install python-pip
fi
fi
fi
