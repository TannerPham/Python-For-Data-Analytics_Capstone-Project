# Overview

Welcome to my analysis of the data job market in the SEA (South East Asia) region, focusing only on data analyst roles. This project was created to put all my Python knowledge that I have just accquired in the Python Course by Luke Barrouse into good practice as well as to understand the job market more effectively. The project delves into the top-paying and in-demand skills to help find optimal job opportunities for data analysts.

The data sourced from [Luke Barousse's Python Course](https://lukebarousse.com/python) which provides a foundation for my analysis, containing detailed information on job titles, working modes, salaries, perks, working locations, and required skills. Through a series of Python scripts, I managed to find answers for key questions such as what is the most demanded skills, what is the salary trends, and how can we identify the intersection of demand and salary in the data analytics sector.

# Key Questions

Below are the questions needed to be answered in the project:

1. What are the top 5 in-demand skills for the top 3 most popular data roles in SEA countries?
2. How are in-demand skills trending for Data Analysts in SEA countries?
3. What are the most well-paid data jobs and data skills in SEA countries?
4. What are the optimal skills for data analysts to learn? (High Demand AND High Paying)
5. Which country in the SEA region has the highest demand of Data Analyst positions as well as offer the most attractive salary for Data Analysts?  

# Tools of Choice

For my extensive analysis into the data analyst job market in the SEA region, I harnessed the power of several key tools:

- **Python:** The backbone of the analysis process which helps to dissect the raw data and find critical insights. The following Python libraries were used:
    - **Pandas Library:** This was used to analyze the data. 
    - **Matplotlib Library:** This was used to visualize the data.
    - **Seaborn Library:** This was used for customizing advanced visuals. 
- **Jupyter Notebooks:** This tool is used to run Python scripts as well as to include notes and analysis along the way for reference purpose.
- **Visual Studio Code:** It is used for executing the Python scripts.
- **Git & GitHub:** This is an essential tool for version controling and online-sharing the Python code and analysis, enabling collaboration and changes tracking capabilities.

# Data Preparation and Cleanup

This section outlines the steps taken to prepare the data for analysis, ensuring data accuracy, integrity and usability.

## Import & Clean Up Data

Import necessary libraries and load the dataset from an online source, followed by initial data cleaning tasks to ensure data quality.

```python
# Importing Libraries
import ast
import pandas as pd
import seaborn as sns
from datasets import load_dataset
import matplotlib.pyplot as plt  

# Loading Data
dataset = load_dataset('lukebarousse/data_jobs')
df = dataset['train'].to_pandas()

# Data Cleanup
df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])
df['job_skills'] = df['job_skills'].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else x)
```

## Filter Jobs in the SEA region

To extensively focus the analysis on the SEA job market, filters were applied to the dataset, narrowing down to roles based in the ASEAN countries.

```python

SEA_countries = ['Vietnam', 'Thailand','Malaysia','Philippines','Indonesia','Laos','Cambodia','Myanmar','Singapore']

df_SEA = df[df['job_country']isin(SEA_countries)] 
# SEA stands for South East Asia

```

# Data Analysis

Each Jupyter notebook for this project aimed at investigating specific aspects of the data job market in the SEA (South East Asia) region. Here’s how I approached each question:

## 1. What are the top 5 in-demand skills for the top 3 most popular data roles in SEA countries?

To find the most demanded skills for the top 3 most popular data roles. I filtered out those positions by which ones were the most popular, and got the top 5 skills for these top 3 roles. This query highlights the most popular job titles and their top skills, showing which skills I should pay attention to depending on the role I'm targeting. 

View my notebook with detailed steps here: [02. Skills_Demand.ipynb](./Capstone%20Project/02.%20Skills_Demand.ipynb)

### Visualize Data

```python
fig, ax = plt.subplots(len(top_titles),1)
fig.set_size_inches((7,7))
for i, job_title in enumerate(top_titles):
    df_plot = df_skills_perc[df_skills_perc['job_title_short']== job_title].head(5) # filter for top 5 skills
    sns.barplot(
        data = df_plot,
        x='skill_percent',
        y='job_skills',
        ax = ax[i],
        hue = 'skill_percent',
        palette= 'dark:g_r' # r stands for reverse -> blue and reverse 
    )
    sns.despine()
    ax[i].legend('')
    ax[i].set_title(job_title)
    ax[i].set_ylabel('')
    ax[i].set_xlabel('')
    ax[i].set_xlim(0,70)
    if i != len(top_titles)-1: # this mean that if i = 2, the below code will not be executed
        ax[i].set_xticks([])
    
    #create a loop to place data labels onto the chart
    for n,v in enumerate(df_plot['skill_percent']):
        ax[i].text(x= v+1, y= n, s=f'{v:.0f}%', va= 'center') # va stands for vertical alignment, i guess

fig.suptitle('Likelihood of Skills Requested in SEA Job Postings', fontsize = 15)
fig.tight_layout(h_pad= 2)

plt.show()
```

### Results

![Likelihood of Skills Requested in the SEA region Job Postings](./Capstone%20Project/images/skills_demand_all_data_roles.png)


*Bar graph visualizing the likelihood of top 5 skills required in job postings of top 3 data roles in the SEA region*

### Insights:

- `SQL` is the most requested skill for Data Analysts and Data Engineer, this skill appears in over half the job postings for both roles. For Data Scientist, `Python` is the most sought-after skill, appearing in 59% of job postings.
- Data Engineers and Data Scientists require more specialized technical skills (AWS, Azure, Spark) compared to Data Analysts who are expected to be proficient in more general data management and analysis tools (Excel, Tableau, Power BI).
- `Python` is a versatile skill and it is always in the top 3 most sought-after skills in all these 3 roles , but this programming language is mostly demanded for Data Scientists Roles (59%).

## 2. How are in-demand skills trending for Data Analysts in SEA countries?

To find how data skills are trending in 2023 for Data Analysts, only data analyst positions are filtered and a pivot table was created with months of job postings on the row and skills on the column. The outcome is a table depicting top 5 skills of data analysts by month, showing how likely are the top skills going to be required in job postings throughout 2023.

View my notebook with detailed steps here: [03. Skills_Trend.ipynb](./Capstone%20Project/03.%20Skills_Trend.ipynb)

### Visualize Data

```python

from matplotlib.ticker import PercentFormatter

sns.lineplot(
    data= df_plot,
    dashes= False,
    palette= 'tab10'
)
sns.set_theme(style = 'ticks')
sns.despine()

plt.title('Trending Top Skills for Data Analysts in the SEA region')
plt.ylabel('Likelihood in Job Posting')
plt.xlabel('2023')
plt.legend().remove()

ax = plt.gca()
ax.yaxis.set_major_formatter(PercentFormatter(decimals=0))


for i in range(5):
    if df_plot.columns[i] != 'excel' :
        plt.text(x= 11.2, y= df_plot.iloc[-1,i]+0.5, s= df_plot.columns[i])
    else: 
        plt.text(x= 11.2, y= df_plot.iloc[-1,i]-0.7, s= df_plot.columns[i]) # df.columns returns the name of the column
plt.show()

```

### Results

![Trending Top Skills for Data Analysts in the SEA region](/Capstone%20Project/images/Skills_Trend_DA_SEA.png)  
*Bar graph visualizing the trending top skills for data analysts in the SEA region in 2023.*

### Insights:
- `SQL` remains the most consistently demanded skill throughout the year, although it shows a gradual decrease in demand from September to November but it goes up again in the final month of 2023.
- `Excel` experienced a significant decrease in demand in the fourth quarter, it is also surpassed by Python by the end of the year.
- `Python` show relatively unstable demand throughout the year with significant fluctuations in Q2 and a demand surge in the last month. However, this skill still has a upward trend on overall and replaces `Excel` to become the second most sought-after skills in job postings.
- `Power BI`, which is less demanded compared to the other skills, shows a slight upward trend towards the year's end. Meanwhile, the demand of `Tableau` has not increased much after the year 2023.

## 3. What are the most well-paid data jobs and what are the most well-paid data skills for Data Analysts in SEA countries?

### Salary Distributions of the top 6 popular jobs in SEA countries
To identify the highest-paying roles and skills, only jobs in the SEA countries were chosen and the median salary were calculated. But first, in order to get an idea of which jobs are paid the most, the salary distributions of the most common data jobs in the SEA region will be calculated.

View my notebook with detailed steps here: [04. Salary_Analysis.ipynb](./Capstone%20Project/04.%20Salary_Analysis.ipynb)

#### Visualize Data 

```python
sns.boxplot(
    data= df_SEA_top6,
    x= "salary_year_avg",
    y= "job_title_short",
    order= job_order # seaborn also has a param to organize the order of categories
)
sns.set_theme(style= 'ticks')
sns.despine()

plt.title('Salary Distributions in the SEA Region')
plt.xlabel('Yearly Salary (USD)')
plt.ylabel('')
ticks_x = plt.FuncFormatter(lambda y, pos: f'{int(y/1000)}K')
plt.gca().xaxis.set_major_formatter(ticks_x)
plt.show()

```

#### Results

![Salary Distributions of Data Jobs in SEA countries](/Capstone%20Project/images/Salary_Distributions_SEA.png)  
*Box plot visualizing the salary distributions for the top 6 data job titles across countries in the SEA region.*

#### Insights

- There's a significant variation in salary ranges across different job titles. Data Scientist positions tend to have the highest salary potential, with up to $200K annually; however, the median salary of Data Scientist positions is only the fifth highest (around $80K), indicating that only a few DS positions in SEA countries can be offered as much as 200k per year. 

- Data Analyst and Data Scientist roles show a much wider salary spectrum than others, suggesting that job seekers should be prepared for the pay disparity between different companies and different countries in those 2 roles. In contrast, Senior DA and DE roles demonstrate more consistency in salary, with a narrower range.

- The median salaries increase with the seniority and specialization of the roles. Senior roles (Senior Data Analyst, Senior Data Engineer) not only have higher median salaries but also larger differences in typical salaries, reflecting greater variance in compensation as responsibilities increase.

### Highest Paid & Most Demanded Skills for Data Analysts

Next, The analysis is narrowed down only on  Data Analyst roles. The objective of this section is to compare the highest-paid skills with the most in-demand skills, figuring out the kills that are simultaenously highly sought-after and well-paid

#### Visualize Data

```python

fig, ax = plt.subplots(2,1)

sns.barplot(
    data= df_DA_SEA_top_pay,
    x= 'median',
    y= 'job_skills',
    hue = 'median',
    palette= 'dark:b_r',
    ax= ax[0]
)

ax[0].set_xlabel('')
ax[0].set_ylabel('')
ax[0].legend('')
ax[0].set_xlim(0,170000)
ax[0].set_title('Top 10 Highest Paid Skills for Data Analysts')
ax[0].xaxis.set_major_formatter(plt.FuncFormatter(lambda x,pos: f'${int(x/1000)}K'))

sns.barplot(
    data= df_DA_SEA_pop_skills,
    x= 'median',
    y= 'job_skills',
    hue = 'median',
    palette= 'light:b',
    ax= ax[1]
)

ax[1].set_xlabel('Median Salary (USD)')
ax[1].set_ylabel('')
ax[1].legend('')
ax[1].set_xlim(0,170000)
ax[1].set_title('Top 10 Most In-Demand Skills for Data Analysts')
ax[1].xaxis.set_major_formatter(plt.FuncFormatter(lambda x,pos: f'${int(x/1000)}K'))

fig.tight_layout()

plt.show()

```

#### Results
Here's the breakdown of the highest-paid & most in-demand skills for data analysts in the US:

![The Highest Paid & Most In-Demand Skills for Data Analysts in the US](/Capstone%20Project/images/Top_Pay_vs_In_Demand.png)
*Two separate bar graphs visualizing the highest paid skills and most in-demand skills for data analysts in the US.*

#### Insights:

- The top graph shows specialized technical skills like `Golang`, `Redshift`, and `kafka` are associated with higher salaries, some reaching up to $165K, suggesting that advanced technical proficiency such as progamming languages and cloud-computing technology can increase earning potential in the SEA region.

- The bottom graph highlights that foundational skills like `Excel`, `Tableau`, `SQL` and `Looker` are the most in-demand, even though they may not offer the highest salaries. While `spark` has dominantly outnumbered in terms of median salary but the ocurrence of this skill in job postings is only 8, much lower than other skills in the graph. This demonstrates the importance of developing these fundamental core skills for landing the very first entry-level data jobs.

- Except for `spark`, there's a clear distinction between the skills that are highest paid and those that are most in-demand. Data analysts aiming to maximize their career potential should consider focusing on the core skills that are currently in demand in the earlier career stage and develop high-paying skills in the later stage based on the fact that Senior DA and Senior DE in SEA countries are the roles which are paid the most in terms of median salary in 2023.

## 4. What are the most optimal skills to learn for Data Analysts in the SEA region?

To identify the most optimal skills to learn (the ones that are the highest paid and the highly sought-after), the percent of skill demand and the median salary of these skills were calculated so as to easily identify which are the most optimal skills to learn as Data Analysts working in SEA countries. 

View my notebook with detailed steps here: [05. Optimal_Skills.ipynb](./Capstone%20Project/05.%20Optimal_Skills.ipynb).

#### Visualize Data

```python
from adjustText import adjust_text
import matplotlib.pyplot as plt

plt.scatter(df_DA_skills_high_demand['skill_percent'], df_DA_skills_high_demand['median_salary'])
plt.show()

```

#### Results

![Most Optimal Skills for Data Analysts in the US](/Capstone%20Project/images/Optimal_skills_no_group.png)    
*A scatter plot visualizing the most optimal skills (high paying & high demand) for data analysts in SEA countries.*

#### Insights:

- The skill `spark` appears to have the highest median salary of over $130K, despite being less common in job postings. This suggests a high value placed on specialized large-scale data analytics skills within the data analyst profession in the SEA region.

- More commonly required skills like `SQL` and `Python` have a large presence in job listings but lower median salaries compared to foundational skills like `excel` or `tableau`, which not only have higher salaries but are also moderately prevalent in job listings.

- Skills such as `power bi`, `r`, `excel`and `tableau` are towards the middle part of the salary spectrum (around $90K-$100K) while also being fairly common in job listings (above 20%), indicating that proficiency in these tools can result in the better likelihood of earning job opportunities in in the data analytics industry across SEA countries  

### Visualizing Different Techonologies

Let's visualize the different technologies as well in the graph. Color labels will be added based on the technology (e.g., {Programming: Python})

#### Visualize Data

```python
# Create the scatter plot

sns.scatterplot(
    data = df_plot,
    x = 'skill_perc',
    y= 'median_salary',
    hue = 'technology'
)
sns.despine()

# Prepare texts for adjustText
texts=[]
for i, txt in enumerate(df_plot['skills']):
    texts.append(plt.text(df_plot['skill_perc'].iloc[i],df_plot['median_salary'].iloc[i], txt))

# Adjust text to avoid overlaps
adjust_text(texts,arrowprops=dict(arrowstyle='->',color = 'red'))

# Set axis labels, title
plt.xlabel('Percent of DA jobs') 
plt.ylabel('Median Yearly Salary')
plt.title(f'Most Optimal Skills for Data Analysts in SEA countries')

# Format X&Y axes' tick values
ax = plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y,pos: f'${int(y/1000)}K'))
from matplotlib.ticker import PercentFormatter
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x,pos: f'{int(x)}%'))

plt.show()

```

#### Results

![Most Optimal Skills for Data Analysts in SEA countries with Coloring by Technology](/Capstone%20Project/images/Optimal_skills.png)  
*A scatter plot visualizing the most optimal skills (high paying & high demand) for data analysts in the SEA region with color labels for different types of technology.*

#### Insights:

- The colored scatter plot shows that most of the `programming` skills (colored blue) tend to cluster at higher demand compared to other categories, indicating that programming expertise might offer greater job opportunities within the data analytics field.

- The `librabries` skills (colored green), such as Spark, are associated with some of the highest salaries among required tools of a data analyst. This indicates a significant  valuation for large-scale data-procesing and analytics expertise in the industry.

- The skills relating to `analyst_tools` (colored orange), including Tableau, Power BI, Excel and Looker, offer competitive salaries (above $95K) and half of them are relatively prevalent in job postings. This shows that visualization and data analysis softwares are crucial for current DA roles. This category not only has good salaries but is also versatile across different types of data tasks (querying, wrangling, visualizing, presentation).

## 5. Which country in the SEA region has the highest demand of Data Analyst positions as well as offer the most attractive salary for Data Analysts??



View my notebook with detailed steps here: [06. Countries_Demand&Pay.ipynb](./Capstone%20Project/06.%20Countries_Demand&Pay.ipynb).

#### Visualize Data

```python
fig, ax = plt.subplots(2,1)

# Create the job demand plot
sns.barplot(
    data = df_DA_SEA_demand,
    x='job_perc',
    y='job_country',
    ax = ax[0],
    hue = 'job_perc',
    palette= 'dark:b_r'
)
# Format the axes and add data labels
ax[0].legend('')
ax[0].xaxis.set_major_formatter(plt.FuncFormatter(lambda x,pos : f'{int(x)}%'))
for i, num in enumerate(df_DA_SEA_demand['job_perc']):
    ax[0].text(x= num, y = i + 0.2, s= num)
ax[0].set_xlabel('Percent of Job Postings')
ax[0].set_ylabel('')
ax[0].set_title('Proportion of Data Analyst Jobs in SEA countries')

# Create the salary plot
sns.barplot(
    data= df_DA_SEA_pay,
    x= 'median_salary',
    y='job_country',
    ax= ax[1],
    hue = 'median_salary',
    palette= 'dark:g_r'
)
# Format the axes
ax[1].invert_yaxis()
ax[1].legend('')
ax[1].xaxis.set_major_formatter(plt.FuncFormatter(lambda x,pos : f'${int(x/1000)}K'))
ax[1].set_xlim(0,120000)
ax[1].set_xlabel('Median Annual Salary')
ax[1].set_ylabel('')
ax[1].set_title('Median Income for Data Analysts in SEA countries')

# Modify layout of the figure
sns.despine()
fig.tight_layout()

```

#### Results

![Job Demand and Median Salary in SEA countries](/Capstone%20Project/images/SEA_countries_demand_pay.png)    
*Two bar charts visualizing the job demand in each SEA country and the median salary for data analysts across SEA countries.*

#### Insights:

-  There are strong demand for DA positions in Singapore (40.83%), Philipines(29.34%) compared to the rest of SEA countries. Meanwhile, there are very few DA job postings in the last 4 countries when the demand in all these countries combined only take up less than 0.3% of the total job postings in the SEA region.

- In terms of compensation, Thailand is offering the highest median income for Data Analys, up to $110K despite the fact that the demand proportion of this country is only 9%, following after is Singapore with the median salary up to $100K and it should be noted that DA jobs are most demanded in this country. On the other hand, there is no salary data for the bottom 3 countries in job demand (Myanmar, Laos, Brunei) so it can't be concluded about the median salary that those countries have to offer given that the demand is really low.


# General Insights

This project provided several general insights into the data job market in the SEA region for aspiring Data Analysts:

- **Skill Demand and Salary Correlation**: There is no clear correlation between the demand for specific skills and the salaries these skills command. Advanced and specialized skills like `Spark` often lead to higher salaries but farily scarce in demand, while more common data analysis skills such as `Python`,`SQL`, `Excel`, `Tableau` are way more prevalent in job listings of the SEA region and the median salary is also really attractive considering the living standards in the SEA countries.

- **Market Trends**: There are changing trends in demand of different data skills, highlighting the dynamic nature of the data job market in SEA countries. Keeping up with these trends is essential for career growth in this industry

- **Economic Value of Skills**: 
It is clear that in-demand and foundational skills are essential for entry-level analysts to land the very first data jobs. However, in the long run, understanding which skills are both in-demand and well-compensated can guide data analysts in choosing to learn the optimal skills which is both beneficial to the career path and the economic returns.

- **Country of Choice**: Among countries in the SEA region, there is a distinguishable difference in the job demand but the income is not really different. Singapore is undoubtedly the go-to country to work as Data Analysts with high demand and great compensation while other countries such as Thailand and Cambodia offer such attractive income but the demand is not comparable with that of Singapore.  

# Lessons Learned

Throughout this project, I deepened my understanding of the data analyst job market and enhanced my technical skills in Python, especially in data manipulation and visualization. Here are a few specific things I learned:

- **Advanced Python Usage**: Utilizing libraries such as Pandas for data manipulation, Seaborn and Matplotlib for data visualization, and other libraries helped perform complex data analysis tasks more efficiently.

- **Data Cleaning Importance**: Thorough data cleaning and preparation are crucial before any analysis can be conducted, because it ensures the data integrity and the accuracy of insights derived from the data.

- **Strategic Skill Analysis**: The project emphasized the importance of aligning one's skills with market demand. Understanding the relationship between skill demand, salary ranges, and job availability allows for more strategic career planning in the data analytics industry.

# Challenges

This project was not without its challenges, but it provided good learning opportunities:

- **Data Inconsistencies**: Handling missing or inconsistent data entries requires careful consideration and thorough data-cleaning techniques to ensure the data integrity and data quality which cement the validity of the analysis.

- **Complex Data Visualization**: Designing  visually-compelling representations of complex datasets using programming languae like Python was intuitively hard to execute but critical for conveying insights clearly and effectivly.

- **Balancing Breadth and Depth**: Deciding how deeply to dive into each analysis while maintaining a broad overview of the data landscape required constant balancing to ensure comprehensive coverage without getting lost in details.

- **Adapting to new tools**: It's quite uneasy to learn how to log and comment on the Python code with Jupiter Notebook and present the project using Visual Code Studio. Besides, Git is also a new concept that requires practical exercises to really understand how it works.

# Conclusion

This exploration into the data analyst job market in the SEA region in 2023 has been incredibly informative, highlighting the critical skills and trends that shape this emerging field as well as suggesting the most in-demand and well-paid country to work as Data Analysts across SEA countries. The insights provide actionable guidance for anyone looking to advance their career in data analytics. As the job market in 2024 continues to be unexectedly volatile, further analysis will be needed for data job-seekers to stay updated with the latest trend. This project is a foundation for future explorations and underscores the paramount importance of continuous learning and adaptation in the data field.


