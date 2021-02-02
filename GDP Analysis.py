#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


gdp_current_price=pd.read_csv("E:/Decode_Lectures/Case Study/Case study_3/gdp.csv")
gdp_current_price


# In[3]:


pd.pivot_table(gdp_current_price,index=["Items Description","Duration"])#Set "Items Description","Duration" column as Index


# In[4]:


gdp_current_price


# In[5]:


gdp_current_price=gdp_current_price.drop(gdp_current_price.index[[3,9]])# Drop Index no 3 & 9 due to los of NA values
gdp_current_price


# In[6]:


gdp_current_price.info()


# In[7]:


#index_to_drop=gdp_current_price.index[((gdp_current_price["Items Description"]=='(% Growth over previous year)')&(gdp_current_price["Duration"]=="2016=17"))]


# In[ ]:


#gdp_current_price.drop(index_to_drop)


# In[7]:


gdp_current_price


# In[8]:


gdp_current_price.columns


# In[9]:


column_attributes=list(gdp_current_price.columns)


# In[10]:


del(column_attributes[0])


# In[11]:


del(column_attributes[0])


# In[12]:


states=column_attributes


# In[13]:


states


# In[14]:


#Calculate the Avg. & store it in below
state_mean={}
for column in gdp_current_price:
    if column in states:
        mean=gdp_current_price[gdp_current_price["Items Description"]=="(% Growth over previous year)"][column].mean()
        state_mean[column]=mean
state_mean["Items Description"]="Average growth rate"
gdp_current_price=gdp_current_price.append(state_mean,ignore_index=True)


# In[15]:


gdp_current_price


# In[16]:


gdp_current_price=gdp_current_price.iloc[[2,7,8],:]


# In[17]:


gdp_current_price


# In[18]:


gdp=gdp_current_price.T
gdp


# In[19]:


gdp.columns=gdp.iloc[0]
gdp


# In[20]:


gdp=gdp[1:]
gdp


# In[21]:


gdp=gdp[1:]
gdp


# In[22]:


gdp.index


# In[23]:


gdp["Average growth rate"].sort_values()


# In[24]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[25]:


sns.barplot(gdp["Average growth rate"])


# In[26]:


gdp["Average growth rate"].sort_values().plot.bar()


# 1. Rate of GDP Growth in North East States like mizoram, Tripura and Nagaland is high.
# 2. States like goa, Meghalaya, Odisha, sikkim and J&K is struggling with GDP growth
# 3. All India GDP is not so relatively low
# 4. GDP growth of bihar, chattisgarh, A&N, Andhra Pradesh, Karnataka and Arunachal Pradesh are relatively high
# 5. For all other states, GDP growth is medium

# In[27]:


gdp["GSDP - CURRENT PRICES (` in Crore)"].drop("All_India GDP",axis=0).sort_values().plot.bar()


# In[28]:


states


# # Part-1_B

# In[29]:


states=['Andhra_Pradesh',
 'Arunachal_Pradesh',
 'Assam',
 'Bihar',
 'Chhattisgarh',
 'Goa',
 'Gujarat',
 'Haryana',
 'Himachal_Pradesh',
 'Jammu & Kashmir',
 'Jharkhand',
 'Karnataka',
 'Kerala',
 'Madhya_Pradesh',
 'Maharashtra',
 'Manipur',
 'Meghalaya',
 'Mizoram',
 'Nagaland',
 'Odisha',
 'Punjab',
 'Rajasthan',
 'Sikkim',
 'Tamil Nadu',
 'Telangana',
 'Tripura',
 'Uttar_Pradesh',
 'Uttarakhand',
 'West Bengal']


# In[30]:


states


# In[31]:


import os


# In[32]:


gsva=pd.DataFrame()


# In[33]:


path=("E:\\Decode_Lectures\\Case Study\\Case study_3\\Datasets-20201224T053210Z-001\\Datasets\\GSVA\\")


# In[34]:


listOfFiles=os.listdir(path)


# In[35]:


len(listOfFiles)


# In[36]:


len(states)


# In[38]:


gsva


# In[37]:


for filename in listOfFiles:
    for statename in states:
        if statename in filename:
            filepath=path+filename
            data=pd.read_csv(filepath,encoding="ISO-8859-1")
            data=data[['Item','2014-15']]
            data=data.T
            data.columns=data.iloc[0]
            data=data[1:]
            data["state"]=statename
            gsva=pd.concat([data,gsva])


# In[40]:


gsva


# In[41]:


gsva.set_index("state",inplace=True)#set State column as index


# In[42]:


gsva


# In[41]:


gsva.columns


# In[42]:


gsva["Per Capita GSDP (Rs.)"].sort_values().plot.bar()


# In[43]:


gsva["Per Capita GSDP (Rs.)"].sort_values()["Goa"]/gsva["Per Capita GSDP (Rs.)"].sort_values()["Bihar"]


# In[44]:


gsva.columns


# In[45]:


gsva


# In[46]:


gsva["Primary_gdp_percent"]=0
gsva["Secondary_gdp_percent"]=0
gsva["Tertiary_gdp_percent"]=0


# In[47]:


gsva


# In[48]:


list(gsva.columns).index("Tertiary")


# In[49]:


for i in range(len(gsva)):
    gsva.iloc[i,37]=gsva.iloc[i,6]/gsva.iloc[i,30]
    gsva.iloc[i,38]=gsva.iloc[i,10]/gsva.iloc[i,30]
    gsva.iloc[i,39]=gsva.iloc[i,26]/gsva.iloc[i,30]


# In[50]:


