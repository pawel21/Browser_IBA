import dash
from dash import html, dcc

import plotly.express as px
import pandas as pd

dash.register_page(__name__)

layout = html.Div([
    html.H1('This is our Archive page'),
    html.Div('This is our Archive page content.'),
])

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
data = {
    'nazwa_ostoi': ['Ostoja A', 'Ostoja A', 'Ostoja B', 'Ostoja C', 'Ostoja B'],
    'nazwa_polska': ['Sikora', 'Dzięcioł', 'Orzeł', 'Sowa', 'Orzeł'],
    'rok': [2020, 2021, 2022, 2021, 2020],
    'liczba': [10, 15, 5, 8, 12]
}
df = pd.DataFrame(data)
fig = px.bar(df, x="nazwa_ostoi", y="liczba")

layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])