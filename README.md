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

# About mouse (MPL)

<img width="1438" alt="mpl" src="https://user-images.githubusercontent.com/43011806/61304748-f28c2480-a7e9-11e9-98eb-31e0ef33f09e.png">

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

<img width="1440" alt="payloads" src="https://user-images.githubusercontent.com/43011806/61581483-fe942100-ab1e-11e9-96e9-76a4a3da6b4a.png">

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
    
## MacOS Application payload

    INFO: This is a standart Mouse (MPL) Payload 
    that converted to the MacOS Application.
    
***

# Mouse CLI

<img width="1440" alt="cli" src="https://user-images.githubusercontent.com/43011806/62371639-a0f7cf80-b535-11e9-97e1-5298c99c117a.png">

    INFO: After a session is established, we can execute commands on that device 
    through the Mouse (MPL) CLI. We can show all available commands by typing "help".
    
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

<img width="1440" alt="mh" src="https://user-images.githubusercontent.com/43011806/62371637-a0f7cf80-b535-11e9-95cb-d2801225aa78.png">

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

<img width="1440" alt="s" src="https://user-images.githubusercontent.com/43011806/62371839-1cf21780-b536-11e9-91f9-dfa4d211aa27.png">

    INFO: MPL commands are commands that allow you to control a remote device via 
    Mouse CLI or via MultiHandler CLI. Each operating system of the remote device has 
    its own set of MPL commands. You can explore supported operating systems bellow.
    
## Local commands

<img width="1434" alt="exec" src="https://user-images.githubusercontent.com/43011806/61304762-f4ee7e80-a7e9-11e9-946b-9c45395fde2c.png">

    clear          : Clear terminal input/output.
    help           : Show all available commands.
    exec           : Execute local shell commands.
    exit           : Close current session and exit.

## System commands

<img width="1434" alt="mount" src="https://user-images.githubusercontent.com/43011806/61304757-f3bd5180-a7e9-11e9-90e2-d4c2e14045b8.png">

### macOS

    cat            : Concatenate and print files.
    cd             : Change current directory.
    chflags        : Change flags on file.
    chgrp          : Change files groups.
    chmod          : Change permissions.
    cp             : Copy files or directories.
    date           : Display current date.
    du             : Display disk usage statistics.
    echo           : Write arguments to standard output.
    hash           : Display last executed commands.
    head           : Display first new lines of file.
    kill           : Terminate or signal a process.
    killall        : Kill process by name.
    ln             : Create softlink on oldname.  
    ls             : List contents of a directory.
    mkdir          : Create directories.
    more           : Read contents of a file.
    mount          : Mount file systems.
    mv             : Move files or directories.
    netstat        : Show network status.
    ps             : Show process status.
    pwd            : Show current directory.
    read           : Read user input.
    rm             : Remove files or directories.
    rmdir          : Remove directories.
    sudo           : Execute command as root.
    ssh            : OpenSSH SSH client.
    syscmds        : Display all system commands.
    time           : Display current time.
    touch          : Create files.
    trap           : Configure signals.
    w              : List terminal sessions.
    
### iOS

    cat            : Concatenate and print files.
    cd             : Change current directory.
    chflags        : Change flags on file.
    chgrp          : Change files groups.
    chmod          : Change permissions.
    cp             : Copy files or directories.
    date           : Display current date.
    du             : Display disk usage statistics.
    echo           : Write arguments to standard output.
    hash           : Display last executed commands.
    head           : Display first new lines of file.
    kill           : Terminate or signal a process.
    killall        : Kill process by name.
    ln             : Create softlink on oldname.  
    ls             : List contents of a directory.
    mkdir          : Create directories.
    more           : Read contents of a file.
    mount          : Mount file systems.
    mv             : Move files or directories.
    netstat        : Show network status.
    ps             : Show process status.
    pwd            : Show current directory.
    read           : Read user input.
    rm             : Remove files or directories.
    rmdir          : Remove directories.
    sudo           : Execute command as root.
    ssh            : OpenSSH SSH client.
    syscmds        : Display all system commands.
    time           : Display current time.
    touch          : Create files.
    trap           : Configure signals.
    w              : List terminal sessions.
    
