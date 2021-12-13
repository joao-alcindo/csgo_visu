#import streamlit as st
import json
import pandas as pd
import pycountry
import plotly.express as px

teams_18 = ['Natus Vincere',
 'Vitality',
 'G2',
 'Gambit',
 'Heroic',
 'Virtus.pro',
 'NIP',
 'FaZe',
 'Astralis',
 'Entropiq',
 'FURIA',
 'Liquid',
 'ENCE',
 'Copenhagen Flames',
 'OG',
 'BIG',
 'MOUZ',
 'fnatic']

players_20 = ['FalleN',
 'ZywOo',
 's1mple',
 'device',
 'NiKo',
 'electronic',
 'blameF',
 'ropz',
 'EliGE',
 'dupreeh',
 'syrsoN',
 'Magisk',
 'stavn',
 'huNter-',
 'yuurih',
 'Brollan',
 'HEN1',
 'KRIMZ',
 'KSCERATO',
 'jks',
 'Brehze']

with open('./src/data/top20_players.json', 'r', encoding='utf-8') as player_file:
    data_players = json.load(player_file)

players = {}

for player in data_players:
    players[player['nick']] = player


with open('./src/data/top18_teams.json', 'r', encoding='utf-8') as team_file:
    data_teams = json.load(team_file)

teams = {}

for team in data_teams:
    teams[team['name']] = team







#-------------------------------------------------------------------------------------------------

#jogadores ao redor do mundo


player_dataset =  pd.read_csv('./src/data/player_stats.csv')

player_dataset_p = player_dataset.groupby('country', as_index= False).count()[['country','name']]
player_dataset_p = player_dataset_p.rename(columns = {'name': 'count'})

player_dataset_p['iso_alpha'] = player_dataset_p['country']

countries = {}

for country in pycountry.countries:
    countries[country.name] = country.alpha_3

#erros = ['Czech Republic', 'Korea', 'Macedonia', 'Russia', 'Taiwan', 'Vietnam']

erros = {'Czech Republic':'CZE', 'Korea':'KOR', 'Macedonia':'MKD', 'Russia':'RUS', 'Taiwan':'TWN', 'Vietnam':'VNM'}


def name_to_iso(x):
    try:
        iso = countries[x]
    except KeyError:
        iso = erros[x]
    return iso


player_dataset_p['iso_alpha'] = player_dataset_p['iso_alpha'].apply(name_to_iso)

#-------------------------------------------------------------------------------------------------

#times ao redor do mundo

team_dataset =  pd.read_csv('./src/data/team_stats.csv')


team_dataset_p = team_dataset.groupby('country', as_index= False).count()[['country','name']]
team_dataset_p = team_dataset_p.rename(columns = {'name': 'count'})

team_dataset_p['iso_alpha'] = team_dataset_p['country']

countries = {}

for country in pycountry.countries:
    countries[country.name] = country.alpha_3

erros = {'Asia':'NPL',
 'CIS':'RUS',
 'Czech Republic':'CZE',
 'Europe':'ITA',
 'Korea':'KOR',
 'North America': 'USA',   
 'Oceania':'AUS',
 'Russia':'RUS',
 'South America':'BRA'}

def name_to_iso(x):
    try:
        iso = countries[x]
    except KeyError:
        iso = erros[x]
    return iso

team_dataset_p['iso_alpha'] = team_dataset_p['iso_alpha'].apply(name_to_iso)

#-------------------------------------------------------------------------------------------------

#texto introducao

