import argparse

VERSION = "beta"
IG_LINK = "instagram.com/laser01/"

BANNER = ("""
 _____          _          _ _ 
|_   _|        | |        | | |
  | |______ ___| |__   ___| | |
  | |______/ __| '_ \ / _ \ | |
  | |      \__ \ | | |  __/ | |
  \_/      |___/_| |_|\___|_|_|
                                                 
	dev {0}
	Version {1}                           

""".format(
    IG_LINK, VERSION
    )
          )

def main():
    parser = argparse.ArgumentParser(prog="telpot.py", add_help=True, usage=("python t-shell.py -hh"))
    parser.add_argument("-hh", dest="helpusing", action="store_true" ,
                        help="Display help command message and exit")
    args = parser.parse_args()

    print(BANNER)
    
    if args.helpusing:
        helpmsg = ("""

#Check who is online
online?

#Choose victem
<ip> [option]
or for all victims
all [option]

#Display sysinfo
<ip> sysinfo

#Excute shell command
<ip> cmd [commands]

#Change dir
<ip> cd dir

#List dir
<ip> lsdir

#Get path
<ip> path

#Open url
<ip> url [url]

""")
        print(helpmsg)
if __name__ == '__main__':
    main()
