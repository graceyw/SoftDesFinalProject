# Rowan Sharman, Gracey Wilson

'''
Given a book's ISBN code, this file produces a map that highlights the
author's country of origin, location of the book's publisher, and location
of the book's plot.

To work, must install isbnlib library by running: sudo pip3 install isbnlib
'''
import isbnlib
from LocationsToMap import plotGraph
from classBook import Book


def getIsbn():
    code = input('Scan book barcode or enter ISBN code: ')
    if code == 'x':              # Exit program when 'x' entered
        return False
    while isbnlib.notisbn(code):
        code = input('\nPlease scan or enter a valid ISBN code: ')
        if code == 'x':          # Exit program when 'x' entered
            return False
    return code


def pickInput():
    choice = ''
    while choice != 's' and choice != 't':
        choice = input("Press 's' to scan or enter ISBN or 't' to enter title: ")
        if choice == 'x':
            return False
    return choice


def getTitle():
    title = input("Enter a book title: ")
    if title == 'x':
        return False
    return title


def doEverything():
    while True:
        choice = pickInput()

        if choice == 's':
            isbn = getIsbn()
            if not isbn:  # Exit program when 'x' entered
                break
            thisBook = Book(isbn)

        elif choice == 't':
            title = getTitle()
            if not title:  # Exit program when 'x' entered
                break
            thisBook = Book(title)
        else:
            break
        # if not isbn:  # Exit program when 'x' entered
        #     break
        if choice == 's':
            thisBook.getInfo()
        thisBook.getLocations()
        print(thisBook)
        # plotGraph(thisBook)
        # return thisBook


if __name__ == '__main__':
    doEverything()

"""
THESE CURRENTLY "WORK"            ** author, publisher, plot **
9780143039990 War and Peace          Russia, London, Russia
9781461035930 The Tempest            not found, Naples, not found
9781594631931 Kite Runner            US, not found, Kabul
9780743273565 Great Gatsby           US, not specific enough, West Egg
9780679886181 Jane Eyre              UK, US, London
9780316769488 Catcher in the Rye     US, NYC, Rye (lol)
9780486280615 Huckleberry Finn       book not found on Wikipedia
9780451524935 1984                   UK, Mississippi, Great Britain
9780143107668 Scarlet Letter         not found, London, Mass Bay Colony
9780143035008 Anna Kerenina          Russia, not found (Penguin), Serbia (wrong)

"""
