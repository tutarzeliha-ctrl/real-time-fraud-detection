import streamlit as st
import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine("postgresql://postgres:postgres@localhost:5432/fraud_db")

st.title("Real-Time Fraud Detection Dashboard")

# Auto-refresh and manual refresh controls
if st.button("Refresh Data"):
    st.rerun()

try:
    df = pd.read_sql("SELECT * FROM transactions ORDER BY timestamp DESC LIMIT 50", engine)
    if df.empty:
        st.warning("No transaction records found in the database yet. Please ensure the Producer and Spark Streaming processor are running.")
    else:
        st.success(f"Displaying a total of {len(df)} transactions.")
        st.dataframe(df, use_container_width=True)
except Exception as e:
    st.info("Waiting for database connection or table creation.")