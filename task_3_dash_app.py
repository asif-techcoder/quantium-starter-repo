import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load processed data
df = pd.read_csv("processed_sales.csv")

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Sort by date
df = df.sort_values("date")

# Create line chart
fig = px.line(
    df,
    x="date",
    y="sales",
    color="region",
    title="Pink Morsel Sales Over Time",
    labels={
        "date": "Date",
        "sales": "Total Sales"
    }
)

# Create Dash app
app = Dash(__name__)


app.layout = html.Div(
    style={
        "backgroundColor": "#0f172a",
        "padding": "30px",
        "fontFamily": "Arial"
    },
    children=[
    html.H1(
        "Pink Morsel Sales Analysis",
        style={"textAlign": "center"}
    ),

    html.Label("Select Region:"),

    dcc.RadioItems(
        id="region-filter",
        options=[
            {"label": "All", "value": "all"},
            {"label": "North", "value": "north"},
            {"label": "South", "value": "south"},
            {"label": "East", "value": "east"},
            {"label": "West", "value": "west"},
        ],
        value="all",
        inline=True,
    ),

    dcc.Graph(id="sales-line-chart")
])
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):

    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"].str.lower() == selected_region]

    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        color="region",
        title="Pink Morsel Sales Over Time",
        labels={
            "date": "Date",
            "sales": "Total Sales"
        }
    )

    return fig

if __name__ == "__main__":
    app.run(debug=True)