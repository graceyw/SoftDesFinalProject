# Sarah Barden
'''Takes an ISBN code and returns a plotly map highlighting the locations of
the Author, Plot and Publisher.'''

import folium
from geopy.geocoders import Nominatim


def geocode(place):
    geolocator = Nominatim()
    location = geolocator.geocode(place)
    print(location)
    if location is None:
        pass
    else:
        return [location.latitude, location.longitude]


def plotGraph(book):
    map1 = folium.Map(zoom_start=2, tiles='Mapbox bright')
    folium.Marker(geocode(book.authorLoc),
                  icon=folium.Icon(color='red'),
                  popup='{} is from {}'.format(book.author, book.authorLoc)
                  ).add_to(map1)

    folium.Marker(geocode(book.publisherLoc),
                  icon=folium.Icon(color='green'),
                  popup='This edition was published in {}'.format(book.publisherLoc)
                  ).add_to(map1)

    folium.Marker(geocode(book.plotLoc),
                  icon=folium.Icon(color='blue'),
                  popup='{} takes place in {}'.format(book.title, book.plotLoc),
                  ).add_to(map1)
    map1.save('map.html')


if __name__ == '__main__':
    pass
    # book = Book('9780143039990')
    # book.getInfo()
    # plotGraph(book)

    # HarryPotter = Book('9780747560777')
    # HarryPotter.getInfo()
    # plotGraph(HarryPotter)

    # KiteRunner = Book('9781594631931')
    # KiteRunner.getInfo()
    #
    # KiteRunner.authorLoc = "Afghanistan"
    # KiteRunner.plotLoc = "Pakistan, Fremont, CA"
    # KiteRunner.publisherLoc = "United States"
    # plotGraph(KiteRunner)

    # Tempest = Book('9781461035930')
    # Tempest.getInfo()
    # plotGraph(Tempest)
