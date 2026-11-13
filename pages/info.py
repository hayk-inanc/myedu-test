import streamlit as st 

if "revenue_values" in st.session_state:
    min, max = st.session_state["revenue_values"]
    st.metric("минимальная грань прибыли: ", min)
    st.metric("максимальная грань прибыли: ", max)

else:
    st.info("для начала задайте грани прибыли")