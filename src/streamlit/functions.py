
import streamlit as st
from variables import *

def top_players(nick):
    data = players[nick]

    cl1, cl2,cl3 =  st.columns(3)

    with cl1:
        st.image(data['img'], width=280, output_format='png')

    information = f"""
    #### Informações

    **Nick**:  [{data['nick']}]({data['profile']})

    **Nome**:  {data['name']}

    **Idade**:  {data['age']}

    **País**:  {data['country']}

    **Time Atual**:  {data['team']}

    **Ranking**:  {data['ranking']}
    """


    with cl2:
        st.markdown(information)

    stats =  f"""
    #### Estatísticas (sep 2021)

    **Mapas jogados**:  {data['total_maps']}

    **Rodadas jogadas**:  {data['total_rounds']}

    **KD difference**:  {data['kd_diff']}

    **KD Ratio**:  {data['kd']}

    **Rating**:  {data['rating']}
    """

    with cl3:
        st.markdown(stats)

def top_teams(name):


    data = teams[name]

    cl1, cl2,cl3 =  st.columns(3)

    with cl1:
        st.image(data['img'], width=230, output_format='png')

    information = f"""
    #### Informações

    **Nome**:  [{data['name']}]({data['profile']})

    **País**:  {data['country']}

    **Ranking**:  {data['ranking']}

    **Média de idade**:  {data['ava']}

    **Semanas no top 30**:  {data['wt30']}

    **Coach**:  {data['Coach']}

    **Line-UP**:  {data['lineup']}




    """


    with cl2:
        st.markdown(information)

    stats =  f"""
    #### Estatísticas (sep 2021)

    **Mapas jogados**:  {data['total_maps']}

    **KD difference**:  {data['kd_diff']}

    **KD Ratio**:  {data['kd']}

    **Rating**:  {data['rating']}
    """

    with cl3:
        st.markdown(stats)






def set_home():
    st.write("home")

def set_players():
    st.write('Jogadores')
    nick = st.selectbox('selecione',players_20)
    top_players(nick)


    

def set_teams():
    st.write('Times')
    nome = st.selectbox('selecione',teams_18)
    top_teams(nome)