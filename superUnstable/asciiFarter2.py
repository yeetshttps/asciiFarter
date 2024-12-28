#!/usr/bin/python
# Copyright (c) 2024 mangolover1899(itsYeetsup)
# Licensed under nothing, this code is free to edit and
# tinker as you please with no conditions.

# Import modules:
from bs4 import BeautifulSoup # To parse XML
import requests # To get XML and other various text files from a website*
from configparser import ConfigParser as conf # Get configuration settings from INI files
conf = conf()
import os # Various useful features
import sys # ^Same, bro
import random # random stuff, duh
import urllib.request
urlOpen = urllib.request.urlopen
import time
import yeettools

# Set up variables:

# Get configuration settings
confPath = os.environ['HOME'] + '/.config/'
confPathSecondary = "./"
confFile = 'asciiFarter.ini'
scriptName = 'asciiFarter2.py'
conf.read(confPath + confFile)


def connectedToInternet(url='https://google.com', url2='https://github.com/'):
    try:
        requests.get(url)
        return True
    except requests.ConnectionError:
        try:
            requests.get(url2)
            return True
        except requests.ConnectionError:
            return False


try:
    for key in conf['defaults']:
        if key == 'behavior':
            behavior = str(conf['defaults']['behavior'])
            shownames = conf['defaults']['shownames']
except KeyError:
    conf.read(confPathSecondary + confFile)
    try:
        for key in conf['defaults']:
            if key == 'behavior':
                behavior = str(conf['defaults']['behavior'])
                shownames = conf['defaults']['shownames']
    except KeyError:
        print("\x1b[31mKeyError: " + confPath + confFile + " or " + confPathSecondary + confFile + " is misconfigured or doesn't exist.\x1b[0m")
        exit(1)


# URL of the main website(the main path)
website = 'https://yeetshttps.github.io/asciiFarter/'

# Version stuff
version = 2.0
versionLong =  str('v' + str(version) + '-alpha')

# Interndet stuff:

# Get https://yeetshttps.github.io/asciiFarter/status.xml and parse it with BeautifulSoup
if not connectedToInternet():
    sys.stdout.write("[31m")
    sys.stdout.flush()
    errorTip = yeettools.errorTips(1)
    raise ConnectionError("Cannot verify an internet connection.\n\n" + errorTip)
status = requests.get(website + 'status.xml')
stats = BeautifulSoup(status.text, 'xml')

# Various lists
crawlIDs = stats.find('crawlIDs')
cID = crawlIDs.find('ID')

# make a crawlID(cID) list

# We'll be re-running this code a lot, so let's make it a function
def listerate(sub, root):
    rList = list()
    for sub in root:
        rList.append(str(sub.text))
    emptyItem = str('')
    newLine = '\n'
    while emptyItem in rList:
        rList.remove(str(emptyItem))
    while newLine in rList:
        rList.remove('\n')
    return list(rList)

cIDlist = listerate(cID, crawlIDs)

artsNames = stats.find('asciiArtsNames')
name = artsNames.find('name')

artsList = listerate(name, artsNames)
art_count = 0
for item in artsList:
    art_count = int(art_count + 1)


newestArt = stats.find('newestAscii')
newestArt = str(newestArt.text)

args = sys.argv[0]


def randomArt():
    randart = random.choice(artsList)
    url = str("https://yeetssite.github.io/" + randart)
    print("Random ascii art:")
    if shownames == "True":
        if "asciiArt/" in randart:
            print("[47;30m" + randart.replace("asciiArt/", "") + "[0m")
        else:
            print("[47;30m" + randart + "[0m")
    for line in urlOpen(url):
        sys.stdout.write(line.decode('UTF-8'))
        sys.stdout.flush()
        time.sleep(0.005)

def newArt():
    url = str("https://yeetssite.github.io/" + newestArt)
    print("Newest ascii art:")
    if shownames == "True":
        if "asciiArt/" in newestArt:
            print("[47;30m" + newestArt.replace("asciiArt/", "") + "[0m")
        else:
            print("[47;30m" + newestArt + "[0m")
    for line in urlOpen(url):
        sys.stdout.write(line.decode('UTF-8'))
        sys.stdout.flush()
        time.sleep(0.005)


