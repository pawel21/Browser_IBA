import dash
from dash import dcc, html, Input, Output
import dash_table
import plotly.express as px
import pandas as pd

# Sample data
data = {
    'nazwa_ostoi': ['Ostoja A', 'Ostoja A', 'Ostoja B', 'Ostoja C', 'Ostoja B'],
    'nazwa_polska': ['Sikora', 'Dzięcioł', 'Orzeł', 'Sowa', 'Orzeł'],
    'rok': [2020, 2021, 2022, 2021, 2020],
    'liczba': [10, 15, 5, 8, 12],
    'latitude': [52.2297, 52.4064, 52.6695, 52.4064, 52.6695],
    'longitude': [21.0122, 16.9252, 20.6036, 16.9252, 20.6036]
}
df = pd.DataFrame(data)

# Initialize the Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Dash App with Data Table and Plots'),

    dcc.Tabs(id='tabs', value='tab-1', children=[
        dcc.Tab(label='Data Table', value='tab-1'),
        dcc.Tab(label='Plots', value='tab-2'),
    ]),

    html.Div(id='tabs-content')
])

@app.callback(Output('tabs-content', 'children'),
              Input('tabs', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            dash_table.DataTable(
                id='datatable',
                columns=[{"name": i, "id": i} for i in df.columns],
                data=df.to_dict('records'),
                filter_action='native',
                sort_action='native',
                page_action='native',
                page_current=0,
                page_size=10,
            )
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.Label('Choose X-axis:'),
            dcc.Dropdown(
                id='xaxis-column',
                options=[{'label': col, 'value': col} for col in df.columns if col not in ['latitude', 'longitude']],
                value='nazwa_ostoi'
            ),
            html.Label('Choose Y-axis:'),
            dcc.Dropdown(
                id='yaxis-column',
                options=[{'label': col, 'value': col} for col in df.columns if col not in ['latitude', 'longitude']],
                value='liczba'
            ),
            dcc.Graph(id='graph')
        ])

@app.callback(
    Output('graph', 'figure'),
    Input('xaxis-column', 'value'),
    Input('yaxis-column', 'value'))
def update_graph(xaxis_column_name, yaxis_column_name):
    fig = px.scatter(df, x=xaxis_column_name, y=yaxis_column_name, color='nazwa_polska')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)