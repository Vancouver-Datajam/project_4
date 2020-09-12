from datetime import datetime as dt
from pathlib import Path
import re

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

DATA_DIR = Path(__file__).parent / "data"
USER_DATA_FILE = Path(DATA_DIR, "User_WasteData.csv")

###############
# Our Data Here
###############
user_data_frame = pd.read_csv(USER_DATA_FILE)

# Graph of User Data
fig = px.bar(user_data_frame, x="date", y="weight_kg", color="plastic_family")

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


@app.callback(
    dash.dependencies.Output("on-track-button-submit-output", "children"),
    [dash.dependencies.Input("track-button", "n_clicks")],
    [
        dash.dependencies.State("plastic-type", "value"),
        dash.dependencies.State("date-picker", "date"),
    ],
)
def on_track_submit(n_clicks, plastic_type_value, date_value):
    print(f"Entries! [Num Clicks: {n_clicks}] {plastic_type_value} {date_value}")
    if n_clicks is None:
        return ""

    # Parse date string into a date object
    date_value_obj = dt.strptime(re.split("T| ", date_value)[0], "%Y-%m-%d")
    # Format it according to our needs: MM/DD/YYYY
    date_string = date_value_obj.strftime("%m/%d/%Y")
    data = {
        "plastic_family": plastic_type_value,
        "weight_kg": str(utils.get_weight_kg_of_plastic(plastic_type_value)),
        "count": "1",
        # TODO
        "date": date_string,
    }

    new_entry = ",".join(data.values())
    with open(USER_DATA_FILE, "a") as f:
        f.write(f"{new_entry}\n")

    return "Tracked!"


if __name__ == "__main__":
    app.run_server(debug=True, dev_tools_hot_reload=True)
