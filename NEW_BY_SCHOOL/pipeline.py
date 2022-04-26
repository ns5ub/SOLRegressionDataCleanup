#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 16:21:58 2022

@author: niki
"""

import pandas as pd
#DATA IMPORTS

'''STEP 1'''
#Response Variable, Base Dataset
sol_df = pd.read_csv('data/assessment_statistics.csv',header=0)

print()
print("SOL RESPONSE DATAFRAME")
pd.set_option('display.max_columns', None)
sol_df = sol_df.filter(['School Number','School Name','Pass Rate'], axis=1)
#sol_df['School Name'] = sol_df['School Name'].str.upper()
sol_df = sol_df.rename(columns={"School Name":"School"})
print(sol_df.head(3))
print(sol_df.shape)

'''STEP 2'''
#Teacher Quality
print()
print("TEACHER QUALITY DATAFRAME")
tq_df = pd.read_csv('data/Teacher_Quality.csv',header=0)
tq_df = tq_df[tq_df['Title1 Code'] == 'All Schools']
tq_df = tq_df.drop(columns=['Year', 'Division', 'Level', 'Title1 Code', 'Percent of Out-of-Field and Inexperienced Teachers'])
print(tq_df.head(3))
print(tq_df.shape)


'''STEP 3'''
#Spending
print()
print("PER PUPIL SPENDING DATAFRAME")
pps_df = pd.read_csv('data/Per_Pupil_Spending.csv',header=0)
pps_df = pps_df[pps_df['Year'] == '2018 - 2019']
pps_df = pps_df.filter(['School','Total Per-Pupil Expenditures', 'Total Expenditures', 'Per-Pupil Federal Funds', 'Per-Pupil State Funds'], axis=1)
print(pps_df.head(3))
print(pps_df.shape) #131 rows

'''STEP 4: TEACHER SALARIES'''
print()
print("Average Teacher Salaries")
sal_df = pd.read_excel('data/2016_2017_Average_Salary_BySchool.xlsx',header=0)
sal_df = sal_df[sal_df['Division'] == 'Fairfax County Public Schools']
sal_df = sal_df.filter(['School Number', 'School Name', 'Average 2016-2017 Salary'])
print(sal_df.head(3))
print(sal_df.shape)

'''STEP 5: ELSI '''
print()
print("ELSI Financial and District Information")
elsi_df = pd.read_csv('data/ELSI_Enrollment_Finance_Information.csv',header=0)
elsi_df = elsi_df.filter(['School Name [Public School] 2018-19', 'Pupil/Teacher Ratio [Public School] 2018-19', 'Locale [Public School] 2018-19', 'National School Lunch Program [Public School] 2018-19'])
elsi_df = elsi_df.rename(columns={'School Name [Public School] 2018-19':'School Name', 'Pupil/Teacher Ratio [Public School] 2018-19':'Student/Teacher Ratio', 'Locale [Public School] 2018-19':'Locale', 'National School Lunch Program [Public School] 2018-19':'School Lunch Program'})
print(elsi_df.head(3))
print(elsi_df.shape)




print()
print("Merging Per Pupil and Teacher quality")
pps_tq_df = pd.merge(tq_df, pps_df, on='School', how='outer')
#pps_tq_df.to_csv('pps_tq.csv')
print(pps_tq_df.head(3))
print(pps_tq_df.shape)

print()
print("Merging SOL...")
SOL_pps_tq_df = pd.merge(sol_df, pps_tq_df, on='School', how='outer') #left join because pps has more rows
SOL_pps_tq_df = SOL_pps_tq_df.dropna(subset=['Pass Rate'])
#SOL_pps_tq_df.to_csv('SOL_pps_tq_df.csv')
print(SOL_pps_tq_df.head(3))
print(SOL_pps_tq_df.shape)




print()
print("Merging Salary and ELSI")
sal_elsi_df = pd.merge(sal_df, elsi_df, on='School Name', how='outer') #left join because pps has more rows
sal_elsi_df = sal_elsi_df.dropna(subset=['School Number'])
#sal_elsi_df.to_csv('sal_elsi_df.csv')
print(sal_elsi_df.head(3))
print(sal_elsi_df.shape)


print()
print("final merge")
final_df = pd.merge(SOL_pps_tq_df, sal_elsi_df, on='School Number', how='outer') #left join because pps has more rows
#sal_elsi_df = sal_elsi_df.dropna(subset=['School Number'])
final_df = final_df.dropna(subset=['Pass Rate'])
final_df = final_df.dropna()
final_df.to_csv('SOL_Data_Fairfax_County.csv')
print(final_df.head(3))
print(final_df.shape)


