#!/usr/bin/env python
# coding: utf-8

# ## Import Libraries

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from textblob import TextBlob


# In[2]:


print(matplotlib.__version__)


# ## Data Loading and Exploration | Cleaning

# In[ ]:


#Load a CSV file then creating a dataframe
amazon = pd.read_csv(r"C:\Users\sonay\Downloads\amazon.csv")
amazon


# In[4]:


#have a look on the columns and their data types using detailed info function
amazon.info()


# In[44]:


#column names
amazon.columns


# ##  Missing Values

# In[5]:


#Finding the missing values in each columns
amazon.isnull().sum()


# In[6]:


#Finding columns, where missing values
amazon[amazon.isnull().sum(axis=1)>0]


# In[7]:


#clear columns from null values
amazon.dropna(inplace=True)


# In[8]:


#Cheking missing values
amazon.isna().sum()


# In[9]:


# Finding unusual string in rating column
amazon['rating'].value_counts()


# ##  Changing Data Types of Columns from object to float

# In[10]:


amazon = amazon[amazon['rating']!="|"]
amazon['rating'] = amazon['rating'].astype('float64')
amazon.info()


# In[11]:


amazon['rating'].dtype


# In[12]:


#Creating a function that replaces "," with an empty line
def f(x):
    if isinstance(x, str):
        x =  x.replace(',', '')
    return x
 


amazon['rating_count'] = amazon['rating_count'].apply(f)
amazon['rating_count'] = amazon['rating_count'].astype('float64')

amazon.head(3)


# In[13]:


amazon['rating_count'].dtype


# In[14]:


#Creating and implementing functions for shortening names from 'category' column
def short_name(name):
    name = name.split('|')
    return name[0] + '|' + name[-1]
amazon['category'] = amazon['category'].apply(short_name)


#Creating and accepting functions for converting value for columns 'discounted_price', 'actual_price'
def f1(x):
    if isinstance(x, str):
        x =  x.replace('₹', '').replace(',', '')
    return x
amazon[['discounted_price', 'actual_price']] = amazon[['discounted_price', 'actual_price']].applymap(f1)
amazon = amazon.astype({'discounted_price':'float64', 'actual_price': 'float64'})

#Converting the value of the 'discount_percentage' column
amazon['discount_percentage'] = amazon['discount_percentage'].apply(lambda x: float(x.replace('%', '')))

amazon.head(3)


# In[15]:


#Checking data types
amazon['discount_percentage'].dtype


# In[16]:


