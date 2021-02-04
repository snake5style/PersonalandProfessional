from django.shortcuts import render
import os
import sqlalchemy
from sqlalchemy import create_engine
import psycopg2
import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
from personal_portfolio.settings import DATABASES
from futbolallinone.models import bund, epl, liga, ligue, serie


User = DATABASES['default']['USER']
Password = DATABASES['default']['PASSWORD']
Host = DATABASES['default']['HOST']
Port = DATABASES['default']['PORT']
Database = DATABASES['default']['NAME']

engine = create_engine("postgresql://" + User + ":" + Password + "@" + Host + ":" + Port + "/" + Database)

page = [
      'https://www.skysports.com/premier-league-table',
      'https://www.skysports.com/la-liga-table',
      'https://www.skysports.com/bundesliga-table',
      'https://www.skysports.com/serie-a-table',
      'https://www.skysports.com/ligue-1-table'
]


league = [ "epl", "liga", "bund", "serie", "ligue", ]
columns = ['Rank', 'Team', 'Pl', 'W', 'D', 'L', 'F', 'A', 'GD', 'Pts', 'Last 6']

for pag, leag in zip(page, league):
   response = requests.get(pag)
   soup = BeautifulSoup(response.text, 'html.parser')
 
   last_df = pd.DataFrame(columns=columns)
   last_df

   contents = soup.find_all('tr', attrs={'class':re.compile('standing-table__row')})
   for content in contents:

      teams = [tea.get_text().strip('\n') for tea in content.find_all('td')]
      first_df = pd.DataFrame(teams, columns).T
      first_df.columns=columns

      last_df = pd.concat([last_df,first_df], ignore_index=True)
      last_df.to_sql('{0}'.format(leag), engine, if_exists='replace',index=False)   
  
bund_table = list(bund.objects.values_list())
epl_table = list(epl.objects.values_list())
liga_table = list(liga.objects.values_list())
ligue_table = list(ligue.objects.values_list())
serie_table = list(serie.objects.values_list())
context = {
    'bund_table': bund_table,
    'epl_table': epl_table,
    'liga_table': liga_table,
    'ligue_table': ligue_table,
    'serie_table': serie_table,
}

def futbol_index(requests):
   return render(requests, 'futbol.html', context) 
