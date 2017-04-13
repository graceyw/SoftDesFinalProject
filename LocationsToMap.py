# Sarah Barden
# Takes book information as inputs and creates a local map of the locations

import plotly
from plotly.graph_objs import Choropleth, Data, Layout, Figure
from classBook import Book
from plotly import widgets


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
        text=[book.authorLoc],
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
        text=[book.publisherLoc],
        zauto=False,
        zmax=1,
        zmin=0,
    )

    # combines graphs into one data set
    data = Data([author, publisher])

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

    # interactive widget
    # g2 = widgets.GraphWidget('https://plot.ly/~kevintest/1178/')
    #
    # button = widgets.Button(description="Submit")
    #
    # text_input = widgets.Text(
    #     description='Borough:',
    #     value='MANHATTAN',
    # )
    #
    # message = widgets.HTML(value="",)
    #
    # valid = widgets.Valid(value=True,)
    #
    # # this will be initalize our listener
    # button.on_click()
    #
    # container = widgets.HBox(children=[text_input, button, valid, message])
    # plotly.offline.plot(container)
    # plotly.offline.plot(g2)


# example for demo
if __name__ == '__main__':
    # WarAndPeace = Book('9780143039990')
    # WarAndPeace.getInfo()
    # plotGraph(WarAndPeace)

    HarryPotter = Book('9780747560777')
    HarryPotter.getInfo()
    plotGraph(HarryPotter)

    # KiteRunner = Book('9781594631931')
    # KiteRunner.getInfo()
    # plotGraph(KiteRunner)

    # Tempest = Book('9781461035930')
    # Tempest.getInfo()
    # plotGraph(Tempest)
