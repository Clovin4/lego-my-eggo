import dash
from dash import dcc, html
import plotly.graph_objects as go

import pandas as pd
import numpy as np

# Create dataframes for dashboard visualization
df = pd.read_csv('/Users/christianl/repos/lego-my-eggo/data/raw/lego-database/themes.csv')

# Create a list of unique themes
themes = df['name'].unique()

# dash app
app = dash.Dash(__name__)

# layout
app.layout = html.Div([
    html.H1('Lego My Eggo'),
    html.H2('A dashboard for visualizing the Lego dataset'),
    html.H3('Select a theme:'),
    dcc.Dropdown(
        id='theme-dropdown',
        options=[{'label': i, 'value': i} for i in themes],
        value='Star Wars'
    )
])

# callback
@app.callback(
    dash.dependencies.Output('theme-dropdown', 'figure'),
    [dash.dependencies.Input('theme-dropdown', 'value')])
def update_figure(selected_theme):
    filtered_df = df[df.theme_name == selected_theme]

    fig = go.Figure(data=[go.Bar(
        x=filtered_df['year'],
        y=filtered_df['num_parts'],
        text=filtered_df['set_name'],
        textposition='auto',
    )])

    fig.update_layout(
        title_text=f'Number of parts in {selected_theme} sets over time',
        xaxis_title='Year',
        yaxis_title='Number of parts',
        xaxis_tickangle=-45,
        yaxis_type='log',
        height=600,
        width=800
    )

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)


# Path: src/visualization/visualize.py
