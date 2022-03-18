#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 18:55:23 2022

@author: niki
"""

import pandas as pd

df = pd.read_csv('SOL_Data_ByDivision_Merged.csv',header=0)
pd.set_option('display.max_columns', None)
df = df.filter(['Division', 'Pass Rate', 'Division Locale',
                'Average 2016-2017 Salary', 'Student/Teacher Ratio', 'Percent of Inexperienced Teachers', 'Percent of Out-of-Field Teachers',
                'Total Per-Pupil Expenditures', 'Total Expenditures', 'Per-Pupil Federal Funds', 'Per-Pupil State Funds'], axis=1)
print(df.head(3))
print(df.shape)

print()
df = df[df['Pass Rate'].notna()]
print(df.head(3))
print(df.shape)

print()
df = df[df['Percent of Inexperienced Teachers'].notna()]
print(df.head(3))
print(df.shape)

df = df[df['Total Per-Pupil Expenditures'].notna()]
print(df.head(3))
print(df.shape)

df.to_csv('SOL_Data_ByDivision_CLEAN.csv')