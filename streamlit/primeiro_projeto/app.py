from altair import themes
import streamlit as st
import pandas as pd


st.set_page_config(layout="wide")

df_reviews = pd.read_csv("dataset/customer_reviews.csv")
df_top100_books = pd.read_csv("dataset/Top-100_Trending_Books.csv")

df_reviews




