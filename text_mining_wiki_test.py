# Sam Eppinger, Gracey Wilson

import wikipedia
from bs4 import BeautifulSoup
import sys

def find_author_origin(book_page_name):
    '''Input: the name of a book's wikipedia page in the form of a string.
    Returns: the author and the country where the book takes place.

    Common program holes: books that are part of a series, books whose pages don't list
    the Country in the info box.
    Common user errors will probably include: inputting just the title of a book
    when the title of its wikipedia page contains more than simply the title of
    the book (i.e. "Emma (novel)").'''
    # Works for books with Gatsby, Name of the Wind, War and Peace
    # Does not work for: Harry Potter, Artemis Fowl

    page_results = wikipedia.page(book_page_name)
    page_html = page_results.html()    # generate the page's html. TODO Could be optimized by only generating the first x char
    soup = BeautifulSoup(page_html, 'html.parser')    # make it readable (not nessassary after testing)
    table = soup.findAll("table", { "class" : "infobox" }) # select all parts that are prefixed by <th> (includes the country of the book)
                                                           # TODO This could prob be optimized by begining approx 800 char in.
    all_th = soup.table.find_all('th')
    country_header = next(element for element in all_th if element.getText() == 'Country')
    country_name = country_header.findNext('td').getText().strip()
    return country_name

if __name__ == '__main__':
        print(find_author_origin('War and Peace'))

# dir(table[0].find_all('th')[2])       # print some things you can do i.e. findNext

# '''To deal with the errors:
#     try:
#         print(find_country('War and Peace'))
#     except ValueError:'''

# This step uses the search to find the book. This is used to confirm that a book
# does exist when the page function doesn't return something that makes sense
# Use if something doesn't work.
# wiki_results = wikipedia.search("War and Peace")
# pg_results = wikipedia.page(title=wiki_results[0])
