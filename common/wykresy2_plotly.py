import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

pio.renderers.default='browser'

x = [1,2,3,4,5]
y = [10,15,13,17,20]

fig1 = px.line(x=x, y=y, title="Wykres liniowy", markers=True)

# fig1.show()

produkty = ["A","B","C","D"]
wyniki = [12,19,7,15]

fig2 = px.bar(
    x=produkty,
    y=wyniki,
    title="Wykres slupkowy",
    orientation="h",
)
# fig2.show()

a = [1,2,3,4,5]
b = [3,7,4,9,6]

fig3= px.scatter(x=a, y=b)
# fig3.show()


# oceny = [2,2,5,5,4,3,2,5,4,3]
# fig4 = px.histogram(x=oceny, title="Oceny", nbins=4)
# fig4.show()

etykiety = ["Python","Java","C++","JS"]
wartosci = [40,25,15,20]

fig5 = px.pie(names=etykiety, values=wartosci, title="Udział języków")
# fig5.show()


# dni = ["Pon", "Wt", "Śr", "Czw", "Pt", "Sob", "Nd"]
# sprzedaz = [120, 150, 180, 160, 170, 210, 190]
#
# fig6 = px.area(x=dni, y=sprzedaz, title="Wykres obszarowy")
# fig6.show()

dni = [1,2,3,4,5]
sprzedaz = [10,12,35,14,78]
koszty = [6,7,8,7,9]

fig = go.Figure()

fig.add_trace(
    go.Scatter(x=dni, y=sprzedaz, mode="lines+markers", name="Sprzedaż")
)
fig.add_trace(
    go.Scatter(x=dni, y=koszty, mode="lines+markers", name="Koszty")
)

fig.update_layout(
    title="Wykresy liniowe",
    xaxis_title="Dzień",
    yaxis_title="Kwota",
)

# fig.show()


# Zadanie 4 Plotly
# Stwórz wykres punktowy, który pokaże zależność między:
# - liczbą godzin nauki
# - wynikiem egzaminu

godziny_nauki = [1, 2, 3, 4, 5, 6, 7]
wyniki = [40, 50, 55, 60, 70, 75, 85]
fig8= px.scatter(x=godziny_nauki, y=wyniki)
# fig8.show()


# Zadanie 5 Plotly
# Stwórz wykres kołowy, który pokaże udział języków programowania używanych przez programistów w projekcie.
jezyki = ["Python", "JavaScript", "Java", "C++", "Go"]
udzial = [35, 30, 15, 10, 10]
fig9 = px.pie(names=jezyki, values=udzial, title="Udział języków")
# fig9.show()

# Zadanie 6 Plotly
# Stwórz interaktywny wykres liniowy, który pokaże temperaturę w kolejnych dniach tygodnia.
dni = ["Pon", "Wt", "Śr", "Czw", "Pt", "Sob", "Nd"]
temperatura = [18, 20, 19, 23, 25, 22, 21]
fig10 = px.line(x=dni, y=temperatura, title="Rozkład temperatury", markers=True)
fig10.show()

import dash
from dash import dcc, html
import plotly.express as px

# Dane
x = [1,2,3,4,5]
y1 = [10,15,13,20,17]
y2 = [3,7,4,9,6]

produkty = ["A","B","C","D"]
wyniki = [12,19,7,15]

oceny = [2,4,5,2,3,4,5,4,3,2,3,4,5]

etykiety = ["Python","Java","C++","Javascript"]
wartosci = [40,25,15,20]

# Wykresy
fig_line = px.line(x=x, y=y1, title="Trend", markers=True)
fig_bar = px.bar(x=produkty, y=wyniki, title="Produkty")
fig_scatter = px.scatter(x=x, y=y2, title="Relacja")
fig_hist = px.histogram(x=oceny, nbins=4, title="Oceny")
fig_pie = px.pie(names=etykiety, values=wartosci, title="Języki")

# Dashboard
app = dash.Dash(__name__)

app.layout = html.Div(
    style={"fontFamily": "Arial", "backgroundColor": "#f5f7fa"},
    children=[
        html.H1("Mój Dashboard", style={"textAlign": "center"}),

        html.Div([
            dcc.Graph(figure=fig_line),
            dcc.Graph(figure=fig_bar),
        ], style={"display": "flex"}),

        html.Div([
            dcc.Graph(figure=fig_scatter),
            dcc.Graph(figure=fig_hist),
        ], style={"display": "flex"}),

        html.Div([
            dcc.Graph(figure=fig_pie)
        ])
    ]
)

if __name__ == "__main__":
    app.run(debug=True)