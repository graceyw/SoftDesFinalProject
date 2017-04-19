import wikipedia
# from text_mining_wiki_test import find_author_origin
from bs4 import BeautifulSoup
import indicoio
from key import indico_key
indicoio.config.api_key = indico_key


def getAuthorLocation(book):
    if book.has['title']:
        loc = find_author_origin(book.title)
        if loc is 'DisambiguationError':
            loc = find_author_origin(book.title + ' (novel)')
        if loc is 'StopIteration':
            return 'Author location not found on Wikipedia'
        if loc is 'PageError':
            return 'Book not found on Wikipedia'
        return loc



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
    try:
        page_results = wikipedia.page(book_page_name)
    except wikipedia.exceptions.DisambiguationError:
        return 'DisambiguationError'
    except StopIteration:
        return 'StopIteration'
    except wikipedia.exceptions.PageError:
        return 'PageError'
    page_html = page_results.html()    # generate the page's html. TODO Could be optimized by only generating the first x char
    soup = BeautifulSoup(page_html, "lxml")    # make it readable (not nessassary after testing)
    table = soup.findAll("table", {"class": "infobox"})  # select all parts that are prefixed by <th> (includes the country of the book)
                                                           # TODO This could prob be optimized by begining approx 800 char in.
    all_th = soup.table.find_all('th')
    country_header = next(element for element in all_th if element.getText() == 'Country')
    country_name = country_header.findNext('td').getText().strip()
    return country_name
