import pandas as pd
from datasets import load_dataset
dataset = load_dataset(path='lukebarousse/data_jobs')
df = dataset["train"].to_pandas()
df['job_posted_date'] = pd.to_datetime(df.job_posted_date)
# print(df.describe())
# # 1. count non NA rows in a column or columns
# print(df.count())

# # 2. find the median value of column(s), only applicable to numerical columns
# print(df[['salary_year_avg', 'salary_hour_avg']].median())

# # 3. find the index of the min value on the table and retrieve the according record
# min_salary_index = df['salary_year_avg'].idxmin()
# print(df.iloc[min_salary_index])

# # 4. find the occurring frequency of each unique value in the column
# print(df['job_title_short'].value_counts())

# # 5. grouped by multiple columns: 'job_title_short' and 'job_country' column
# groupby_df = df.groupby(by=['job_title_short','job_country'])['salary_year_avg'].median()
# print(groupby_df.sort_values(ascending=False))

# # 6. perform an aggregation on multiple numerical columns
# print(df.groupby(by=['job_title_short'])[['salary_year_avg','salary_hour_avg']].median())

# # 7. perform multiple aggregations (min,max,sum) on the grouped-by table
print(df.groupby(by=['job_title_short'])['salary_year_avg'].agg(['min','max','sum']))