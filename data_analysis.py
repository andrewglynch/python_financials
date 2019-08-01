# set up initial libraries

import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
from date_parameters import oldest_year
from date_parameters import current_year

# set data URLs

f = open('data_series_names.csv')
csv_f = csv.reader(f)

data_series_id_list = []

for item in csv_f:
  data_series_id_list.append(item)

for data_series_id in data_series_id_list:
    print(data_series_id)
    '''
    data_url = 'https://www.bankofengland.co.uk/boeapps/database/fromshowcolumns.asp?Travel=NIxAZxSUx&FromSeries=1&ToSeries=50&DAT=RNG&FD=1&FM=Jan&FY=' + str(oldest_year) + '&TD=11&TM=May&TY=' + str(current_year) '&FNY=Y&CSVF=TT&html.x=66&html.y=26&SeriesCodes=' + data_series_id + '&UsingCodes=Y&Filter=N&title=' + data_series_id + '&VPD=Y'
    page = urllib.request.urlopen(data_url)
    soup = BeautifulSoup(page)
    stats_table = soup.find('table', id="stats-table")
    print(stats_table)
    '''
