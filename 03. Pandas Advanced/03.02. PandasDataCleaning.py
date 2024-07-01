# Import Libs
import matplotlib.pyplot as plt
import pandas as pd
from datasets import load_dataset
# Loading Data
dataset = load_dataset(path='lukebarousse/data_jobs')
df = dataset["train"].to_pandas()

# Data Cleaning
df['job_posted_date'] = pd.to_datetime(df.job_posted_date)

# # 1. find the median of the column in a DataFrame
# print(df['salary_year_avg'].median())

# # 2. Use "fillna" method to fill the Nan values in a column
# # note1: remember not to modify directly on the origin dataset, just create a copy you stupid idot
df_fillna = df
median_salary_year = df['salary_year_avg'].median()
median_salary_hour = df['salary_hour_avg'].median()
# -> use these median to fill the nan values, common practice in Machine Learning (Luke says so)
df_fillna['salary_year_avg']= df_fillna['salary_year_avg'].fillna(median_salary_year)
df_fillna['salary_hour_avg']= df_fillna['salary_hour_avg'].fillna(median_salary_hour)
# # note2: can use loc to check specific rows of the data table
# print(df_fillna.loc[:10,'salary_year_avg':'salary_hour_avg']) # filter the first 10 rows

# # 3. use "drop_duplicates" to remove duplicated rows
# df_unique = df_fillna # make a copy of the na-filled dataset above
# df_unique = df_unique.drop_duplicates() # assign the df to itself when applying a function to keep the new outcome
# # if you don't assign no param to this fx, it will remove rows that have the same values in all columns
# print(df_unique)
# # check how many duplicated rows were removed
# print(f'Length of origin df: {len(df_fillna)}')
# print(f'Length of duplicate-removed df: {len(df_unique)}')
# print(f'Rows that were removed: {len(df)-len(df_unique)}')

# 4. specify 'subset' param inside the "drop_duplicates" function
df_unique = df_fillna # make a copy of the na-filled dataset above
df_unique = df_unique.drop_duplicates(subset= ['job_title','company_name']) # use a list for the subset param
# -> this means that the function will remove rows that has the same job title and company name

# check how many duplicated rows were removed
print(f'Length of origin df: {len(df_fillna)}')
print(f'Length of duplicate-removed df: {len(df_unique)}')
print(f'Rows that were removed: {len(df)-len(df_unique)}')