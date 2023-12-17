# Climate Prediction Project

## Overview

This project aims to explore the climate of Konongo Odumase (Latitude 6.6237, Longitude -1.2132) and build time series models to predict rainfall and temperature for this area. The community is predominantly a farming community, with over 90% of the people engaged in farming activities. Given the community's heavy reliance on climate conditions for planting and harvesting, accurate weather predictions can significantly impact their farming decisions.

## Motivation

The motivation behind this project is to alleviate the challenges faced by the farming community in Konongo Odumase. By developing accurate time series models for predicting rainfall and temperature, farmers can make informed decisions about their agricultural activities, leading to improved crop yield and better livelihoods.

## Dataset

The dataset used for this project is sourced from the NASA Power Data Center, utilizing MEERA-2 satellite data. The dataset provides valuable climate information that forms the basis for our exploratory data analysis (EDA) and time series modeling.

## Methodology

### Exploratory Data Analysis (EDA)

A thorough EDA was conducted on the dataset to understand the patterns, trends, and anomalies in the climate data. This step was crucial in informing subsequent modeling decisions and ensuring a comprehensive understanding of the underlying data.

### Time Series Models

AR (AutoRegressive) and ARIMA (AutoRegressive Integrated Moving Average) models were built for both temperature and rainfall. These models leverage historical climate data to make predictions for future time points. The goal is to provide accurate forecasts that can aid farmers in planning their agricultural activities.


## Results

The project outcomes, including model predictions and evaluation metrics:

The following table summarizes the performance of the models:

| Model | Climate | Mean Absolute Error |
|-------|---------|----------------------|
| AR    | Temperature | 0.4874 |
| ARIMA | Temperature | 0.4826 |
| AR    | Rainfall    | 2.5897 |

The mean absolute error provides an indication of the average absolute difference between the observed and predicted values. Lower values indicate better model performance.
More about the models' prediction can be found in the notebook of this project, `weather_prediction.ipynb`


# Future Improvements

- Explore additional modeling techniques for enhanced accuracy.
- Incorporate real-time weather data for more up-to-date predictions.
- Develop a user-friendly interface for farmers to access predictions easily.


## Project Structure

- `data/`: Contains the dataset used for the project.
- `notebooks/`: Jupyter notebooks documenting the EDA and modeling process.
- `src/`: Source code for data processing, modeling, and any utility functions.
- `results/`: Stores the model outputs, such as predictions and evaluation metrics.

## Getting Started

To replicate or extend this project, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/climate-prediction.git
