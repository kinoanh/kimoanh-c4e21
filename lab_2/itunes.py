from urllib.request import urlopen
from bs4 import BeautifulSoup
url="https://www.apple.com/itunes/charts/songs/"
conn=urlopen(url)
raw_data=conn.read() 
html_page=raw_data.decode("utf-8")
soup = BeautifulSoup(html_page,"html.parser")
div_list= soup.find_all("div","section-content" )
div=div_list[1]
ul_list=div.find_all("ul")
ul=ul_list[0]
li_list=ul.find_all("li")

new_list=[]
for li in li_list:
    a=li.h3.a
  
    b=li.h4.a
    artist=b=li.h4.a.string  
    name= li.h3.a.string
    news={
        "name": name,
        "artist": artist,
    }
    new_list.append(news)
    print(name)
    print(artist)
    print("*" *10)
import pyexcel
pyexcel.save_as(records=new_list,dest_file_name="itune.xlsx")        