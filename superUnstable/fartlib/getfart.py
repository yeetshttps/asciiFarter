from urllib import request # to get links
import bs4 # to parse xml - EXTERNAL (pip3)
import random # Random item selection
from time import sleep # for stdout animation work
from sys import stdout # to work with stdout
art_list = [] # Initiate art_list and newest_art here because python is gay and is obsessed with local object errors
new_art = ''
# Open status.xml and add some of it's contents to the art_list
with request.urlopen("https://yeetshttps.github.io/asciiFarter/status.xml") as status_file:
    status_text = status_file.read().decode('utf-8')
    status = bs4.BeautifulSoup(status_text, 'xml')
    art_names = status.find('asciiArtsNames')
    for name in art_names.find_all('name'):
        art_list.append(name.text)
    new_art = status.find('newestAscii').text

# CLASSES
# Get a random art from the art_list:
class random_art:
    def __init__(self):
        self.name = random.choice(art_list) # choose a random art's filename from the art_list
        with request.urlopen('https://yeetssite.github.io/'+self.name) as art_file: # open that random art's url
            self.File = art_file # save the file-like object as an attribute
            self.text = art_file.read().decode('utf-8') # convert the file-like object into a string

    def poop(self, line_delay=0.000001): # print the art asciiFarter style
        for line in self.text: # iterate art text line-by-line
            stdout.write(line) # write(print) the line to stdout (print adds extra newlines)
            sleep(line_delay)  # sleep for a fraction of a second between every line
        stdout.flush()         # flush stdout after art is pooped.

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
