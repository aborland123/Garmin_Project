import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

def plot_ADM(df):
    st.subheader('Average Distance by Month')

    df["Date"] = pd.to_datetime(df["Date"], format='%Y-%m-%d %H:%M:%S').dt.strftime('%Y-%m-%d')
    df["Distance"] = pd.to_numeric(df["Distance"], errors='coerce')
    df["Date"] = pd.to_datetime(df["Date"], format='%Y-%m-%d')

    monthly_avg_distance = df.groupby(df["Date"].dt.to_period("M"))["Distance"].sum()
    plt.figure(figsize=(10, 6))
    monthly_avg_distance.plot(kind="bar", color="blue")
    plt.title("Average Distance by Month")
    plt.xlabel("Month")
    plt.ylabel("Average Distance")
    plt.show()
    st.pyplot(plt)

def plot_ADM_NoRaces(df):
    st.subheader('Average Distance by Month Without Races')

    df["Date"] = pd.to_datetime(df["Date"], format='%Y-%m-%d %H:%M:%S').dt.strftime('%Y-%m-%d')
    df["Distance"] = pd.to_numeric(df["Distance"], errors='coerce')
    df["Date"] = pd.to_datetime(df["Date"], format='%Y-%m-%d')

    keywords_to_remove = ['Marathon', '5k', 'Race', 'Jim', 'Half']

    mask = ~df['Title'].str.contains('|'.join(keywords_to_remove), case=False)
    df = df[mask]
    monthly_avg_pace = df.groupby(df["Date"].dt.to_period("M"))["Distance"].sum()


    plt.figure(figsize=(10, 6))
    monthly_avg_pace.plot(kind="bar", color="blue")
    plt.title("Average Distance by Month W/O Races")
    plt.xlabel("Month")
    plt.ylabel("Average Distance")
    plt.show()
    st.pyplot(plt)

def plot_ADM_WithRaces(df):
    st.subheader('Average Distance by Month With Races')
    df["Date"] = pd.to_datetime(df["Date"], format='%Y-%m-%d %H:%M:%S').dt.strftime('%Y-%m-%d')
    df["Distance"] = pd.to_numeric(df["Distance"], errors='coerce')
    df["Date"] = pd.to_datetime(df["Date"], format='%Y-%m-%d')

    keywords_to_remove = ['Marathon', '5k', 'Race', 'Jim', 'Half']

    mask = df['Title'].str.contains('|'.join(keywords_to_remove), case=False)
    df = df[mask]

    monthly_avg_pace = df.groupby(df["Date"].dt.to_period("M"))["Distance"].sum()

    plt.figure(figsize=(10, 6))
    monthly_avg_pace.plot(kind="bar", color="blue")
    plt.title("Average Distance by Month With Races")
    plt.xlabel("Month")
    plt.ylabel("Average Distance")
    plt.show()
    st.pyplot(plt)
    
def plot_AHRD(df):
    st.subheader('Average Heart Rate by Distance')
    rows_to_drop = [37, 69, 156, 170, 174, 181, 182, 793, 940]
    df = df.drop(index=rows_to_drop)

    df["Avg HR"] = pd.to_numeric(df["Avg HR"], errors='coerce')
    df = df.dropna(subset=["Avg HR"])

    plt.figure(figsize=(10, 6))
    plt.scatter(df["Avg HR"], df["Distance"], color="blue", alpha=0.5)
    plt.title("Average HR by Distance")
    plt.xlabel("Avg HR")
    plt.ylabel("Distance")
    plt.show()
    st.pyplot(plt)
    
