import dash
from dash import html, dcc, Input, Output
import pandas as pd
import plotly.express as px

data = {
    'ptak_nr': [101, 102, 103, 104],
    'id': [1, 2, 3, 4],
    'kod_ostoi': ['O001', 'O002', 'O003', 'O004'],
    'nazwa_ostoi': ['Ostoja A', 'Ostoja B', 'Ostoja C', 'Ostoja D'],
    'nazwa_polska': ['Sikora', 'Jaskółka', 'Wróbel', 'Kruk'],
    'nazwa_lacinska': ['Parus', 'Hirundo', 'Passer', 'Corvus'],
    'status': ['chroniony', 'niechroniony', 'chroniony', 'chroniony'],
    'liczba_par_min': [50, 100, 150, 200],
    'liczba_par_max': [55, 150, 200, 250],
    'dokladnosc_oszac': ['wysoka', 'średnia', 'niska', 'wysoka'],
    'kryterium': ['I', 'II', 'III', 'IV'],
    'rok': [2021, 2020, 2020, 2021],
    'aktualne': [True, True, True, True]
}

df = pd.DataFrame(data)

# df = pd.read_excel("../../przydzielanie kryteriow.xls")

# Inicjalizacja aplikacji Dash
app = dash.Dash(__name__)

# Layout aplikacji, wprowadzanie Dropdown do filtrowania i wyświetlenie tabeli
app.layout = html.Div([
    html.H1("Filtracja danych o ptakach"),
    html.Label("Wybierz nazwę ostoi:"),
    dcc.Dropdown(
        id='nazwa_ostoi_dropdown',
        options=[{'label': i, 'value': i} for i in df['nazwa_ostoi'].unique()],
        multi=True
    ),
    html.Label("Wybierz nazwę polską ptaka:"),
    dcc.Dropdown(
        id='nazwa_polska_dropdown',
        options=[{'label': i, 'value': i} for i in df['nazwa_polska'].unique()],
        multi=True
    ),
    html.Label("Wybierz rok:"),
    dcc.Dropdown(
        id='rok_dropdown',
        options=[{'label': i, 'value': i} for i in df['rok'].unique()],
        multi=True
    ),
    html.Div(id='tabela_div')
])




# Callback do aktualizacji danych w tabeli
@app.callback(
    Output('tabela_div', 'children'),
    [Input('nazwa_ostoi_dropdown', 'value'),
     Input('nazwa_polska_dropdown', 'value'),
     Input('rok_dropdown', 'value')]
)
def update_table(selected_nazwa_ostoi, selected_nazwa_polska, selected_rok):
    filtered_df = df.copy()
    if selected_nazwa_ostoi:
        filtered_df = filtered_df[filtered_df['nazwa_ostoi'].isin(selected_nazwa_ostoi)]
    if selected_nazwa_polska:
        filtered_df = filtered_df[filtered_df['nazwa_polska'].isin(selected_nazwa_polska)]
    if selected_rok:
        filtered_df = filtered_df[filtered_df['rok'].isin(selected_rok)]

    return html.Div([
        html.H2("Wyniki filtrowania:"),
        dash.dash_table.DataTable(
            data=filtered_df.to_dict('records'),
            columns=[{'name': i, 'id': i} for i in filtered_df.columns]
        )
    ])

# Uruchomienie serwera
if __name__ == '__main__':
    app.run_server(debug=True)