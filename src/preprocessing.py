import pandas as pd

def create_age_group(age):
    if age < 18:
        return "<18"
    elif 18 <= age <= 25:
        return "18-25"
    elif 26 <= age <= 35:
        return "26-35"
    elif 36 <= age <= 45:
        return "36-45"
    else:
        return "45+"


def preprocess_data(df):
    """
    Clean and transform data
    """

    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values (simple way)
    df = df.dropna()

    # Create Age Group column
    df['AgeGroup'] = df['Age'].apply(create_age_group)

    return df


# Test run
if __name__ == "__main__":
    from data_loader import get_final_data

    file = "../data/EduPro Online Platform.xlsx"

    df = get_final_data(file)
    df = preprocess_data(df)

    print(df[['Age', 'AgeGroup']].head())