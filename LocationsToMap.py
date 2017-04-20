# Sarah Barden
'''Takes an ISBN code and returns a plotly map highlighting the locations of
the Author, Plot and Publisher.'''

import plotly
from plotly.graph_objs import Choropleth, Data, Layout, Figure
from classBook import Book


def plotGraph(book):

    # makes a choropleth for the author's location
    author = Choropleth(
        z=['1'],
        autocolorscale=False,
        colorscale=[[0, 'rgb(255,255,255)'], [1, 'rgb(68,94,150)']],
        hoverinfo='text',
        locationmode='country names',
        locations=[book.authorLoc],
        name='Author',
        showscale=False,
        text=["{} was born in {}".format(book.author, book.authorLoc)],
        zauto=False,
        zmax=1,
        zmin=0,
    )

    # making a choropleth for the publisher's location.
    publisher = Choropleth(
        z=['1'],
        autocolorscale=False,
        colorscale=[[0, 'rgb(255,255,255)'], [1, 'rgb(186,58,51)']],
        hoverinfo='text',
        locationmode='country names',
        locations=[book.publisherLoc],
        name='Publisher',
        showscale=False,
        text=["{} was published in {}".format(book.title, book.publisherLoc)],
        zauto=False,
        zmax=1,
        zmin=0,
    )

    # making a choropleth for the plot's location.
    plot = Choropleth(
        z=['1'],
        autocolorscale=False,
        colorscale=[[0, 'rgb(255,255,255)'], [1, 'rgb(50,205,50)']],
        hoverinfo='text',
        locationmode='country names',
        locations=[book.plotLoc],
        name='Plot',
        showscale=False,
        text=["{} takes place in {}".format(book.title, book.plotLoc)],
        zauto=False,
        zmax=1,
        zmin=0,
    )

    # combines graphs into one data set
    data = Data([author, publisher, plot])

    # creates a text box to add to layout
    box1 = dict(x=0.50,
                y=0.95,
                yanchor="bottom",
                borderpad=10,
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
            countrycolor='rgb(102, 102, 102)',
            countrywidth=0.1,
            lakecolor='rgb(255, 255, 255)',
            landcolor='rgba(237, 247, 138, 0.25)',
            lonaxis=dict(
                gridwidth=1.5999999999999999,
                range=[-180, 180],
                showgrid=False),
            projection=dict(type='equirectangular'),
            scope='world',
            showcountries=True,
            showland=True,
            showrivers=False,
            showsubunits=True,
            subunitcolor='rgb(102, 102, 102)',
            subunitwidth=0.5
        ),
        hovermode='closest',
        showlegend=True,
        title=None,
        margin=dict(l=5, r=5, b=10, t=70, pad=2)
    )

    fig = Figure(data=data, layout=layout)
    # plots the graph
    plotly.offline.plot(fig, filename='map2.html')


# example for demo
if __name__ == '__main__':
    WarAndPeace = Book('9780143039990')
    WarAndPeace.getInfo()
    WarAndPeace.authorLoc = "Russia"
    WarAndPeace.plotLoc = "USA"
    WarAndPeace.publisherLoc = "USA"

    plotGraph(WarAndPeace)

    # HarryPotter = Book('9780747560777')
    # HarryPotter.getInfo()
    # plotGraph(HarryPotter)

    # KiteRunner = Book('9781594631931')
    # KiteRunner.getInfo()
    # plotGraph(KiteRunner)

    # Tempest = Book('9781461035930')
    # Tempest.getInfo()
    # plotGraph(Tempest)
