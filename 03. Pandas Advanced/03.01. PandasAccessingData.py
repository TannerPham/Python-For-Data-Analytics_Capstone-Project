# Import Libs
import matplotlib.pyplot as plt
import pandas as pd
from datasets import load_dataset
# Loading Data
dataset = load_dataset(path='lukebarousse/data_jobs')
df = dataset["train"].to_pandas()

# Data Cleaning
df['job_posted_date'] = pd.to_datetime(df.job_posted_date)

# # 1. Access the rows in the DataFrame with iloc[]
# print(df.iloc[0:10])

# # 2. Access all the rows and the 3rd column in the DataFrame
# print(df.iloc[0:10,2]) # you have to remember the index of the column if you use iloc
print(df.loc[:,'salary_rate':'salary_hour_avg'].dropna(subset = 'salary_rate')) # you dont have to remember shit if you use loc


