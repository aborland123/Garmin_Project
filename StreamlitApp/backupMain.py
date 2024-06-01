import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def plot_AD(df):

    df["Date"] = pd.to_datetime(df["Date"], format='%Y-%m-%d %H:%M:%S').dt.strftime('%Y-%m-%d')
    df["Distance"] = pd.to_numeric(df["Distance"], errors='coerce')
    df["Date"] = pd.to_datetime(df["Date"], format='%Y-%m-%d')

    fig1 = px.line(df, x='Date', y='Distance', title="Average Distance")
    st.plotly_chart(fig1)


def plot_ADM_JustRaces(df):

    df["Date"] = pd.to_datetime(df["Date"], format='%Y-%m-%d %H:%M:%S').dt.strftime('%Y-%m-%d')
    df["Distance"] = pd.to_numeric(df["Distance"], errors='coerce')
    df["Date"] = pd.to_datetime(df["Date"], format='%Y-%m-%d')

    keywords_to_remove = ['Marathon', 'Half', '5k', '10k', '100', 'Jim']

    mask = ~df['Title'].str.contains('|'.join(keywords_to_remove), case=False)
    df = df[mask]
    monthly_avg_dist = df.groupby(df["Date"].dt.to_period("M"))["Distance"].sum()

    fig2 = px.bar(x=monthly_avg_dist.index.astype(str), y=monthly_avg_dist.values, title="Average Distance by Month Just Races", labels={'x':'Month', 'y':'Distance'}, color_discrete_sequence=['light blue'])
    st.plotly_chart(fig2)


def plot_ADM_NoRaces(df):
    df["Date"] = pd.to_datetime(df["Date"], format='%Y-%m-%d %H:%M:%S').dt.strftime('%Y-%m-%d')
    df["Distance"] = pd.to_numeric(df["Distance"], errors='coerce')
    df["Date"] = pd.to_datetime(df["Date"], format='%Y-%m-%d')

    keywords_to_remove = ['Marathon', 'Half', '5k', '10k', '100', 'Jim']

    #removes these values
    mask = df['Title'].str.contains('|'.join(keywords_to_remove), case=False)
    df = df[mask]
    monthly_avg_pace = df.groupby(df["Date"].dt.to_period("M"))["Distance"].sum()
    
    fig3 = px.bar(x=monthly_avg_pace.index.astype(str), y=monthly_avg_pace.values, title="Average Distance by Month (Practice/Workout)", labels={'x':'Month', 'y':'Distance'}, color_discrete_sequence=['light blue'])
    st.plotly_chart(fig3)

    
def plot_AHRD(df):
    df["Avg HR"] = pd.to_numeric(df["Avg HR"], errors='coerce')
    df = df.dropna(subset=["Avg HR"])

    fig4 = px.line(df, x='Avg HR', y='Distance', title="Average Heart Rate by Distance")
    st.plotly_chart(fig4)

    
def plot_AHRM(df):
    df["Date"] = pd.to_datetime(df["Date"], format='%Y-%m-%d %H:%M:%S').dt.strftime('%Y-%m-%d')
    df["Date"] = pd.to_datetime(df["Date"], format='%Y-%m-%d')

    keywords_to_include = ['Marathon']

    mask = df['Title'].str.contains('|'.join(keywords_to_include), case=False)
    df = df[mask]
    keywords_to_remove = ['half']

    mask = ~df['Title'].str.contains('|'.join(keywords_to_remove), case=False)
    df = df[mask]

    df["Avg HR"] = pd.to_numeric(df["Avg HR"], errors='coerce')
    df = df.dropna(subset=["Avg HR"])
    monthly_avg_hr = df.groupby(df["Date"].dt.to_period("M"))["Avg HR"].mean()

    fig5 = px.bar(x=monthly_avg_hr.index.astype(str), y=monthly_avg_hr.values, title="Average Heart Rate by Month JUST Marathons", labels={'x':'Month', 'y':'Average Heart Rate'}, color_discrete_sequence=['light blue'])
    st.plotly_chart(fig5)
    

    
