import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

def get_html(url):
    _html = ""
    resp = requests.get(url)
    if resp.status_code == 200:
        _html = resp.text
    return _html

#https://search.shopping.naver.com/search/all.nhn?query=gtx%201080%20%22gtx%201080%22%20-ti&frm=NVSHSRC

URL = "https://search.shopping.naver.com/search/all.nhn?query="
     # "gtx%201070" \
     # "%20%22gtx%201070" \
    #  "%22%20-ti" \
     # "&frm=NVSHSRC"
company = str(input("company?"))
model = str(input("model?"))
match = str(input("match?"))
noSearch = str(input("not search?"))

fullURL = URL + company +"%20"+model+"%22%20-"+noSearch+"&frm=NVSHSRC"

html = get_html(fullURL)
soup = BeautifulSoup(html, 'html.parser')

#find("div",{"class": "product_list_area"}).
#print(soup) / #_search_list > div.search_list.basis > ul > li > div.info > a
#_search_list > div.search_list.basis > ul > li > div.info > span.price > em > span.num._price_reload
# #_search_list > div.search_list.basis > ul > li > div.info > span.price > em > span
#_search_list > div.search_list.basis > ul > li > div.info > span.price > em > span
name = "#" + "_search_list > div.search_list.basis > ul > li > div.info > a"
price = "#" + "_search_list > div.search_list.basis > ul > li > div.info > span.price > em > span.num"


pN = soup.select(name)
pP = soup.select(price)

for i in range(len(pP)):
    print(pN[i].text , pP[i].text + "won")