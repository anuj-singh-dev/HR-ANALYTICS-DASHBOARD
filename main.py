from src.data_loader import load_data
from src.preprocessing import (data_summary, 
                               check_missing_values, 
                               check_duplicates, 
                               statistical_summary)
from src.analysis import (attrition_summary, 
                          attrition_rate, 
                          employee_attrition_by_department, 
                          job_wise_attrition, 
                          salary_statistics, 
                          age_vs_attrition, 
                          monthly_income_vs_attrition, 
                          department_wise_attrition,
                          job_wise_attrition, 
                          gender_wise_attrition, 
                          overtime_wise_attrition, 
                          year_wise_attrition,
                          job_satisfaction_vs_attrition,
                          work_life_balance_vs_attrition)
from src.visualization import (plot_attrition, 
                               pie_attrition,
                               plot_monthly_income, 
                               plot_age_vs_attrition, 
                               plot_monthly_income_vs_attrition, 
                               plot_department_wise_attretion, 
                               plot_job_wise_attretion, 
                               plot_gender_wise_attretion, 
                               plot_overtime_wise_attretion,
                               plot_experience_vs_attrition,
                               plot_job_satisfaction_vs_attrition,
                               plot_work_life_balance_vs_attrition,
                               plot_correlation_heatmap,
                               plot_dashboard)

df = load_data("data/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv")

data_summary(df)
check_missing_values(df)
check_duplicates(df)
statistical_summary(df)
attrition_summary(df)
pie_attrition(df)
attrition_rate(df)
plot_attrition(df)
plot_monthly_income(df)
employee_attrition_by_department(df)
job_wise_attrition(df)
salary_statistics(df)
age_vs_attrition(df)
plot_age_vs_attrition(df)
monthly_income_vs_attrition(df)
plot_monthly_income_vs_attrition(df)
department_wise_attrition(df)
plot_department_wise_attretion(df)
job_wise_attrition(df)
plot_job_wise_attretion(df)
gender_wise_attrition(df)
plot_gender_wise_attretion(df)
overtime_wise_attrition(df)
plot_overtime_wise_attretion(df)
year_wise_attrition(df)
plot_experience_vs_attrition(df)
job_satisfaction_vs_attrition(df)
plot_job_satisfaction_vs_attrition(df)
work_life_balance_vs_attrition(df)
plot_work_life_balance_vs_attrition(df)
plot_correlation_heatmap(df)
plot_dashboard(df)
