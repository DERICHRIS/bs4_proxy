import pandas as pd
from bs4 import BeautifulSoup
import requests

current_page=1
proceed=True

# print(page) ---> gives 200 status (means ok) , 400 means error

# print(page.text) ---> gives entire page html code

# print(soup.title.text) --> will give the title of the page 

# print(soup.text) ----. gives only the string which is written in html tags
data=[]
while proceed==True:
    url="https://books.toscrape.com/catalogue/page-"+str(current_page)+".html"
    page=requests.get(url)   # to request and fetch the data
    soup=BeautifulSoup(page.text,"html.parser")  # beautiful soup scraps the data which we want from the page and parser is the feature extraction
    if soup.title.text=='404 Not Found':
        proceed=False
    else:
        all_books=soup.find_all("li",class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
        for book in all_books:
            item={}
            item['Title']=book.find('img').attrs['alt']
            item['Link']=book.find('a').attrs['href']
            item['Price']=book.find('p',class_='price_color').text[2:]
            item['Stock']=book.find('p',class_='instock availability').text.strip()  # strip() actually eliminates the space in between 
            print(f"the price is {item['Price']} and {item['Stock']}")
            data.append(item)



    current_page+=10

df=pd.DataFrame(data)
df.to_csv('book1.csv')
df.to_excel('book1.xlsx')



        
    

    
    



