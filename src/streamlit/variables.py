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

players_20 = ['ZywOo',
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



