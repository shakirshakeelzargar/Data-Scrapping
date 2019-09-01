#Author: Shakir Shakeel
#This code will scrap product data fromFlipkart.com
#This code will only work if you search for mobiles
#Goto flipkart.com and search for mobiles. Copy the link and pass that as first argument to the function data_scrap.
#Pass the second argument as how many pages you want to scrap
#Enjoy


import bs4
from urllib.request import urlopen as ureq

import os
from bs4 import BeautifulSoup


def data_scrap(url,no_of_pages):
    if os.path.exists("d:/flipkartProductInfo.csv"):
        os.remove("d:/flipkartProductInfo.csv")
    #Opens the webpage 
    n=1
    fileSave="d:/flipkartProductInfo.csv"
    f=open(fileSave,"w",encoding="utf-8")
    header="Product Name,Product Rating,Product Description,New Price, Old Price, Discount, Total Ratings, Total Reviews\n"
    f.write(header)
    while n<=no_of_pages:
        page="&page="+str(n)
        urlToScrap=url+page
        print("scrapping page "+str(n))
        web=ureq(urlToScrap)
        scrappedPage=web.read()
        # web.close()
        #parse the html page
        page_soup=BeautifulSoup(scrappedPage,"lxml")


        containers=page_soup.findAll("div",{"class":"_1UoZlX"})



        # fileSave="d:/flipkartProductInfo.csv"
        # f=open(fileSave,"w",encoding="utf-8")
        # header="Product Name,Product Rating,Product Description,New Price, Old Price, Discount, Total Ratings, Total Reviews\n"
        # f.write(header)
        # print(container)
        for container in containers:
            newProductName="None"
            div1=container.find("div","col col-7-12")
            div2=div1.find("div","_3wU53n")
            productName=div2.text
            newProductName=productName.replace(",","-")


            productRating="None"
            div1=container.find("div","col col-7-12")
            if div1 is not None:
                div2=div1.find("div","niH0FQ")
            else:
                div2=None
            if div2 is not None:
                div3=div2.find("div","hGSR34")
            else:
                div3=None
            if div3 is not None:
                productRating=div3.text
            # print(productRating)


            div1=container.find("div","col col-7-12")
            div2=div1.find("div","_3ULzGw")
            div3=div2.find("ul","vFw0gD")
            div4=div3.findAll("li","tVe95H")
            d=""
            for all in div4:
                text=all.text
                d=d+text+"--"
            productDescription1=d
            productDescription=productDescription1.replace(",","--")
            # print(productDescription)

            newPrice="None"
            div1=container.find("div","col col-5-12 _2o7WAb")
            if div1 is not None:
                div2=div1.find("div","_6BWGkk")
            else:
                div2=None
            if div2 is not None:
                div3=div2.find("div","_1uv9Cb")
            else:
                div3=None
            if div1 is not None:
                div4=div3.find("div","_1vC4OE _2rQ-NK")
                newPrice1=div4.text
                newPrice2=newPrice1[1:]
                newPrice=newPrice2.replace(",","")
            # print(newPrice)

            oldPrice="None"
            div1=container.find("div","col col-5-12 _2o7WAb")
            if div1 is not None:
                div2=div1.find("div","_6BWGkk")
            else:
                div2=None
            if div2 is not None:
                div3=div2.find("div","_1uv9Cb")
            else:
                div3=None
            if div3 is not None:
                div4=div3.find("div","_3auQ3N _2GcJzG")
            else:
                div4=None
            if div4 is not None:
                oldPrice1=div4.text
                oldPrice2=oldPrice1[1:]
                oldPrice=oldPrice2.replace(",","")
            # print(oldPrice)

            productDiscount="None"
            div1=container.find("div","col col-5-12 _2o7WAb")
            if div1 is not None:
                div2=div1.find("div","_6BWGkk")
            else:
                div2=None
            if div2 is not None:
                div3=div2.find("div","_1uv9Cb")
            else:
                div3=None
            if div3 is not None:
                div4=div3.find("div","VGWI6T")
            else:
                div4=None
            if div4 is not None:
                productDiscount=div4.span.text
            # print(productDiscount)

            productRatings="None"
            div1=container.find("div","col col-7-12")
            if div1 is not None:
                div2=div1.find("div","niH0FQ")
            else:
                div2=None
            if div2 is not None:
                div3=div2.find("span","_38sUEc")
            else:
                div3=None
            if div3 is not None:
                div4=div3.findAll("span")[1]
                productRatings1=div4.text
                productRatings2=productRatings1.replace(" Ratings","")
                productRatings3=productRatings2.replace(",","")
                productRatings=productRatings3.strip()
            # print(productRatings)

            productReviews="None"
            div1=container.find("div","col col-7-12")
            if div1 is not None:
                div2=div1.find("div","niH0FQ")
            else:
                div2=None
            if div2 is not None:
                div3=div2.find("span","_38sUEc")
            else:
                div3=None
            if div3 is not None:
                div4=div3.findAll("span")[3]
                productReviews1=div4.text
                productReviews2=productReviews1.replace(" Reviews","")
                productReviews3=productReviews2.replace(",","")
                productReviews=productReviews3.strip()
            # print(productReviews)

            f.write(newProductName +"," + productRating + "," + productDescription + "," + newPrice + "," + oldPrice + "," + productDiscount + "," + productRatings + "," + productReviews + "\n")
        
        print("scrappinr page "+str(n)+" done")
        
        n=n+1
    f.close()
    print("Check your file here : "+fileSave)

data_scrap('http://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off',10)

