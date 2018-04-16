import telepot
from telepot.loop import MessageLoop

#Here you enter your API like  (514659315:AkFPt_8_hv1ewsvMtPyA9JmS0halHxhhX74)
HTTPbased = ""

def bot():
    return telepot.Bot(HTTPbased)

def MessageAnalysis(msg):
    Msgtext, Msgtype, Msgid = telepot.glance(msg)
    print(msg)
    From = msg["from"]
    firstname = From["first_name"]
    is_bot = From["is_bot"]
    print("\nid :",Msgid,
          "\ntext :",Msgtext,
          "\ntype :",Msgtype,
          "\nfirst name :",firstname,
          "\nis bot :",is_bot,
          "\nmessage text :",msg["text"])

    print("-"*30)


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
