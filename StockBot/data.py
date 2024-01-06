"""
This class has function and attribute to query live stock data from Alpha Vantage using their freely available API.
"""
import requests
import pandas as pd



class AlphaVantageAPI:
    def __init__(self):
        self.api_key = 'R3VPI6DQAXPJCNVZ'
    

    def fetch_data(self, ticker, interval = '5min', output_size = 'full'):
        """Get daily time series of an equity from AlphaVantage API.

            Parameters
            ----------
            ticker : str
                The ticker symbol of the equity.
            interval: str, optional
                The interval between data points. e.g. '1min', '2min', etc.
                Default value is '5min'. 
            output_size : str, optional
                Number of observations to retrieve. "compact" returns the
                latest 100 observations. "full" returns all observations for
                equity. By default "full".

            Returns
            -------
            pd.DataFrame
                Columns are 'open', 'high', 'low', 'close', and 'volume'.
                All are numeric.
            """

        # url
        url = ("https://www.alphavantage.co/query?"
        "function=TIME_SERIES_INTRADAY&"
        f"symbol={ticker}&"
        f"interval={interval}&"
        f"&outputsize={output_size}&"
        f"apikey={self.api_key}")

        # make a pull request
        r = requests.get(url)

        # fetch the json data from the API call
        response = r.json()

        # fetch the stock data
        stock_data = response['Time Series (5min)']
        # convert stock data to a dataframe
        df = pd.DataFrame.from_dict(stock_data, orient = "index", dtype = float)
        # Convert index to `DatetimeIndex` named "date"
        df.index = pd.to_datetime(df.index)
        df.index.name = "date"

        # Remove numbering from columns (8.1.15)
        df.columns = [c.split(" ")[1] for c in df.columns]

        # sort dataframe for more current data to be at the bottom
        df = df.sort_index()

        # Return DataFrame
        return df

    
