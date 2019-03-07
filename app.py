# -*- coding: utf-8 -*-
import os

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np



df = pd.read_csv('stephen_curry.csv')

style_sheet = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=style_sheet)


steph_table = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict("rows"),
)


scatter_plot_points = dcc.Graph(
            id='pts-per-season',
            figure={
                'data': [
                    go.Scatter(
                        x=df['Season'],
                        y=df['PTS'],
                        mode='markers'
                    ),
                ],
                'layout': go.Layout(
                    title='Points per Season',
                    xaxis= {'title': 'Season',
                            'type': 'category'},
                    yaxis={'title': 'Points'},
                    hovermode='closest'
                )
            }
        )

bar_field_goals = dcc.Graph(
            id='field-goals',
            figure={
                'data': [
                    go.Bar(
                        x=df['Season'],
                        y=df['3P'],
                        name='Three Pointers',
                        marker=go.bar.Marker(
                            color='rgb(255, 255, 0)'
                        )
                    ),
                    go.Bar(
                        x=df['Season'],
                        y=df['2P'],
                        name='Two Pointers',
                        marker=go.bar.Marker(
                            color='rgb(0, 0, 255)'
                        )
                    ),
                    go.Bar(
                        x=df['Season'],
                        y=df['FT'],
                        name='Free Throws',
                        marker=go.bar.Marker(
                            color='rgb(0, 255, 100)'
                        )
                    ),
                ],
                'layout' : go.Layout(
                    title='Field Goals',
                    xaxis= {'title': 'Season',
                            'type': 'category'},
                    yaxis={'title': 'Field Goals'},
                    hovermode='closest'
                )
            }   
        )


app.layout = html.Div([
    html.H1(children='Stephen Curry'),
    html.H2(children='Golden State Warriors, 30, PG'),
    html.P(children='Born: March 14, 1988 in Akron, OH'),
    html.P(children='Age: 30'),
    html.P(children='Drafted: 2009: 1st Rnd, 7th by the Golden State Warriors'),
    html.P(children='College: Davidson'),
    html.Div([
        html.H3(children='Career Statistics'),
        html.P(children= 'Points per Game: ' + str(df['PTS'][10])),
        html.P(children= 'Assists per Game: ' + str(df['AST'][10])),
        html.P(children= 'Rebounds per Game: ' + str(df['TRB'][10])),
    ]),
    steph_table,

    scatter_plot_points,

    bar_field_goals

])



if __name__ == '__main__':
    app.run_server(debug=True)