import dash
from dash import html, dcc

import plotly.express as px
import pandas as pd

dash.register_page(__name__)

layout = html.Div([
    html.H1('This is our Archive page'),
    html.Div('This is our Archive page content.'),
])

# Sample data similar to the one provided in the Dash app example
data = {
    'nazwa_ostoi': ['Ostoja A', 'Ostoja A', 'Ostoja B', 'Ostoja C', 'Ostoja B'],
    'nazwa_polska': ['Sikora', 'Dzięcioł', 'Orzeł', 'Sowa', 'Orzeł'],
    'rok': [2020, 2021, 2022, 2021, 2020],
    'liczba': [10, 15, 5, 8, 12],
    'latitude': [52.2297, 52.4064, 52.6695, 52.4064, 52.6695],
    'longitude': [21.0122, 16.9252, 20.6036, 16.9252, 20.6036]
}
df = pd.DataFrame(data)

# Create a scatter mapbox plot
fig = px.scatter_mapbox(df, lat='latitude', lon='longitude', color='nazwa_polska', size='liczba',
                        color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=5,
                        mapbox_style="carto-positron")

fig.show()

layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-map',
        figure=fig
    )
],
    style = {'display': 'inline-block', 'width': '48%'})