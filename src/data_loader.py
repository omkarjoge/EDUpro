import pandas as pd

def load_data(file_path):
    """
    Load all sheets from Excel file
    """
    users = pd.read_excel(file_path, sheet_name="Users")
    courses = pd.read_excel(file_path, sheet_name="Courses")
    transactions = pd.read_excel(file_path, sheet_name="Transactions")

    return users, courses, transactions


def merge_data(users, courses, transactions):
    """
    Merge all datasets into one dataframe
    """
    df = transactions.merge(users, on="UserID", how="inner")
    df = df.merge(courses, on="CourseID", how="inner")

    return df


def get_final_data(file_path):
    """
    Complete pipeline: load + merge
    """
    users, courses, transactions = load_data(file_path)
    df = merge_data(users, courses, transactions)
    
    return df


# Test run (optional)
if __name__ == "__main__":
    file = "../data/EduPro Online Platform.xlsx"
    df = get_final_data(file)
    print(df.head())