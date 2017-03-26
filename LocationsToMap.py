# Takes book information as inputs and creates a local map of the locations

import plotly
from plotly.graph_objs import Choropleth, Data, Layout, Figure


def plotGraph(bookTitle, authName, authLoc, pubName, pubLoc, pubDate, isbn):
    author = Choropleth(
        z=['1'],
        autocolorscale=False,
        colorscale=[[0, 'rgb(255,255,255)'], [1, 'rgb(68,94,150)']],
        hoverinfo='text',
        locationmode='country names',
        locations=[authLoc],
        name='Author',
        showscale=False,
        text=[authName+' is from ' + authLoc],
        zauto=False,
        zmax=1,
        zmin=0,
    )
    publisher = Choropleth(
        z=['1'],
        autocolorscale=False,
        colorscale=[[0, 'rgb(255,255,255)'], [1, 'rgb(186,58,51)']],
        hoverinfo='text',
        locationmode='country names',
        locations=[pubLoc],
        name='Publisher',
        showscale=False,
        text=['This edition published in '+pubLoc+' by '+pubName+' in '+pubDate],
        zauto=False,
        zmax=1,
        zmin=0,
    )

    data = Data([author, publisher])

    layout = Layout(
        autosize=True,
        geo=dict(
            countrycolor='rgb(102, 102, 102)',
            countrywidth=0.1,
            lakecolor='rgb(255, 255, 255)',
            landcolor='rgba(237, 247, 138, 0.25)',
            lonaxis=dict(
                gridwidth=1.5999999999999999,
                range=[-180, 180],
                showgrid=False
            ),
            projection=dict(
                type='mollweide'
            ),
            scope='world',
            showland=True,
            showrivers=False,
            showsubunits=True,
            subunitcolor='rgb(102, 102, 102)',
            subunitwidth=0.5
        ),
        hovermode='closest',
        showlegend=True,
        title='Locations of ' + bookTitle,

        margin=dict(
            l=5,
            r=5,
            b=10,
            t=70,
            pad=2)
    )
    fig = Figure(data=data, layout=layout)
    # plots the graph
    plotly.offline.plot(fig, filename='map.html')

# example
plotGraph('War and Peace', 'Leo Tolstoy', 'Russia', 'Signet', 'USA', '2012', '978-0451532114')
