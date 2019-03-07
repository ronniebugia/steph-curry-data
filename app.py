# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np



style_sheet = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=style_sheet)


app.layout = html.Div([
    html.H1(children='Stephen Curry'),
    html.H2(children='Golden State Warriors, 30, PG'),
    html.P(children='Born: March 14, 1988 in Akron, OH'),
    html.P(children='Age: 30'),
    html.P(children='Drafted: 2009: 1st Rnd, 7th by the Golden State Warriors'),
    html.P(children='College: Davidson')
])



if __name__ == '__main__':
    app.run_server(debug=True)