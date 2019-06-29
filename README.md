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

    INFO: Most Often Useful Super Exploit (Mouse) is a post exploitation 
    surveillance tool written in Python. It gives you a command line session 
    with extra functionality between you and a target machine. Mouse gives you 
    the power and convenience of uploading/downloading files, tab completion, 
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

    INFO: Mouse payloads are executed on the target machine. The payload first sends over 
    instructions for getting and sending back device details to our server and then chooses 
    the appropriate executable to establish a secure remote control session.

## Bourne-Again Shell payloads

    INFO: Selecting bash from the payload menu will give us a 1 liner that 
    establishes an eggshell session upon execution on the target machine.
    
## Teensy macOS payload (USB injection)

    INFO: Teensy is a USB development board that can be programmed 
    with the Arduino ide. It emulates usb keyboard strokes extremely 
    fast and can inject the Mouse payload just in a few seconds.

![687474703a2f2f6c756361736a61636b736f6e2e696f2f696d616765732f6567677368656c6c2f7465656e73792e6a7067](https://user-images.githubusercontent.com/43011806/60386737-e42bd200-9aa1-11e9-89b4-1431e7bbd731.jpeg)

# Interacting with a session

    INFO: After a session is established, we can execute commands 
    on that device through the Mouse command line interface. 
    We can show all the available commands by typing "help".
    
## Taking pictures

    INFO: Both iOS and macOS payloads have picture taking capability. 
    The picture command lets you take a picture from the iSight on 
    macOS as well as the front or back camera on iOS.
    
## Tab completion

    INFO: Similar to most command line interfaces, Mouse supports 
    tab completion. When you start typing the path to a directory or 
    filename, we can complete the rest of the path using the tab key.

# Multihandler CLI

    INFO: The Multihandler option lets us handler multiple 
    sessions. We can choose to interact with different devices 
    while listening for new connections in the background.

# Thats all!
