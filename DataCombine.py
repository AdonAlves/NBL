# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 23:57:58 2020

@author: adoor
"""

import pandas as pd 

df12 = pd.read_csv('2012.csv')
df12.drop(columns=['Team'], inplace = True)
df13 = pd.read_csv('2013.csv')
df13.drop(columns=['Team'], inplace = True)
df14 = pd.read_csv('2014.csv')
df14.drop(columns=['Team'], inplace = True)
df15 = pd.read_csv('2015.csv')
df15.drop(columns=['Team'], inplace = True)
df16 = pd.read_csv('2016.csv')
df16.drop(columns=['Team'], inplace = True)
df17 = pd.read_csv('2017.csv')
df17.drop(columns=['Team'], inplace = True)
df18 = pd.read_csv('2018.csv')
df18.drop(columns=['Team'], inplace = True)
df19 = pd.read_csv('2019.csv')
df19.drop(columns=['Team'], inplace = True)
df20 = pd.read_csv('2020.csv')
df20.drop(columns=['Team'], inplace = True)

frames =  [df12, df13, df14, df15, df16, df17, df18, df19, df20]

data = pd.concat(frames, ignore_index=True)
data.to_csv('nbl.csv', index=False)
