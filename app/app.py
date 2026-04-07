import streamlit as st
import pandas as pd

# Import your modules
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_loader import get_final_data
from src.preprocessing import preprocess_data
from src.analysis import get_kpis, age_vs_category, gender_vs_level

# Load Data
file = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/EduPro Online Platform.xlsx"))
df = get_final_data(file)
df = preprocess_data(df)

# ---------------- UI ---------------- #

st.set_page_config(page_title="EduPro Dashboard", layout="wide")

st.title("📊 EduPro Analytics Dashboard")

# ---------------- Sidebar Filters ---------------- #

st.sidebar.header("🔍 Filters")

age_filter = st.sidebar.selectbox(
    "Select Age Group",
    ["All"] + list(df['AgeGroup'].unique())
)

gender_filter = st.sidebar.selectbox(
    "Select Gender",
    ["All"] + list(df['Gender'].unique())
)

category_filter = st.sidebar.selectbox(
    "Select Course Category",
    ["All"] + list(df['CourseCategory'].unique())
)

# Apply filters
filtered_df = df.copy()

if age_filter != "All":
    filtered_df = filtered_df[filtered_df['AgeGroup'] == age_filter]

if gender_filter != "All":
    filtered_df = filtered_df[filtered_df['Gender'] == gender_filter]

if category_filter != "All":
    filtered_df = filtered_df[filtered_df['CourseCategory'] == category_filter]

# ---------------- KPIs ---------------- #

kpis = get_kpis(filtered_df)

col1, col2, col3 = st.columns(3)

col1.metric("Total Enrollments", kpis['Total Enrollments'])
col2.metric("Avg Courses/User", round(kpis['Avg Courses Per User'], 2))
col3.metric("Unique Users", filtered_df['UserID'].nunique())

# ---------------- Charts ---------------- #

st.subheader("📈 Age Group Distribution")
st.bar_chart(filtered_df['AgeGroup'].value_counts())

st.subheader("👨‍🎓 Gender Distribution")
st.bar_chart(filtered_df['Gender'].value_counts())

st.subheader("📚 Course Category Popularity")
st.bar_chart(filtered_df['CourseCategory'].value_counts())

# ---------------- Heatmaps ---------------- #

st.subheader("🔥 Age vs Course Category")
st.dataframe(age_vs_category(filtered_df))

st.subheader("⚡ Gender vs Course Level")
st.dataframe(gender_vs_level(filtered_df))

# ---------------- Raw Data ---------------- #

st.subheader("📄 Data Preview")
st.dataframe(filtered_df.head())