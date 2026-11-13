import streamlit as st
import pandas as pd
import custom_tools


st.header("Страница!")

df = pd.read_csv("data/sales_demo_dataset.csv")
st.info("Изначально точки на 0.25 и на 0.75 квантилях")
min_revenue, max_revenue = custom_tools.revenue_slider(df)

filtered_df = df[df.revenue.between(min_revenue, max_revenue)]
custom_tools.metrics(filtered_df)

st.dataframe(filtered_df)