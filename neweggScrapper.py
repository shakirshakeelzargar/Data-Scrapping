#Author: Shakir Shakeel
#This code will scrap product data from newegg.com
#goto newegg.com and search for something and pass the search url to the function "data_scrap"


import bs4
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup


def data_scrap(url):
    try:
        print("Datascrapping started")
        #Opens the webpage 
        urlToScrap=url
        web=ureq(urlToScrap)
        scrappedPage=web.read()
        web.close()
        #parse the html page
        page_soup=soup(scrappedPage,"html.parser")
        # print(page_soup.p)
        #find the class containing items 
        #and save that class to a variable
        containers=page_soup.findAll("div",{"class":"item-container"})
        # print(type(containers))
        # print(containers[0])
        # oneContainer=containers[0]
        # divtag=oneContainer.find("div","item-info")
        # x=divtag.div.a.img["title"]
        # print(x)

        fileSave="d:/productInfo.csv"
        f=open(fileSave,"w")
        header="Brand,Product Name,Price,Shipping\n"
        f.write(header)
        for container in containers:
            # print("#############################################")
            #####################
            #getting brand name
            divtag=container.find("div","item-info")
            brand=divtag.div.a.img["title"]
            # print(brand)
            ######################
            #getting product name
            nametag=divtag.find("a","item-title")
            name=nametag.text
            name2=name.replace(",","|")
            # print(name2)
            ######################
            #getting price
            divtag2=container.find("div","item-action")
            p=divtag2.find("ul","price has-label-membership")
            p2=p.find("li","price-current")
            d=(p2.strong.text)
            c=(p2.sup.text)
            price=d+c
            # print(price)
            #######################
            #getting shipping
            divtag2=container.find("div","item-action")
            p=divtag2.find("ul","price has-label-membership")
            p2=p.find("li","price-ship")
            ship=p2.text
            ship2=ship.strip("\t")
            ship3=ship2.strip("\n")
            ship4=ship3.strip()
            # print(ship4)
            # print("#############################################")


            f.write(brand+","+name2+","+price+","+ship4+"\n")
        f.close()
    except Exception as ex:
        print("Faced some error")
        print("The error is : " +str(ex))
    else:
        print("Data scrapping Successfully done")
        print("Check your file here : "+fileSave)


data_scrap('https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card')


