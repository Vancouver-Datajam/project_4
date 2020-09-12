import dash_core_components as dcc
import dash_html_components as html


def graph_section(fig):
    return html.Div(
        children=[
            html.H1(children="Hello Graphs"),
            html.Div(
                children="""
            Dash: A Graphs here
        """
            ),
            # TODO GRAPH HERE
            # dcc.Graph(id="example-graph", figure=fig),
        ],
    )
