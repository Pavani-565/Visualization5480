import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title("📊 Data Visualization App")

# Upload dataset
uploaded_file = st.file_uploader("Upload Dataset (CSV)", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Dataset Preview", df.head())

    # Choose visualization type
    st.subheader("Choose the dimensions of visualization")
    viz_type = st.radio("Select Dimension:", ("1D", "2D"))

    if viz_type == "1D":
        column = st.selectbox("Choose a column for 1D visualization", df.columns)

        # Plot 1 - Histogram
        fig, ax = plt.subplots()
        sns.histplot(df[column], kde=True, ax=ax)
        st.pyplot(fig)

        # Plot 2 - Boxplot
        fig, ax = plt.subplots()
        sns.boxplot(x=df[column], ax=ax)
        st.pyplot(fig)

    elif viz_type == "2D":
        x_axis = st.selectbox("Choose X-axis", df.columns)
        y_axis = st.selectbox("Choose Y-axis", df.columns)

        # Plot 1 - Scatterplot
        fig, ax = plt.subplots()
        sns.scatterplot(x=df[x_axis], y=df[y_axis], ax=ax)
        st.pyplot(fig)

        # Plot 2 - Lineplot
        fig, ax = plt.subplots()
        sns.lineplot(x=df[x_axis], y=df[y_axis], ax=ax)
        st.pyplot(fig)
