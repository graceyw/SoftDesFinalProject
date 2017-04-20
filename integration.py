# Rowan Sharman, Gracey Wilson

'''
Given a book's ISBN code, this file produces a map that highlights the
author's country of origin, location of the book's publisher, and location
of the book's plot.

To work, must install isbnlib library by running the code:
sudo pip3 install isbnlib
'''
import isbnlib
from LocationsToMap import plotGraph
from classBook import Book     # is this necessary, since it's already imported in LocationsToMap?

'''FILES INVOLVED:
Code below taken from test.py, which can now be discarded.
The same functionality exists in ScannerToData.py, which can also be discarded.

Uses textMiner.py to get locations of the Plot, Author, and Publisher.
Uses LocationsToMap to plot those locations on a map.
'''
def getISBN():
    code = input('Scan book barcode or enter ISBN code: ')
    if code == 'x':              # Exit program when 'x' entered
        return False
    while isbnlib.notisbn(code):
        code = input('\nPlease scan or enter a valid ISBN code: ')
        if code == 'x':          # Exit program when 'x' entered
            return False
    return code


if __name__ == '__main__':
    while True:
        ISBN = getISBN()
        if not ISBN:     # Exit program w978-3-16-148410-0hen 'x' entered
            break
        thisBook = Book(ISBN)
        thisBook.getInfo()
        thisBook.getLocations()
        # want to run the location searches with the title of the book as input
        print(thisBook)
        plotGraph(thisBook)
