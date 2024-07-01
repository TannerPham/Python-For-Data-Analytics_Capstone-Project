# Import Libs
import matplotlib.pyplot as plt
import pandas as pd
from datasets import load_dataset
# Loading Data
dataset = load_dataset(path='lukebarousse/data_jobs')
df = dataset["train"].to_pandas()

# Data Cleaning
df['job_posted_date'] = pd.to_datetime(df.job_posted_date)

# # 1. Create a line chart from date column
# plt.plot(df.job_posted_date,df.job_posted_date)

# # 2. Create a line chart depicting number of jobs during months
# df['job_posted_month'] =df['job_posted_date'].dt.month #add a new column
# monthly_counts = df.job_posted_month.value_counts()
# monthly_counts = monthly_counts.sort_index() # sort by the index of the "monthly_count" series
# plt.plot(monthly_counts.index,monthly_counts.values) # x is the index, y is the value of the series

# # 3. Quick lessons on Series in Pandas: One Dimensional, Indexed, Diverse Dtype
# series = pd.Series([10,20,30,40,50],index=['a','b','c','d','e']) # you can add custom indexes
# print(series.index) # returns a list of indexes of the Series
# print(series.values) # returns  a list of values of the Series
# # -> a column of data within a DataFrame is also a Series

# # 4. Create a column chart using bar function of pyplot, how confusing it is
# job_counts = df.job_title_short.value_counts().head(3)
# plt.bar(job_counts.index, job_counts) # 1st arg is for the x-axis, the 2nd is the height of the column

# # 5. Create a bar chart using barh function of pyplot, barh stands for bar horizontal
job_counts = df.job_title_short.value_counts()
job_counts = job_counts.sort_values(ascending= True) # sort by descending order
plt.barh(job_counts.index,job_counts) # 1st arg is for the y-axis, the 2nd is for the width of the x axis


plt.show()