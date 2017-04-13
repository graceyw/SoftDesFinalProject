# Sarah Barden
# Takes in a book's publisher and returns the location of the publisher's headquarters

import wikipedia
from bs4 import BeautifulSoup


def find_publisher_location(book_publisher):
    # Input: the name of a book's publisher
    # Returns: the country where the book was published

    # Works: 9780486295060 (Dover Publications)
    #        9780375842207 (Alfred A. Knopf)
    #         9780199583027 (Oxford University Press)
    # Does not work for: Harry Potter, Artemis Fowl

    page_results = wikipedia.page(book_publisher)
    page_html = page_results.html()    # generate the page's html.
    soup = BeautifulSoup(page_html, 'html.parser')    # make it readable

    all_tr = soup.find_all('tr')  # finds all of the table rows
    trlist = [element.getText() for element in all_tr]  # makes a pretty list with just text

    for i in trlist:
        if i.startswith("Headquarters"):
            location = i

    return location[22:]  # starts after "Location headquarters" and just returns the location


if __name__ == '__main__':
        print(find_publisher_location('Oxford University Press'))
