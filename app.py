#python -m streamlit run app.py

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

import streamlit as st

import plotly.express as px

# Page title

st.title("🌍 World Happiness Index Dashboard")

# Load dataset

df = pd.read_csv("happinessdataset.csv")

# Show dataset

st.header("Dataset")

st.dataframe(df)

# Dataset info

st.header("Dataset Information")

st.write(df.describe())

# Top 10 happiest countries

st.header("Top 10 Happiest Countries")

top10 = df.sort_values(

    by='Happiness Score',

    ascending=False

).head(10)

plt.figure(figsize=(10,6))

sns.barplot(

    x='Happiness Score',

    y='Country',

    data=top10,

    palette='viridis'

)

plt.title('Top 10 Happiest Countries')

st.pyplot(plt)

# Bottom 10 countries

st.header("Bottom 10 Countries")

bottom10 = df.sort_values(

    by='Happiness Score'

).head(10)

st.dataframe(bottom10)

# Correlation Heatmap

st.header("Correlation Heatmap")

plt.figure(figsize=(10,8))

sns.heatmap(

    df.corr(numeric_only=True),

    annot=True,

    cmap='coolwarm'

)

st.pyplot(plt)

# GDP vs Happiness

st.header("GDP vs Happiness Score")

plt.figure(figsize=(8,6))

sns.scatterplot(

    x='Economy (GDP per Capita)',

    y='Happiness Score',

    data=df,

    color='blue'

)

st.pyplot(plt)

# Health vs Happiness

st.header("Health vs Happiness Score")

plt.figure(figsize=(8,6))

sns.scatterplot(

    x='Health (Life Expectancy)',

    y='Happiness Score',

    data=df,

    color='green'

)

st.pyplot(plt)

# Correlation values

st.header("Most Influential Factors")

correlation = df.corr(

    numeric_only=True

)['Happiness Score']

st.write(

    correlation.sort_values(

        ascending=False

    )

)

# World Happiness Map

st.header("World Happiness Map")

fig = px.choropleth(

    df,

    locations="Country",

    locationmode="country names",

    color="Happiness Score",

    hover_name="Country",

    color_continuous_scale="Viridis",

    title="World Happiness Index"

)

st.plotly_chart(fig)


