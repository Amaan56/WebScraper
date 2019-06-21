from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pandas

my_url = 'http://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'

uClient = uReq(my_url)

page_html = uClient.read()

uClient.close()

page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div", {"class": "item-container"})

l = []

for container in containers:
    d = {}
    try:
        d["Brand"] = container.find(
            "div", {"class": "item-branding"}).a.img["title"]
        title_container = container.findAll("a", {"class": "item-title"})
        d["ProductName"] = title_container[0].text
        shipping_container = container.findAll("li", {"class": "price-ship"})
        d["ShippingStatus"] = shipping_container[0].text.strip()
    except:
        pass
    l.append(d)

df = pandas.DataFrame(l)

df.to_csv("Output.csv")
