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
VANCITY_DATA_FILE = Path(DATA_DIR, "MetroVan_WasteCompData_2018.csv")

###############
# Our Data Here
###############
user_data_frame = pd.read_csv(USER_DATA_FILE)
vancity_data_frame = pd.read_csv(VANCITY_DATA_FILE)  #-- Contains City of Vancouver Waste data from 2018


user_data_frame["date"] = pd.to_datetime(user_data_frame["date"], format="%m/%d/%Y")
# Graph of User Data
fig = px.bar(user_data_frame, x="date", y="weight_kg", color="plastic_family")

# Comparison Graph
currentday = dt.date(dt.now())
user_today = user_data_frame.tail(5)

vancity_families = vancity_data_frame.loc[(vancity_data_frame['source_type'] == 'multi family') | (vancity_data_frame['source_type'] == 'single family')]   #-- Extract only Single/Multi family data
families_boxline = px.box(vancity_families, x="plastic_family", y="weight_kg", color="source_type")     #-- Genereate boxplot with Vancouver data
families_boxline.add_scatter(y=user_today['weight_kg'], x=user_today['plastic_family'], name="user")    #-- Add scatter plots with data provided by user
families_boxline.update_layout(    #-- Update graph labels
    title="Plastic Waste Comparison",
    xaxis_title="Plastic Waste Type",
    yaxis_title="Plastic Waste in Kg",
    legend_title="Source"
)

###############
# App Layout
###############
app.layout = html.Div(
    children=[
        user_tracking_section,
        #graph_section(fig),
        graph_section(families_boxline),
    ],
    style={"display": "flex", "margin": "50px"},
)


@app.callback(
    dash.dependencies.Output("on-track-button-submit-output", "children"),
    [dash.dependencies.Input("track-button", "n_clicks")],
    [
        dash.dependencies.State("plastic-type", "value"),
        dash.dependencies.State("date-picker", "date"),
        dash.dependencies.State("count-field", "value"),
    ],
)
def on_track_submit(n_clicks, plastic_type_value, date_value, count_value):
    print(f"Entries! [Num Clicks: {n_clicks}] {plastic_type_value} {date_value}")
    if n_clicks is None:
        return ""

    # Parse date string into a date object
    date_value_obj = dt.strptime(re.split("T| ", date_value)[0], "%Y-%m-%d")
    # Format it according to our needs: MM/DD/YYYY
    date_string = date_value_obj.strftime("%m/%d/%Y")

    weight_kg_plastic_type = utils.get_weight_kg_of_plastic(plastic_type_value)
    weight_kg_total = weight_kg_plastic_type * count_value
    # Rounding off to 3 decimal places
    weight_kg_total_str = "{0:.3f}".format(weight_kg_total)
    data = {
        "plastic_family": plastic_type_value,
        "weight_kg": weight_kg_total_str,
        "count": str(count_value),
        "date": date_string,
    }

    new_entry = ",".join(data.values())
    with open(USER_DATA_FILE, "a") as f:
        f.write(f"{new_entry}\n")

    return f"""
        Recorded {count_value} {plastic_type_value} 
        (estimated {weight_kg_total_str} kg) for {date_string}
    """


if __name__ == "__main__":
    app.run_server(debug=True, dev_tools_hot_reload=True)
