import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Employee Flight Risk Index Dashboard")

df = pd.read_csv("dataset.csv")
df = df.sort_values(by="risk_score", ascending=False)

top_10 = int(len(df) * 0.10)
high_risk_df = df.head(top_10)

at_risk_percent = (len(high_risk_df) / len(df)) * 100
avg_risk_score = df["risk_score"].mean()

col1, col2 = st.columns(2)
col1.metric("Workforce At Risk (%)", f"{at_risk_percent:.1f}%")
col2.metric("Average Risk Score", f"{avg_risk_score:.3f}")

st.subheader("Top 25 Highest-Risk Employees")
top25 = df[["employee_id", "risk_score", "department", "job_role"]].head(25).copy()
top25["risk_score"] = top25["risk_score"].round(3)
st.dataframe(top25)

st.subheader("Top 15 Highest-Risk Employees")
top15 = df.head(15)

fig1, ax1 = plt.subplots()
ax1.barh(top15["employee_id"].astype(str), top15["risk_score"])
ax1.invert_yaxis()
ax1.set_xlabel("Risk Score")
ax1.set_title("Top 15 Highest-Risk Employees")
st.pyplot(fig1)

st.subheader("Average Contribution of Risk Factors")
factors = ["satisfaction_risk", "overtime_risk", "salary_risk", "promotion_risk", "tenure_risk"]

fig2, ax2 = plt.subplots()
df[factors].mean().plot(kind="bar", ax=ax2)
ax2.set_ylabel("Average Value")
ax2.set_title("Average Contribution of Risk Factors")
st.pyplot(fig2)

st.subheader("High-Risk Employees by Department")
fig3, ax3 = plt.subplots()
high_risk_df["department"].value_counts().plot(kind="bar", ax=ax3)
ax3.set_ylabel("Count")
ax3.set_title("High-Risk Employees by Department")
st.pyplot(fig3)
