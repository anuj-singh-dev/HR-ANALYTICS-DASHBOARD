def data_summary(df):
    """ 
    Display Basic Information about the data set
    """
    print("\n ===== Dataset Summary====")
    print(f"Rows:{df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    print("\n Column Name")
    print(df.columns.to_list())

    print("\n Data Types")
    print(df.dtypes)


def check_missing_values(df):
    """
    Display the no. of missing value in each columns
    """
    print("\n ====Missing Values====")
    missing_values = df.isnull().sum()
    print(missing_values)

def check_duplicates(df):
    """
    Display the no. of Duplicate rows in the dataset.
    """

    print("\n ====Duplicate Records====")
    duplicate_count = df.duplicated().sum()
    print(f"Duplicated Rows:{duplicate_count}")

def statistical_summary(df):
    """
    Display Statistical Summary of the numerical columns
    """

    print(f"\n ==== Statistical Summary====")
    print(df.describe())