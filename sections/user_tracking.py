from datetime import datetime as dt
import dash_core_components as dcc
import dash_html_components as html


user_tracking_section = html.Div(
    children=[
        html.H1(children="Plastic Footprint"),
        html.P(children="By default you are seeing..."),
        dcc.DatePickerSingle(
            id="date-picker",
            date=dt.today(),
        ),
        html.P(children="Plastic Waste"),
        # TODO UI looks like this should be a button?
        dcc.RadioItems(
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
        ),
        html.Button("Track", id="track"),
    ],
    style={"margin-right": "50px"},
)
