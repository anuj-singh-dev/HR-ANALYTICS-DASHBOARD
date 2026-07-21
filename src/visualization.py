import matplotlib.pyplot as plt
import seaborn as sns

def plot_attrition(df):
    """"
    Plot Employees Attrition Counts
    """

    attrition = df["Attrition"].value_counts()

    plt.figure(figsize=(8,5))
    plt.bar(attrition.index, attrition.values)

    plt.title("Employees Attrition", fontsize=14, fontweight="bold")
    plt.xlabel("Attrition", fontsize=12, fontweight="bold")
    plt.ylabel("Number Of Employees", fontsize=12, fontweight="bold")
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)    
    plt.savefig("reports/charts/attrition_distribution.png")
    plt.show()

def pie_attrition(df):
    """"
    Plot Pie  Employees Attrition Counts
    """

    attrition = df["Attrition"].value_counts()
    plt.figure(figsize=(8,5))

    plt.pie(
        attrition.values,
        labels=attrition.index,
        autopct="%1.1f%%")

    plt.title("Attrition Distribution")  
    plt.savefig("reports/charts/pie_attrition_distribution.png")  
    plt.show()

def plot_monthly_income(df):
    """
    Plot Monthly Salary
    """
    
    monthly_income = df["MonthlyIncome"]
    plt.figure(figsize=(8,5))

    plt.hist(monthly_income, bins = 20, color= "green", edgecolor = "black")
    plt.title("Distribution of Monthly Employee Income", fontsize=14, fontweight="bold")
    plt.xlabel("Monthly Income", fontsize=12, fontweight="bold")
    plt.ylabel("Number of Employees", fontsize=12, fontweight="bold")
    plt.savefig("reports/charts/monthly_salary_atrrition.png")
    plt.show()

def plot_age_vs_attrition(df):
    """
    Plot Relation between Age And Attrition
    """
    yes_attrition = df.loc[df["Attrition"] =="Yes", "Age"]
    no_attrition = df.loc[df["Attrition"] == "No", "Age"]
    plt.figure(figsize=(8,5))

    plt.boxplot([yes_attrition, no_attrition],
                tick_labels=["Yes","No"])
    
    plt.title("Age Distribution by Attrition Status", fontsize=14, fontweight="bold")
    plt.xlabel("Attrition", fontsize=12, fontweight="bold")
    plt.ylabel("Emplyees Age", fontsize=12, fontweight="bold")
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.savefig("reports/charts/age_atrrition.png")
    plt.show()

def plot_monthly_income_vs_attrition(df):
    """
    Plot relation between age and attrition
    """

    yes_attrition = df.loc[df["Attrition"] =="Yes", "MonthlyIncome"]
    no_attrition = df.loc[df["Attrition"] == "No", "MonthlyIncome"]
    plt.figure(figsize=(8,5))

    plt.boxplot([yes_attrition, no_attrition],
                tick_labels=["yes","No"])
    plt.title("Salary Distribution by Attrition Status", fontsize=14, fontweight="bold")
    plt.xlabel("No Attrition", fontsize=12, fontweight="bold")
    plt.ylabel("Monthly Income", fontsize=12, fontweight="bold")
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.savefig("reports/charts/monthly_income_atrrition.png")
    plt.show()

def plot_department_wise_attretion(df):
    """
    Plot the relation between department and attrition
    """

    yes_attrition = df.loc[df["Attrition"] == "Yes", "Department"].value_counts()
    
    total_employees = df["Department"].value_counts()

    attrition_rate = (yes_attrition/total_employees)*100

    plt.figure(figsize =(8,5))
    plt.bar(attrition_rate.index, attrition_rate.values)

    plt.title("Department_Wise Attrition Rate", fontsize=14, fontweight="bold")
    plt.xlabel("Department", fontsize=12, fontweight="bold")
    plt.ylabel("Attrition Rate (%)", fontsize=12, fontweight="bold")
    plt.grid(axis="y", linestyle = "--", alpha = 0.6)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.savefig("reports/charts/department_atrrition.png")
    plt.show()

def plot_job_wise_attretion(df):
    """
    Plot the relation between job and attrition
    """

    yes_attrition = df.loc[df["Attrition"] == "Yes", "JobRole"].value_counts()
    
    total_job_role = df["JobRole"].value_counts()

    attrition_rate = (yes_attrition/total_job_role)*100

    plt.figure(figsize =(8,5))
    plt.bar(attrition_rate.index, attrition_rate.values)

    plt.title("Job-Wise Attrition Rate", fontsize=14, fontweight="bold")
    plt.xlabel("Job Role", fontsize=12, fontweight="bold")
    plt.ylabel("Attrition Rate (%)", fontsize=12, fontweight="bold")
    plt.xticks(rotation = 45)
    plt.grid(axis="y", linestyle = "--", alpha = 0.6)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.savefig("reports/charts/job_atrrition.png")
    plt.show()

