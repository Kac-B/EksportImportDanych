#-*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from pandas import Series, DataFrame
import requests
import lxml.html as lh
import html5lib
import bs4
from datetime import date
import time
from pandas.io.html import read_html

page='https://www.nbp.pl/home.aspx?f=/kursy/kursya.html'
infobox=read_html(page, index_col=0,attrs={'class':'pad5'})

data=date.today()

file_save=('C:/Users/ja/Documents/Python/download data/tabela_kursow_walut_'+str(data)+'.csv')

infobox[0].to_csv(file_save,sep='\t' )
print(file_save)
