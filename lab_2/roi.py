from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict

url = 'http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn'
conn = urlopen(url)
raw_data = conn.read()
html_page = raw_data.decode('utf-8')
soup = BeautifulSoup(html_page, 'html.parser')
h_list = soup.find_all('td','h_t')
h_data_list = []
table = soup.find(id='tableContent')
row = table.find_all('tr')
row_list = []
for item in h_list:   
    h_data_list.append(item)


for item in row:
    r_list = item.find_all('td','b_r_c')
    r_data_list = []
    for j in r_list:
        j = j.string     
        r_data_list.append(j)  
 

final= []
for item in row_list:
    val__list = []
    val = {
            "Danh Muc" : item[0]
        }  
    for i in range(len(h_data_list)):
        val[h_data_list[i]] =  item[1+i]   
              
    final.append(val)



pyexcel.save_as(records=final,dest_file_name="vinamlk.xlsx")