#!/usr/bin/env python
# coding: utf-8

# In[214]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)
import requests
#from collections import defaultdict


# In[2]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[3]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')
slide_elem.find('div', class_='content_title')


# In[4]:


news_title = slide_elem.find('div', class_='content_title').get_text() ##This is to remove the HTML code additions in the line above
news_title


# In[5]:


#Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured images

# In[6]:


#Visit URL
url = 'https://spaceimages-mars.com/'
browser.visit(url)


# In[7]:


#Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[8]:


#parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[9]:


#Find the relative image URL
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[10]:


#Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# # Mars Facts

# In[11]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns = ['description', 'Mars', 'Earth']
df.set_index('description', inplace = True)
df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ## Hemispheres

# In[238]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[239]:


html = browser.html
item_soup = soup(html, 'html.parser')


# In[240]:


#import pandas as pd
i = 0
# 2. Create a list to hold the images and titles.
html = browser.html
item_soup = soup(html, 'html.parser')
Temp = {}
hemisphere_image_url = []


# In[241]:


for item in item_soup.find_all('h3'):
    title = item.text
    
    open_file = browser.find_by_text(title)[0]
    if title == "Back":
        continue
    open_file.click()
    html = browser.html
    item_soup = soup(html, 'html.parser')
    image = item_soup.find('img', class_='wide-image').get('src')

    item_url = f'https://marshemispheres.com/{image}'
      
    Temp = {'image_url': item_url, 'title':title}
    hemisphere_image_url.append(Temp)
    
        html = browser.back()
       
    i = i +1


# In[242]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_url


# In[243]:


#to quite the automated browser session
browser.quit()


# In[ ]:




