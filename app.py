import streamlit as st
import pandas as pd

st.set_page_config(page_title="CSV Integrity Checker", layout="wide")
st.title("📊 CSV Integrity Checker – QA Support Tool")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("Preview of Uploaded Data")
    st.dataframe(df)

    st.subheader("Basic Stats")
    st.write("Rows:", df.shape[0])
    st.write("Columns:", df.shape[1])

    st.subheader("Missing Values Report")
    missing = df.isnull().sum()
    st.write(missing[missing > 0] if missing.any() else "✅ No missing values detected.")

    st.subheader("Duplicate Rows")
    duplicates = df.duplicated().sum()
    if duplicates > 0:
        st.warning(f"⚠️ {duplicates} duplicate rows found.")
    else:
        st.success("✅ No duplicate rows found.")

    st.subheader("Column Data Types")
    st.write(df.dtypes)
