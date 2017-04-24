# Sam Eppinger

'''Requires indicoio library to run. Install by running the code:
sudo pip3 install indicoio
'''
import wikipedia
from bs4 import BeautifulSoup
import sys
import indicoio
from key import indico_key
indicoio.config.api_key = indico_key

def find_plot_country(book_page_name):

    page_results = wikipedia.page(book_page_name)
    page_summary = page_results.summary
    places = indicoio.places(page_summary)
    # print('page_results', page_results)
    # print('page_summary', page_summary)

    if places == []:
        print(page_results.section("Plot"))
        page_plot = page_results.section("Plot")
        plot_places = indicoio.places(page_plot)
        pp = plot_places[1]['text']
        print(pp)
    else:
        plot_places_sum = indicoio.places(page_summary)
        ps = plot_places_sum[1]['text']
        print(ps)


if __name__ == '__main__':
        find_plot_country('Adventures of Huckleberry Finn')
#Good to test The Da Vinci Code, and War and Peace, and the Book Thief. These are types of cases