def plot_APM(df):
    df["Date"] = pd.to_datetime(df["Date"], format='%Y-%m-%d %H:%M:%S').dt.strftime('%Y-%m-%d')
    df["Date"] = pd.to_datetime(df["Date"], format='%Y-%m-%d')

    df["Avg Pace"].replace("--", pd.NA, inplace=True)
    df.dropna(subset=["Avg Pace"], inplace=True)

    df["Avg Pace"] = df["Avg Pace"].str.replace(":", "")
    df = df.astype({"Avg Pace":int})
    df["Avg Pace"] = df["Avg Pace"]/100
    monthly_avg_pace = df.groupby(df["Date"].dt.to_period("M"))["Avg Pace"].mean()
    df = df.astype({"Avg Pace":str})

    fig6 = px.bar(x=monthly_avg_pace.index.astype(str), y=monthly_avg_pace.values, title="Average Pace by Month", labels={'x':'Month', 'y':'Average Pace'}, color_discrete_sequence=['light blue'])
    st.plotly_chart(fig6)

    
def plot_APMD_JustRaces(df):
    df["Date"] = pd.to_datetime(df["Date"], format='%Y-%m-%d %H:%M:%S').dt.strftime('%Y-%m-%d')
    df["Date"] = pd.to_datetime(df["Date"], format='%Y-%m-%d')

    keywords_to_include = ['Marathon', 'Half', '5k', '10k', '100', 'Jim']

    mask = df['Title'].str.contains('|'.join(keywords_to_include), case=False)
    df = df[mask]

    df["Avg Pace"] = df["Avg Pace"].str.replace(":", "")
    df = df.astype({"Avg Pace":int})
    df["Avg Pace"] = df["Avg Pace"]/100
    monthly_avg_pace = df.groupby(df["Date"].dt.to_period("M"))["Avg Pace"].mean()

    fig7 = px.bar(x=monthly_avg_pace.index.astype(str), y=monthly_avg_pace.values, title="Average Pace by Month & Distance Just Races (No Workouts)", labels={'x':'Month', 'y':'Average Pace'}, color_discrete_sequence=['light blue'])
    st.plotly_chart(fig7)

    
def plot_APM_JustMarathons(df):
    df["Date"] = pd.to_datetime(df["Date"], format='%Y-%m-%d %H:%M:%S').dt.strftime('%Y-%m-%d')
    df["Date"] = pd.to_datetime(df["Date"], format='%Y-%m-%d')

    df["Avg Pace"].replace("--", pd.NA, inplace=True)
    df.dropna(subset=["Avg Pace"], inplace=True)

    keywords_to_include = ['Marathon']

    mask = df['Title'].str.contains('|'.join(keywords_to_include), case=False)
    df = df[mask]

    keywords_to_remove = ['half']

    mask = ~df['Title'].str.contains('|'.join(keywords_to_remove), case=False)
    df = df[mask]

    df["Avg Pace"] = df["Avg Pace"].str.replace(":", "")
    df = df.astype({"Avg Pace":int})
    df["Avg Pace"] = df["Avg Pace"]/100

    monthly_avg_pace = df.groupby(df["Date"].dt.to_period("D"))["Avg Pace"].mean()

    fig8 = px.bar(x=monthly_avg_pace.index.astype(str), y=monthly_avg_pace.values, title="Average Pace by Month JUST Marathons", labels={'x':'Month', 'y':'Average Pace'}, color_discrete_sequence=['light blue'])
    st.plotly_chart(fig8)

    
def plot_APM_NoRaces(df):
    df["Date"] = pd.to_datetime(df["Date"], format='%Y-%m-%d %H:%M:%S').dt.strftime('%Y-%m-%d')
    df["Date"] = pd.to_datetime(df["Date"], format='%Y-%m-%d')

    df["Avg Pace"].replace("--", pd.NA, inplace=True)
    df.dropna(subset=["Avg Pace"], inplace=True)

    keywords_to_remove = ['Marathon', 'Half', '5k', '10k', '100', 'Jim']

    mask = ~df['Title'].str.contains('|'.join(keywords_to_remove), case=False)
    df = df[mask]

    
    df["Avg Pace"] = df["Avg Pace"].str.replace(":", "")
    df = df.astype({"Avg Pace":int})
    df["Avg Pace"] = df["Avg Pace"]/100

    monthly_avg_pace = df.groupby(df["Date"].dt.to_period("M"))["Avg Pace"].mean()
    df = df.astype({"Avg Pace":str})

    fig9 = px.bar(x=monthly_avg_pace.index.astype(str), y=monthly_avg_pace.values, title="Average Pace by Month (Practice/Workout)", labels={'x':'Month', 'y':'Average Pace'}, color_discrete_sequence=['light blue'])
    st.plotly_chart(fig9)


    
