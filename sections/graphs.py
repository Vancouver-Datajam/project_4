import dash_core_components as dcc
import dash_html_components as html


def graph_section(fig):
    return html.Div(
        children=[
            # TODO GRAPH HERE
            dcc.Graph(id="example-graph", figure=fig),
        ],
        style={"width": "100%"},
    )
