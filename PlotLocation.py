# Sam Eppinger

import wikipedia
from bs4 import BeautifulSoup
import sys
import indicoio
from key import indico_key
indicoio.config.api_key = indico_key

def find_plot_country(book_page_name):

    page_results = wikipedia.page(book_page_name)
    page_summary = wikipedia.summary(page_results)
    places = indicoio.places(page_summary)

    if places == []:
        page_plot = page_results.section("Plot")
        plot_places = indicoio.places(page_plot)
        pp = plot_places[1]['text']
        print(pp)
    else:
        plot_places_sum = indicoio.places(page_summary)
        ps = plot_places_sum[1]['text']
        print(ps)


if __name__ == '__main__':
        find_plot_country('The Book Thief')
#Good to test The Da Vinci Code, and War and Peace, and the Book Thief. These are types of cases