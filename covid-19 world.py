# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 11:07:38 2020

@author: pragati
"""
import pandas as pd
import numpy as np
import geopandas as gpd
import sklearn
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('darkgrid')
data = pd.read_csv('COVID_Data_Basic.csv')
data.shape

data.info()

data = data.drop('Date', 1)
df = data.drop('bad', 1)
df.head()

list(df.columns.values)

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
country_data = list(df['Country'].unique())
country_geo = list(world['name'])

country_diff = [country for country in country_data if country not in country_geo]
country_diff

temp = pd.DataFrame(df['Country'].replace({'US' : 'United States of America'}))


df['Country'] = temp
country_data = list(df['Country'].unique())
country_data


death_sum = df.groupby('Country', sort=False)["Death"].sum().reset_index(name ='total_deaths')
death_sum = death_sum.sort_values(by="total_deaths", ascending=False)

death_sum.head()


mapped = world.set_index('name').join(death_sum.set_index('Country')).reset_index()

to_be_mapped = 'total_deaths'
vmin, vmax = 0,1300000
fig, ax = plt.subplots(1, figsize=(25,25))

mapped.dropna().plot(column=to_be_mapped, cmap='RdPu', linewidth=0.8, ax=ax, edgecolors='0.8')
ax.set_title('Number of deaths due to covid-19', fontdict={'fontsize':30})
ax.set_axis_off()

sm = plt.cm.ScalarMappable(cmap='RdPu', norm=plt.Normalize(vmin=vmin, vmax=vmax))
sm._A = []

cbar = fig.colorbar(sm, orientation='horizontal')









