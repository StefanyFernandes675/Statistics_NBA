import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import plotly.express as px

st.title('NBA Teams')

df = pd.read_csv("all_seasons.csv")
df = df.drop('Unnamed: 0', axis=1)
df["draft_year"] = pd.to_numeric(df["draft_year"], errors="coerce")
df["draft_round"] = pd.to_numeric(df["draft_round"], errors="coerce")
df["draft_number"] = pd.to_numeric(df["draft_number"], errors="coerce")

st.sidebar.header('Escolha o time que você quer filtrar')

teams = sorted(df.team_abbreviation.unique())
selected_team = st.sidebar.selectbox('Times', teams)

@st.cache
def select_data(team_selected):
    select = df[df["team_abbreviation"] == team_selected]
    return select
new_data = select_data(selected_team)

image = './images/' + selected_team.lower() + '.png'
images = Image.open(image)

captions = selected_team + ' logo'
st.image(image, caption=captions, width=200)

st.dataframe(new_data)

line_chart = new_data.copy()
seasons = sorted(line_chart.season.unique())
season_start = 2021 - len(seasons)
pts_sum = []
years = list((range(season_start, 2021)))
for ano in seasons:
    select = line_chart[line_chart["season"] == ano]
    pontos = select["pts"].sum()
    pts_sum.append(pontos)
st.title("Somatória de pontos por temporada")
grafico = px.line(line_chart, x=years, y=pts_sum)
st.write(grafico)