def findArt(art):
    if ".txt" not in art:
        art = str(art + ".txt")
    try:
        url = urlOpen(str("https://yeetssite.github.io/asciiArt/" + art))
        art_found_upper = False
        art_found_lower = False
    except:
        og_input = art
        art = art.replace(".txt","")
        art_found_upper = False
        art_found_lower = False
        try:
            url = urlOpen(str("https://yeetssite.github.io/asciiArt/" + art.upper() + ".txt"))
            art_found_upper = True
            art_found_lower = False
            art = art.upper() + ".txt"
        except:
            try:
                url = urlOpen(str("https://yeetssite.github.io/asciiArt/" + art.lower() + ".txt"))
                art_found_lower = True
                art_found_upper = False
                art = art.lower() + ".txt"
            except:
                class FuckError(ValueError):
                    pass
                raise FuckError("[31mCouldn't find what you're looking for\n\n" \
                        "Basically, all this red stuff means ya fucked up, and I couldn't find any ascii arts named \"" + og_input + "\"\nThis could be for one of the following reasons:\n" + "Miscaps\n" + "- I tried re-searching for your thingy for ALL CAPS and lower case, but if it's got Mixed Caps, I'm screwed.\n" + "Wrong letters\n" + "- idior\n" + "Doesn't exist\n" + "- skitzo idor\n") 
    if shownames == "True":
        if art_found_upper:
            print("Couldn't find \"" + og_input + "\"")
            sys.stdout.write("Best match: ")
        elif art_found_lower:
            print("Couldn't find \"" + og_input + "\".")
            sys.stdout.write("Best match: ")
        if "asciiArt/" in art:
            print(art.replace("asciiArt/", ""))
        else:
            print("[47;30m" + art + "[0m")
    for line in url:
        sys.stdout.write(line.decode('UTF-8'))
        sys.stdout.flush()
        time.sleep(0.005)

def stats(art=False):
    if not art:
        print("[47;30mASCIIFARTER STATISTICS[0m")
        print("Arts count: " + str(art_count))
        print("Version: " + versionLong + " Python Edition")
        print("Config:")
        print("\tDefault behavior: " + behavior)
        print("\tShow arts/pastas names: " + shownames)
        print("\nUse the \"-l\" option to list ascii arts.")
    else:
        art = str(art)
        art_counter = 0
        art = art.replace(".txt","")
        art = art.lower()
        for item in artsList:
            item_og = item
            art_counter = art_counter + 1
            if "asciiArt/" in item:
                item = item.replace("asciiArt/","")
            if ".txt" in item:
                item = item.replace(".txt","")
            if item.strip() == str(art.strip()):
                found_art = True
                break
            else:
                item = item.lower()
                if item.strip() == art.strip():
                    found_art = True
                    break
                else:
                    found_art = False
                
        if found_art:
            print("Yes")
        else:
            print("no")

def help():
    help = """
USAGE: asciiFarter2.py [ OPTION ] [ SUB-OPTION ]
OPTIONs:
    -h, --help:             Bring up this help message.
    -r, --randomascii:      Print a random ascii art.
    -n, --newestascii:      Print the newest ascii art from 
                            <https://yeetssite.github.io/>.
    -f, --findart [ART]:    Find an ascii art named [ART].** 
    -l, --listart:          List the names of available ascii arts.*
    -s, --stats [ART]:      Show stats for the [ART] provided, or shows
                            stats about asciiFarter if no [ART] provided.


    You can change the "behavior" setting in ~/.config/asciiFarter.ini(or 
    ./asciiFarter.ini) to change what asciiFarter does when run without
    options.

    * Excludes the path "asciiArt/".

    ** Option required.
        """
    print(help)

def checkArgs(args):
    if args == '-r' or '-randomascii' in args:
        randomArt()
    elif args == '-n' or '-newestascii' in args:
        newArt()
    elif args == '-h' or '-help' in args:
        help()
    elif args == '-f' or '-findart' in args:
        try:
            findee = sys.argv[1]
            if findee == "-f" or '-findart' in findee:
                try:
                    findee = sys.argv[2]
                    findArt(findee)
                except IndexError:
                    print("Error: option '" + args + "' has to find something!")
            else:
                findArt(findee)
        except IndexError:
            print("You must enter a file to find")
    elif args == "-l" or "-listart" in args:
        for item in artsList:
            if "asciiArt/" in item:
                item = item.replace("asciiArt/", "")
            print(item)
            time.sleep(0.005)
    elif args == "-s" or "--stats" in args:
        try:
            art_stats = sys.argv[1]
            if art_stats == args:
                art_stats = sys.argv[2]
                stats(art=art_stats)
        except IndexError:
            stats()

    else:
        class OptionError(ValueError):
            pass
        help()
        sys.stdout.write('[31m')
        if args == "--random" or args == "-random":
            errorTip = '\a  | (i) "' + args + '" is removed. Use "--randomascii" or "-r" intead.'
        else:
            errorTip = yeettools.errorTips(2)
        raise OptionError('"' + str(args) + '" is not a valid option.\n\n' + errorTip)


if scriptName in args or "./" + scriptName in args:
    try:
        args2 = sys.argv[1]
        checkArgs(args2)
    except IndexError:
        if behavior == 'ascii new':
            newArt()
        elif behavior == 'ascii random':
            randomArt()
elif not args:
    if behavior == 'ascii new':
        newArt()
    elif behavior == 'ascii random':
        randomArt()
else:
    checkArgs(args)
