import streamlit as st
import pandas as pd
import numpy as np

season_year = []

st.title('NBA Statistics')

df = pd.read_csv("all_seasons.csv")
df = df.drop('Unnamed: 0', axis=1)
df = df.dropna(how="any", axis=0) #linhas com valores vazios
df["draft_year"] = pd.to_numeric(df["draft_year"], errors="coerce")
df["draft_round"] = pd.to_numeric(df["draft_round"], errors="coerce")
df["draft_number"] = pd.to_numeric(df["draft_number"], errors="coerce")

# filter

st.sidebar.header('Escolha o que você quer filtrar')
seasons = sorted(df.season.unique())
selected_year = st.sidebar.selectbox('Temporada', reversed(seasons))

teams = sorted(df.team_abbreviation.unique())
selected_team = st.sidebar.multiselect('Team', teams, teams)

@st.cache
def select_data(year_season):
    select = df[df["season"] == year_season]
    return select
new_data = select_data(selected_year)

df_selected = new_data[(new_data.team_abbreviation.isin(selected_team))]

st.dataframe(df_selected)