#!/usr/bin/env python
# coding: utf-8

# A. READING THE FILE 

# In[5]:


import csv
import os
import numpy as np
import pandas as pd
import matplotlib
from File_Path import collect_file_path



df_car_sales = pd.read_csv('../COM728_Project/Car_Price.csv')

df_car_sales.head()


# B. RETREIVING INFORMATION

# In[2]:


df_car_sales.index = df_car_sales['car_ID']
df_car_sales.head()


# In[36]:


# The aim of this funtion is to help the user retrieve all information of specific transactions.
# To do this, we define a function that displays all the information in a row of the given table, and make the 
# information easily accessible when the user inputs the ID number
def retrieve_by_card_ID():
    car_ID = int(input('Enter Car ID number: '))
    for row in df_car_sales:
        row = df_car_sales.loc[car_ID]
        print(row)
        
retrieve_by_card_ID()
   
        


# In[35]:



def table_resize():
    cs1 = df_car_sales[['CarName', 'cylindernumber']]
    return cs1

def cn_exact_num():
    cn = int(input('Enter Cylinder Number: '))
    exact_cn = cs1[cs1['cylindernumber']==cn]
    print(exact_cn)

cs1 = table_resize()
cn_exact_num()


# In[32]:


def table_car_type():
    cs2 = df_car_sales[['CarName', 'carbody']]
    return cs2

def cb_exact_():
    cn2 = input('Enter Car bodytype: ')
    exact_cb = cs2[cs2['carbody']==cn2]
    print(exact_cb)

cs2 = table_car_type()
cb_exact_()


# In[31]:


def retrieve_4col_by_id():
    car_ID = int(input('Enter Car ID: '))
    cs3 = df_car_sales[['CarName','cylindernumber', 'doornumber', 'carbody']]
    result = cs3[car_ID - 1: car_ID]
    print(result)
retrieve_4col_by_id()


# C. QUERYING THE FILE

# In[30]:


def retrieve_by_alpha():
    CarName = df_car_sales.CarName
    print(CarName.sort_values())
retrieve_by_alpha()


# In[ ]:


df_car_sales.CarName[90]


# In[29]:



def resize_4():
    car_price_per_body = df_car_sales[['price', 'carbody']]
    by_body = car_price_per_body.groupby(['carbody'])
    cb = input('Enter car body: ')
    exact_body = by_body.get_group(cb)
    total_sales_per_body = sum(exact_body.price)
    print(f' The total sales for {cb} cars is {total_sales_per_body}')
resize_4()


# In[28]:



def resize_5():
    car_body_price = df_car_sales[['CarName','price', 'carbody']]
    by_body = car_body_price.groupby(['carbody'])
    cb = input('Enter car body: ')
    exact_body = by_body.get_group(cb)
    exact_body_sorted = exact_body.sort_values('price', ascending = False)
    print(exact_body_sorted[0:5])
resize_5()


# VISUALIZE DATA

# In[3]:



def cs_visuals_1():
    car_per_fs = df_car_sales[['CarName','fuelsystem']]
    fs =np.array(car_per_fs['fuelsystem'])
    fs_element = np.unique(fs, return_counts = True)
    print(fs_element)

    Fuel_system = ['1bbl', '2bbl', '4bbl', 'idi', 'mfi', 'mpfi', 'spdi', 'spfi']
    Number_of_cars_per_fs = [11, 66,  3, 20,  1, 94,  9,  1]
    df_test = pd.DataFrame([Fuel_system,Number_of_cars_per_fs])

    df_test_plot = df_test.T

    df_test_plot.columns = ['Fuel Systems', 'Number of Cars']

    df_test_plot.plot.bar(xlabel = 'Fuel Systems', ylabel = 'Number of Cars', title = 'NUMBER OF CAR BY FUEL SYSTEMS')
    
cs_visuals_1()


# In[45]:


get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt

def cs_visuals_2():
    hp_price = df_car_sales[['CarName', 'horsepower', 'price']]
    top_5_sales = hp_price.sort_values(ascending = True, by = 'price')[0:5]
    print(top_5_sales)
    fig, (ax1,ax2,ax3,ax4,ax5) = plt.subplots(1,5,figsize=(20,7))
    
    ax1.bar(top_5_sales['CarName'].loc[139], df_car_sales['horsepower'].loc[139], color = 'black')
    ax1.set(title = 'SUBARU HORSEPOWER')
    
    ax2.bar(top_5_sales['CarName'].loc[19], df_car_sales['horsepower'].loc[19], color = 'purple')
    ax2.set(title = 'CHEVROLET IMPALA HORSEPOWER')
    
    ax3.bar(top_5_sales['CarName'].loc[51], df_car_sales['horsepower'].loc[51], color = 'green')
    ax3.set(title = 'MAXDA RX3 HORSEPOWER')
    
    ax4.bar(top_5_sales['CarName'].loc[151], df_car_sales['horsepower'].loc[151], color = 'orange')
    ax4.set(title = 'TOYOTA CORONA MARK ii HORSEPOWER')
    
    ax5.bar(top_5_sales['CarName'].loc[77], df_car_sales['horsepower'].loc[77], color = 'indigo')
    ax5.set(title = 'MISTUBISHI MIRAGE HORSEPOWER')
    
    
    
cs_visuals_2()


# In[31]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df_car_sales = pd.read_csv('../COM728_Project/Car_Price.csv')
df_car_sales.head()


# In[12]:


df_car_sales.carbody.head()


# In[13]:


each_car_type = np.unique(np.array([df_car_sales.carbody]), return_counts = True)
print(each_car_type)


# In[15]:


carbody = ['covertible', 'hardtop', 'hatchback', 'sedan', 'wagon']
carbody_count = [6,  8, 70, 96, 25]

plt.pie(carbody_count, labels = carbody)


plt.show()


# In[ ]:




