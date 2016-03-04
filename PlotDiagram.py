import plotly.graph_objs as go
import plotly.offline as py

trace1 = go.Bar(
    x=['giraffes', 'orangutans', 'monkeys'],
    y=[20, 14, 23],
    name='SF Zoo'
)
trace2 = go.Bar(
    x=['giraffes', 'orangutans', 'monkeys'],
    y=[12, 18, 29],
    name='LA Zoo'
)
trace3 = go.Bar(
    x=['giraffes', 'orangutans', 'monkeys'],
    y=[15, 7, 8],
    name='SF Zoo'
)
data = [trace1, trace2, trace3]
layout = go.Layout(
    barmode='stack'
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='stacked-bar1')

#########################################
trace1 = go.Bar(
    x=['dog', 'cat', 'mouse'],
    y=[3, 7, 8],
    name='SF Zoo'
)
trace2 = go.Bar(
    x=['dog', 'cat', 'mouse'],
    y=[7, 11, 12],
    name='LA Zoo'
)
trace3 = go.Bar(
    x=['dog', 'cat', 'mouse'],
    y=[5, 6, 9],
    name='SF Zoo'
)
data = [trace1, trace2, trace3]
layout = go.Layout(
    barmode='stack'
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='stacked-bar2')
