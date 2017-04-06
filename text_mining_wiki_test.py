import wikipedia
from bs4 import BeautifulSoup

# This step uses the search to find the book. This is used to confirm that a book
# does exist when the page function doesn't return something that makes sense
# Use if something doesn't work.
# wiki_resaults = wikipedia.search("War and Peace")
# pg_resaults = wikipedia.page(title=wiki_resaults[0])

# When this becomes a function change this to aelement user input
# Works for: Great Gatsby, Name of the Wind, War and Peace
# Does not work for: Harry Potter, Artemis Fowl
pg_results = wikipedia.page("The Kite Runner")

# This generates the page's html. This can be optimized by not doing the whole doc.
pg_html = pg_results.html()

# This makes it readable (not nessassary after testing)
soup = BeautifulSoup(pg_html, 'html.parser')

# This will select all parts that are prefixed by <tr> (includes the country of the book)
# This could prob be optimized by begining approx 800 char in.
# all_tr = soup.table.find_all('tr')
table = soup.findAll("table", { "class" : "infobox" })

all_th = soup.table.find_all('th')
header = next(element for element in all_th if element.getText() == 'Country')
header.findNext('td').getText().strip()           # Print country name

# dir(table[0].find_all('th')[2])       # test
