import requests
from bs4 import BeautifulSoup 
from openpyxl import Workbook

wb = Workbook() 
ws = wb.create_sheet('TV Ratings')
ws.append(['', ' ', '', '39'])


for tr_tag in range(0,3):
 
  row = [
    1
  ]
  ws.append(row)
  
wb.save('X33_2010419177.xlsx')
