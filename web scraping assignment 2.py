#!/usr/bin/env python
# coding: utf-8

# Q6 : Scrape data of first 100 sunglasses listings on flipkart.com. 

# In[1]:


import pandas as pd
from bs4 import BeautifulSoup
import requests


# In[2]:


url = "https://www.flipkart.com/search?q=sunglasses&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
page = requests.get(url)
page


# In[29]:


soup = BeautifulSoup(page.content)
soup


# In[30]:


Brand = []
Discription = []
Price = []
Discount = []


# In[31]:


for i in soup.find_all("div",class_="_2WkVRV"):
    Brand.append(i.text)


# In[25]:


Brand


# In[38]:


for i in soup.find_all("div",class_="_30jeq3"):
    Price.append(i.text) 


# In[40]:


Price


# In[41]:


for i in soup.find_all("div",class_="_3Ay6Sb"):
    Discount.append(i.text) 


# In[42]:


Discount


# In[43]:


len(Discount)


# In[61]:


for i in soup.find_all("a",class_="IRpwTa"):
    Discription.append(i.text)


# In[62]:


Discription


# In[63]:


sunglass=pd.DataFrame({})
sunglass ['Brand']=Brand[:10]
sunglass ['Discription']=Discription[:10]
sunglass ['Price']=Price[:10]
sunglass ['Discount']=Discount[:10]
sunglass


# Q7: Scrape 100 reviews data from flipkart.com for iphone11 phone

# In[64]:


import pandas as pd
from bs4 import BeautifulSoup
import requests


# In[65]:


url = "https://www.flipkart.com/apple-iphone-11-black-64-gb-includes-earpods-power-adapter/p/itm0f37c2240b217?pid=MOBFKCTSVZAXUHGR&lid=LSTMOBFKCTSVZAXUHGREPBFGI&marketplace"
page = requests.get(url)
page


# In[66]:


soup = BeautifulSoup(page.content)
soup


# In[67]:


Rating = []
Review_summary = []
Full_review = []


# In[69]:


for i in soup.find_all("div",class_="_3LWZlK _1BLPMq"):
    Rating.append(i.text)
   


# In[70]:


Rating


# In[71]:


for i in soup.find_all("p",class_="_2-N8zT"):
    Review_summary.append(i.text)
    


# In[72]:


Review_summary


# In[73]:


for i in soup.find_all("div",class_="t-ZTKy"):
    Full_review.append(i.text)


# In[74]:


Full_review


# In[75]:


apple_iphone=pd.DataFrame({})
apple_iphone ['Rating']=Rating[:10]
apple_iphone ['Review_summary']=Review_summary[:10]
apple_iphone ['Full_review']=Full_review[:10]
apple_iphone


# Q8: Scrape data for first 100 sneakers you find when you visit flipkart.com and 
# search for “sneakers” in the search field

# In[76]:


# Importing Libraries
import pandas as pd
from bs4 import BeautifulSoup
import requests


# In[77]:


url = "https://www.flipkart.com/search?q=sneakers&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
page = requests.get(url)


# In[78]:


page


# In[79]:


soup = BeautifulSoup(page.content)
soup


# In[80]:


product_discription = []  #empty list
price = []    #empty list
Brand = []   #empty list
discount = []   #empty list


# In[81]:


for i in soup.find_all("div",class_="_2B099V"):
    product_discription.append(i.text)


# In[82]:


product_discription


# In[83]:


for i in soup.find_all("div",class_="_30jeq3"):
    price.append(i.text)


# In[84]:


price


# In[85]:


for i in soup.find_all("div",class_="_3879cV"):
    Brand.append(i.text)


# In[86]:


Brand


# In[87]:


for i in soup.find_all("div",class_="_3Ay6Sb"):
    discount.append(i.text)


# In[88]:


discount


# In[90]:


product=pd.DataFrame({})
product['product_discription']=product_discription[:10]
product['price']=price[:10]
product['Brand']=Brand[:10]
product['discount'] = discount[:10]
product


# Q9: Go to the link - https://www.myntra.com/shoes

# In[ ]:


# Importing Libraries
import pandas as pd
from bs4 import BeautifulSoup
import requests


# In[ ]:


url = "https://www.myntra.com/shoes?f=Color%3ABlack_36454f&plaEnabled=false&rf=Price%3A6362.0_12575.0_6362.0%20TO%2012575.0"
page5 = requests.get(url)
page5


# In[ ]:





# Q10: Go to webpage https://www.amazon.in/
#  Enter “Laptop” in the search field and then click the search icon.

# In[93]:


import pandas as pd
from bs4 import BeautifulSoup
import requests


# In[94]:


url = "https://www.amazon.in/s?k=Laptop&i=computers&rh=n%3A1375424031%2Cp_n_feature_thirteen_browse-bin%3A12598163031%7C16757432031&dc&qid=1628324230&rnid=12598141031&ref=sr_nr_p_n_feature_thirteen_browse-bin_27" 
page = requests.get(url)


# In[95]:


page


# In[96]:


soup = BeautifulSoup(page.content)
soup


# In[97]:


title=[]
Ratings=[]
Price=[]


# In[108]:


for i in soup.find_all("span",class_="a-size-medium a-color-base a-text-normal"):
    title.append(i.text)
 


# In[109]:


title


# In[ ]:




