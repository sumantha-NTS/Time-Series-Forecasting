# Time-Series-Forecasting
The Objective of this project is to forecast the particulate matter (PM) for next 24 hours.
## Input:
The dataset used for this project consists of hourly data of particulate matter for 4 months.\
The dataset has 2374 records with 2 columns i.e., Date and PM 2.5 columns.

## Exploratory data analysis:
The dataset has missing values as well as missing records which has been explained in **.ipynb** file.\
The missing values are imputed with different techniques i.e., 
1) Mean Imputation
2) previous day imputation
3) interpolation with time
Model has been built for all the imputation methods and the models are evaluated with RMSE values.

## Model Building:
In order build any time series model, it is necessary that time series should be stationary.\
**Rolling statistics** and **Augmented Dickey Fuller test** are used to check the stationarity of the time series.\
Different time series models considered for forecasting are as follows,
1) Auto Regression (AR)
2) Autoregressive Moving Average (ARMA)
3) Autoregressive Integrated Moving Average (ARIMA)
4) Seasonal Autoregressive Integrated Moving-Average (SARIMA)
5) Simple Exponential Smoothing (SES)
6) Holt method
7) Holt Winter’s Exponential Smoothing (HWES) with additive seasonality
8) Holt Winter’s Exponential Smoothing (HWES) with multiplicative seasonality

## Model Evaluation:
All the models with all different imputation techniques which are mentioned above are considered for forecasting with evaluation metric as **RMSE**.\
The model with least **RMSE** value is considered for deployment.

| Model Name  | Interpolate with time | Impute with mean | Impute with previous day data |
|:----------------:|:---------------------:|:----------:|:---------:|
|AR                | 64.46   |    73.30   |    65.10  |
|ARMA (4,0,4)      | 82.17   |    62.25   |    78.66|
|ARIMA (4,1,4)     | 119.84  |    116.68   |    120.65  | 
|SARIMA (1,0,1,24) | 42.60   |    46.30    |    **37.37**  |
|SimpleExpSmoothing| 69.71   |    69.70   |    69.70  |
|Holt method       | 69.85   |    70.06  |    69.92  |
|Exponential Add   | 48.92   |    42.98   |    47.86  |
|Exponential Mul   | 76.47   |    73.31    |    77.55  |

## Model Deployment:
I have used **Streamlit** library and **Heroku** platform to deploy the app.\
App URL :https://forecasting-pm.herokuapp.com/
