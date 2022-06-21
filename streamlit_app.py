import streamlit as st
import pandas as pd
import numpy as np

st.title('NBA Statistics')

df = pd.read_csv("all_seasons.csv")
df = df.drop('Unnamed: 0', axis=1)
df["draft_year"] = pd.to_numeric(df["draft_year"], errors="coerce")
df["draft_round"] = pd.to_numeric(df["draft_round"], errors="coerce")
df["draft_number"] = pd.to_numeric(df["draft_number"], errors="coerce")

# filter

st.sidebar.header('Escolha o que você quer filtrar')
seasons = sorted(df.season.unique())
selected_year = st.sidebar.selectbox('Temporada', reversed(seasons))

teams = sorted(df.team_abbreviation.unique())
selected_team = st.sidebar.multiselect('Times', teams, teams)

country = sorted(df.country.unique())
selected_country = st.sidebar.multiselect('País', country, country)

@st.cache
def select_data(year_season):
    select = df[df["season"] == year_season]
    return select
new_data = select_data(selected_year)

df_selected = new_data[(new_data.team_abbreviation.isin(selected_team)) & (new_data.country.isin(selected_country))]

st.write(f"Banco de dados: {df_selected.shape[0]} linhas X {df_selected.shape[1]} colunas")

st.dataframe(df_selected)