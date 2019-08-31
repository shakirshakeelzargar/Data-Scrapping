#Author: Shakir Shakeel
#This code will scrap product data from newegg.com
#goto newegg.com and search for something and pass the search url to the function "data_scrap"


import bs4
from urllib.request import urlopen as ureq

import os



def data_scrap(url,no_of_pages):
    if os.path.exists("d:/flipkartProductInfo.csv"):
        os.remove("d:/flipkartProductInfo.csv")
    #Opens the webpage 
    n=1
    fileSave="d:/flipkartProductInfo.csv"
    f=open(fileSave,"w",encoding="utf-8")
    header="Product Name,Product Rating,Product Description,New Price, Old Price, Discount, Total Ratings, Total Reviews\n"
    f.write(header)
    from bs4 import BeautifulSoup
    while n<=no_of_pages:
        page="&page="+str(n)
        urlToScrap=url+page
        from bs4 import BeautifulSoup
        print("scrapping page "+str(n))
        web=ureq(urlToScrap)
        scrappedPage=web.read()
        web.close()
        #parse the html page
        page_soup=BeautifulSoup(scrappedPage,"html.parser")


        containers=page_soup.findAll("div",{"class":"_1UoZlX"})



        # fileSave="d:/flipkartProductInfo.csv"
        # f=open(fileSave,"w",encoding="utf-8")
        # header="Product Name,Product Rating,Product Description,New Price, Old Price, Discount, Total Ratings, Total Reviews\n"
        # f.write(header)
        # print(container)
        for container in containers:
            div1=container.find("div","col col-7-12")
            div2=div1.find("div","_3wU53n")
            productName=div2.text
            newProductName=productName.replace(",","-")


            div1=container.find("div","col col-7-12")
            div2=div1.find("div","niH0FQ")
            div3=div2.find("div","hGSR34")
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


            div1=container.find("div","col col-5-12 _2o7WAb")
            div2=div1.find("div","_6BWGkk")
            div3=div2.find("div","_1uv9Cb")
            div4=div3.find("div","_1vC4OE _2rQ-NK")
            newPrice1=div4.text
            newPrice2=newPrice1[1:]
            newPrice=newPrice2.replace(",","")
            # print(newPrice)


            div1=container.find("div","col col-5-12 _2o7WAb")
            div2=div1.find("div","_6BWGkk")
            div3=div2.find("div","_1uv9Cb")
            div4=div3.find("div","_3auQ3N _2GcJzG")
            oldPrice1=div4.text
            oldPrice2=oldPrice1[1:]
            oldPrice=oldPrice2.replace(",","")
            # print(oldPrice)


            div1=container.find("div","col col-5-12 _2o7WAb")
            div2=div1.find("div","_6BWGkk")
            div3=div2.find("div","_1uv9Cb")
            div4=div3.find("div","VGWI6T")
            productDiscount=div4.span.text
            # print(productDiscount)


            div1=container.find("div","col col-7-12")
            div2=div1.find("div","niH0FQ")
            div3=div2.find("span","_38sUEc")
            div4=div3.findAll("span")[1]
            productRatings1=div4.text
            productRatings2=productRatings1.replace(" Ratings","")
            productRatings3=productRatings2.replace(",","")
            productRatings=productRatings3.strip()
            # print(productRatings)


            div1=container.find("div","col col-7-12")
            div2=div1.find("div","niH0FQ")
            div3=div2.find("span","_38sUEc")
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


