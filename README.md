# Fetch Rewards Scanned Receipts Prediction App

## Project Overview

This project is designed to predict the number of receipts that will be scanned by Fetch Rewards app users. The prediction is based on historical data from the year 2021 and uses machine learning models to estimate future counts.

## Models Used

- **Linear Regression**: A baseline model for initial prediction attempts.
- **LSTM (Long Short-Term Memory)**: An advanced neural network model suited for time-series prediction.
- **ARIMA/SARIMA**: Traditional time-series forecasting models used for comparison with LSTM results.

## Data

The data used for this project consists of daily counts of receipts scanned by users throughout 2021.

## Batch Processing

The model is designed to run batch predictions for the entire year of 2022. It uses features generated from the 2021 dataset to make future predictions.

## Running the App

### With Docker:

1. Ensure you have Docker installed on your machine.
2. Clone the repository and navigate to the project directory.
3. Build the Docker image: docker build -t fetch-receipts-prediction .
4. Run the Docker container: docker run -p 8501:8501 fetch-receipts-prediction
5. Open your web browser and go to `http://localhost:8504` to view the app.

### Without Docker:

1. Ensure you have Python and the necessary packages installed.
2. Clone the repository and navigate to the project directory.
3. Install the required packages: pip install -r requirements.txt
4. Run the Streamlit app: streamlit run app.py
5. Streamlit will automatically open the app in your default web browser.

## Features

- Interactive Streamlit dashboard for data visualization.
- Monthly aggregated plot for understanding trends over 2021.
- Batch prediction capability for forecasting the entire year of 2022.

## Contributing

We welcome contributions to improve the models or the app interface. Please feel free to fork the repository, make changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
