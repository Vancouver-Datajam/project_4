from datetime import datetime as dt
import dash_core_components as dcc
import dash_html_components as html


user_tracking_section = html.Div(
    children=[
        html.H1(children="Plastic Footprint"),
        html.P(
            children="""
            By default you are seeing a graph of Vancouver's Plastic Waste.
             Track your plastic waste to see how you compare with the city.
        """,
            style={"margin-bottom": "40px"},
        ),
        html.Label(children="Date", style={"font-weight": "bold"}),
        dcc.DatePickerSingle(
            id="date-picker",
            min_date_allowed=dt(2000, 8, 5),
            max_date_allowed=dt.today(),
            date=dt.today(),
            style={"margin-bottom": "40px"},
        ),
        html.Label(children="Plastic Waste Type", style={"font-weight": "bold"}),
        # TODO UI looks like this should be a button?
        dcc.RadioItems(
            id="plastic-type",
            value="film",
            options=[
                {"label": "Film", "value": "film"},
                {"label": "Textiles", "value": "textiles"},
                {
                    "label": "Rigid Beverage Container",
                    "value": "rigid beverage container",
                },
                {
                    "label": "Rigid Non-Beverage Containers",
                    "value": "rigid non-beverage container",
                },
                {"label": "Other", "value": "other"},
            ],
            style={"margin-bottom": "40px"},
        ),
        html.Label(children="Plastic Waste Count", style={"font-weight": "bold"}),
        dcc.Input(
            id="count-field",
            type="number",
            placeholder=1,
            value=1,
            min=1,
            style={"margin-bottom": "40px"},
        ),
        html.Button("Track", id="track-button"),
        html.P(id="on-track-button-submit-output", children=""),
    ],
    style={"margin-right": "50px", "width": "300px"},
)
