# Import Libs
import matplotlib.pyplot as plt
import pandas as pd
from datasets import load_dataset
# Loading Data
dataset = load_dataset(path='lukebarousse/data_jobs')
df = dataset["train"].to_pandas()

# Data Cleaning
df['job_posted_date'] = pd.to_datetime(df.job_posted_date)

# # 1. Create plots with a Pandas Series which also has plotting functions, how interesting
# job_counts = df['job_title_short'].value_counts()
# job_counts_viz = job_counts.plot(kind='bar') # you dont need to specify x or y params when working with a Series
# # // you can format the chart just like the way you do in Matplotlib
# plt.title('Job Counts by Job Title')
# plt.ylabel("Count of Job Postings")
# plt.xlabel('')
# plt.xticks(rotation = 45, ha = 'right')

# # 2. Create plots with a Pandas DataFrame
df[['job_posted_date','salary_year_avg']].dropna(subset='salary_year_avg')
df['job_posted_month'] = df['job_posted_date'].dt.month
df.plot(x='job_posted_month',y='salary_year_avg',kind='line')
# # -> this is an unsolved mess

plt.show()