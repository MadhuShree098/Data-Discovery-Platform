import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns


# Function to set page configuration with clear defaults
def set_page_config():
    st.set_page_config(
        page_title="Data Visualization",
        page_icon=":tv:",
        layout="wide",
        initial_sidebar_state="expanded"
    )


# Function to display a warning message
def display_warning():
    st.warning("Please upload a CSV file.")


# Function to display the home page with background image
def display_home_page():
    st.title("Uncover Data Stories")
    st.markdown("Explore insights from your data in an interactive way!", unsafe_allow_html=True)

    # Define background image CSS in a separate variable for readability
    bg_image = """
    <style>
        .stApp {
            background-image: url("https://th.bing.com/th/id/R.925b93eae11e5734f43d913dd56d0052?rik=UkRipJZxK7WxrA&riu=http%3a%f%2fwww.divinepnc.com%2fwp-content%2fuploads%2f2016%2f05%2fbig-data.jpg&ehk=okSeFM7ES3%2fuMgy70rIRK50oLbY19Xru8VDEdzIgvjE%3d&risl=&pid=ImgRaw&r=0");
            background-size: cover;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            color: white;
            text-align: center;
        }
        .title {
            font-size: 3em;
            color: white;
        }
    </style>
    """

    # Render background image
    st.markdown(bg_image, unsafe_allow_html=True)


# Set page configuration
set_page_config()

# Navigation section in sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("", options=['Home', 'Sample Data', 'Missing Values', 'Data Types', 'Summary Statistics', 'Correlation Matrix', 'Pairplot'])

# Upload CSV file section
uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

# Display content based on the selected page
if page == 'Home':
    display_home_page()

elif page == 'Sample Data':
    st.title("Data Visualization")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.subheader("Sample of Data")
        st.dataframe(df.head(10))
    else:
        display_warning()

elif page == 'Missing Values':
    st.title("Missing Values")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        missing_values_counts = df.isnull().sum()
        st.bar_chart(missing_values_counts)
    else:
        display_warning()

elif page == 'Data Types':
    st.title("Data Types Distribution")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        data_types_df = pd.DataFrame({'Column Name': df.columns, 'Data Type': df.dtypes.astype(str)})
        fig_data_types_violin = px.bar(
            data_types_df,
            x='Column Name',
            y='Data Type',
            title='Data Types Distribution',
            labels={'x': 'Column Name', 'y': 'Data Type'}
        )
        st.plotly_chart(fig_data_types_violin)
    else:
        display_warning()

elif page == 'Summary Statistics':
    st.title("Summary Statistics")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df.describe())
    else:
        display_warning()

elif page == 'Correlation Matrix':
    st.title("Correlation Matrix")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        corr_matrix = df.select_dtypes(include=['float64', 'int64']).corr()
        fig_corr_matrix = go.Figure(data=go.Heatmap(z=corr_matrix.values, x=corr_matrix.columns, y=corr_matrix.columns, colorscale='Viridis'))
        st.plotly_chart(fig_corr_matrix)
    else:
        display_warning()

elif page == 'Pairplot':
    st.title("Pair Plot")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("This may take a while...")
        sns.pairplot(df)
        st.pyplot()
    else:
        display_warning()
