import streamlit as st
import pandas as pd



# C-3
st.set_page_config(page_title="Titanic Passenger Explorer", layout="wide")
# D-2
st.title("Titanic Passenger Explorer")
# E-1
uploaded_file = st.file_uploader("Upload titanic.csv", type=["csv"])

# F-3
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.dataframe(df.head(5))
  st.metric("Total Passengers", len(df))
  column = st.selectbox("Filter column", options=["class", "sex", "embark_town", "alive", "who"])
  filter_enabled = st.checkbox("Enable passenger filter", value=False)
  filtered = df.copy()
  if filter_enabled
    choices = sorted(df[column].dropna().astype(str).unique().tolist())
    selected = st.multiselect("Select values", options=choices, default=choices)
    filtered = filtered[filtered[column].astype(str).isin(selected)]
  st.dataframe(filtered)
  st.metric("Survivors", int(filtered["survived"].sum()))
  counts = filtered[column].fillna("Missing").astype(str).value_counts()
  st.bar_chart(counts)
  st.download_button("Download Titanic CSV", filtered.to_csv(index=False), file_name="titanic_filtered.csv", mime="text/csv")