introducao_text = """
# Counter Strike : Global Offensive (CS:GO)

## O que é ?

Counter-Strike: Global Offensive, mais famoso como CS:GO, é um jogo competitivo de tiro em primeira pessoa (FPS).

CS:GO é o último lançamento da série Counter Strike, e tem atraído uma média de 11 milhões de jogadores por mês desde o seu lançamento em 2012.

## Dinâmica de jogo:

O jogo coloca dois times de cinco jogadores um contra o outro, com cada time tendo que completar certos objetivos para vencer.

Uma equipe assume o papel dos Terroristas (Ts), enquanto a outra equipe são os Contra-Terroristas (CTs).

Existem vários modos de jogo disponíveis, mas os jogos de e-sports profissionais são sempre jogados no modo Competitivo 5 x 5 (5 contra 5).

Neste modo, os Terroristas são os atacantes e devem plantar e detonar uma bomba em um dos locais específicos - Bombsite A ou B - ou eliminar os cinco CTs para ganhar a rodada.

Os CTs devem desativar a bomba se esta for plantada, ou eliminar tirar os cinco Ts para ganhar a rodada.

Cada partida é composta de 30 rodadas no total, com rodadas que duram no máximo um minuto e 55 segundos. A primeira equipa a ganhar 16 rodadas ganha o mapa.

O CS:GO também incorpora um sistema financeiro no jogo, que recompensa os jogadores por ganhar rodadas, matar inimigos e usar com sucesso determinadas armas.

Os jogadores podem então gastar seus dólares em novas armas e granadas entre as rodadas, aumentando suas chances de ganhar as rodadas posteriores.

#### Visão de um jogador durante a partida

![](https://s2.glbimg.com/FVu3q8Xw9UQ7AE_fkO-UPTAEjuM=/0x0:695x521/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_08fbf48bc0524877943fe86e43087e7a/internal_photos/bs/2018/A/n/ABqJuKTPGzVVI1UORUVA/passo-5.jpg)

## Maiores Eventos de CS:GO :

O jogo é tão popular que existem muitos times profissionais ao redor do mundo e torneios com premiações de até 1 milhão de dólares. Os maiores eventos de CS:GO são os Majors que acontecem duas vezes por ano. Semelhantes aos grandes eventos de esportes como golfe e o tênis, estes são os eventos de maior prestígio no calendário dos times e jogadores.

Em 2020 seria realizado o major na cidade do Rio de Janeiro, porém com a pandemia esse Major foi adiado. Como os casos de covid-19 na europa diminuiram, no mês de novembro foi realizado um Major em Estocolmo na Suécia, no qual a [Natus Vincere(NaVi)](https://www.hltv.org/team/4608/natus-vincere) se sagrou campeã pela primeira vez.

#### Natus Vincere erguendo o troféu de campeã

![Natus Vincere erguendo o troféu de campeã](https://cdn.ome.lt/85knpl5n_nwdClTSZ1w67S07KCA=/970x360/smart/uploads/conteudo/fotos/NaVi_campea_Major.png)

#### Avicii Arena durante os Play-offs do Major de 2021

![Avicii Arena durante os Play-offs do Major de 2021](https://img-cdn.hltv.org/gallerypicture/c7-8tdQxkOAHR6R_CCHGo0.jpg?ixlib=java-2.1.0&w=800&s=0f48bdc6f5bf56e126a3309f87dabdd3)

Outros torneios importantes também são a IEM Katowice, IEM Cologne, ESL Pro League organizados pela [ESL](https://www.eslgaming.com/) e  Blast Premier Spring Finals, Blast Premier Fall Finals e Blast Premier World Finals organizados pela [Blast Premier](https://blastpremier.com/).

Os brasileiros já ganharam dois majors, MLG Major Championship: Columbus 2016 e ESL One Cologne 2016 , com a seguinte Line-UP nos dois campeonatos Gabriel "FalleN" Toledo, Marcelo "coldzera" David, Lincoln "fnx" Lau, Fernando "fer" Alvarenga e Epitácio "TACO" de Melo. Atualmente a melhor equipe brasileira é a [FURIA](https://www.hltv.org/team/8297/furia). 

#### Equipe brasileira após a conquista do MLG Major Championship: Columbus 2016

![](https://img-cdn.hltv.org/gallerypicture/QOXJRSghsXmR0GLhqvpIjV.jpg?ixlib=java-2.1.0&w=500&s=f366acff0269fcd7c2264e9c54891242)

## Curiosidades:

* Existem skins no jogo, que mudam a aparência das armas e dos bonecos dos jogadores, o preço dessas skins variam de alguns centavos até alguns milhões de reais. A skin mais cara do jogo está avaliada em 6,2 milhões de reais, segundo essa [notícia do GE](https://ge.globo.com/esports/csgo/noticia/csgo-skin-mais-cara-do-mundo-e-avaliada-em-r-62-milhoes.ghtml).

* Além do modo competitivo existem outros modos, como mata-mata, corrida armada, mata pombo, entre outros.



"""

