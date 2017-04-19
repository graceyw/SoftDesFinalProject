# Gracey Wilson

'''
Given a book's ISBN code, this file produces a map that highlights the
author's country of origin, location of the book's publisher, and location
of the book's plot.

To work, must install isbnlib library by running the code:
sudo pip3 install isbnlib
'''
from classBook import Book
import isbnlib
import LocationsToMap
import classBook       # is this necessary, since it's already imported in LocationsToMap?
import text_mining_wiki_test
import PlotLocation

'''Files involved:
Code below taken from test.py, which can now be discarded.
The same functionality exists in ScannerToData.py, which can also be discarded.

Use PlotLocation.py and PublisherLocation.py to get respective locations
Uses LocationsToMap to create the map
'''
def getISBN():
    code = input('Scan book barcode or enter ISBN code: ')
    if code == 'x':  # Exit program when 'x' entered
        return False
    while isbnlib.notisbn(code):
        code = input('\nPlease scan or enter a valid ISBN code: ')
        if code == 'x':  # Exit program when 'x' entered
            return False
    return code


if __name__ == '__main__':
    while True:
        ISBN = getISBN()
        if not ISBN:  # Exit program w978-3-16-148410-0hen 'x' entered
            break
        thisBook = Book(ISBN)
        thisBook.getInfo()
        thisBook.getLocations()
        # want to run the location searches with the title of the book as input
        print(thisBook)
# '''I want to access the elements of thisBook.
# Also would be nice to make the locations elements of thisBook'''
#         # thisBook.authorLoc = print(find_author_origin(book_page_name))
#         thisBook.plotLoc = print(find_plot_country(book_page_name))
#         thisBook.publisherLoc = print(find_publisher_location(book_publisher))
#         plotGraph(thisBook)
