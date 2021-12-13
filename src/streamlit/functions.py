
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
    #### Estatísticas

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


@st.cache
def around_world(dataset):
    fig = px.scatter_geo(dataset, 
                            locations="iso_alpha",
                            size="count",
                            hover_name = 'country',
                            projection="equirectangular",
                            template='plotly_dark')

    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0},
                 plot_bgcolor='rgba(0,0,0,0)',
                 paper_bgcolor='rgba(0,0,0,0)')

    fig.update_traces(marker = dict(color = '#FFA500',
                                    line_width=0,
                                    sizeref=.1,
                                    sizemin=5),
                         mode = 'markers+text',
                        textfont = dict(size=10))
    
    return fig

@st.cache
def box_plox(dataset,country, data):
    fig = px.box(dataset[dataset['country'] == country], 
                                x="country",
                                y= data,
                                hover_name='name', 
                                points="all", 
                                template = 'plotly_dark')

    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    fig.update_traces(marker = dict(color = '#FFA500',
                                    line_width=0))
    
    return fig

@st.cache
def histogram(dataset,country, data):
    fig = px.histogram(dataset[dataset['country'] == country], x=data,template = 'plotly_dark')
    fig.update_traces(marker = dict(color = '#FFA500',line_width=0))
    fig.update_layout(bargap=0.1)
    
    return fig










def set_home():
    st.markdown(introducao_text)

def set_players():
    st.header('Jogadores')
    nick = st.selectbox('',players_20)
    top_players(nick)
    st.write(around_world(player_dataset_p))
    country = st.selectbox('',options = player_dataset_p['country'].iloc[:], index = 8)
    data = st.radio("",['total_maps','total_rounds','kd','kd_diff','rating'], index = 4)
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    st.write(box_plox(player_dataset,country, data))
    st.write(histogram(player_dataset,country, data))


    

def set_teams():
    st.header('Times')
    nome = st.selectbox('',teams_18, index = 10)
    top_teams(nome)
    st.write(around_world(team_dataset_p))
    country = st.selectbox('',options = team_dataset_p['country'],index = 6)



    data = st.radio("",['total_maps','kd','kd_diff','rating'], index = 3)
    st.write(box_plox(team_dataset,country, data))
    st.write(histogram(team_dataset,country, data))

