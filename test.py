# Rowan Sharman

from classBook import Book
import isbnlib


def getIsbn():
    code = input('Scan book barcode or enter ISBN: ')
    if code == 'x':  # Exit program when 'x' entered
        return False
    while isbnlib.notisbn(code):
        code = input('\nPlease scan or enter a valid ISBN: ')
        if code == 'x':  # Exit program when 'x' entered
            return False
    return code


if __name__ == '__main__':
    while True:
        isbn = getIsbn()
        if not isbn:  # Exit program when 'x' entered
            break
        thisBook = Book(isbn)
        thisBook.getInfo()
        thisBook.getLocations()
        print(thisBook)
