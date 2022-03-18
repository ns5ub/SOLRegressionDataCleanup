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
sol_df = pd.read_csv('data/Response_Variable_SOLReading.csv',header=0)

print()
print("SOL RESPONSE DATAFRAME")
pd.set_option('display.max_columns', None)
sol_df = sol_df.filter(['Division Number','Division Name','Pass Rate'], axis=1)
sol_df['Division Name'] = sol_df['Division Name'].str.upper()
sol_df = sol_df.rename(columns={"Division Name":"Division"})
print(sol_df.head(3))
print(sol_df.shape)


'''STEP 2'''
#Teacher Quality
print()
print("TEACHER QUALITY DATAFRAME")
tq_df = pd.read_csv('data/Teacher_Quality.csv',header=0)

'''
#this data has 134 divisions, not 132?
data_nums = tq_df['Division'].unique()
print(data_nums)
print(data_nums.shape)
'''

tq_df = tq_df[tq_df['Poverty Level'] == 'All Schools'] 
tq_df = tq_df[tq_df['Title1 Code'] == 'All Schools'] 
tq_df = tq_df.drop(columns=['Year', 'Level', 'Poverty Level', 'Title1 Code', 'Percent of Out-of-Field and Inexperienced Teachers'])
print(tq_df.head(3))
print(tq_df.shape)

'''STEP 3'''
#Spending
print()
print("PER PUPIL SPENDING DATAFRAME")
pps_df = pd.read_csv('data/Per_Pupil_Spending.csv',header=0)
pps_df = pps_df[pps_df['Year'] == '2018 - 2019'] 
pps_df = pps_df.filter(['Division','Total Per-Pupil Expenditures', 'Total Expenditures', 'Per-Pupil Federal Funds', 'Per-Pupil State Funds'], axis=1)
print(pps_df.head(3))
print(pps_df.shape) #131 rows

'''STEP 4: MERGING PER PUPIL SPENDING/TEACHER QUALITY'''
'''
print()
print("Merging Per Pupil and Teacher quality")
pps_tq_df = pd.merge(tq_df, pps_df, on='Division', how='outer') #left join because pps has more rows
pps_tq_df['Division'] = pps_tq_df['Division'].str[:-15]
pps_tq_df.to_csv('pps_tq.csv')
pps_tq_df['Division'] = pps_tq_df['Division'].str.upper()
print(pps_tq_df.head(3))
print(pps_tq_df.shape)

print()
print("Merging into SOL")
sol_pps_tq_df = pd.merge(sol_df, pps_tq_df, on='Division', how='outer') #left join because pps has more rows
sol_pps_tq_df.to_csv('sol_pps_tq.csv')
print(sol_pps_tq_df.head(3))
print(sol_pps_tq_df.shape)
'''

'''STEP 5: TEACHER SALARIES'''
print()
print("Average Teacher Salaries")
sal_df = pd.read_excel('data/2016_2017_Average_Salary_BySchool.xlsx',header=0)
sal_df = sal_df.filter(['Division Number', 'Division', 'Average 2016-2017 Salary'])
sal_df = sal_df.groupby(['Division Number', 'Division']).mean()
print(sal_df.head(3))
print(sal_df.shape)

print()
print("Merging Per Pupil and Teacher quality")
pps_tq_df = pd.merge(tq_df, pps_df, on='Division', how='outer')
#pps_tq_df.to_csv('pps_tq.csv')
print(pps_tq_df.head(3))
print(pps_tq_df.shape)

print()
print("Merging Salary...")
pps_tq_sal_df = pd.merge(pps_tq_df, sal_df, on='Division', how='outer')
#pps_tq_sal_df.to_csv('pps_tq_sal.csv')
print(pps_tq_sal_df.head(3))
print(pps_tq_sal_df.shape)

print()
print("Clean up for Merge into SOL")
pps_tq_sal_df['Division'] = pps_tq_sal_df['Division'].str[:-15]
pps_tq_sal_df['Division'] = pps_tq_sal_df['Division'].str.upper()
print(pps_tq_sal_df.head(3))
print(pps_tq_sal_df.shape)

print()
print("Merging SOL...")
SOL_pps_tq_sal_df = pd.merge(sol_df, pps_tq_sal_df, on='Division', how='outer') #left join because pps has more rows
#SOL_pps_tq_sal_df.to_csv('SOL_pps_tq_sal.csv')
print(SOL_pps_tq_sal_df.head(3))
print(SOL_pps_tq_sal_df.shape)

print()
print("ELSI Financial and District Information")
elsi_df = pd.read_csv('data/ELSI_Enrollment_Finance_Information.csv',header=0)
elsi_df = elsi_df.filter(['County Name [District] 2018-19', 'Pupil/Teacher Ratio [District] 2018-19', 'Locale [District] 2018-19', 'Total Number Operational Schools [Public School] 2018-19', 'Total Students All Grades (Excludes AE) [District] 2018-19', 'Individualized Education Program Students [District] 2018-19', 'Limited English Proficient (LEP) / English Language Learners (ELL) [District] 2018-19'])
elsi_df = elsi_df.rename(columns={'County Name [District] 2018-19':'Division', 'Pupil/Teacher Ratio [District] 2018-19':'Student/Teacher Ratio', 'Locale [District] 2018-19':'Division Locale', 'Total Number Operational Schools [Public School] 2018-19': 'Operational Public Schools', 'Total Students All Grades (Excludes AE) [District] 2018-19':'Total Students', 'Individualized Education Program Students [District] 2018-19':'IEP Students', 'Limited English Proficient (LEP) / English Language Learners (ELL) [District] 2018-19':'LEP+ELL Students'})
elsi_df['Division'] = elsi_df['Division'].str.upper()
elsi_df['Division Locale'] = elsi_df['Division Locale'].str.extract(r'(-.*:)')
elsi_df['Division Locale'] = elsi_df['Division Locale'].str[1:-1]
print(elsi_df.head(3))
print(elsi_df.shape)

print()
print("FINAL MERGE")
final_df = pd.merge(SOL_pps_tq_sal_df, elsi_df, on='Division', how='outer')
print(final_df.head(3))
print(final_df.shape)
final_df.to_csv('SOL_Data_ByDivision_Merged.csv')