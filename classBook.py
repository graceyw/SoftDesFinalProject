# Rowan Sharman

import isbnlib
import textMiner


class Book:

    def __init__(self, isbn):  # TODO create instantiation case for title
        self.has = {'isbn': 0,
                    'title': 0,
                    'author': 0,
                    'publisher': 0,
                    'year': 0,
                    'language': 0,
                    'authorLoc': 0,
                    'publisherLoc': 0,
                    'plotLoc': 0}

        if isbnlib.notisbn(isbn):
            self.title = isbn
            self.isbn = None
            self.has['title'] = 1
            self.has['isbn'] = 0

        else:
            self.isbn = isbn
            self.title = None
            self.has['title'] = 0
            self.has['isbn'] = 1

        self.gotInfo = False
        self.hasInfo = False

        self.author = ''
        self.publisher = ''
        self.year = ''
        self.language = ''
        self.authorLoc = ''
        self.publisherLoc = ''
        self.plotLoc = ''

    def getInfo(self):
        self.gotInfo = True
        self.info = isbnlib.meta(self.isbn)

        if self.info is None:
            self.hasInfo = False
        else:
            self.hasInfo = True
            self.title = self.info['Title']
            self.author = self.info['Authors']
            self.publisher = self.info['Publisher']
            self.year = self.info['Year']
            self.language = self.info['Language']

        self.authorLoc = ''
        self.publisherLoc = ''
        self.plotLoc = ''
        self.updateMissing()

    def getLocations(self):
        if self.has['title'] and self.title != '':
            self.authorLoc = textMiner.getAuthorLocation(self)
            self.plotLoc = textMiner.getPlotLocation(self)
        else:
            self.authorLoc = 'Book is missing title'
        if self.has['publisher'] and self.publisher != '':
            self.publisherLoc = textMiner.getPublisherLocation(self)
        else:
            self.publisherLoc = 'Book is missing publisher info'

        self.updateMissing()

    def __str__(self):
        # if not self.gotInfo:
        #     return 'No info yet'
        # if not self.hasInfo:
        #     return 'No info available'

        infoString = ''
        infoString += ('Title:\t\t  ' + self.title + '\n')
        plural = 'Author:\t  '
        authors = ''
        if self.has['author']:
            for element in self.author:
                if len(authors) > 1:
                    plural = 'Authors:\t  '
                    authors += ', ' + element
                else:
                    authors += element

        infoString += (plural + authors + '\n')
        infoString += ('Publisher:\t  ' + self.publisher + '\n')
        infoString += ('Year:\t  ' + self.year + '\n')
        infoString += ('Language: ' + self.language + '\n')
        infoString += ('Author Location:\t ' + self.authorLoc + '\n')
        infoString += ('Publisher Location:\t ' + self.publisherLoc + '\n')
        infoString += ('Plot Location:\t\t ' + self.plotLoc + '\n')

        return infoString

    def updateMissing(self):
        if self.title != '':
            self.has['title'] = 1

        if self.author != '':
            self.has['author'] = 1

        if self.publisher != '':
            self.has['publisher'] = 1

        if self.year != '':
            self.has['year'] = 1

        if self.language != '':
            self.has['language'] = 1

        if self.authorLoc != '':
            self.has['authorLoc'] = 1

        if self.publisherLoc != '':
            self.has['publisherLoc'] = 1

        if self.plotLoc != '':
            self.has['plotLoc'] = 1
