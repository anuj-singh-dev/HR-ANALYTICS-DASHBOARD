def attrition_summary(df):
    """
    Displaying the count of employees who stayed and left the company
    """

    print("\n ====Attrition Summary====")
    print(df["Attrition"].value_counts())

def attrition_rate(df):
    """
    calculate and display attrition rate
    """

    print("\n ====Attrition Rate====")
    total_employees = len(df)
    employees_left = df[df["Attrition"]=="Yes"].shape[0]

    rate = (employees_left/total_employees)*100

    print(f"Total Employees:{total_employees}")
    print(f"Employees Left:{employees_left}")
    print(f"Attrition Rate:{rate:.2f}%")

def employee_attrition_by_department(df):
    """
    Calculate and display the  attrition by department
    """

    print("\n ====Department-wise Attrition====")
    department_wise_attrition =  df.loc[df["Attrition"]== "Yes","Department"].value_counts()
    print(department_wise_attrition) 


def job_wise_attrition(df):
    """
    Calculate the job wise attrition
    """

    print("\n ====Job-Wise Attrition====")
    job_wise_attrition = df.loc[df["Attrition"]=="Yes", "JobRole"].value_counts()
    print(job_wise_attrition)

def salary_statistics(df):
    """
    Calculate descriptive statistics for employee monthly income.
    """

    print("\n ==== Salary Statistics ====")
    monthly_income = df["MonthlyIncome"]
    print(monthly_income.describe().round(2))


def age_vs_attrition(df):
    """
    Calculate the relationship between age and attrition
    """

    print("\n ====Relation between age and attrition====")
    yes_attrition = df.loc[df["Attrition"] =="Yes", "Age"]
    no_attrition = df.loc[df["Attrition"] == "No", "Age"]
    print(f"Attrition = Yes \n {yes_attrition.describe().round(2)}")
    print(f"Attrition = No \n {no_attrition.describe().round(2)}")


def monthly_income_vs_attrition(df):
    """
    Calculate the relationship between Monthly Income and attrition
    """

    print("\n==== Relationship between Monthly Income and Attrition ====")
    yes_attrition = df.loc[df["Attrition"] =="Yes", "MonthlyIncome"]
    no_attrition = df.loc[df["Attrition"] == "No", "MonthlyIncome"]
    print(f"Attrition = Yes \n {yes_attrition.describe().round(2)}")
    print(f"Attrition = No \n {no_attrition.describe().round(2)}")

def department_wise_attrition(df):
    """
    Calculate the relationship between department and attrition
    """

    print("\n ==== Relationship between Department and attrition ====")
    yes_attrition = df.loc[df["Attrition"] == "Yes", "Department"].value_counts()
    
    total_employees = df["Department"].value_counts()

    attrition_rate = (yes_attrition/total_employees)*100
    print(attrition_rate.round(2))

    highest_department = attrition_rate.idxmax()

    print("\n Department with Highest Attrition Rate")
    print(f"{highest_department}={attrition_rate.max():.2f}%")

def job_wise_attrition(df):
    """
    Calculate the job role attration
    """

    
    print("\n ==== Relationship between Job role and attrition ====")
    yes_attrition = df.loc[df["Attrition"] == "Yes", "JobRole"].value_counts()
    
    total_job_role = df["JobRole"].value_counts()

    attrition_rate = (yes_attrition/total_job_role)*100
    print(attrition_rate.round(2))

    highest_job_role = attrition_rate.idxmax()

    print("\n Job with Highest Attrition Rate")
    print(f"{highest_job_role}={attrition_rate.max():.2f}%")

def gender_wise_attrition(df):
    """
    Calculate the Gender Wise Attrition
    """

    print("\n ==== Relationship between Gender and attrition ====")
    yes_attrition = df.loc[df["Attrition"] == "Yes", "Gender"].value_counts()
    
    total_gender = df["Gender"].value_counts()

    attrition_rate = (yes_attrition/total_gender)*100
    print(attrition_rate.round(2))

    highest_gender = attrition_rate.idxmax()

    print("\n Gender with Highest Attrition Rate")
    print(f"{highest_gender}={attrition_rate.max():.2f}%")

def overtime_wise_attrition(df):
    """
    Calculate the overtime wise attrition
    """

    print("\n ==== Overtime Wise Attrition ====")
    yes_attrition = df.loc[df["Attrition"] == "Yes", "OverTime"].value_counts()

    total_employees = df["OverTime"].value_counts()

    attrition_rate = (yes_attrition/total_employees)*100

    print(attrition_rate.round(2))

    highest = attrition_rate.idxmax()

    print("\n Highest Attrition Rate")
    print(f"{highest}={attrition_rate.max():.2f}%")

def year_wise_attrition(df):
    """
    Calculate the experience wise attrition
    """

    print("\n ==== Experience Wise Attrition ====")
    yes_attrition = df.loc[df["Attrition"] == "Yes", "TotalWorkingYears"].value_counts()
    no_attrition = df.loc[df["Attrition"] == "No", "TotalWorkingYears"].value_counts()
    print(f"Attrition = Yes \n {yes_attrition}")
    print(f"Attrition = No \n {no_attrition}")

def job_satisfaction_vs_attrition(df):
    """
    Calculate the  job satisfaction wise attrition
    """

    print("\n ==== Job Satisfaction Wise Attrition Rate ====")
    sorted_job_satisfaction = df["JobSatisfaction"].value_counts().sort_index()

    yes_attrition = df.loc[df["Attrition"] == "Yes", "JobSatisfaction"].value_counts()

    total_employees  = df["JobSatisfaction"].value_counts().sort_index()

    attrition_rate = (yes_attrition/total_employees)*100

    print(attrition_rate.round(2))
    highest = attrition_rate.idxmax()

    print("\n Highest Attrition Rate")
    print(f"Job Satisfaction ={highest}")
    print(f"Attrition Rate ={attrition_rate[highest]:.2f}%")

def  work_life_balance_vs_attrition(df):
    """
    Calculate the life balance wise attrition
    """

    print("\n ==== Life Balance Wise Attrition ====")
    sorted_work_life_balance = df["WorkLifeBalance"].value_counts().sort_index()

    yes_attrition = df.loc[df["Attrition"] == "Yes", "WorkLifeBalance"].value_counts()

    total_employees  = df["WorkLifeBalance"].value_counts().sort_index()

    attrition_rate = (yes_attrition/total_employees)*100
    
    print(attrition_rate.round(2))
    highest = attrition_rate.idxmax()

    print("\n Highest Work Life Balance Rate")
    print(f"Work Life Balance ={highest}")
    print(f"Attrition Rate ={attrition_rate[highest]:.2f}%")