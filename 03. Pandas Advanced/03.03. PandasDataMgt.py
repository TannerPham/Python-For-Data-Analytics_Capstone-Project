# Import Libs
import matplotlib.pyplot as plt
import pandas as pd
from datasets import load_dataset
# Loading Data
dataset = load_dataset(path='lukebarousse/data_jobs')
df = dataset["train"].to_pandas()

# Data Cleaning
df['job_posted_date'] = pd.to_datetime(df.job_posted_date)

# # 1. get a statistically significant sample of our data set
# df.sample() # no argument assigned, 1 row only
# print (df.sample(10)) # return a 10-row sample
# print(df.sample(10,random_state= 42)) # get the same sample every time with random_state

# # 2. copy the dataset with "copy" function
# # why dont we just use "=" to create a copy of the org df, let's find out
#
# df_altered = df
# print (id(df) == id (df_altered))
# # -> these 2 datasets will have the same Id number
# # -> changes on the altered df will also take place in the original one
# # -> we dont want that to happen all the time, don't mess with the origin
#
# df_copied = df.copy()
# print (id(df) == id (df_copied))
#
# # -> these 2 df have different ID now
# # -> changes on one df will not affect the other
# # -> so you dont fuck up the origin dataset




