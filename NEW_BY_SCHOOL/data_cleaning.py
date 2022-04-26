#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 18:55:23 2022

@author: niki
"""

import pandas as pd

df = pd.read_csv('SOL_Data_Fairfax_County.csv',header=0)
pd.set_option('display.max_columns', None)
df = df.filter(['School', 'Pass Rate', 'Locale', 'Poverty Level',
                'Average 2016-2017 Salary', 'Student/Teacher Ratio', 'Percent of Inexperienced Teachers', 'Percent of Out-of-Field Teachers',
                'Total Per-Pupil Expenditures', 'Total Expenditures', 'Per-Pupil Federal Funds', 'Per-Pupil State Funds'], axis=1)

df = df.rename(columns={'Poverty Level':'PovertyLevel', 'Pass Rate':'PassRate',
                'Average 2016-2017 Salary':'TeacherSalary', 'Student/Teacher Ratio':'StudentTeacherRatio',
                'Percent of Inexperienced Teachers':'PercentInexperiencedTeachers', 'Percent of Out-of-Field Teachers':'PercentOutofFieldTeachers',
                'Total Per-Pupil Expenditures':'TotalPerPupilExpenditures', 'Total Expenditures':'TotalExpenditures',
                'Per-Pupil Federal Funds':'PerPupilFederalFunds', 'Per-Pupil State Funds':'PerPupilStateFunds'})

print(df.head(3))
print(df.shape)


df.to_csv('SOL_Data_Fairfax_County_CLEAN.csv')