import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

from sections.user_tracking import user_tracking_section
from sections.graphs import graph_section

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

###############
# Our Data Here
###############
df = pd.DataFrame(
    {
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"],
    }
)

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

###############
# App Layout
###############
app.layout = html.Div(
    children=[
        user_tracking_section,
        graph_section(fig),
    ],
    style={"display": "flex", "margin": "50px"},
)


if __name__ == "__main__":
    app.run_server(debug=True, dev_tools_hot_reload=True)
