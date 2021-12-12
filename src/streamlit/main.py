import streamlit as st
import pandas as pd
from functions import *

st.set_page_config(page_title='CS:GO visu',
                   layout="centered")


st.sidebar.image('../img/csgo-logo.png', width=250)



st.sidebar.header('Visualizações e Informações sobre CS:GO')
st.sidebar.markdown('Alguns dados e visualizações sobre os principais jogadores e times do cenário mundial de CS:GO.')


menu = st.sidebar.radio(
    "",
    ("Introdução", "Jogadores", "Times"),
)



st.sidebar.markdown('---')
st.sidebar.write('João Alcindo | Dezembro 2021 joaoalcindo27@gmail.com')


if menu == 'Introdução':
    set_home()
elif menu == 'Jogadores':
    set_players()
elif menu == 'Times':
    set_teams()