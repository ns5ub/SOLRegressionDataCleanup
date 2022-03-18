#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 21:05:01 2022

@author: niki
"""

import pandas as pd
#DATA IMPORTS

'''DATA IMPORTS'''

#Response Variable, Base Dataset
sol_df = pd.read_csv('data/Response_Variable_SOLReading.csv',header=0)

print()
print("SOL RESPONSE DATAFRAME")
pd.set_option('display.max_columns', None)
sol_df = sol_df.filter(['Division Number','Division Name','Pass Rate'], axis=1)
sol_df['Division Name'] = sol_df['Division Name'].str.upper()
print(sol_df.head(3))
print(sol_df.shape)

#ELSI DATASET
elsi_df = pd.read_csv('data/ELSI_Enrollment_Finance_Information.csv',header=0)

print()
print("ELSI Financial and District Information")
#checking unique values
#data_nums = elsi_df['School District Level Code (SCHLEV) [District Finance] 2018-19'].unique()
#print(data_nums)
#print(data_nums.shape)

elsi_df = elsi_df.drop(columns=['Agency Name', 'State Name [District] Latest available year', 'State Name [District] 2018-19', 'County Number [District] 2018-19', 'Agency Type [District] 2018-19', 'School District Level Code (SCHLEV) [District Finance] 2018-19', 'Prekindergarten offered [District] 2018-19', 'Kindergarten offered [District] 2018-19', 'Agency Level (SY 2017-18 onward) [District] 2018-19'])
elsi_df = elsi_df.rename(columns={"County Name [District] 2018-19": "Division Name"})
elsi_df['Division Name'] = elsi_df['Division Name'].str.upper()
print(elsi_df.head(3))
print(elsi_df.shape)

merged = pd.merge(sol_df, elsi_df, on='Division Name', how='left')
merged.to_csv('testing.csv')
print(merged.shape)