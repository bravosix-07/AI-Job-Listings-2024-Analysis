import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set Seaborn theme for consistent, professional styling
sns.set(style="whitegrid", context="notebook", font="Arial", font_scale=1.2)

# Setting up output directory for visualizations
if not os.path.exists('visualizations'):
    os.makedirs('visualizations')

# Loading the dataset
try:
    df = pd.read_csv('data/ai_job_dataset.csv')
except FileNotFoundError:
    print("Error: 'data/ai_job_dataset.csv' not found. Please ensure the file is in the 'data/' directory.")
    exit(1)

# Preprocessing: Handle missing or invalid data
df = df.dropna(subset=['salary_usd', 'job_title', 'experience_level', 'industry'])
df['salary_usd'] = pd.to_numeric(df['salary_usd'], errors='coerce').fillna(df['salary_usd'].median())
df['years_experience'] = pd.to_numeric(df['years_experience'], errors='coerce').fillna(df['years_experience'].median())
df['remote_ratio'] = df['remote_ratio'].astype(int)

# Convert date columns to datetime (assuming standard format in CSV)
df['posting_date'] = pd.to_datetime(df['posting_date'], errors='coerce')
df['application_deadline'] = pd.to_datetime(df['application_deadline'], errors='coerce')

# Analysis 1: Salary Distribution by Job Title (Boxplot)
top_jobs = df['job_title'].value_counts().head(10).index
plt.figure(figsize=(14, 7))
sns.boxplot(x='job_title', y='salary_usd', hue='job_title', data=df[df['job_title'].isin(top_jobs)], 
            palette="Blues", linewidth=1.5, fliersize=3, legend=False)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.title('Salary Distribution by Job Title (Top 10)', fontsize=14, pad=15)
plt.xlabel('Job Title', fontsize=12)
plt.ylabel('Salary (USD)', fontsize=12)
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('visualizations/salary_by_job_title.png', dpi=300)
plt.show()
plt.close()

# Analysis 2: Average Salary by Experience Level (Bar Chart)
exp_salary = df.groupby('experience_level')['salary_usd'].mean().sort_values()
plt.figure(figsize=(10, 6))
sns.barplot(x=exp_salary.index, y=exp_salary.values, hue=exp_salary.index, palette="viridis", legend=False)
plt.title('Average Salary by Experience Level', fontsize=14, pad=15)
plt.xlabel('Experience Level', fontsize=12)
plt.ylabel('Average Salary (USD)', fontsize=12)
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
for i, v in enumerate(exp_salary.values):
    ax.text(i, v + 1000, f'${v:,.0f}', ha='center', fontsize=10)
plt.tight_layout()
plt.savefig('visualizations/salary_by_experience_level.png', dpi=300)
plt.show()
plt.close()

# Analysis 3: Average Salary by Industry (Bar Chart)
top_industries = df['industry'].value_counts().head(10).index
industry_salary = df[df['industry'].isin(top_industries)].groupby('industry')['salary_usd'].mean().sort_values()
plt.figure(figsize=(14, 7))
sns.barplot(x=industry_salary.index, y=industry_salary.values, hue=industry_salary.index, palette="viridis", legend=False)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.title('Average Salary by Industry (Top 10)', fontsize=14, pad=15)
plt.xlabel('Industry', fontsize=12)
plt.ylabel('Average Salary (USD)', fontsize=12)
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
for i, v in enumerate(industry_salary.values):
    ax.text(i, v + 1000, f'${v:,.0f}', ha='center', fontsize=10)
plt.tight_layout()
plt.savefig('visualizations/salary_by_industry.png', dpi=300)
plt.show()
plt.close()

# Analysis 4: Remote Work Ratio Distribution (Pie Chart)
remote_counts = df['remote_ratio'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(remote_counts, labels=[f'{int(x)}%' for x in remote_counts.index], 
        autopct='%1.1f%%', startangle=140, colors=sns.color_palette("Set2", len(remote_counts)),
        textprops={'fontsize': 12}, shadow=True)
plt.title('Distribution of Remote Work Ratios', fontsize=14, pad=15)
plt.tight_layout()
plt.savefig('visualizations/remote_ratio_distribution.png', dpi=300)
plt.show()
plt.close()

# Analysis 5: Top Required Skills (Bar Chart)
skills = df['required_skills'].str.split(', ', expand=True).stack().value_counts().head(10)
plt.figure(figsize=(12, 7))
sns.barplot(x=skills.values, y=skills.index, hue=skills.index, palette="viridis", legend=False)
plt.title('Top 10 Required Skills', fontsize=14, pad=15)
plt.xlabel('Frequency', fontsize=12)
plt.ylabel('Skill', fontsize=12)
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
for i, v in enumerate(skills.values):
    ax.text(v + 50, i, f'{v:,}', va='center', fontsize=10)
plt.tight_layout()
plt.savefig('visualizations/top_skills.png', dpi=300)
plt.show()
plt.close()

# Analysis 6: Salary vs. Years of Experience (Scatter Plot)
plt.figure(figsize=(10, 6))
sns.scatterplot(x='years_experience', y='salary_usd', data=df, color='#1f77b4', alpha=0.5, s=100)
plt.title('Salary vs. Years of Experience', fontsize=14, pad=15)
plt.xlabel('Years of Experience', fontsize=12)
plt.ylabel('Salary (USD)', fontsize=12)
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('visualizations/salary_vs_experience.png', dpi=300)
plt.show()
plt.close()

# Printing key insights
print("Key Insights:")
print(f"Average salary: ${df['salary_usd'].mean():,.2f}")
print(f"Most common job title: {df['job_title'].mode()[0]}")
print(f"Most common skill: {skills.index[0]}")
print(f"Percentage of fully remote jobs: {(df['remote_ratio'] == 100).mean() * 100:.1f}%")