#Creating a function using a TextBlob object that checks the tone of the reviews
def analiz_text(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neytral'
    
amazon['comment'] = amazon['review_title'].apply(analiz_text)
amazon['comment_copy'] = amazon['comment']
amazon.head(3)


# ## Duplicates

# In[47]:


amazon.duplicated().any()


# ## Grouping and Aggregation

# In[75]:


a = amazon[['category', 'product_name']].groupby('category', sort=False).count()
a[a['product_name']<5]


# In[76]:


df_group_rating = amazon[['category', 'rating']].groupby('category').mean().sort_values(by='rating', ascending=False)

df_group_rating.head()


# In[77]:


discount_rating = amazon[['category', 'discount_percentage']].groupby(['category']).mean().merge(merge_table, on='category', how='inner').sort_values(by='rating', ascending=False)
discount_rating.head()


# ## Creating a pivot table 

# In[86]:


#Creating a pivot table that summarizes the number of positive, negative, and neutral reviews by category
df_comment_percent = amazon.pivot_table(values='comment_copy', index='category', columns='comment', aggfunc='count', fill_value=0, sort=False)
df_comment_percent.sort_values(by='Positive', ascending=False, inplace=True)
df_comment_percent = df_comment_percent[df_comment_percent.sum(axis=1)>5]
df_comment_percent.head()


# In[87]:


#Convert the number of comments to a percentage
df_comment_percent['comment_sum'] = df_comment_percent.iloc[:, 0:3].sum(axis=1)
df_comment_percent ['positive_comm_percent'] =round(df_comment_percent['Positive']*100/df_comment_percent['comment_sum'])
df_comment_percent ['negative_comm_percent'] = round(df_comment_percent['Negative']*100/df_comment_percent['comment_sum'])
df_comment_percent['neytral_com_percent'] = round(df_comment_percent['Neytral']*100/df_comment_percent['comment_sum'])
df_comment_percent.head()


# ## Joining dataframes 

# In[94]:


#Joining two dataframes, that to compare columns 'rating' and 'positive_comment'
merge_table = df_comment_percent.merge(df_group_rating, how='inner', on='category')
merge_table.sort_values(by='Positive',ascending=False, inplace=True)
merge_table.head()


# In[ ]:





# # Data Visualization

# ## Histogram

# In[111]:


# Plot distribution of actual_price
plt.hist(amazon['actual_price'], color='c',alpha=0.7)
plt.xlabel('Actual Price')
plt.ylabel('Frequency')
plt.show()


# ## Bar

# In[89]:


# Creating a bar chart that shows the top 10 popular products
plt.figure(figsize=(16, 6))
plt.title('Top 10 products by category')

plt.bar(df_group_rating.iloc[0:10].index.values, df_group_rating['rating'].iloc[0:10] , color='c')
plt.grid(linestyle='--', axis='y',alpha=0.5)
plt.ylim(4, 5)
plt.yticks([4, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5])
plt.tick_params(axis='x', labelrotation=90)
plt.ylabel('Rating')
plt.show()


#   ## Determining the factors influencing the rating

# In[90]:


# Создание график поквзывающий сравнения 'rating' и 'positive_comment'
merge_table[['Positive', 'Negative', 'Neytral']].iloc[0:10].plot(kind='bar',figsize=(16, 6), title='Top 10 Most Reviewed Products' ,ylabel='Count of comments', color=['darkcyan', 'darkred', 'olive'])
merge_table['rating'].iloc[0:10].plot(secondary_y=True,figsize=(16, 6), style='o--', title='Top 10 Most Reviewed Products', grid='horizontal',ylabel='Rating', color='lightcoral', alpha=0.7, rot=90)


# In[91]:


merge_table.iloc[0:10].plot(kind='bar',figsize=(16, 6), y=['Positive', 'Negative', 'Neytral'], title='Top 10 Most Reviewed Products', grid='horizontal',ylabel='Count of comments', color=['darkcyan', 'darkred', 'olive'])


# In[95]:


#changing merge_table to dataframe with the new index
merge_table.reset_index(inplace=True)
merge_table.head()


# In[107]:


# Установка цвета
fig, ax1 = plt.subplots(figsize=(16, 6))
plt.title('Comparison of Rating and Count of Positive Comments by Category')
# Создание столбиковой диаграммы для positive comments

ax1.bar(merge_table['category'], merge_table['positive_comm_percent'], color='teal', alpha=0.6, label='Positive Comments')
ax1.set_ylabel('Percent of Positive Comments', color='teal', fontsize=14)
plt.ylim(0,120)
plt.xticks(rotation=90)
# Создание вторичной оси для отображения рейтинга
ax2 = ax1.twinx()
ax2.plot(merge_table['category'], merge_table['rating'], color='firebrick', marker='o', label='Rating')
ax2.set_ylabel('Average Rating', color='firebrick', fontsize=14)
plt.ylim(3, 4.7)
plt.grid(linestyle='--', alpha=0.6)


# Добавление легенды
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')


plt.show()


# In[ ]:


amazon['discount_percentage'].dtype


# In[99]:


#Соединяем столбцы 'discount_percentage' и 'rating', чтобы сравнить их
discount_rating.reset_index(inplace=True)
discount_rating.head()


# In[100]:


# Установка цвета
fig, ax1 = plt.subplots(figsize=(16, 6))
plt.title('Comparison of Rating and Percent of discount_percentage by Category')
# Создание столбиковой диаграммы для positive comments
ax1.bar(discount_rating['category'], discount_rating['discount_percentage'].sort_values(), color='g', alpha=0.4, label='Discount percentage')
ax1.set_ylabel('Percent of discount_percentage', color='g')
plt.xticks(rotation=90)

# Создание вторичной оси для отображения рейтинга
ax2 = ax1.twinx()
ax2.plot(discount_rating['category'], discount_rating['rating'], color='g',linewidth=4 , label='Rating')
ax2.set_ylabel('Average Rating', color='g')
ax2.set_xticks('')

# Добавление легенды
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')


plt.show()


# In[ ]:




