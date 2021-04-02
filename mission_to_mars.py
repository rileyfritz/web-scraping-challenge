#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
from bs4 import BeautifulSoup
import requests
import pymongo
import pandas as pd
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:


# Bringing in browser
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# Visit url 
url = 'https://redplanetscience.com/'
browser.visit(url)
 # HTML object
html = browser.html
# Parse HTML with Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')


# In[4]:


# Retrieve the parent divs for all articles
results = soup.find_all('div', class_ = "list_text")
# Get the title and teaser from first article
title = results[0].find('div', class_='content_title').text
teaser = results[0].find('div', class_='article_teaser_body').text


# In[5]:


# print(title)
# print(teaser)


# In[6]:


url = 'https://spaceimages-mars.com/'
browser.visit(url)
 # HTML object
html = browser.html
# Parse HTML with Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')


# In[7]:


img_result = soup.find('a', class_="showimg fancybox-thumbs")
featured_img_url = url + img_result['href']
# print(featured_img_url)


# In[8]:



url = 'https://galaxyfacts-mars.com/'
browser.visit(url)
 # HTML object
html = browser.html
# Parse HTML with Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')


# In[9]:


tables = pd.read_html(url)
mars_facts = tables[0]


# In[10]:


mars_facts.drop(index=0, inplace=True)
# mars_facts.head()


# In[11]:


mars_facts.rename(columns = {0:"Mars - Earth Comparison", 1 : "Mars", 2 : "Earth"}, inplace=True)
# mars_facts.head()


# In[12]:


mars_facts.set_index(inplace=True, keys = 'Mars - Earth Comparison')
# mars_facts.head()


# In[13]:


mars_facts_html = mars_facts.to_html()
# mars_facts_html


# In[14]:


url = 'https://marshemispheres.com/'
browser.visit(url)
 # HTML object
html = browser.html
# Parse HTML with Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')


# In[15]:


img_titles = []
img_urls = []
results = soup.find_all('div', class_ = "item")

for result in results:
    header = result.find('h3').text
    # print(header)

    try:
        browser.links.find_by_partial_text(header).click()
        soup = BeautifulSoup(browser.html, 'html.parser')
        img_url = url + soup.find('img', class_='wide-image')['src']
        # print(img_url)
        # print("link found!")
        browser.back()
        img_titles.append(header)
        img_urls.append(img_url)
    
    except:
        # print("Scraping error!")
    


# In[23]:


img_urls_titles = []
for x in range(0, len(img_titles)):
    img_dict = {'title': img_titles[x], 'url': img_urls[x]}
    img_urls_titles.append(img_dict)


# In[24]:


# img_urls_titles

