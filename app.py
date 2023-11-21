import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from calendar import month_name
import matplotlib.dates as mdates
import seaborn as sns

# Assuming data_2021 is your DataFrame containing historical data for 2021
# Function to plot daily scanned receipts
def plot_daily_receipts(data_new):
    plt.figure(figsize=(10, 6))
    plt.plot(data_new['# Date'], data_new['Receipt_Count'], marker='o', linestyle='-')
    plt.title('Daily Scanned Receipts in 2021')
    plt.xlabel('Date')
    plt.ylabel('Scanned Receipts')
    plt.xticks(rotation=45)
    plt.tight_layout()
    return plt

def aggregate_predictions_for_month(month, predictions_df):
    # Filter the DataFrame for the selected month
    monthly_predictions = predictions_df[predictions_df.index.month == month]
    # Aggregate (e.g., sum or mean) the predictions for the selected month
    aggregate_value = monthly_predictions['Predicted_Receipt_Count'].sum()  # or .mean(), depending on your preference
    return aggregate_value

# Function to plot daily scanned receipts
def plot_daily_receipts(data_new):
    plt.figure(figsize=(10, 6))
    plt.plot(data_new.index, data_new['Receipt_Count'], marker='o', linestyle='-')
    plt.title('Daily Scanned Receipts in 2021')
    plt.xlabel('Date')
    plt.ylabel('Scanned Receipts')
    plt.xticks(rotation=45)
    plt.tight_layout()
    return plt


def plot_monthly_aggregated_counts(data):
    # Ensure data is for 2021 only
    data_2021 = data[data.index.year == 2021]
    # Resample and sum the 'Receipt_Count' for each month
    monthly_data = data_2021.resample('M').sum()
    # Create the plot
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(monthly_data.index, monthly_data['Receipt_Count'], marker='o', linestyle='-')
    ax.set_title('Monthly Aggregated Receipt Counts for 2021')
    ax.set_xlabel('Month')
    ax.set_ylabel('Total Receipt Counts')
    ax.grid(True)
    # Format x-ticks to show month names
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%B'))
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig


