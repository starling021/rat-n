# Mouse Payload Loader (MPL)

               _     __,..---""-._                 ';-,
        ,    _/_),-"`             '-.                `\
       \|.-"`    -_)                 '.                ||
       /`   a   ,                      \              .'/
       '.___,__/                 .-'    \_        _.-'.'
          |\  \      \         /`        _``_.-'
             _/;--._, >        |   --.__/ ``
           (((-'  __//`'-......-;\      )
                (((-'       __//  '--. /   mouse/MPL
                          (((-'    __//
                                 (((-'

***

# About mouse

    INFO: Mouse Payload Loader (MPL) is a post exploitation surveillance tool written 
    in Python, C and Objective-C. It gives you a command line session with extra functionality 
    between you and a target machine with simple MPL payload. MPL gives you the power and convenience 
    of uploading/downloading files, tab completion, taking pictures, location tracking, shell command 
    execution, persistence, escalating privileges, password retrieval, and much more.
  
***
    
# Getting started

## macOS/Linux installation

> cd mouse

> chmod +x install.sh

> ./install.sh

## iOS (jailbroken) installation

> cd mouse

> chmod +x install.sh

> ./install.sh

***

# Building payloads (macOS/iOS)

    INFO: MPL payloads are executed on the target machine. The payload first sends over 
    instructions for getting and sending back device details to our server and then chooses 
    the appropriate executable to establish a secure remote control session.

## Bourne-Again Shell payload

    INFO: Selecting bash from the payload menu will give us a 1 liner that 
    establishes a remote MPL session upon execution on the target machine.
    
## Entynet PI payload (USB injection)

    INFO: Entynet PI is a development board that can be programmed 
    with the Arduino IDE. It emulates USB keyboard strokes extremely 
    fast and can inject the MPL payload just in a few seconds.
    
    Developer: Entynetproject (Ivan Nikolsky)

## Rubber Duck payload (USB injection)

    INFO: USB Rubber Duck is a development USB board that can inject 
    uploaded to duck SD card inject.bin payload in a few seconds!
    
    Developer: Hak5 (Darren Kitchen)
    
***

# Mouse CLI

    INFO: After a session is established, we can execute commands on that device 
    through the Mouse CLI. We can show all available commands by typing "help".
    
## Taking pictures

    INFO: Both iOS and macOS payloads have picture taking capability. 
    The picture command lets you take a picture from the iSight on 
    macOS as well as the front or back camera on iOS.
    
## Tab completion

    INFO: Similar to most command line interfaces, MPL supports 
    tab completion. When you start typing the path to a directory or 
    filename, we can complete the rest of the path using the tab key.

***

# MultiHandler CLI

    INFO: The Multihandler option lets us handler multiple 
    sessions. We can choose to interact with different devices 
    while listening for new connections in the background.
    
***

# Mouse Substrate (MPL Substrate)

    INFO: Mouse Substrate (MPL Substrate) is a package that will 
    be installed on the victim's iOS device after receiving remote 
    control. Mouse Substrate allows you to run substrate commands 
    and services on the victim’s remote iOS device.

***
    
# MPL commands

    INFO: MPL commands are commands that allow you to control a remote device via 
    Mouse CLI or via MultiHandler CLI. Each operating system of the remote device has 
    its own set of MPL commands. You can explore supported operating systems bellow.

## macOS

    setbright      : Set screen brightness.
    cd             : Change directory.
    download       : Download file.
    getfacebook    : Retrieve facebook session cookies.
    getpaste       : Get pasteboard contents.
    getvol         : Get speaker output volume.
    idletime       : Get the amount of time since the keyboard/cursor were touched.
    imessage       : Send message through the messages app.
    itunes         : iTunes Controller.
    keyboard       : Your keyboard -> is target's keyboard.
    lazagne        : Firefox password retrieval.
    ls             : List contents of a directory.
    mic            : Record mic sound.
    picture        : Take picture through iSight.
    pid            : Get MPL process ID.
    prompt         : Prompt user to type password.
    pwd            : Show current directory.
    screenshot     : Take screenshot.
    setvol         : Set output volume.
    sleep          : Put device into sleep mode.
    su             : Login as root.
    suspend        : Suspend current session.
    upload         : Upload local file.

## iOS

    alert          : Make alert show up on device.
    battery        : Get battery level.
    bundleids      : List bundle identifiers.
    cd             : Change directory.
    dhome          : Simulate a double home button press.
    dial           : Dial a phone number.
    download       : Download file.
    getcontacts    : Download addressbook.
    getnotes       : Download notes.
    getpasscode    : Retreive the device passcode.
    getsms         : Download SMS.
    getvol         : Get volume level.
    home           : Simulate a home button press.
    ipod           : Control music player.
    islocked       : Check if the device is locked.
    lastapp        : Get last opened application.
    locate         : Get device location coordinates.
    location       : Toggle location services.
    lock           : Simulate a lock button press.
    ls             : List contents of a directory.
    mic            : Record mic sound.
    mute           : Update and view mute status.
    open           : Open application.
    openurl        : Open URL on device.
    picture        : Take picture through iSight.
    pid            : Get MPL process ID.
    pwd            : Show current directory.
    respring       : Restart SpringBoard.
    safemode       : Put device into safe mode.
    say            : Text to speach.
    setvol         : Set output volume.
    sysinfo        : View system information.
    upload         : Upload local file.
    vibrate        : Vibrate device.
    
***

# Terms of use

    This tool is only for educational purposes only.
    Use this tool wisely and never without permission.
    I am not responsible for anything you do with this tool.

***

# Mouse (MPL) license
 
        --------------------------------------------------
                       Mouse Payload Loader          
        --------------------------------------------------
      Copyright (C) <2015>  <Entynetproject (Ivan Nikolsky)>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.                

***

# Mouse substrate license
 
        --------------------------------------------------
                          Mouse Substrate                  
        --------------------------------------------------
      Copyright (C) <2015>  <Entynetproject (Ivan Nikolsky)>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.                

***

# Thats all!
