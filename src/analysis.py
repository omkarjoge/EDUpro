import pandas as pd

def get_kpis(df):
    """
    Calculate key performance indicators
    """

    kpis = {}

    # Total enrollments
    kpis['Total Enrollments'] = len(df)

    # Gender ratio
    kpis['Gender Distribution'] = df['Gender'].value_counts()

    # Age group distribution
    kpis['Age Group Distribution'] = df['AgeGroup'].value_counts()

    # Category popularity
    kpis['Category Popularity'] = df['CourseCategory'].value_counts()

    # Course level distribution
    kpis['Course Level Distribution'] = df['CourseLevel'].value_counts()

    # Avg courses per user
    kpis['Avg Courses Per User'] = df.groupby('UserID').size().mean()

    return kpis


def age_vs_category(df):
    return pd.crosstab(df['AgeGroup'], df['CourseCategory'])


def gender_vs_level(df):
    return pd.crosstab(df['Gender'], df['CourseLevel'])


def age_vs_level(df):
    return pd.crosstab(df['AgeGroup'], df['CourseLevel'])


# Test run
if __name__ == "__main__":
    from data_loader import get_final_data
    from preprocessing import preprocess_data

    file = "../data/EduPro Online Platform.xlsx"

    df = get_final_data(file)
    df = preprocess_data(df)

    kpis = get_kpis(df)

    print("\n📊 KPIs:")
    for key, value in kpis.items():
        print(f"\n{key}:\n{value}")

    print("\n📊 Age vs Category:\n", age_vs_category(df))
    print("\n📊 Gender vs Level:\n", gender_vs_level(df))