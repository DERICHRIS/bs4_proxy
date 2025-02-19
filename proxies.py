import pandas as pd
from bs4 import BeautifulSoup
import requests


url="http://ident.me/"
proxy=""
page=requests.get(url,proxies=proxy)
print(page.text)

