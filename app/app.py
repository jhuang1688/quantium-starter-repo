# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Soul Foods'),

    html.Div(
        [
            html.H4("Pink Morsel's Sale Data", className="app__header__title"),
        ],
        className="app__header__desc",
    ),

    # dcc.Graph(
    #     id='example-graph',
    #     figure=fig
    # ),

    html.Button("Switch Axis", n_clicks=0, 
                id='button'),

    dcc.Graph(id="graph"),

])

@app.callback(
    Output("graph", "figure"),
    Input("button", "n_clicks"))
def display_graph(n_clicks):
    df = pd.read_csv('output.csv') # replace with your own data source

    x, y = 'Date', 'Sales'
    fig = px.line(df, x=x, y=y)    
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