gsva.sort_values("Per Capita GSDP (Rs.)")[["Primary_gdp_percent","Secondary_gdp_percent","Tertiary_gdp_percent"]].plot(kind="bar",stacked=True)


# In[51]:


gsva.sort_values("Per Capita GSDP (Rs.)")["Population ('00)"].plot(kind="bar")


# 1. For states which has low per capita income, has significant dependence on primary source whereas states which have high per capta income relies more on secondary and tertiary
# 2.UP has high GDP but due to its population, has low per capita income
# 

# In[52]:


per_capita=gsva.sort_values("Per Capita GSDP (Rs.)")
per_capita


# In[54]:


per_capita=gsva["Per Capita GSDP (Rs.)"].sort_values()
per_capita.quantile([0.2,0.5,0.8,1])


# In[55]:


per_capita.sort_values(ascending=False)


# In[56]:



category_1 = ['Goa', 'Sikkim', 'Kerala', 'Haryana']
category_2 = ['Arunachal_Pradesh', 'Punjab','Telangana', 'Gujarat', 'Karnataka', 
       'Maharashtra', 'Uttarakhand']
category_3 = [ 'Madhya_Pradesh', 'Odisha', 'Meghalaya', 'Tripura', 'Rajasthan',
       'Chhattisgarh', 'Nagaland', 'Andhra_Pradesh']
category_4 = ['Bihar', 'Uttar_Pradesh', 'Manipur', 'Assam', 'Jharkhand' ]

categories_columns = ['Agriculture, forestry and fishing', 'Mining and quarrying', 'Manufacturing',
                      'Electricity, gas, water supply & other utility services', 'Construction',
                      'Trade, repair, hotels and restaurants',
                      'Transport, storage, communication & services related to broadcasting', 
                      'Financial services', 'Real estate, ownership of dwelling & professional services',
                      'Public administration', 'Other services', 'Taxes on Products', 'Subsidies on products']


# In[57]:


gsva


# # Category_1

# In[59]:


gsva.loc[category_1,categories_columns]


# In[58]:


agg=gsva.loc[category_1,categories_columns].sum()
agg


# In[62]:


agg_gsdp=gsva.loc[category_1,'Gross State Domestic Product'].sum()
agg_gsdp


# In[63]:


round(100*agg/agg_gsdp).sort_values(ascending=False)[0:6].plot.bar()


# Category 1: There are only 4 states in this category, all of which are small (area-wise) and have good industrial base , agricultural, trade and real estate. 
# 1. Trade and hospitality bisiness should be promoted further
# 2. Manufacturing should be further promoted

# # Category_2 State

# In[64]:


agg=gsva.loc[category_2,categories_columns].sum()
agg_gsdp=gsva.loc[category_2,"Gross State Domestic Product"].sum()
round(100*agg/agg_gsdp).sort_values(ascending=False)[0:6].plot.bar()


# 1. These states have relatively good per capita gdp and are drivcen by around equal percentage by industries and agriclture. These implies that these states have pool of talent to drive industries and agriculture. Because of the talent, other industries can take their advantage and set up good industries.
# 2. States like karnataka, tamil nadu , gujarat and maharashtra, which has huge coastal area can setup ports. Coastal area can help in harness clean energy and fisheries can be increased. Similarly, tourism industry should also be encouraged.

# # Category_3 State

# In[65]:


agg=gsva.loc[category_3,categories_columns].sum()
agg_gsdp=gsva.loc[category_3,"Gross State Domestic Product"].sum()
round(100*agg/agg_gsdp).sort_values(ascending=False)[0:6].plot.bar()


# # Category 4 States

# In[66]:


agg=gsva.loc[category_4,categories_columns].sum()
agg_gsdp=gsva.loc[category_4,"Gross State Domestic Product"].sum()
round(100*agg/agg_gsdp).sort_values(ascending=False)[0:6].plot.bar()


# # Part 2

# In[70]:


drop_out_rate=pd.read_csv("E:/Decode_Lectures/Case Study/Case study_3/Datasets-20201224T053210Z-001/resession.csv",index_col=0)
drop_out_rate


# In[71]:


drop_out_rate.rename(columns={'Level of Education - State':'State'},inplace=True)


# In[72]:


drop_out_rate.replace({"Andhra Pradesh":"Andhra_Pradesh","Arunachal Pradesh":"Arunachal_Pradesh",
                      "Uttar Pradesh":"Uttar_Pradesh","Madhya Pradesh":"Madhya_Pradesh"},inplace=True)


# In[86]:


drop_out_rate


# In[87]:


gsva


# In[90]:


drop_out_rate=drop_out_rate.set_index("State")


# In[91]:


gsva_drop=pd.merge(gsva,drop_out_rate,how="inner",left_index=True,right_index=True)
gsva_drop


# In[76]:


gsva_drop.columns


# In[92]:


gsva_primary=gsva_drop[["Per Capita GSDP (Rs.)","Primary - 2014-2015"]]
gsva_primary


# In[93]:


gsva_primary.dropna(inplace=True)


# In[94]:


gsva_primary['Primary - 2014-2015']=gsva_primary['Primary - 2014-2015'].astype(int)


# In[95]:


gsva_primary.plot.scatter(x="Per Capita GSDP (Rs.)",y="Primary - 2014-2015")


# In[96]:


gsva_secondary=gsva_drop[["Per Capita GSDP (Rs.)","Secondary - 2014-2015"]]
gsva_secondary.dropna(inplace=True)
gsva_secondary['Secondary - 2014-2015']=gsva_secondary['Secondary - 2014-2015'].astype(int)
gsva_secondary.plot.scatter(x="Per Capita GSDP (Rs.)",y="Secondary - 2014-2015")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