def plot_AHRM(df):
    st.subheader('Average Heart Rate by Month')
    df["Date"] = pd.to_datetime(df["Date"], format='%Y-%m-%d %H:%M:%S').dt.strftime('%Y-%m-%d')
    df["Date"] = pd.to_datetime(df["Date"], format='%Y-%m-%d')

    rows_to_drop = [37, 69, 156, 170, 174, 181, 182, 793, 940]
    df = df.drop(index=rows_to_drop)
    keywords_to_include = ['Marathon']

    mask = df['Title'].str.contains('|'.join(keywords_to_include), case=False)
    df = df[mask]
    keywords_to_remove = ['half']

    mask = ~df['Title'].str.contains('|'.join(keywords_to_remove), case=False)
    df = df[mask]

    df["Avg HR"] = pd.to_numeric(df["Avg HR"], errors='coerce')
    df = df.dropna(subset=["Avg HR"])
    monthly_avg_hr = df.groupby(df["Date"].dt.to_period("M"))["Avg HR"].mean()


    plt.figure(figsize=(10, 6))
    monthly_avg_hr.plot(kind="bar", color="blue")
    plt.title("Average HR by Month JUST Marathons")
    plt.xlabel("Month")
    plt.ylabel("Average HR")
    plt.show()
    st.pyplot(plt)
    
def plot_APM(df):
    st.subheader('Average Pace by Month')
    df["Date"] = pd.to_datetime(df["Date"], format='%Y-%m-%d %H:%M:%S').dt.strftime('%Y-%m-%d')
    df["Date"] = pd.to_datetime(df["Date"], format='%Y-%m-%d')

    rows_to_drop = [37, 69, 156, 170, 174, 181, 182, 793, 940]
    df = df.drop(index=rows_to_drop)

    df["Avg Pace"] = df["Avg Pace"].str.replace(":", "")
    df = df.astype({"Avg Pace":int})
    monthly_avg_pace = df.groupby(df["Date"].dt.to_period("M"))["Avg Pace"].mean()

    plt.figure(figsize=(10, 6))
    monthly_avg_pace.plot(kind="bar", color="blue")
    plt.title("Average Pace by Month")
    plt.xlabel("Month")
    plt.ylabel("Average Pace")
    plt.show()
    st.pyplot(plt)
    
def plot_APMD_JustRaces(df):
    st.subheader('Average Pace by Month & Distance Just Races')
    df["Date"] = pd.to_datetime(df["Date"], format='%Y-%m-%d %H:%M:%S').dt.strftime('%Y-%m-%d')
    df["Date"] = pd.to_datetime(df["Date"], format='%Y-%m-%d')

    rows_to_drop = [37, 69, 156, 170, 174, 181, 182, 793, 940]
    df = df.drop(index=rows_to_drop)

    keywords_to_include = ['Marathon', '5k', 'Race', 'Jim', 'Half']

    mask = df['Title'].str.contains('|'.join(keywords_to_include), case=False)
    df = df[mask]

    df["Avg Pace"] = df["Avg Pace"].str.replace(":", "")
    df = df.astype({"Avg Pace":int})
    monthly_avg_pace = df.groupby(df["Date"].dt.to_period("M"))["Avg Pace"].mean()

    plt.figure(figsize=(10, 6))
    plt.scatter(df["Date"], df["Distance"], c=df["Avg Pace"], cmap='viridis', alpha=0.7)
    plt.title("Scatter Plot of Avg Pace vs Distance vs. Date with Distance as Color")
    plt.xlabel("Date")
    plt.ylabel("Distance")
    plt.colorbar(label="Avg Pace")
    plt.show()
    st.pyplot(plt)
    
def plot_APM_JustMarathons(df):
    st.subheader('Average Pace by Month Just Marathons')
    df["Date"] = pd.to_datetime(df["Date"], format='%Y-%m-%d %H:%M:%S').dt.strftime('%Y-%m-%d')
    df["Date"] = pd.to_datetime(df["Date"], format='%Y-%m-%d')

    rows_to_drop = [37, 69, 156, 170, 174, 181, 182, 793, 940]
    df = df.drop(index=rows_to_drop)

    keywords_to_include = ['Marathon']

    mask = df['Title'].str.contains('|'.join(keywords_to_include), case=False)
    df = df[mask]

    keywords_to_remove = ['half']

    mask = ~df['Title'].str.contains('|'.join(keywords_to_remove), case=False)
    df = df[mask]

    df["Avg Pace"] = df["Avg Pace"].str.replace(":", "")
    df = df.astype({"Avg Pace":int})

    monthly_avg_pace = df.groupby(df["Date"].dt.to_period("D"))["Avg Pace"].mean()


    plt.figure(figsize=(10, 6))
    monthly_avg_pace.plot(kind="bar", color="blue")
    plt.title("Average Pace by Month JUST Marathons")
    plt.xlabel("Month")
    plt.ylabel("Average Pace")
    plt.show()
    st.pyplot(plt)
    
