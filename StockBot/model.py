"""
This class loads the built Garch model and provides users with method to forecast prices with ease.
"""

import pandas as pd
import joblib


#class VolatilityModel:
#    def __init__(self):
#        # load the Garch model
#        self.model = joblib.load('model.joblib')
#    
#    # method to forecast stock prices
#    def forecast_stock_price(self, forecast_days, start_date = '2023-12-26 19:55:00'):
#        # connect to the Garch model
#        model = self.model
#        # Create a datetime index for the forecast horizon
#        forecast_index = pd.date_range(start=pd.to_datetime(start_date), periods=forecast_days, freq='5T')
#        # forecast stock prices
#        forecast = model.forecast(horizon=forecast_days)
#        forecast = forecast.variance.iloc[-1].values
#        # convert forecast prices to dataframe
#        forecast = pd.DataFrame(forecast, index=forecast_index)
#
#        return forecast


class VolatilityModel:      
    def __init__(self, data):
        # build Garch model
        from sklearn.preprocessing import StandardScaler
        scaler = StandardScaler()
        self.data = scaler.fit_transform(data.values.reshape(-1, 1))
        #self.data = data
        from arch import arch_model
        self.model = arch_model(self.data, vol='Garch', p=2, q=2)
        self.model = self.model.fit(disp="off")

    # method to forecast stock prices
    def forecast_stock_price(self, forecast_days, start_date = '2023-12-26 19:55:00'):
        # connect to the Garch model
        model = self.model
        # Create a datetime index for the forecast horizon
        forecast_index = pd.date_range(start=pd.to_datetime(start_date), periods=forecast_days, freq='5T')
        # forecast stock prices
        forecast = model.forecast(horizon=forecast_days)
        forecast = forecast.variance.iloc[-1].values
        # convert forecast prices to dataframe
        forecast = pd.DataFrame(forecast, index=forecast_index)

        return forecast
