

def errorTips(tip):
    if tip == 1: # Internet Connection tip
        errorTip = """                                       
  [37;1;41m[1] Check your internet connection.[31;22;49m
  |     - Check if your Modem/WiFi Router is working.
  |     - If you're using Ethernet, check how tightly
  |       your cables are connected.
  |     - Your WiFi card may be faulty 
  |     - Your device's internet connection settings
  |       (Proxy, Firewall, IP address, etc) may not
  |       be configured properly.[0m
  		"""
        return errorTip
    elif tip == 2: # Argument error tip
        errorTip = """
  [37;1;41m[2] Run the "--help" or "-h" option.[31;22;49m
  |     - These are usually the [1mhelp[22m option, and will 
  |       show available options/arguments/flags.
  |     - If you're sure the option you ran actually
  |       exists, check your spelling.[0m
        """ 
        return errorTip
    elif tip == 3: # Go fuck yourself
        errorTip = """
  [37;1;41m[3] Error:[31;22;49m
  |     - Go fuck yourself
  |     - Contact the devs
  |         - They wont care
  |         - Double fuck yourself
  |     - Devs the contact?[0m
        """
        return errorTip


def numsplit(num):
    if num >= 251:
        raise MemoryError("Too many numbers to split")
    count = 0
    splitNum = list()
    while count is not num:
        count = count + 1
        splitNum.append(count)
    return splitNum

