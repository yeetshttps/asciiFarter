#!/data/data/com.termux/files/usr/bin/python
from fartlib import getfart
import fartlib
from sys import argv
from sys import exit
from urllib import error
# VERSION - used for updates and versioning(duh)
version = 2.2
# HELP TEXT - displayed when 'help' command is used
help_text="""AsciiFarter - Help
usage: asciifarter COMMAND [--FLAGS]
       asciifarter [--FLAGS]

COMMANDS:
Commands change what AsciiFarter outputs, for example,
the art AsciiFarter will display can be changed using
different commands. 

Commands have to be put in a specific order and cannot 
be combined.

VALID COMMANDS ARE:
    COMMAND:            DESCRIPTION:
    help, h:            Displays this message and then exits.
    version, v:         Displays the reported version of AsciiFarter 
                        and then exits.
    random, r:          Shows a random Ascii Art.
    newest, n:          Shows the newest Ascii Art.
    find, f [ART]:      Find and show the Ascii Art named [ART]
    list, l:            Lists all of AsciiFarter's Arts by name

FLAGS:
Flags change how AsciiFarter outputs, for example,
you can tell AsciiFarter to display the names of Ascii
Arts with the '--name' flag. 

Flags do not have to be put in a specific order and can
be combined.

No Flags are currently implemented in AsciiFarter at this 
time, however.

Please note that internet is required to run AsciiFarter.
"""
try:
    if argv[1] == 'help' or argv[1] == 'h':
        print(help_text)
        exit(0)
    elif argv[1] == 'version' or argv[1] == 'v':
        print(str('AsciiFarter v'+str(version)+' running with FartLib v'+str(fartlib.version)))
        print('Copyright (C) 2024-2026 Jacob Haché (mangolover1899).')
        exit(0)
    elif argv[1] == 'random' or argv[1] == 'r':
        fart = getfart.random_art()
        fart.poop()
    elif argv[1] == 'newest' or argv[1] == 'n':
        fart = getfart.newest_art()
        fart.poop()
    elif argv[1] == 'find' or argv[1] == 'f':
        try:
            fart = getfart.find_art(argv[2])
            fart.poop()
        except IndexError:
            print('You have to tell me which art to find idior')
        except getfart.find_art.SearchError as err:
            print("Couldn't show <"+argv[2]+">: "+str(err))
        except AttributeError:
            exit(2)
    elif argv[1] == 'list' or argv[1] == 'l':
        getfart.list_art()
    elif argv[1]:
        print('[1;37;41mAsciiFarter: "'+argv[1]+'" is not a valid command or flag.[m')
        fart = getfart.random_art()
        fart.poop()
        exit(2)
except IndexError:
    try:
        fart = getfart.random_art()
        fart.poop()
    except IndexError:
        print("[1;37;41m* AsciiFarter needs internet to run. *[m")
        exit(1)
    except AttributeError:
        print("[1;37;41m* AsciiFarter needs internet to run. *[m")
        exit(1)
except AttributeError:
    print("[1;37;41m* AsciiFarter needs internet to run. *[m")
    exit(1)
except error.URLError:
    print("[1;37;41m* AsciiFarter needs internet to run. *[m")
    exit(1)
