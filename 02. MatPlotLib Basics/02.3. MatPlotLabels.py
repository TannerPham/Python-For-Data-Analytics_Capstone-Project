# Import Libs
import matplotlib.pyplot as plt
import pandas as pd
from datasets import load_dataset
# Loading Data
dataset = load_dataset(path='lukebarousse/data_jobs')
df = dataset["train"].to_pandas()

# Data Cleaning
df['job_posted_date'] = pd.to_datetime(df.job_posted_date)

# Create a column chart
job_counts = df.job_title_short.value_counts()
job_counts = job_counts.sort_values(ascending=False)
plt.bar(job_counts.index,job_counts)

# # 1. Adding a title, a legend
plt.title('Job Counts by Job Titles')
plt.ylabel('Count of Job Postings')
# # 2. Rotate the x-axis label by 45 degree, align the x-axis label with tick label
plt.xticks(rotation= 45,ha= 'right' ) # ha = horizontal alignment



plt.show()