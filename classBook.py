import isbnlib


class Book:

    def __init__(self, isbn):
        self.isbn = isbn
        self.gotInfo = False
        self.hasInfo = False
        self.authorLoc = 'UK'
        self.publisherLoc = 'USA'

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

        return infoString
