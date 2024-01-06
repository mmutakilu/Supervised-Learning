"""
This script contains everything about the trading bot. 
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



class StockBot:
    """
    This class creates a simple trading bot using the Simple Moving Average(SMA) crossover strategy. The 'stockbot' method does 
    this magic.
    """
    def __init__(self):
        pass
  
    def stockbot(self, dataset, short_window, long_window):
        """
        This method creates a simple trading bot using the SMA strategy. When the short-term SMA crosses above the long-term SMA
        it signals a BUY and with the otherwise, it signals a SELL.
        
        Parameters
        ==========
        - dataset: dataframe
          The stock dataset.
        - short_window: int 
          The short window e.g. 20 for 20 days
        - long_window
          The long window e.g. 200 for 200 days
        """
        # re-assign the stock dataset
        data = dataset

        # calculate short-term and long-term SMAs
        data['short_sma'] = data['close'].rolling(window = short_window, min_periods=1).mean()
        data['long_sma'] = data['close'].rolling(window = long_window, min_periods=1).mean()

        # generate signals
        data['signal'] = 0.0
        data['signal'][short_window:] = np.where(data['short_sma'][short_window:] > data['long_sma'][short_window:], 1.0, 0.0)

        # generate trading orders
        data['position'] = data['signal'].diff()

        return data
    
    

    
class StockViz:
    """
    This class has a method to visualize the stock bot's predictions.
    """
    def __init__(self):
        pass

    def stockviz(self, data, short_window, long_window):
        """
        A method to visualize the buy and sell signals. 
        
        Parameters:
        ===========
        - data: dataframe
          The stock dataframe.
        - short_window: int
          The short window e.g. 20 for 20 days
        - long_window
          The long window e.g. 200 for 200 days
        """
        # plot stock prices and the SMAs
        sns.set(rc = {'figure.figsize': (12, 6)})
        plt.plot(data['close'], label = 'close price', color = 'b')
        plt.plot(data['short_sma'], label=f'short {short_window} days SMA', color='orange')
        plt.plot(data['long_sma'], label=f'long {long_window} days SMA', color='green')

        # Plot buy signals
        plt.plot(data[data['position'] == 1.0].index, data['short_sma'][data['position'] == 1.0],
                  '^', markersize=10, color='g', lw=0, label='Buy Signal')

        # Plot sell signals
        plt.plot(data[data['position'] == -1.0].index, data['short_sma'][data['position'] == -1.0],
                  'v', markersize=10, color='r', lw=0, label='Sell Signal')

        # Label the chart
        plt.title('Stock Price with SMA Trading Signals')
        plt.xlabel('Date')
        plt.ylabel('Stock Price')
        plt.legend()
        plt.show();