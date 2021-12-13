# Visualisações sobre CS:GO

## Trabalho Final de Visualização da Informação 

## Briefing 

Desenvolver visualizações sobre o cenário competitivo do jogo [Counter Strike:Global Offensive](https://pt.wikipedia.org/wiki/Counter-Strike:_Global_Offensive).

**Motivação:** Durante a pandemia comecei a jogar CS:GO e acompanhar o cenário competitivo e fazer amigos através dele, então como me apaixonei pelo jogo e suas estatísticas.

**Inspiração de vis:** https://share.streamlit.io/casiopa/eda-imdb/main/src/utils/streamlit/EDA_IMDb_main.py

## Ferramentas Utilizadas:

**Tratamento e Limpeza de dados:** pycounty e pandas.

**Visualizações:** [plotly](https://plotly.com/).

**Implementação:** [Streamlit](https://streamlit.io/).


## Dados 

Os dados que eu usei durante o trabalho foram coletados das seguintes fontes:

* [HLTV](https://www.hltv.org/)
* [CSGO : Player and Team stats](https://www.kaggle.com/patrasaurabh/csgo-player-and-team-stats)

## Desenvolvimento 

A primeira parte do trabalho foi encontrar dados interessantes e relevantes para realização do trabalho, os dados usados no trabalho estão na pasta [`./src/data`](./src/data), os arquivos [`./src/data/top18_teams_dec_2021.json_`](./src/data/top18_teams_dec_2021.json) e [`./src/data/top20_players_2020.json`](./src/data/top20_players_2020.json) foram ambos feitos em processo manual, todos os dados deles foram retirados do site [HLTV](https://www.hltv.org/).Após a coleta dos dados, alguns dados dos arquivos foram anexados nos arquivos json, esse processo foi feito em [`./src/preprocessing/add_data_jsons.ipynb`](./src/preprocessing/add_data_jsons.ipynb) e novos arquivos jsons foram criados, [`./src/data/top20_players.json`](./src/data/top20_players.json) e [`./src/data/top18_teams.json`](./src/data/top18_teams.json).

Depois de dados coletados e previamente organizados, fui em busca de ideias e inpirações pras visualizações, então encontrei o seguinte dashboard [link](https://share.streamlit.io/casiopa/eda-imdb/main/src/utils/streamlit/EDA_IMDb_main.py), gostei bastante do que foi proposto nele, então busquei fazer algo semelhante. Com os dados obtidos decidi dividir o meu projeto final em três páginas (Introdução, Jogadores e Times), como pode-se ver na imagem abaixo:

![](.img/menu.png)

A partir disso fiz uma introdução explicando um pouco sobre o jogo, o que é, dinâmica de jogo, principais eventos e algumas curiosidades. 

Com a introdução já feita, parti para a parte das visualizações, as visualizações das duas páginas são muito semelhantes, o processo de plotagem pode ser encontrado nos arquivos
[`./src/preprocessing/analise_players.ipynb `](./src/preprocessing/analise_players.ipynb) e [`./src/preprocessing/analise_teams.ipynb `](./src/preprocessing/analise_teams.ipynb).







Resultado final em https://share.streamlit.io/joao-alcindo/csgo_visu/main/src/streamlit/main.py
