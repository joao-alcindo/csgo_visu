#import streamlit as st
import json

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
    
print(teams)



