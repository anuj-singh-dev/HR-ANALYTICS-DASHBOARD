import pandas as pd

def load_data(path):
    df = pd.read_csv("data/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv")
    return df
