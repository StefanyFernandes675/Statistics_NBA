import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title('NBA Statistics')

df = pd.read_csv("all_seasons.csv")
df = df.drop('Unnamed: 0', axis=1)

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
players = df_selected["player_name"].unique()

st.write(f"Banco de dados: {df_selected.shape[0]} linhas X {df_selected.shape[1]} colunas")
st.subheader(f"{len(players)} jogadores na temporada {selected_year}")

st.dataframe(df_selected)

st.title("Análise geral por temporada")
st.header("Faculdade vs Sem faculdade")

data_not_college = new_data[new_data['college'] == 'None'].count().college
data_college = new_data[new_data['college'] != 'None'].count().college
total = data_not_college + data_college
pct_not_college = round(100 * (data_not_college/total), 2)
pct_college = round(100 * (data_college/total), 2)
data_college_graphic = [pct_not_college, pct_college]
label = ["Sem faculdade", "Faculdade"]
grafico = px.pie(data_college_graphic, values=data_college_graphic, names=label)
st.write(grafico)

st.header("USA vs Outros países")

data_usa = new_data[new_data['country'] == 'USA'].count().country
data_no_usa = new_data[new_data['country'] != 'USA'].count().country
total = data_usa + data_no_usa
pct_no_usa = round(100 * (data_no_usa/total), 2)
pct_usa = round(100 * (data_usa/total), 2)
data_usa_graphic = [pct_no_usa, pct_usa]
label_usa = ["Outros países", "USA"]
grafico_usa = px.pie(data_usa_graphic, values=data_usa_graphic, names=label_usa)
st.write(grafico_usa)

st.header("Drafted vs Undrafted")

data_drafted = new_data[new_data['draft_year'] != 'Undrafted'].count().draft_year
data_undrafted = new_data[new_data['draft_year'] == 'Undrafted'].count().draft_year
total = data_drafted + data_undrafted
pct_undrafted = round(100 * (data_undrafted/total), 2)
pct_drafted = round(100 * (data_drafted/total), 2)
data_drafted_graphic = [pct_undrafted, pct_drafted]
label_drafted = ["Undrafted", "Drafted"]
grafico_draft = px.pie(data_drafted_graphic, values=data_drafted_graphic, names=label_drafted)
st.write(grafico_draft)

st.header("Drafted USA vs Undrafted USA")
st.header("Drafted outros países vs Undrafted outros países")
