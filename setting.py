VERSION = "beta 1.0"
IG_LINK = "instagram.com/laser01/"
def print_banner(banner=False):
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
  if banner:
    print(BANNER)
  
