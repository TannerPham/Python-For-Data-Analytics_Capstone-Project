# # put comma after the semicolon to add thousand separator
# # put .2f after the semicolon to specify the decimal place
# value = 100000
# print(f'{value:.0f}') # this is how you format the number


## ----- numpy basics ------ ##

import random
import timeit
import statistics
import numpy as np

# # 1. numpy is faster than statistics
# salary_list = [random.randint(50000,100000) for _ in range(10000000)]
# print(statistics.median(salary_list))
#
# print(timeit.timeit())
# print(np.median(salary_list))
# print(timeit.timeit())

# # 2. work with array
# a = np.array([1,2,3,4,5])
# print(f'{a.mean():.0f}')

# # 3. array examples
# # job titles
# job_titles = np.array(['Data Analyst','Data Engineer','Data Scientist','Machine Learning Engineer','AI Engineer'])
# # base salaries
# base_salaries = np.array([60000, 75000, 80000, 90000,np.nan])
# # Bonus rates
# bonus_rates = np.array([.05,.08,.1,.12,np.nan])
#
# total_salary = base_salaries * (1+bonus_rates)
# # print(f'{total_salary}')
# print(total_salary)
# # print(np.mean(total_salary)) # mean function is not meant to handle nan values
# print(np.nanmean(total_salary)) # use nanmean function instead

