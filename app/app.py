# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
# Our dataframe
df = pd.read_csv('output.csv')
 
fig = px.scatter(df, x='Date', y='Sales')
fig.update_traces(mode='markers+lines')
 
app.layout = html.Div(children=[
    html.H1(children='Soul Foods Sales Data'),
 
    html.Div(children='''
        Pink Morsel Product
    '''),
 
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
