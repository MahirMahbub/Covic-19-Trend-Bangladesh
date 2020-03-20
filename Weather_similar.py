# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 14:28:45 2020

@author: Mahir Mahbub
"""

# %% 
import pandas as pd

# %%
similar_weather = pd.read_csv(r'C:\Users\Mahir Mahbub\Desktop\Similar_Weather.csv', header=None)
similar_weather_country = similar_weather.iloc[0:73,[1]]
similar_weather_country = similar_weather_country.apply(lambda x: x.str.capitalize() )

unique_similar_weather_country = similar_weather_country.drop_duplicates()
print(unique_similar_weather_country)

# %%
unique_similar_weather_country.to_csv(r"C:\Users\Mahir Mahbub\Desktop\COV-19\modified\Similar_Weather_98_Percent.csv")
