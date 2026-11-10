import streamlit as st
import pandas as pd
st.set_page_config(page_title="Diamonds Explorer", layout="wide")
st.title("Diamonds Explorer")
uploaded_file = st.file_uploader("Upload diamonds.csv", type=["csv"])
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.dataframe(df.head(5))
  st.metric("Diamonds", len(df))
  column = st.selectbox("Group by", options=["cut", "color", "clarity"])
  filter_enabled = st.checkbox("Enable category filter", value=False)
  filtered = df.copy()
  if filter_enabled:
    choices = sorted(df[column].dropna().astype(str).unique().tolist())
    selected = st.multiselect("Keep categories", options=choices, default=choices)
    filtered = filtered[filtered[column].astype(str).isin(selected)]
  st.dataframe(filtered)
  st.metric("Filtered diamonds", filtered.shape[0])
  mean_price = filtered.groupby(column)["price"].mean()
  st.bar_chart(mean_price)
  st.download_button("Download filtered CSV", filtered.to_csv(index=False), file_name="diamonds_filtered.csv", mime="text/csv")

