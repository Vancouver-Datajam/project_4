from pathlib import Path

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

from sections.user_tracking import user_tracking_section
from sections.graphs import graph_section
import utils

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


DATA_DIR = Path(__file__).parent / "data"
USER_DATA_FILE = Path(DATA_DIR, "User_WasteData.csv")


@app.callback(
    dash.dependencies.Output("on-track-button-submit-output", "children"),
    [dash.dependencies.Input("track-button", "n_clicks")],
    [dash.dependencies.State("plastic-type", "value")],
)
def on_track_submit(n_clicks, plastic_type_value):
    print(f"Tracking! {n_clicks} {plastic_type_value}")
    if n_clicks is None:
        return ""

    data = {
        "plastic_family": plastic_type_value,
        "weight_kg": str(utils.get_weight_kg_of_plastic(plastic_type_value)),
        "count": "1",
        # TODO
        "date": "01/12/2000",
    }

    new_entry = ",".join(data.values())
    with open(USER_DATA_FILE, "a") as f:
        f.write(f"{new_entry}\n")

    return "Tracked!"


if __name__ == "__main__":
    app.run_server(debug=True, dev_tools_hot_reload=True)
