import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
req = requests.get("https://www.hkifa.org.hk/eng/affiliate-members.aspx")
soup = BeautifulSoup(req.content,"html.parser")
#soup = BeautifulSoup(req.content, "lxml")
#res=soup.a
#print(soup.prettify)
print(soup.get_text(""))
