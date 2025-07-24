# AI Job Listings Analysis

## Overview
This project analyzes a dataset of 15,000 AI job listings(2024) to uncover trends in job titles, salaries, experience levels, industries, and remote work. Using Python (pandas, numpy, matplotlib, seaborn), it performs exploratory data analysis (EDA) and generates visualizations to replicate a PowerBI dashboard, providing insights into salary distributions, skill demands, and more.

## Repository Structure
```
AI-Job-Listings-Analysis/
├── data/
│   └── ai_job_dataset.csv   # Dataset
|   └── ai_job_dataset.xlsx
├── analysis.py        # Analysis and visualization script
├── visualizations/        # Generated plots
├── screenshots/           # Screenshots of visualizations
├── README.md              # Documentation
└── requirements.txt       # Dependencies
```

## Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/<your-username>/AI-Job-Listings-Analysis.git
   cd AI-Job-Listings-Analysis
   ```

2. **Install Dependencies**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Place Dataset**:
   - Copy `ai_job_dataset.csv` into the `data/` directory.

4. **Run Analysis**:
   ```bash
   python analysis.py
   ```

## Requirements
Listed in `requirements.txt`:
```
pandas==2.2.2
numpy==1.26.4
matplotlib==3.8.4
seaborn==0.13.2
```

## Analysis
The script (`analysis.py`) generates:
- **Salary by Job Title**: Boxplot of salaries for top 10 job titles.
- **Salary by Experience Level**: Bar chart of average salaries (Entry, Mid, Senior, Expert).
- **Salary by Industry**: Bar chart for top 10 industries.
- **Remote Work Trends**: Pie chart of remote work ratios (0%, 50%, 100%).
- **Top Skills**: Bar chart of top 10 required skills.
- **Salary vs. Experience**: Scatter plot of salary vs. years of experience.

Visualizations are saved in `visualizations/` and displayed interactively.

## Screenshots
Below are key visualizations from the Python analysis and the PowerBI dashboard:

![Salary Distribution by Job Title](screenshots/salary_distribution.png)  
*Boxplot showing salary distributions for the top 10 AI job titles.*

![Remote Work Ratio Distribution](screenshots/remote_job_ratios.png)  
*Pie chart illustrating the prevalence of remote work options in AI jobs.*

![Top 10 demanded skills](screenshots/top_10_skills.png)  
*Bar chart illustrating the most required and demanded skills in AI jobs.*

![Salary distribution by years of experience](screenshots/salary_vs_yrs.png)  
*Scatter plot illustrating illustrating salary distribution versus years of experience in AI jobs.*

![PowerBI Dashboard](screenshots/powerbi_dashboard.png)  
*PowerBI dashboard summarizing key metrics, aligned with Python visualizations.*

## Key Insights
- **High Salaries**: Machine Learning Engineers and Principal Data Scientists earn median salaries above $150,000 USD.
- **Experience Impact**: Senior/Expert roles earn 30–50% more than Entry/Mid-level roles.
- **Top Industries**: Technology and Finance lead in salaries.
- **Remote Work**: ~40% of jobs are fully remote.
- **In-Demand Skills**: Python and TensorFlow appear in over 50% of listings.
 