def plot_gender_wise_attretion(df):
    """
    Plot the relation between gender and attrition
    """

    yes_attrition = df.loc[df["Attrition"] == "Yes", "Gender"].value_counts()
    
    total_gender = df["Gender"].value_counts()

    attrition_rate = (yes_attrition/total_gender)*100

    plt.figure(figsize =(8,5))
    plt.bar(attrition_rate.index, attrition_rate.values)

    plt.title("Gender-Wise Attrition Rate", fontsize=14, fontweight="bold")
    plt.xlabel("Gender", fontsize=12, fontweight="bold")
    plt.ylabel("Attrition Rate (%)", fontsize=12, fontweight="bold")
    plt.grid(axis="y", linestyle = "--", alpha = 0.6)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.savefig("reports/charts/gender_atrrition.png")
    plt.show()

def plot_overtime_wise_attretion(df):
    """
    Plot the relation between overtime and attrition
    """

    yes_attrition = df.loc[df["Attrition"] == "Yes", "OverTime"].value_counts()

    total_employees = df["OverTime"].value_counts()

    attrition_rate = (yes_attrition/total_employees)*100

    plt.figure(figsize =(8,5))
    plt.bar(attrition_rate.index, attrition_rate.values, color = "green", edgecolor = "black")

    plt.title("Overtime-Wise Attrition Rate", fontsize=14, fontweight="bold")
    plt.xlabel("Overtime", fontsize=12, fontweight="bold")
    plt.ylabel("Attrition Rate (%)", fontsize=12, fontweight="bold")
    plt.grid(axis="y", linestyle = "--", alpha = 0.6)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.savefig("reports/charts/overtime_atrrition.png")
    plt.show()

def plot_experience_vs_attrition(df):
    """
    Plot Relation between Experience And Attrition
    """
    yes_attrition = df.loc[df["Attrition"] == "Yes", "TotalWorkingYears"].value_counts()
    no_attrition = df.loc[df["Attrition"] == "No", "TotalWorkingYears"].value_counts()
    plt.figure(figsize=(8,5))

    plt.boxplot([yes_attrition, no_attrition],
                tick_labels=["Yes","No"])
    
    plt.title("Experience Distribution by Attrition Status", fontsize=14, fontweight="bold")
    plt.xlabel("Attrition", fontsize=12, fontweight="bold")
    plt.ylabel("Emplyees Experience", fontsize=12, fontweight="bold")
    plt.grid(axis="y", linestyle = "--", alpha = 0.6)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.savefig("reports/charts/experience_atrrition.png")
    plt.show()

def plot_job_satisfaction_vs_attrition(df):
    """
    Plot Relation between job satisfaction And Attrition
    """

    yes_attrition = df.loc[df["Attrition"] == "Yes", "JobSatisfaction"].value_counts()

    total_employees  = df["JobSatisfaction"].value_counts().sort_index()

    attrition_rate = (yes_attrition/total_employees)*100

    plt.figure(figsize=(8,5))
    plt.bar(attrition_rate.index , attrition_rate.values)
    plt.title("Job Satisfaction vs Attrition Rate", fontsize=14, fontweight="bold")
    plt.xlabel("Job Satisfaction", fontsize=12, fontweight="bold")
    plt.ylabel("Attrition Rate (%)", fontsize=12, fontweight="bold")

    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.savefig("reports/charts/job_satisfaction_atrrition.png")
    plt.show()

def plot_work_life_balance_vs_attrition(df):
    """
    Plot Relation between work life balance  And Attrition
    """

    yes_attrition = df.loc[df["Attrition"] == "Yes", "WorkLifeBalance"].value_counts()

    total_employees  = df["WorkLifeBalance"].value_counts().sort_index()

    attrition_rate = (yes_attrition/total_employees)*100

    plt.figure(figsize=(8,5))
    plt.bar(attrition_rate.index , attrition_rate.values)
    plt.title("Work-Life Balance vs Attrition Rate", fontsize=14, fontweight="bold")
    plt.xlabel("WorK-Life Balance", fontsize=12, fontweight="bold")
    plt.ylabel("Attrition Rate (%)", fontsize=12, fontweight="bold")

    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.savefig("reports/charts/life_balance_atrrition.png")
    plt.show()

