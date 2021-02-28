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
| Model Name       |       RMSE                                                               |
| Model Name       | Interpolate with time | Impute with mean | Impute with previous day data |
|:----------------:|:---------------------:|:----------:|:---------:|
|AR                | Linear Regression   |    0.439   |    64.60  |
|ARMA (4,0,4)      | Ridge               |    0.44    |    64.56  |
|ARIMA (4,1,4)     | Lasso               |    0.44    |    64.56  | 
|SARIMA (1,0,1,24) | KNN                 |    0.42    |    67.56  |
|SimpleExpSmoothing| Decision Tree       |    0.374   |    74.38  |
|Holt method       | XG Boost            |    0.314   |    81.87  |
|Exponential Add   | Random Forest       |    0.343   |    78.45  |
|Exponential Mul   | Neural Network      |    0.48    |    57.73  |

## Model Deployment:
I have used **Streamlit** library and **Heroku** platform to deploy the app.\
App URL :https://forecasting-pm.herokuapp.com/
