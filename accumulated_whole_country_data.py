# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 17:17:31 2020

@author: Mahir Mahbub
"""
# %%
import  pandas as pd
import numpy as np

# %%
similar_weather = pd.read_csv(r"C:\Users\Mahir Mahbub\Desktop\COV-19\modified\Similar_Weather_98_Percent.csv")
# %%
confirmed_cases = pd.read_csv(r"..\time_series_covid_19_confirmed.csv")
confirmed_cases_country_and_count = confirmed_cases.drop(["Province/State", "Lat", "Long"], axis = 1)
# %%
unique_countries =  confirmed_cases_country_and_count["Country/Region"].unique()

# %%
whole_country_data = confirmed_cases_country_and_count.groupby("Country/Region").sum()
whole_country_data.to_csv(r"accumulated_whole_country_data.csv")