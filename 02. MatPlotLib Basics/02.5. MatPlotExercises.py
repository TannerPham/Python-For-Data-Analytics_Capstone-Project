# Import Libs
import matplotlib.pyplot as plt
import pandas as pd
from datasets import load_dataset
# Loading Data
dataset = load_dataset(path='lukebarousse/data_jobs')
df = dataset["train"].to_pandas()

# Data Cleaning
df['job_posted_date'] = pd.to_datetime(df.job_posted_date)

# Group by job title, calculate the median value of each job
jobsalary_df = df.groupby('job_title_short')['salary_year_avg'].median().sort_values(ascending=True)

# create a bar chart
jobsalary_df.plot(kind='barh')

# format the chart
plt.xlabel('Salary ($USD)')
plt.ylabel('')
plt.title('Median Salary by Job Title')

# show the chart
plt.show()
