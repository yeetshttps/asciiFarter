from urllib import request # to get links
import bs4 # to parse xml - EXTERNAL (pip3)
import random # Random item selection
from time import sleep # for stdout animation work
from sys import stdout # to work with stdout
from sys import exit # ensure exit() actually exits
from urllib import error # deal with url errors

art_list = [] # Initiate art_list and newest_art here because python is gay and is obsessed with local object errors
new_art = ''
error_opener = str("[31m"+str(__file__)+": Error:")
# Open status.xml and add some of it's contents to the art_list
try:
    with request.urlopen("https://yeetshttps.github.io/asciiFarter/status.xml") as status_file:
        status_text = status_file.read().decode('utf-8')
        status = bs4.BeautifulSoup(status_text, 'xml')
        art_names = status.find('asciiArtsNames')
        for name in art_names.find_all('name'):
            art_list.append(name.text)
        new_art = status.find('newestAscii').text
except error.URLError: # Check for internet if connection failed
    try:               # Check if the service provider (github) is up
        with request.urlopen("https://github.com") as ghservercheck:
            print(error_opener)
            print("There was an error connecting to our website: https status code "+str(status_file.code))
            print("[A[m")
    except error.URLError:
        try:           # Check another source to see if its an internet connection problem
            with request.urlopen("https://google.com") as gservercheck:
                print(error_opener)
                print("It seems that our service provider may be down. Check back again in a little while.")
                print("[A[m")
        except error.URLError: # If there was an error connecting to the last source its probably internet-related
            print(error_opener)
            print("It seems that there was a problem connecting to the internet, please check your device's internet connection.")
            print("[A[m")

# CLASSES
# Get a random art from the art_list:
class random_art:
    def __init__(self, randomness=len(art_list)):
        for x in range(randomness):
            self.name = random.choice(art_list) # choose a random art's filename from the art_list
        with request.urlopen('https://yeetssite.github.io/'+self.name) as art_file: # open that random art's url
            self.File = art_file # save the file-like object as an attribute
            self.text = art_file.read().decode('utf-8') # convert the file-like object into a string

    def poop(self, line_delay=0.000001): # print the art asciiFarter style
        for line in self.text: # iterate art text line-by-line
            stdout.write(line) # write(print) the line to stdout (print adds extra newlines)
            sleep(line_delay)  # sleep for a fraction of a second between every line
            stdout.flush()     # no poop left unflushed
            sleep(line_delay)

# Functionally the same as random_art() but uses new_art instead of a random choice from the art_list:
class newest_art: 
    def __init__(self):
        self.name = new_art
        with request.urlopen('https://yeetssite.github.io/'+self.name) as art_file:
            self.File = art_file
            self.text = art_file.read().decode('utf-8')

    def poop(self, line_delay=0.000001):
        for line in self.text:
            stdout.write(line)
            sleep(line_delay)
            stdout.flush()
            sleep(line_delay)

# search specific art by name
class find_art:
    class SearchError(ValueError):
        pass
    def __init__(self, art=None):
        self.found = False
        if art: # check against the art list to see if the search item exists or not
            self.search = art.lower()
            for art_name in art_list:
                if self.search.replace('.txt','') == art_name.lower().replace('asciiart/', '').replace('.txt', ''):
                    self.name = art_name
                    self.found = True
                    break
        else:
            print(error_opener)
            raise self.SearchError('No art to look for[m')

        if self.found:
            try:
                with request.urlopen('https://yeetssite.github.io/'+self.name) as art_file:
                    self.File = art_file
                    self.text = art_file.read().decode('utf-8')
            except error.URLError:
                print(error_opener)
                raise self.SearchError("Couldn't open the art from <https://yeetssite.github.io/"+self.name+">, maybe it doesn't exist?")
        elif not self.found:
            print('[1;34m(i) [30mfind_art: art [37m"'+self.search+'"[30m not found.[m')
    def poop(self, line_delay=0.000001):
        for line in self.text:
            stdout.write(line)
            sleep(line_delay)
            stdout.flush()
            sleep(line_delay)

class list_art:
    def __init__(self, line_delay=0.000001):
        self.count = 0
        for name in art_list:
            self.count += 1
            print(str(self.count)+'. '+name.lower().replace('asciiart/', ''))
            sleep(line_delay)
        print("Total amount of ascii arts: "+str(self.count))
        sleep(line_delay)