def plot_APM_JustRaces(df):
    df["Date"] = pd.to_datetime(df["Date"], format='%Y-%m-%d %H:%M:%S').dt.strftime('%Y-%m-%d')
    df["Date"] = pd.to_datetime(df["Date"], format='%Y-%m-%d')

    df["Avg Pace"].replace("--", pd.NA, inplace=True)
    df.dropna(subset=["Avg Pace"], inplace=True)

    keywords_to_include = ['Marathon', 'Half', '5k', '10k', '100', 'Jim']

    mask = df['Title'].str.contains('|'.join(keywords_to_include), case=False)
    df = df[mask]

    df["Avg Pace"] = df["Avg Pace"].str.replace(":", "")
    df = df.astype({"Avg Pace":int})
    df["Avg Pace"] = df["Avg Pace"]/100

    monthly_avg_pace = df.groupby(df["Date"].dt.to_period("M"))["Avg Pace"].mean()
    df = df.astype({"Avg Pace":str})

    fig10 = px.bar(x=monthly_avg_pace.index.astype(str), y=monthly_avg_pace.values, title="Average Pace by Month Just Races", labels={'x':'Date', 'y':'Average Pace'}, color_discrete_sequence=['light blue'])
    st.plotly_chart(fig10)



    
def main():
    st.title('Garmin CSV Reader and Graph Plotter')
    st.write('Upload your CSV and the graphs will be created!')
    # File upload
    uploaded_file = st.file_uploader('Upload CSV file', type=['csv'])

    if uploaded_file is not None:
        # Read CSV file
        try:
            #df = pd.read_csv(uploaded_file, skiprows=1)
            df = pd.read_csv(uploaded_file)
            st.success('File successfully uploaded and read.')
            df = df.iloc[0:]         
            columns_to_check = ['Time', 'Avg HR', 'Total Ascent', 'Total Descent', 'Distance', 'Title', 'Date', 'Avg Pace']

            # Drop rows with NaNs in the specified columns
            df = df.dropna(subset=columns_to_check)
            #df = df.dropna()

            # turning them to types I need
            df['Time'] = pd.to_timedelta(df['Time'], errors='coerce').dt.total_seconds() / 3600  # Convert time to hours
            df['Avg HR'] = pd.to_numeric(df['Avg HR'], errors='coerce')
            df['Total Ascent'] = pd.to_numeric(df['Total Ascent'], errors='coerce')
            df['Total Descent'] = pd.to_numeric(df['Total Descent'], errors='coerce')


            words_to_search = ['Marathon', 'Half', '5k', '10k', '100', 'Jim']
            pattern = '|'.join(words_to_search)  
            combined_word_count = df['Title'].str.contains(pattern, case=False, regex=True).sum()


            # KPI Metrics
            st.header("Running Metrics Overview")
            kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)
            kpi6, kpi7, kpi8, kpi9, kpi10 = st.columns(5)

            with kpi1:
                st.metric(label="Total Distance (Miles)", value="{:,.0f}".format(df['Distance'].sum()))
            with kpi2:
                st.metric(label="Total Time (Hours)", value="{:,.0f}".format(df['Time'].sum()))
            with kpi3:
                st.metric(label="Total Average Heart Rate", value="{:,.0f}".format(df['Avg HR'].mean()))
            with kpi4:
                st.metric(label="Total Ascent", value="{:,.0f}".format(df['Total Ascent'].sum()))
            with kpi5:
                st.metric(label="Total Descent", value="{:,.0f}".format(df['Total Descent'].sum()))
            with kpi6:
                st.metric(label="Total Races", value="{:,.0f}".format(combined_word_count))
            with kpi7:
                st.metric(label="Total Marathons", value="{:,.0f}".format(df['Title'].str.contains('Marathon', case=False).sum()))
            with kpi8:
                st.metric(label="Total Half Marathons", value="{:,.0f}".format(df['Title'].str.contains('Half', case=False).sum()))
            with kpi9:
                st.metric(label="Total 10k's", value="{:,.0f}".format(df['Title'].str.contains('10k', case=False).sum()))
            with kpi10:
                st.metric(label="Total 5k's", value="{:,.0f}".format(df['Title'].str.contains('5k', case=False).sum()))

            st.header('Graphs:')

            # Plot graphs
            plot_AD(df)
            plot_ADM_JustRaces(df)
            plot_ADM_NoRaces(df)
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
