import pandas as pd
from datasets import load_dataset
dataset = load_dataset(path='lukebarousse/data_jobs')
df = dataset["train"].to_pandas()
# # 1. pandas.to_datetime function convert non-datetime data
# print(pd.to_datetime(df.job_posted_date))
# # 2. assign new data type to a column in a pd dataframe
df['job_posted_date'] = pd.to_datetime(df.job_posted_date)
# print(df.info())
# # 3. extract different timeframes of the date column
# print(df['job_posted_date'].dt.month)
# # 4. adding a new column is similar to accessing a column, replace existing column name with the new column name
# df['job_posted_month'] = df['job_posted_date'].dt.month
# print(df.info())

# # 5. sorting the values in a column, 'inplace' parameter is used to replace the old table with the sorted table
# df.sort_values(by= 'job_posted_date',inplace=True)
# print(df['job_posted_date'])
# # 6. how to remove a column using drop function, axis = 1 means that the you can assign column name into the 'labels' param
# df.drop(labels='salary_hour_avg',axis=1,inplace=True)
# print(df.info())
# # 7. how to drop na values in a dataframe using dropna function, axis = 1 equals to dropping rows, = 0 equals to dropping cols
df.dropna(subset=['salary_year_avg'],inplace=True)
print(df.info())
