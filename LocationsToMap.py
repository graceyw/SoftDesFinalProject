# Sarah Barden
'''Takes an ISBN code and returns a plotly map highlighting the locations of
the Author, Plot and Publisher.'''

import plotly
from plotly.graph_objs import Choropleth, Data, Layout, Figure
from classBook import Book


def plotGraph(book):

    locations = Choropleth(
        z=['0', '1', '2'],
        autocolorscale=False,
        hoverinfo='text',
        locationmode='country names',
        locations=[book.authorLoc, book.publisherLoc, book.plotLoc],
        name='Locations',
        showscale=False,
        text=["{} was born in {}".format(book.author, book.authorLoc),
              "{} was published in {}".format(book.title, book.publisherLoc),
              "{} takes place in {}".format(book.title, book.plotLoc)],
        zauto=False,
        zmax=2,
        zmin=0,
    )

    data = Data([locations])
    # creates a text box to add to layout
    box1 = dict(x=0.50,
                y=0.85,
                yanchor="bottom",
                borderpad=0,
                bordercolor='rgb(0, 0, 0)',
                borderwidth=0,
                # print the book information as a string
                text=book.__str__(),
                font=dict(size=14),
                align="left",
                showarrow=False)

    layout = Layout(
        autosize=True,
        annotations=[box1],
        geo=dict(
            countrycolor='rgb(0, 0, 0)',
            countrywidth=0.1,
            lakecolor='rgb(230, 230, 255)',  # blue
            landcolor='rgb(255, 255, 240)',  # tan
            lonaxis=dict(
                gridwidth=1.5999999999999999,
                range=[-180, 180],
                showgrid=False),
            projection=dict(type='equirectangular'),
            scope='world',
            showcountries=True,
            showland=True,
            showlakes=False,
            showrivers=False,
            showsubunits=True,
            subunitcolor='rgb(0, 0, 0)',
            subunitwidth=0.5
        ),
        hovermode='closest',
        showlegend=False,
        title=None,
        margin=dict(l=20, r=20, b=10, t=10, pad=2)
    )

    fig = Figure(data=data, layout=layout)
    # plots the graph
    plotly.offline.plot(fig, filename='map2.html')


# example for demo
if __name__ == '__main__':

    # book = Book('9780143039990')
    # book.getInfo()
    # plotGraph(book)

    # HarryPotter = Book('9780747560777')
    # HarryPotter.getInfo()
    # plotGraph(HarryPotter)

    KiteRunner = Book('9781594631931')
    KiteRunner.getInfo()

    KiteRunner.authorLoc = "Afghanistan"
    KiteRunner.plotLoc = "Pakistan, Fremont, CA"
    KiteRunner.publisherLoc = "United States"
    plotGraph(KiteRunner)

    # Tempest = Book('9781461035930')
    # Tempest.getInfo()
    # plotGraph(Tempest)
