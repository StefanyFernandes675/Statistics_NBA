import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import plotly.express as px

df = pd.read_csv("all_seasons.csv")
df = df.drop('Unnamed: 0', axis=1)

st.sidebar.header('Escolha o time que você quer filtrar')

teams = sorted(df.team_abbreviation.unique())
selected_team = st.sidebar.selectbox('Times', teams)

@st.cache
def select_data(team_selected):
    select = df[df["team_abbreviation"] == team_selected]
    return select
new_data = select_data(selected_team)

if selected_team == 'ATL':
    st.title("Atlanta Hawks")
elif selected_team == 'BKN':
    st.title("Brooklyn Nets")
elif selected_team == 'BOS':
    st.title("Boston Celtics")
elif selected_team == 'CHA' or selected_team == 'CHH':
    st.title("Charlotte Hornets")
elif selected_team == 'CHI':
    st.title("Chicago Bulls")
elif selected_team == 'CLE':
    st.title("Cleveland Cavaliers")
elif selected_team == 'DAL':
    st.title("Dallas Mavericks")
elif selected_team == 'DEN':
    st.title("Denver Nuggets")
elif selected_team == 'DET':
    st.title("Detroit Pistons")
elif selected_team == 'GSW':
    st.title("Golden State Warriors")
elif selected_team == 'HOU':
    st.title("Houston Rockets")
elif selected_team == 'IND':
    st.title("Indiana Pacers")
elif selected_team == 'LAC':
    st.title("Los Angeles Clippers")
elif selected_team == 'LAL':
    st.title("Los Angeles Lakers")
elif selected_team == 'MEM':
    st.title("Memphis Grizzlies")
elif selected_team == 'MIA':
    st.title("Miami Heat")
elif selected_team == 'MIL':
    st.title("Milwaukee Bucks")
elif selected_team == 'MIN':
    st.title("Minnesota Timberwolves")
elif selected_team == 'NJN':
    st.title("New Jersey Nets")
elif selected_team == 'NOH':
    st.title("New Orleans Hornets")
elif selected_team == 'NOK':
    st.title("New Orleans/Oklahoma City Hornets")
elif selected_team == 'NOP':
    st.title("New Orleans Pelicans")
elif selected_team == 'NYK':
    st.title("New York Knicks")
elif selected_team == 'OKC':
    st.title("Oklahoma City Thunder")
elif selected_team == 'ORL':
    st.title("Orlando Magic")
elif selected_team == 'PHI':
    st.title("Philadelphia 76ers")
elif selected_team == 'PHX':
    st.title("Phoenix Suns")
elif selected_team == 'POR':
    st.title("Portland Trail Blazers")
elif selected_team == 'SAC':
    st.title("Sacramento Kings")
elif selected_team == 'SAS':
    st.title("San Antonio Spurs")
elif selected_team == 'SEA':
    st.title("Seattle SuperSonics ")
elif selected_team == 'TOR':
    st.title("Toronto Raptors")
elif selected_team == 'UTA':
    st.title("Utah Jazz")
elif selected_team == 'VAN':
    st.title("Vancouver Grizzlies")
elif selected_team == 'WAS':
    st.title("Washington Wizards")

if selected_team != 'NOK':
    image = './images/' + selected_team.lower() + '.png'
else:
    image = './images/' + selected_team.lower() + '.gif'
images = Image.open(image)
captions = selected_team + ' logo'
st.image(image, caption=captions, width=200)

line_chart = new_data.copy()
seasons = sorted(line_chart.season.unique())
pts_sum = []
ast_sum = []
reb_sum = []
first_season = line_chart.iloc[0, 20]
last_season = line_chart.iloc[line_chart.shape[0]-1, 20]
first_season = int(first_season[0:4])
last_season = int(last_season[0:4])

st.title("Informações gerais")
st.subheader(f"{first_season}-{last_season}")

if selected_team != 'NOH':
    years = list((range(first_season, last_season+1)))
else:
    years = (2002, 2003, 2004, 2007, 2008, 2009, 2010, 2011, 2012)
for ano in seasons:
    select = line_chart[line_chart["season"] == ano]
    pontos = select["pts"].sum()
    ast = select["ast"].sum()
    reb = select["reb"].sum()
    pts_sum.append(pontos)
    ast_sum.append(ast)
    reb_sum.append(reb)

st.dataframe(new_data)

st.title("Análise geral das temporadas")
grafico = px.bar(x=years, y=pts_sum, title="Somatória de pontos por temporada")
st.write(grafico)

grafico = px.bar(x=years, y=ast_sum, title="Somatória de assitências por temporada")
st.write(grafico)

grafico = px.bar(x=years, y=reb_sum, title="Somatória de rebotes por temporada")
st.write(grafico)