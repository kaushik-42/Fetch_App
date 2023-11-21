# Fetch Rewards Scanned Receipts Prediction App

## Project Overview

This project is designed to predict the number of receipts that will be scanned by Fetch Rewards app users. The prediction is based on historical data from the year 2021 and uses machine learning models to estimate future counts.

![Fetch_Landing_Page_App](Images/Fetch_Main.png)
![Fetch_Next Page](Images/Fetch_2.png)
![Fetch_Next Page - 1](Images/Prediction_result.png)

## Models Used

- **Linear Regression**: A baseline model for initial prediction attempts. (Selected as a model for Predictions for the year 2022).
- **LSTM (Long Short-Term Memory)**: An advanced neural network model suited for time-series prediction.
- **ARIMA/SARIMA**: Traditional time-series forecasting models used for comparison with LSTM results.

## Data

The data used for this project consists of daily counts of receipts scanned by users throughout 2021. The data has 1 target variable i.e. the daily counts of receipts scanned along with that respective date. We used DateTime to convert the dates into a proper format and also have increased some features for better performance of the models. 

## Batch Processing

To reduce the complexity involved while working with a Streamlit app/Flask app, as we need to have all the month's predictions, the model is designed to run batch predictions for the entire year of 2022. It uses features generated from the 2021 dataset to make future predictions. All the 2022 results are saved into the "predicted_receipt_counts_2022.csv", where in the main streamlit application, we can just import that directly and aggregate the results.

## Installation of our Prediction app:

To install the project, follow these steps:

1. Clone the repository to your local machine:
    ```
    git clone https://github.com/kaushik-42/Fetch_App
    ```

2. Navigate to the project directory:
    ```
    cd Fetch_APP
    ```

## Running the App

### With Docker:

1. Ensure you have Docker installed on your machine.
2. Clone the repository and navigate to the project directory.
3. Build the Docker image:
   ```
    docker build -t fetch_app:latest
   ```
4. Run the Docker container:
   ```
    docker run -p 8504:8504 fetch_app:latest
   ```
5. You can also visit `http://localhost:8504` to view the app.

### Without Docker:

1. Ensure you have Python and the necessary packages installed.
2. Clone the repository and navigate to the project directory.
3. Install the required packages: pip install -r requirements.txt
   ```
   pip install -r requirements.txt
   ```
4. Run the Streamlit app: streamlit run app.py
   ```
   streamlit run app.py
   ```
5. Streamlit will automatically open the app in your default web browser.


## Running the .ipynb file:

## Features

- Interactive Streamlit dashboard for data visualization for the Year 2021 if the shareholders want to view that before making 2022 predictions of a month.
- Monthly aggregated plot for understanding trends over 2021.
- Batch prediction capability for forecasting the entire year of 2022.

## Metrics used:

- Rmse (Root Mean Square Error) - LSTM's and Linear regression was performing well.
- MAE (Mean Absolute Error) - Linear Regression was working really well.

## Contributing

We welcome contributions to improve the models or the app interface. Please feel free to fork the repository, make changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