## Settings commands

<img width="1440" alt="mc" src="https://user-images.githubusercontent.com/43011806/62374110-80cb0f00-b53b-11e9-9450-e15dffb03d03.png">

### macOS

    getpaste       : Get pasteboard contents.
    getvol         : Get speaker output volume.
    idletime       : Get the amount of user activity time.
    setbright      : Set screen brightness.
    setvol         : Set output volume.

### iOS

    battery        : Get battery level.
    getvol         : Get volume level.
    location       : Toggle location services.
    mute           : Update and view mute status.
    setvol         : Set output volume.
    sysinfo        : View system information.
    
## Substrate commands

### iOS

    dhome          : Simulate a double home button press.
    home           : Simulate a home button press.

## Development commands

<img width="1435" alt="py" src="https://user-images.githubusercontent.com/43011806/61306735-61b74800-a7ed-11e9-87af-d384a5c71129.png">

### macOS

    clang          : The Clang compiler.
    make           : GNU make utility.
    osascript      : Execute OSA scripts.
    python         : The Python compiler.
    
### iOS

    clang          : The Clang compiler.
    make           : GNU make utility.
    python         : The Python compiler.

## Trolling commands

<img width="1432" alt="alert" src="https://user-images.githubusercontent.com/43011806/61304761-f455e800-a7e9-11e9-9675-62085387b10d.png">

### macOS

    alert          : Make alert show up on device.
    chwall         : Change desktop wallpaper.
    close          : Close application.
    imessage       : Send message through the messages app.
    itunes         : Control iTunes player.
    keyboard       : Control target's keyboard.
    kill           : Terminate or signal a process.
    killall        : Kill process by name.
    open           : Open application.
    say            : Convert text to speach.
    
### iOS

    alert          : Make alert show up on device.
    dial           : Dial a phone number.
    ipod           : Control music player.
    kill           : Terminate or signal a process.
    killall        : Kill process by name.
    lastapp        : Open last opened application.
    open           : Open application.
    openurl        : Open URL on device.
    say            : Convert text to speach.
    vibrate        : Vibrate device.

## Stealing commands

<img width="1440" alt="screen" src="https://user-images.githubusercontent.com/43011806/61304756-f3bd5180-a7e9-11e9-8e6b-5d428e779161.png">

### macOS

    download       : Download remote file.
    getfacebook    : Retrieve facebook session cookies.
    mic            : Record mic sound.
    picture        : Take picture through iSight.
    prompt         : Prompt user to type password.
    screenshot     : Take screenshot.
    
### iOS

    download       : Download remote file.
    getcontacts    : Download addressbook.
    getnotes       : Download notes.
    getpasscode    : Retreive the device passcode.
    getsms         : Download SMS data.
    locate         : Get device location coordinates.
    mic            : Record mic sound.
    picture        : Take picture through the camera.
    
## Boot commands

### macOS

    reboot         : Reboot device.
    shutdown       : Shutdown device.
    sleep          : Put device into sleep mode.
    suspend        : Suspend current session.
    
### iOS

    reboot         : Reboot device.
    respring       : Restart SpringBoard.
    safemode       : Put device into SafeMode.
    shutdown       : Shutdown device.

## Other commands

<img width="1440" alt="su" src="https://user-images.githubusercontent.com/43011806/61306733-61b74800-a7ed-11e9-8db1-a8550b71ba24.png">

### macOS

    icons          : List system alert icons.
    pid            : Get MPL process ID.
    su             : Login as root.
    upload         : Upload local file.

### iOS

    bundleids      : List bundle identifiers.
    islocked       : Check if the device is locked.
    pid            : Get MPL process ID.
    upload         : Upload local file.

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

# Thats all!
