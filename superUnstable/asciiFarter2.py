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
except KeyError:
    conf.read(confPathSecondary + confFile)
    try:
        for key in conf['defaults']:
            if key == 'behavior':
                behavior = str(conf['defaults']['behavior'])
    except KeyError:
        print("\x1b[31mKeyError: " + confPath + confFile + " or " + confPathSecondary + confFile + " is misconfigured or doesn't exist.\x1b[0m")
        exit(1)


# URL of the main website(the main path)
website = 'https://yeetshttps.github.io/asciiFarter/'

# Version stuff
version = 'v1.4a-alpha'
versionFloat = 1.4

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

artsCount = stats.find('asciiArtCount')
artsCount = str(artsCount.text)

newestArt = stats.find('newestAscii')
newestArt = str(newestArt.text)

args = sys.argv[0]


def randomArt():
    url = str("https://yeetssite.github.io/" + random.choice(artsList))
    print("Random ascii art:")
    for line in urlOpen(url):
        sys.stdout.write(line.decode('UTF-8'))
        sys.stdout.flush()
        time.sleep(0.005)

def newArt():
    
    url = str("https://yeetssite.github.io/" + newestArt)
    print("Newest ascii art:")
    for line in urlOpen(url):
        sys.stdout.write(line.decode('UTF-8'))
        sys.stdout.flush()
        time.sleep(0.005)

def help():
    help = """
USAGE: asciiFarter2.py [ OPTION ]
OPTIONs:
    -h, --help:             Bring up this help message
    -r, --randomascii:      Print a random ascii art
    -n, --newestascii:      Print the newest ascii art from 
                            https://yeetssite.github.io/

    You can change the "behavior" setting in ~/.config/asciiFarter.ini(or 
    ./asciiFarter.ini) to change what asciiFarter does when run without
    options.
        """
    print(help)

def checkArgs(args):
    if args == '-r' or '-randomascii' in args:
        randomArt()
    elif args == '-n' or '-newestascii' in args:
        newArt()
    elif args == '-h' or '-help' in args:
        help()
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
