#!/usr/bin/env python
# coding: utf-8

# # Get Stock Price Data 
# 
# As machine learning practitioners, we need to collect stock price data for regression analysis and time series analysis.
# 
# We can easily download it from <a href="https://finance.yahoo.com/">Yahoo Finance.</a> But imagine if we want to create an application where we can analyze the real-time stock prices, we need to collect the latest dataset instead of using the downloaded dataset. So if you want to learn how to get the stock price data between any time interval by using the Python programming language

# Yahoo Finance is one of the most popular websites to collect stock price data. You need to visit the website, enter the company’s name or stock symbol, and you can easily download the dataset. But if you want to get the latest dataset every time you are running your code, you need to use the yfinance API. yfinance is an API provided by Yahoo Finance to collect the latest stock price data.

# **To use this API, you need to install it by using the pip command**

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


import yfinance as yf


import warnings
warnings.filterwarnings("ignore")


# In[11]:


import datetime
from datetime import date, timedelta

today = date.today()
day1 = today.strftime("%Y-%m-%d")
end_date = day1
day2 = date.today() - timedelta(days=360)
day2 = day2.strftime("%Y-%m-%d")
start_date = day2

data = yf.download('AAPL', start=start_date, end=end_date, progress=False)
data.head()


# In[12]:


data.describe()


# In[13]:


data.info()


# In[8]:


data.shape


# In[15]:


data["Date"] = data.index
data = data[["Date", "Open", "High", 
             "Low", "Close", "Adj Close", "Volume"]]
data.reset_index(drop=True, inplace=True)
data.head()


# ## Summary
# 
# So as you can see, the final dataset is just like the dataset that we download from Yahoo Finance. This is how we can get stock price data using Python.
