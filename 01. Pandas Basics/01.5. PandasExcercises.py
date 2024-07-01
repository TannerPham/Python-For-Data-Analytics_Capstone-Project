import pandas as pd
from datasets import load_dataset
dataset = load_dataset(path='lukebarousse/data_jobs')
df = dataset["train"].to_pandas()
df['job_posted_date'] = pd.to_datetime(df.job_posted_date) # change dtype of a date column

# # 1. filter the top 20 countries which have the most data jobs
# print(df['job_country'].value_counts().head(20))

# # 2. check if Vietnam's data jobs are included inside the dataset
# # -> any() function return a boolean value to inform whether the value we look for exists or not
# print(df['job_country'].value_counts().isin(['Vietnam','Viet Nam']).any())

# # 3. top 20 jobs in the US that offer highest yearly salary
# us_jobs = df[df['job_country'] =='United States']
# print(us_jobs[['job_title_short','job_country','salary_year_avg']].sort_values(by='salary_year_avg',ascending=False).head(20))

# # 4. filter jobs at the US, group by job title and perform common aggregations on yearly salary
us_jobs = df[df['job_country'] =='United States']
us_jobs = us_jobs[us_jobs['salary_year_avg'].notna()]
print(us_jobs.groupby(by=['job_title_short'])[['salary_year_avg']].agg(['median','min','max','count']).sort_values(by=('salary_year_avg','median'),ascending= False))
# #-> you need to sort by the tuple (‘salary_year_avg’, ‘median’) when you sort an newly-aggregated column