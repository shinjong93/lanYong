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
company =[]
while(True):
    tmp = str(input("company? enter to save : "))
    tmp = tmp + str(input("model? ctcl+D to save :"))
    if tmp == "":
        break
    URL = URL + tmp + "%20"

while(True):
    tmp = str(input("match? enter to save : "))
    if tmp == "":
        break
    URL = URL + "%22" + tmp + "%22%20"

while(True):
    tmp = str(input("not search? enter to save : "))
    if tmp == "":
        break
    URL = URL + "-" +tmp + "%20"

fullURL = URL+"&frm=NVSHSRC"

html = get_html(fullURL)
soup = BeautifulSoup(html, 'html.parser')
name = "#" + "_search_list > div.search_list.basis > ul > li > div.info > a"
price = "#" + "_search_list > div.search_list.basis > ul > li > div.info > span.price > em > span.num"


pN = soup.select(name)
pP = soup.select(price)

product = [[0 for cols in range(2)] for rows in range(len(pP))]



for i in range(len(pP)):
    product[i][0] = pN[i].text.strip()
    product[i][1] = int(pP[i].text.replace(",",""))
    print(product[i][0] , product[i][1])
