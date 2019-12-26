#-*- coding: utf-8 -*-
from datetime import date
from pandas.io.html import read_html
from openpyxl import Workbook
import csv

page='https://www.nbp.pl/home.aspx?f=/kursy/kursya.html'
infobox=read_html(page, index_col=0,attrs={'class':'pad5'}, encoding="utf-8")

data=date.today()

file_save=('C:/Users/ja/Documents/Python/download data/tabela_kursow_walut_'+str(data)+'.csv')

infobox[0].to_csv(file_save,sep='\t' )
print(file_save)
wb=Workbook()
ws=wb.active
with open('C:/Users/ja/Documents/Python/download data/tabela_kursow_walut_'+str(data)+'.csv','r',encoding='utf-8') as f:
    for row in csv.reader(f):
        ws.append(row)
wb.save('tabela_kursow_walut'+str(data)+'.xlsx')
