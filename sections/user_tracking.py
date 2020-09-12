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
            options=[
                {"label": "Film", "value": "Film"},
                {"label": "Textiles", "value": "Textiles"},
                {
                    "label": "Rigid Beverage Containers",
                    "value": "Rigid Beverage Containers",
                },
                {
                    "label": "Rigid Non-Beverage Containers",
                    "value": "Rigid Non-Beverage Containers",
                },
                {"label": "Other", "value": "Other"},
            ]
        ),
        html.Button("Track", id="track"),
    ],
    style={"margin-right": "50px"},
)