def plot_APM_NoRaces(df):
    st.subheader('Average Pace by Month Without Races')
    df["Date"] = pd.to_datetime(df["Date"], format='%Y-%m-%d %H:%M:%S').dt.strftime('%Y-%m-%d')
    df["Date"] = pd.to_datetime(df["Date"], format='%Y-%m-%d')

    rows_to_drop = [37, 69, 156, 170, 174, 181, 182, 793, 940]
    df = df.drop(index=rows_to_drop)

    keywords_to_remove = ['Marathon', '5k', 'Race', 'Jim', 'Half']

    mask = ~df['Title'].str.contains('|'.join(keywords_to_remove), case=False)
    df = df[mask]

    df["Avg Pace"] = df["Avg Pace"].str.replace(":", "")
    df = df.astype({"Avg Pace":int})

    monthly_avg_pace = df.groupby(df["Date"].dt.to_period("M"))["Avg Pace"].mean()

    plt.figure(figsize=(10, 6))
    monthly_avg_pace.plot(kind="bar", color="blue")
    plt.title("Average Pace by Month W/O Races")
    plt.xlabel("Month")
    plt.ylabel("Average Pace")
    plt.show()
    st.pyplot(plt)
    
def plot_APM_JustRaces(df):
    st.subheader('Average Pace by Month Just Races')
    df["Date"] = pd.to_datetime(df["Date"], format='%Y-%m-%d %H:%M:%S').dt.strftime('%Y-%m-%d')
    df["Date"] = pd.to_datetime(df["Date"], format='%Y-%m-%d')

    rows_to_drop = [37, 69, 156, 170, 174, 181, 182, 793, 940]
    df = df.drop(index=rows_to_drop)

    keywords_to_include = ['Marathon', '5k', 'Race', 'Jim', 'Half']

    mask = df['Title'].str.contains('|'.join(keywords_to_include), case=False)
    df = df[mask]

    df["Avg Pace"] = df["Avg Pace"].str.replace(":", "")
    df = df.astype({"Avg Pace":int})

    monthly_avg_pace = df.groupby(df["Date"].dt.to_period("M"))["Avg Pace"].mean()

    plt.figure(figsize=(10, 6))
    monthly_avg_pace.plot(kind="bar", color="blue")
    plt.title("Average Pace by Month JUST Races")
    plt.xlabel("Month")
    plt.ylabel("Average Pace")
    plt.show()
    st.pyplot(plt)
    
def main():
    st.title('Garmin CSV Reader and Graph Plotter')

    # File upload
    uploaded_file = st.file_uploader('Upload CSV file', type=['csv'])

    if uploaded_file is not None:
        # Read CSV file
        try:
            df = pd.read_csv(uploaded_file, skiprows=1)
            st.success('File successfully uploaded and read.')
            df = df.iloc[0:]         

            # Display DataFrame
            st.write('**DataFrame:**')
            st.write(df.head())

            # Plot graphs
            plot_ADM(df)
            plot_ADM_NoRaces(df)
            plot_ADM_WithRaces(df)
            plot_AHRD(df)
            plot_AHRM(df)
            plot_APM(df)
            plot_APMD_JustRaces(df)
            plot_APM_JustMarathons(df)
            plot_APM_NoRaces(df)
            plot_APM_JustRaces(df)
        except Exception as e:
            st.error(f'Error: {e}')

if __name__ == '__main__':
    main()