def plot_correlation_heatmap(df):
    """
    plot the correlation heatmap of numerical feature
    """

    numeric_df = df.select_dtypes(include = ["number"])

    correlation_matrix = numeric_df.corr()

    plt.figure(figsize=(8,5))

    sns.heatmap(correlation_matrix,
                annot=True,
                cmap="coolwarm",
                fmt=".2f",
                linewidths=0.5)
    
    plt.title("Correlation Heatmap of Numerical Features", fontsize=14, fontweight="bold")
    plt.xticks(rotation=45, ha="right", fontsize=10)
    plt.yticks(fontsize=10)
    plt.tight_layout()
    plt.savefig("reports/charts/heatmap_atrrition.png")
    plt.show()


# creating main dashboard
def plot_dashboard(df):
    plt.figure(figsize=(18, 10))

    # CHART 1

    plt.subplot(2, 3, 1)
    attrition = df["Attrition"].value_counts()

    plt.pie(
        attrition.values,
        labels=attrition.index,
        autopct="%1.1f%%")

    plt.title("Attrition Distribution", fontsize=14, fontweight="bold")

    # CHART 2

    plt.subplot(2,3,2)
    monthly_income = df["MonthlyIncome"]

    plt.hist(monthly_income, bins = 20, color= "green", edgecolor = "black")
    plt.title("Distribution of Monthly Employee Income", fontsize=14, fontweight="bold")
    plt.xlabel("Monthly Income", fontsize=12, fontweight="bold")
    plt.ylabel("Number of Employees", fontsize=12, fontweight="bold")
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)

    # CHART 3
    plt.subplot(2,3,3)
    yes_attrition = df.loc[df["Attrition"] == "Yes", "Department"].value_counts()
    
    total_employees = df["Department"].value_counts()

    attrition_rate = (yes_attrition/total_employees)*100

    plt.bar(attrition_rate.index, attrition_rate.values)

    plt.title("Department_Wise Attrition Rate", fontsize=14, fontweight="bold")
    plt.xlabel("Department", fontsize=12, fontweight="bold")
    plt.ylabel("Attrition Rate (%)", fontsize=12, fontweight="bold")
    plt.grid(axis="y", linestyle = "--", alpha = 0.6)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)

    # CHART 4
    plt.subplot(2,3,4)
    yes_attrition = df.loc[df["Attrition"] == "Yes", "OverTime"].value_counts()

    total_employees = df["OverTime"].value_counts()

    attrition_rate = (yes_attrition/total_employees)*100

    plt.bar(attrition_rate.index, attrition_rate.values, color = "green", edgecolor = "black")

    plt.title("Overtime-Wise Attrition Rate", fontsize=14, fontweight="bold")
    plt.xlabel("Overtime", fontsize=12, fontweight="bold")
    plt.ylabel("Attrition Rate (%)", fontsize=12, fontweight="bold")
    plt.grid(axis="y", linestyle = "--", alpha = 0.6)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)

    # CHART 5
    plt.subplot(2,3,5)
    yes_attrition = df.loc[df["Attrition"] == "Yes", "JobRole"].value_counts()
    
    total_job_role = df["JobRole"].value_counts()

    attrition_rate = (yes_attrition/total_job_role)*100

    plt.bar(attrition_rate.index, attrition_rate.values)

    plt.title("Job-Wise Attrition Rate", fontsize=14, fontweight="bold")
    plt.xlabel("Job Role", fontsize=12, fontweight="bold")
    plt.ylabel("Attrition Rate (%)", fontsize=12, fontweight="bold")
    plt.xticks(rotation=30, ha="right", fontsize=9)
    plt.grid(axis="y", linestyle = "--", alpha = 0.6)


    # CHART 6
    plt.subplot(2,3,6)
    yes_attrition = df.loc[df["Attrition"] == "Yes", "WorkLifeBalance"].value_counts()

    total_employees  = df["WorkLifeBalance"].value_counts().sort_index()

    attrition_rate = (yes_attrition/total_employees)*100

    plt.bar(attrition_rate.index , attrition_rate.values)
    plt.title("Work-Life Balance vs Attrition Rate", fontsize=14, fontweight="bold")
    plt.xlabel("WorK-Life Balance", fontsize=12, fontweight="bold")
    plt.ylabel("Attrition Rate (%)", fontsize=12, fontweight="bold")
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.grid(axis="y", linestyle="--", alpha=0.6)

    plt.suptitle(
    "HR Analytics Dashboard",
    fontsize=18,
    fontweight="bold")

    plt.tight_layout(rect=[0, 0, 1, 0.95])

    # Save The Dashboard
    plt.savefig(
    "reports/charts/dashboard.png",
    dpi=300,
    bbox_inches="tight"
)
    
    # Displaying the main dashboard
    plt.show()

