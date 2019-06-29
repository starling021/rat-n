# Most Often Useful Super Exploit (Mouse)

               _     __,..---""-._                 ';-,
        ,    _/_),-"`             '-.                `\
       \|.-"`    -_)                 '.                ||
       /`   a   ,                      \              .'/
       '.___,__/                 .-'    \_        _.-'.'
          |\  \      \         /`        _``_.-'
             _/;--._, >        |   --.__/ ``
           (((-'  __//`'-......-;\      )
                (((-'       __//  '--. /   Mouse/RAT
                          (((-'    __//
                                 (((-'

# About mouse

![1](https://user-images.githubusercontent.com/43011806/60388760-a0939100-9abe-11e9-8456-a0abaad9892e.png)

    INFO: Most Often Useful Super Exploit (Mouse) is a post exploitation 
    surveillance tool written in Python, C and Objective-C. It gives you a command 
    line session with extra functionality between you and a target machine. Mouse 
    gives you the power and convenience of uploading/downloading files, tab completion, 
    taking pictures, location tracking, shell command execution, persistence, 
    escalating privileges, password retrieval, and much more.
    
# Getting started

## macOS/Linux installation

> cd mouse

> chmod +x install.sh

> ./install.sh

## iOS (jailbroken) installation

> cd mouse

> chmod +x install.sh

> ./install.sh

# Creating payloads

![2](https://user-images.githubusercontent.com/43011806/60388758-a0939100-9abe-11e9-8695-9db9caabda3c.png)

    INFO: Mouse payloads are executed on the target machine. The payload first sends over 
    instructions for getting and sending back device details to our server and then chooses 
    the appropriate executable to establish a secure remote control session.

## Bourne-Again Shell payloads

![6](https://user-images.githubusercontent.com/43011806/60388761-a12c2780-9abe-11e9-8a02-053d2807dffe.png)

    INFO: Selecting bash from the payload menu will give us a 1 liner that 
    establishes an eggshell session upon execution on the target machine.
    
## Entynet PI payload (USB injection)

![3](https://user-images.githubusercontent.com/43011806/60388757-a0939100-9abe-11e9-8077-f00bf521c061.png)

    INFO: Entynet PI is a development board that can be programmed 
    with the Arduino ide. It emulates usb keyboard strokes extremely 
    fast and can inject the Mouse payload just in a few seconds.
    
You can buy Entynet PI here: [Entynet PI](http://entynetproject.simplesite.com/441030055)

![i284008264539754632 _szw1280h1280_](https://user-images.githubusercontent.com/43011806/60388328-67582280-9ab8-11e9-9adc-f0248f31ac38.jpg)

# Interacting with a session

![4](https://user-images.githubusercontent.com/43011806/60388759-a0939100-9abe-11e9-9be7-9b8fa902c762.png)

    INFO: After a session is established, we can execute commands 
    on that device through the Mouse command line interface. 
    We can show all the available commands by typing "help".
    
## Taking pictures

![pic](https://user-images.githubusercontent.com/43011806/60388763-a12c2780-9abe-11e9-8ba4-1a88bdd31b5d.png)

    INFO: Both iOS and macOS payloads have picture taking capability. 
    The picture command lets you take a picture from the iSight on 
    macOS as well as the front or back camera on iOS.
    
## Tab completion

![help](https://user-images.githubusercontent.com/43011806/60388764-a12c2780-9abe-11e9-9c3d-da9a236bf67e.png)

    INFO: Similar to most command line interfaces, Mouse supports 
    tab completion. When you start typing the path to a directory or 
    filename, we can complete the rest of the path using the tab key.

# Multihandler CLI

![23](https://user-images.githubusercontent.com/43011806/60388762-a12c2780-9abe-11e9-96ff-b9f637f0bff0.png)

    INFO: The Multihandler option lets us handler multiple 
    sessions. We can choose to interact with different devices 
    while listening for new connections in the background.

# Commands

## macOS

    brightness : adjust screen brightness
    cd : change directory
    download : download file
    getfacebook : retrieve facebook session cookies
    getpaste : get pasteboard contents
    getvol : get speaker output volume
    idletime : get the amount of time since the keyboard/cursor were touched
    imessage : send message through the messages app
    itunes : iTunes Controller
    keyboard : your keyboard -> is target's keyboard
    lazagne : firefox password retrieval
    ls : list contents of a directory
    mic : record mic
    persistence : attempts to re establish connection after close
    picture : take picture through iSight
    pid : get process id
    prompt : prompt user to type password
    screenshot : take screenshot
    setvol : set output volume
    sleep : put device into sleep mode
    su : su login
    suspend : suspend current session (goes back to login screen)
    upload : upload file

## iOS

    alert : make alert show up on device
    battery : get battery level
    bundleids : list bundle identifiers
    cd : change directory
    dhome : simulate a double home button press
    dial : dial a phone number
    download : download file
    getcontacts : download addressbook
    getnotes : download notes
    getpasscode : retreive the device passcode
    getsms : download SMS
    getvol : get volume level
    home : simulate a home button press
    installpro : install substrate commands
    ipod : control music player
    islocked : check if the device is locked
    lastapp : get last opened application
    locate : get device location coordinates
    locationservice: toggle location services
    lock : simulate a lock button press
    ls : list contents of a directory
    mic : record mic
    mute : update and view mute status
    open : open apps
    openurl : open url on device
    persistence : attempts to re establish connection after close
    picture : take picture through the front or back camera
    pid : get process id
    respring : restart springboard
    safemode : put device into safe mode
    say : text to speach
    setvol : set device volume
    sysinfo : view system information
    upload : upload file
    vibrate : vibrate device
    
## Linux

    cd : change directory
    download : download file
    ls : list contents of a directory
    pid : get process id
    pwd : show current directory
    upload : upload file

# Thats all!
