# Sarah Barden
'''Takes an ISBN code and returns a plotly map highlighting the locations of
the Author, Plot and Publisher.'''

import folium
from opencage.geocoder import OpenCageGeocode
from key import geokey
from time import sleep


def geocode(place):
    geocoder = OpenCageGeocode(geokey)
    location = geocoder.geocode(place, key=geokey)
    if location == []:
        pass
    else:
        longitude = location[0]['geometry']['lng']
        latitude = location[0]["geometry"]["lat"]
        print(latitude, longitude)
        return [latitude, longitude]


def plotGraph(book):
    map1 = folium.Map(zoom_start=2, tiles='Mapbox bright')
    folium.Marker(geocode(book.authorLoc),
                  icon=folium.Icon(color='red'),
                  popup='{} is from {}'.format(book.author, book.authorLoc)
                  ).add_to(map1)
    sleep(1)
    folium.Marker(geocode(book.publisherLoc),
                  icon=folium.Icon(color='green'),
                  popup='This edition was published in {}'.format(book.publisherLoc)
                  ).add_to(map1)
    sleep(1)
    folium.Marker(geocode(book.plotLoc),
                  icon=folium.Icon(color='blue'),
                  popup='{} takes place in {}'.format(book.title, book.plotLoc),
                  ).add_to(map1)
    map1.save('map.html')


if __name__ == '__main__':
    pass
