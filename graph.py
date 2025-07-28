import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc
from sqlalchemy import create_engine

# Database connection
engine = create_engine("mysql+mysqlconnector://root:root@localhost/stock")

# Load data from MySQL
df = pd.read_sql("SELECT * FROM stock_market", engine)

# Format date to dd-mm-yyyy (assumes all data is June 2025)
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
df['DisplayDate'] = df['Date'].dt.strftime('%d-%m-%Y')

# Start Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

btn_style = {
    "backgroundColor": "#E6F2FA", "color": "black", "fontWeight": "bold",
    "padding": "20px 10px", "borderRadius": "5px", "textAlign": "center",
    "fontSize": "18px", "minHeight": "80px"
}

app.layout = dbc.Container([
    html.H2("Stock Market Analysis for June 2025",
            style={'backgroundColor': 'blue', 'color': 'white', 'textAlign': 'center', 'padding': '10px'}),

    dbc.Row([
        dbc.Col([
            html.Label("Tickers", style={'fontWeight':'bold'}),
            dcc.Dropdown(
                id="ticker-filter",
                options=[{"label": t, "value": t} for t in sorted(df["Ticker"].dropna().unique())],
                multi=True, placeholder="Select Ticker(s)"
            ),
            html.Br(),
            html.Label("Date", style={'fontWeight':'bold'}),
            dcc.Dropdown(
                id="date-filter",
                options=[{"label": d, "value": d} for d in sorted(df["DisplayDate"].dropna().unique())],
                multi=True, placeholder="Select Date(s)"
            ),
            html.Br(),
            html.Label("Sector", style={'fontWeight':'bold'}),
            dcc.Dropdown(
                id="sector-filter",
                options=[{"label": s, "value": s} for s in sorted(df["Sector"].dropna().unique())],
                multi=False, placeholder="Select Sector"
            ),
            html.Br(),
            html.Label("Market Cap Range", style={'fontWeight':'bold'}),
            dcc.RangeSlider(
                id='marketcap-filter',
                min=df["Market Cap"].min(),
                max=df["Market Cap"].max(),
                step=1e9,
                value=[df["Market Cap"].min(), df["Market Cap"].max()],
                tooltip={"placement": "bottom", "always_visible": True}
            ),
        ], width=3, style={'backgroundColor': '#d9f2ff', 'padding': '15px'}),

        dbc.Col([
            dbc.Row([dbc.Col(html.Div(id='stock-name-btn', style=btn_style), width=4),
                     dbc.Col(html.Div(id='high-price-btn', style=btn_style), width=4),
                     dbc.Col(html.Div(id='low-price-btn', style=btn_style), width=4)]),
            dbc.Row([dbc.Col(html.Div(id='avg-open-btn', style=btn_style), width=4),
                     dbc.Col(html.Div(id='avg-close-btn', style=btn_style), width=4),
                     dbc.Col(html.Div(id='avg-high-btn', style=btn_style), width=4)]),
            dbc.Row([dbc.Col(html.Div(id='avg-low-btn', style=btn_style), width=4),
                     dbc.Col(html.Div(id='pe-ratio-btn', style=btn_style), width=4),
                     dbc.Col(html.Div(), width=4)]),
        ], width=9),
    ]),

    html.Br(),

    dbc.Row([dbc.Col(dcc.Graph(id='line-chart'), width=6),
             dbc.Col(dcc.Graph(id='bar-chart'), width=6)]),

    dbc.Row([dbc.Col(dcc.Graph(id='sector-pie-chart'), width=6),
             dbc.Col(dcc.Graph(id='comparison-chart'), width=6)]),

    dbc.Row([dbc.Col(dcc.Graph(id='fallback-graph'), width=12)])
], fluid=True)

@app.callback(
    Output('line-chart', 'figure'),
    Output('bar-chart', 'figure'),
    Output('sector-pie-chart', 'figure'),
    Output('comparison-chart', 'figure'),
    Output('fallback-graph', 'figure'),
    Output('stock-name-btn', 'children'),
    Output('high-price-btn', 'children'),
    Output('low-price-btn', 'children'),
    Output('avg-open-btn', 'children'),
    Output('avg-close-btn', 'children'),
    Output('avg-high-btn', 'children'),
    Output('avg-low-btn', 'children'),
    Output('pe-ratio-btn', 'children'),
    Input('ticker-filter', 'value'),
    Input('sector-filter', 'value'),
    Input('date-filter', 'value'),
    Input('marketcap-filter', 'value')
)
def update_dashboard(tickers, sector, dates, cap_range):
    dff = df.copy()
    dff = dff[(dff['Market Cap'] >= cap_range[0]) & (dff['Market Cap'] <= cap_range[1])]

    if tickers:
        dff = dff[dff['Ticker'].isin(tickers)]

    if sector:
        dff = dff[dff['Sector'] == sector]

    if dates:
        dff = dff[dff['DisplayDate'].isin(dates)]

    if not dff.empty:
        line = px.line(dff, x='Date', y='Close Price', color='Ticker', title='Stock Price Over Time')
        bar = px.bar(dff.groupby(['Ticker'])['Close Price'].mean().reset_index(), x='Ticker', y='Close Price',
                     title='Avg Close Price', color='Ticker')
        pie = px.pie(dff, values='Market Cap', names='Sector', title='Sector Market Cap Distribution')
        comp = px.bar(dff, x='Ticker', y='Open Price', color='Ticker', title='Opening Prices Comparison')
        fallback = px.bar(dff.groupby(['Ticker'])['Market Cap'].mean().reset_index(), x='Ticker', y='Market Cap',
                          color='Ticker', title='Fallback Market Cap')
        ticker_names = dff['Ticker'].dropna().unique()
        stock_btn = html.Div(["Tickers", html.Br(), ", ".join(ticker_names[:3]) + ("..." if len(ticker_names) > 3 else "")])
        hp = html.Div(["52 Week High", html.Br(), f"${dff['52 Week High'].max():.2f}"])
        lp = html.Div(["52 Week Low", html.Br(), f"${dff['52 Week Low'].min():.2f}"])
        ao = html.Div(["Avg Open", html.Br(), f"${dff['Open Price'].mean():.2f}"])
        ac = html.Div(["Avg Close", html.Br(), f"${dff['Close Price'].mean():.2f}"])
        ah = html.Div(["Avg High", html.Br(), f"${dff['High Price'].mean():.2f}"])
        al = html.Div(["Avg Low", html.Br(), f"${dff['Low Price'].mean():.2f}"])
        pe = html.Div(["Avg PE Ratio", html.Br(), f"{dff['PE Ratio'].mean():.2f}"])
    else:
        empty = px.bar(title='No data found')
        line = bar = pie = comp = fallback = empty
        stock_btn = hp = lp = ao = ac = ah = al = pe = html.Div("-")

    return line, bar, pie, comp, fallback, stock_btn, hp, lp, ao, ac, ah, al, pe

if __name__ == "__main__":
    app.run(debug=True)
