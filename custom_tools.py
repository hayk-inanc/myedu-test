import streamlit as st

def metrics(df):
    df = df.copy()

    col_1, col_2 = st.columns(2)
    with col_1:
        st.metric(
            "Колличество записей: ", 
            df.shape[0]
        )

    with col_2:
        st.metric(
            "Разброс прибыли: ", 
            round(df.revenue.std(), 2)
        )

def revenue_slider(df):
    df = df.copy()

    if "revenue_values" in st.session_state:
        revenue_values = st.session_state["revenue_values"]
    else:
        revenue_values = (int(df.revenue.quantile(0.25)), int(df.revenue.quantile(0.75)))

    result = st.slider("Укажите прибыль: ",
          min_value=int(df.revenue.min()),
          max_value=int(df.revenue.max()),
          value=revenue_values
    )

    st.session_state["revenue_values"] = result
    return result 