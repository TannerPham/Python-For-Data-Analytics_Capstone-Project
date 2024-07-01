import pandas as pd
from datasets import load_dataset
dataset = load_dataset(path='lukebarousse/data_jobs')
df = dataset["train"].to_pandas()
# # 1.how to turn a csv into a Dataframe
# df = pd.read_csv('california_housing_test.csv')
# # 2. access a row of a series aka column
# print(df.total_bedrooms[0])

# # 3.import datasets package to retrieve data from hugging face

# # 4.get the first 10 rows of job_title_short column
# print(df.job_title_short.head(10))
# # 5.get multiple columns by using double square brackets
# print(df[['job_title_short','job_location']].head())
# # 6. use iloc function to view the all the values of a record or records
# print(df.iloc[90:100]) # the 90th record
# # 7. the second parameter of iloc is used for choosing the columns
# print(df.iloc[90,0:2]) # 0:2 = retrieve the 1st and 2nd column
# print(df[['job_title_short','job_location']].iloc[90]) # have another way to choose the columns

# # 8. the info function of pandas gives out general information of the dataset
# print(df.info())
# # 9. the describe function analyze statistics only for numerical columns
# print(df.describe())
# # 10. the unique function returns what?? unique values of course, but unique values of a specified column
# print(df.job_title_short.unique())

# # 11. this is how you create an expression to filter the dataframe
# print(df.job_title_short == 'Data Analyst')
# # 12. You can take the above to filter the data frame just like this
# print(df[df.job_title_short == 'Data Analyst'])
# # 13. You can filter with multiple criteria with the "ampersand" operator + you can filter the column and then filter the row
# print(df[['job_title_short','salary_year_avg']][(df.job_title_short == 'Data Analyst') & (df.salary_year_avg > 100000)])
# # 14. the sign "|" (shift+ \) stand for OR operator
# print(df[['job_title_short','salary_year_avg']][(df.job_title_short == 'Data Analyst') | (df.salary_year_avg > 100000)])

# # 15. notna function is used to filter out rows that are labeled as NAN a.k.a Not A Number
print(df[['job_title_short','salary_year_avg']][(df.job_title_short == 'Data Analyst') & (df.salary_year_avg.notna())])