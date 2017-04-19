# Rowan Sharman
# no longer necessary; tasks completed in test.py
import isbnlib


def getIsbn():
    code = input('Scan book barcode or enter ISBN: ')
    while isbnlib.notisbn(code):
        code = input('\nPlease scan or enter a valid ISBN: ')
    return code


def printData(data):
    dataString = ''
    dataString += ('Title:\t\t' + data['Title'] + '\n')

    plural = 'Author:\t\t'
    authors = ''
    for element in data['Authors']:
        if len(authors) > 1:
            plural = 'Authors:\t'
            authors += ', ' + element
        else:
            authors += element

    dataString += (plural + authors + '\n')
    dataString += ('Publisher:\t' + data['Publisher'] + '\n')
    dataString += ('Year:\t\t' + data['Year'] + '\n')
    dataString += ('Language:\t' + data['Language'] + '\n')

    print(dataString)


if __name__ == '__main__':
    while True:
        isbn = getIsbn()
        info = isbnlib.meta(isbn)
        if info is None:
            print("We're sorry, but this book is not in our database.\n")
        else:
            printData(info)
