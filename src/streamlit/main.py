import streamlit as st
import pandas as pd
from functions import *

st.set_page_config(page_title='CS:GO visu',
                   layout="wide")


st.sidebar.image('src/img/csgo-logo.png', width=250, output_format='png')


st.sidebar.header('Visualizações e Informações sobre CS:GO')
st.sidebar.markdown('Alguns dados e visualizações sobre os principais jogadores e times do cenário mundial de CS:GO.')


menu = st.sidebar.radio(
    "",
    ("Introdução", "Jogadores", "Times"),
)

st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.markdown('---')
st.sidebar.write('João Alcindo | Dezembro 2021 joaoalcindo27@gmail.com')


if menu == 'Introdução':
    set_home()
elif menu == 'Jogadores':
    set_players()
elif menu == 'Times':
    set_teams()