# Streamlit app UI
def main():
    svg_icon = """
    <svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg"><path d="m13.5368 11.9211c-1.858 4.6366-.2264 7.2175 1.993 10.0577-2.3765 2.3758-1.2893 3.7173-1.1228 5.3337-1.1131 1.27-2.2184 2.7634-4.74 2.4094-1.0108-.1418-1.6815.1963-1.8124.8794-.49 2.5564-2.0464 2.4683-3.0612 3.401-1.29 1.1855 2.0048 3.002 3.4652 1.52a12.7028 12.7028 0 0 0 2.395-3.14c3.4921.1136 7.3531 1.3233 9.5456-2.0741.6463-1.0015 1.4145-.4294 2.1452-.3427 2.2186.2631 4.2473 1.8586 7.0387-.38 1.2311-.9872 1.4324-.328 1.6368.2144.76 2.0156 1.9074 1.1533 3.1574.6987l4.4875-1.89c.6741-.284 1.2032-.3215 1.5779.1891 1.3432 1.83 2.2207 1.2883 3.1734-1.1246.5208-1.3191-1.4743-2.4876-3.4445-1.8171-1.7087.5815-4.6289 1.6378-5.4146.013-1.0153-2.0994.9092-4.7477 2.2493-4.1647 2.9374 1.2781 6.3169-2.019 5.3092-3.1961l-2.4873-.485c-.8832-.1722-1.3227-.4831-1.33-.95-.025-1.6341-.8965-1.9843-1.961-2.2816a5.6936 5.6936 0 0 0 -3.2106-.3687 2.5849 2.5849 0 0 1 -1.9734-.0136c-.4206-.1269-.8356-.2944-1.0551-.1284-1.0109.7647-3.45.133-2.6688.61l3.0017 1.832a8.88 8.88 0 0 1 -16.9647-3.6791 8.9725 8.9725 0 0 1 .0705-1.1227z" fill="none" stroke="#000" stroke-linecap="round" stroke-linejoin="round"/></svg>
    """
    scaled_svg_icon = f'<div style="width: 80px; height: 80px;">{svg_icon}</div>'
    st.markdown(f"""
    <div style="display: flex; align-items: center; gap: -5px;">
        {scaled_svg_icon}
            Fetch Rewards Scanned Receipts Prediction App
    </div>
    """, unsafe_allow_html=True)

    # Load historical data for 2021
    data_2021 = pd.read_csv('data_daily.csv')
    data_2021['Date'] = pd.to_datetime(data_2021['# Date'])
    data_2021.set_index('Date', inplace=True)
    #print(data_2021.head())
    # Load precomputed predictions for 2022
    predictions_2022 = pd.read_csv('predicted_receipt_counts_2022.csv')
    predictions_2022['Date'] = pd.to_datetime(predictions_2022['Date'])
    predictions_2022.set_index('Date', inplace=True)
    #print(predictions_2022.head())

    st.title('Fetch Rewards Scanned Receipts Prediction App ')

    st.markdown("""### Use Case at Fetch: At fetch, we are monitoring the number of the scanned receipts to our app on a daily base as one of our KPIs. From business standpoint, we sometimes need to predict the possible number of the scanned receipts for a given future month.""")
    
    st.markdown("""### The Streamlit application is about forecasting the approximate number of the scanned receipts for each month of 2022 based on the the number of the observed scanned receipts each day for the year 2021""")
    # Ask user if they want to see 2021 stats
    if st.checkbox('Show 2021 Statistics'):
        st.header('2021 Year Statistics')

        # Time Series Plot explanation
        st.markdown("""
        #### Time Series Plot:
        The line chart illustrates the daily scanning trends throughout 2021. It's a visual representation of the data's trend, seasonality, and any unusual fluctuations. By analyzing these patterns, businesses can make informed decisions about resource allocation and marketing strategies throughout the year.
        """)
        # Time Series Plot
        st.pyplot(plot_daily_receipts(data_2021))

        st.markdown("""
        #### Box Plot by Month:
        Each box plot shows the distribution of daily receipt counts for a given month. The box encompasses the interquartile range with the median value marked, while the whiskers show the range of typical data points, excluding outliers. This visualization helps identify the variability in daily transactions and any anomalous days that deviate from the norm.
        """)
        # Box Plot by Month
        st.subheader('Box Plot of Monthly Receipt Counts for 2021')
        fig, ax = plt.subplots()
        data_2021['Month'] = data_2021.index.month  # Extract month for boxplot
        data_2021.boxplot(column='Receipt_Count', by='Month', ax=ax)
        plt.title('Monthly Receipt Counts')
        plt.suptitle('')  # Suppress the default title
        plt.xlabel('Month')
        plt.ylabel('Receipt Count')
        st.pyplot(fig)

        st.markdown("""
        #### Monthly Aggregated Plot:
        This plot displays the total receipts scanned each month in 2021, revealing the high and low activity periods. Peaks indicate months with higher transactions, possibly due to increased customer engagement or promotions. Troughs may suggest less active periods, potentially requiring targeted initiatives to boost sales.
        """)
        # Monthly Aggregated Plot
        #st.subheader('Monthly Aggregated Receipt Counts for 2021')
        # After resampling
        #monthly_data = data_2021[data_2021.index.year == 2021].resample('M').sum().reset_index()
        # This should not be necessary if your data is already filtered for 2021, but just in case:
        #monthly_data = monthly_data[monthly_data['Date'].dt.year == 2021]
        # Now the line_chart should display the correct date range
        #st.line_chart(monthly_data.set_index('Date')['Receipt_Count'])
        fig_1 = plot_monthly_aggregated_counts(data_2021)
        st.pyplot(fig_1)

    # User input for selecting month
    #st.header('Predictions for the Year 2022')
    #selected_month = st.slider('Select Month for Prediction', 1, 12, 1)  # Slider from 1 to 12

    st.header('Predictions for the Year 2022')
    month_names = list(month_name)[1:]  # This will create a list of month names
    selected_month_name = st.selectbox('Select Month for Prediction', month_names)
    selected_month = month_names.index(selected_month_name) + 1  # This will get the month number


    if st.button(f'Predict Receipt Counts for {selected_month_name} in the Year 2022'):
        # Aggregate predictions for the selected month
        aggregated_value = aggregate_predictions_for_month(selected_month, predictions_2022)

        # Display the aggregated prediction value
        st.success(f'Aggregated Predicted Receipts for Month {selected_month_name} (2022): {aggregated_value}')
  

if __name__ == '__main__':
    main()
