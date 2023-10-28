from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(url)
soup = bs(page.text,"html.parser")
print(soup)
star_table = soup.find('table')
temp_list = []
star_table_row =soup.find_all('tr')
for tr in star_table_row:
    star_colum = tr.find_all('td')
    row = [i.text.rstrip() for i in star_colum]
    temp_list.append(row)
    print(row)
star_names = []
distance = []
mass = []
radius = []
for row in range(1,len(temp_list)):
    star_names.append(temp_list[row][1])
    distance.append(temp_list[row][3])
    mass.append(temp_list[row][5])
    radius.append(temp_list[row][6])
df = pd.DataFrame(list(zip(star_names,distance,mass,radius)),columns=['Star_name','Distance','Mass','Radius'])
print(df)
df.to_csv("star table.csv")