# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 18:00:19 2020

@author: Mahir Mahbub
"""

# %%
import pandas as pd
import numpy as np

# %%
similar_weather = pd.read_csv(r"C:\Users\Mahir Mahbub\Desktop\COV-19\modified\Similar_Weather_98_Percent.csv", names=["Country/Region"], header = None)
similar_weather = similar_weather[similar_weather["Country/Region"] != "China"]
similar_weather = similar_weather[similar_weather["Country/Region"] != "Iran"]
whole_country_data = pd.read_csv(r"C:\Users\Mahir Mahbub\Desktop\COV-19\Modified\accumulated_whole_country_data.csv")

#%%

similar_data = pd.merge(similar_weather , whole_country_data, how='left', on = "Country/Region")
final_similar_data = similar_data.dropna()

final_similar_data.to_csv(r"weather_similar_confirmed.csv")