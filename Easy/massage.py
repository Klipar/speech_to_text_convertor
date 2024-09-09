# from colorama import init, Fore, Style
import datetime

class colors:
    BLACK  = '\33[30m'
    RED    = '\33[31m'
    GREEN  = '\33[32m'
    YELLOW = '\33[33m'
    BLUE   = '\33[34m'
    VIOLET = '\33[35m'
    BEIGE  = '\33[36m'
    WHITE  = '\33[37m'
    BLACKBG  = '\33[40m'
    REDBG    = '\33[41m'
    GREENBG  = '\33[42m'
    YELLOWBG = '\33[43m'
    BLUEBG   = '\33[44m'
    VIOLETBG = '\33[45m'
    BEIGEBG  = '\33[46m'
    WHITEBG  = '\33[47m'
    END      = '\33[0m'

def Beautiful_Timestump () -> str:
    return datetime.datetime.now().strftime("[%H:%M:%S]")

# init()
def failed(str, en = "\n"):
    print(Beautiful_Timestump (), colors.RED + ' [FAILED]  ' + colors.END + str, end = en)
    return (f"{Beautiful_Timestump ()} [FAILED] {str}")


def success (str, en = "\n"):
    print(Beautiful_Timestump (), colors.GREEN + ' [SUCCESS] ' + colors.END, str, end = en)
    return (f"{Beautiful_Timestump ()} [SUCCESS] {str}")

def inform(str, en = "\n"):
    print(Beautiful_Timestump (), colors.BLUE + ' [INFORM]  ' + colors.END, str, end = en)
    return (f"{Beautiful_Timestump ()} [INFORM] {str}")

def warn(str, en = "\n"):
    print(Beautiful_Timestump (), colors.YELLOW + ' [ WARN ]  ' + colors.END, str, end = en)
    return (f"{Beautiful_Timestump ()} [WARN] {str}")

def pr(str, en = "\n"):
    print(Beautiful_Timestump (),' [PRINT]   ' , str)
    return (f"{Beautiful_Timestump ()} [PRINT] {str}")

def test(str, en = "\n"):
    print(colors.VIOLET + f"{Beautiful_Timestump ()}  [ TEST ]  " + colors.END, str, end = en)
    return (f"{Beautiful_Timestump ()} [TEST] {str}")

def castom_messeg (massage, texten_in_breskets = "test", color = colors.BLUEBG, en = "\n"):
    print(colors.VIOLET + f"{Beautiful_Timestump ()}  [ TEST ]  " + colors.END, massage, end = en)
    return (f"{Beautiful_Timestump ()} [TEST] {massage}")