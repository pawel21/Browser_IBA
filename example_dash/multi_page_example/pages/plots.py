import dash
from dash import html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd

dash.register_page(__name__)
# Sample data
data = {
    'nazwa_ostoi': ['Ostoja A', 'Ostoja A', 'Ostoja B', 'Ostoja C', 'Ostoja B'],
    'nazwa_polska': ['Sikora', 'Dzięcioł', 'Orzeł', 'Sowa', 'Orzeł'],
    'rok': [2020, 2021, 2022, 2021, 2020],
    'liczba': [10, 15, 5, 8, 12]
}
df = pd.DataFrame(data)

df = pd.read_excel("../../../df_test.xlsx")

layout = html.Div([
    html.H1('Simple Histogram Example'),

    html.Label('Choose a column for the histogram:'),
    dcc.Dropdown(
        id='column-dropdown',
        options=['liczba_par_min', 'liczba_par_max'],
        value='liczba_par_min'
    ),

    dcc.Graph(id='histogram-graph'),

    html.H1('Simple Bar Example'),

    html.Label('Choose a column for the histogram:'),
    dcc.Dropdown(
        id='column-dropdown-2',
        options=[{'label': i, 'value': i} for i in df['nazwa_polska'].unique()],
        value='Bielik'
    ),

    dcc.Graph(id='bar-graph')
])


@callback(
    Output('histogram-graph', 'figure'),
    Input('column-dropdown', 'value'))
def update_histogram(selected_column):
    fig = px.histogram(df, x=selected_column)
    return fig

@callback(
    Output('bar-graph', 'figure'),
    Input('column-dropdown-2', 'value'))
def update_histogram(selected_column):
    print(f"Selected column: {selected_column}")
    # Filter the dataframe for
    df_delta_swiny = df[df['nazwa_ostoi'] == "Delta Świny"]
    df_ptak = df_delta_swiny[df_delta_swiny['nazwa_polska'] == selected_column]
    print(df_ptak['rok'])
    print(df_ptak['liczba_par_max'])
    # Create the bar plot
    fig = px.bar(df_ptak, x='rok', y=['liczba_par_max', 'liczba_par_min'],
                 labels={'value': 'Liczba Par', 'variable': 'Typ Liczby Par', 'rok': 'Rok'},
                 title='Liczba Par Max i Min dla "bąk" w Delta Świny')

    # Update layout for better visualization
    fig.update_layout(barmode='group')


    return fig
