# Rowan Sharman

import isbnlib
import textMiner


class Book:

    def __init__(self, isbn):
        self.isbn = isbn
        self.gotInfo = False
        self.hasInfo = False
        self.has = {'title': 0,
                    'author': 0,
                    'publisher': 0,
                    'year': 0,
                    'language': 0,
                    'authorLoc': 0,
                    'publisherLoc': 0,
                    'plotLoc': 0}

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
        self.authorLoc = textMiner.getAuthorLocation(self)
        self.publisherLoc = textMiner.find_publisher_location(self)
        self.plotLoc = textMiner.find_plot_country(self)
        self.updateMissing()


    def __str__(self):
        if not self.gotInfo:
            return 'No info yet'
        if not self.hasInfo:
            return 'No info available'

        infoString = ''
        infoString += ('Title:\t\t  ' + self.title + '\n')
        plural = 'Author:\t  '
        authors = ''
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
        infoString += ('Author Location: ' + self.authorLoc + '\n')
        infoString += ('Publisher Location: ' + self.publisherLoc + '\n')
        infoString += ('Plot Location: ' + self.plotLoc + '\n')

        return infoString

    def updateMissing(self):
        if self.title is not None:
            self.has['title'] = 1

        if self.author is not None:
            self.has['author'] = 1

        if self.publisher is not None:
            self.has['publisher'] = 1

        if self.year is not None:
            self.has['year'] = 1

        if self.language is not None:
            self.has['language'] = 1

        if self.authorLoc is not None:
            self.has['authorLoc'] = 1

        if self.publisherLoc is not None:
            self.has['publisherLoc'] = 1

        if self.plotLoc is not None:
            self.has['plotLoc'] = 1
