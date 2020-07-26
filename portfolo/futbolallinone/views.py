from django.shortcuts import render
import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
from prettytable import PrettyTable
from prettytable import from_csv

# Create your views here.
page = [
      'https://www.skysports.com/premier-league-table',
      'https://www.skysports.com/la-liga-table',
      'https://www.skysports.com/bundesliga-table',
      'https://www.skysports.com/serie-a-table',
      'https://www.skysports.com/ligue-1-table'
]


league = [ "EPL", "LIGA", "BUND", "SERIE", "LIGUE", ]

for pag, leag in zip(page, league):
   response = requests.get(pag)
   soup = BeautifulSoup(response.text, 'html.parser')

   top_col = soup.find('tr', attrs={'class': 'standing-table__row'})
   columns = [col.get_text() for col in top_col.find_all('th')]

   last_df = pd.DataFrame(columns=columns)
   last_df

   contents = soup.find_all('tr', attrs={'class':re.compile('standing-table__row')})
   for content in contents:

      teams = [tea.get_text().strip('\n') for tea in content.find_all('td')]
      first_df = pd.DataFrame(teams, columns).T
      first_df.columns=columns

      last_df = pd.concat([last_df,first_df], ignore_index=True)

      last_df.to_csv('{0}.csv'.format(leag), index = False, sep=',', encoding='utf-8')


file_path = [ "EPL.csv", "LIGA.csv", "BUND.csv", "SERIE.csv", "LIGUE.csv", ]
final = []

# EPL
csv_file = open(file_path[0])
final1 = from_csv(csv_file)

#Liga
csv_file1 = open(file_path[1])
final2 = from_csv(csv_file1)

#Bund
csv_file2 = open(file_path[2])
final3 = from_csv(csv_file2)

#Serie
csv_file3 = open(file_path[3])
final4 = from_csv(csv_file3)

#Ligue
csv_file4 = open(file_path[4])
final5 = from_csv(csv_file4)

final.append(final1)
final.append(final2)
final.append(final3)
final.append(final4)
final.append(final5)

standings = {
   'final': final
}

def futbol_index(requests):
   return render(requests, 'futbol.html', standings)


