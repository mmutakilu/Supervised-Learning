# StockBot
StockBot is a stock trading bot designed to assist traders by providing signals for buying and selling stocks using a simple moving average (SMA). 
Additionally, the project includes a predictive model to forecast stock volatility. 
The bot is complemented by a Streamlit app that offers a user-friendly interface for deploying and visualizing the trading strategy.

## Key Features
- **Trading Strategy:** The bot employs a simple moving average (SMA) to generate signals for optimal entry and exit points in stock trading.
- **Volatility Prediction:** A predictive model is implemented to forecast stock volatility, aiding traders in risk management.
- **Streamlit App:** The app provides a dashboard to visualize the trading strategy, along with three tabs:
    - **Stock Data:** Displays detailed information about the selected stock.
    - **Predictions:** Presents the predictive model's output.
    - **Stock News:** Aggregates and showcases the latest top 5 news articles about the selected stock.

## File Arrangement
The project is organized into several key files:
- `model.py:` Contains the implementation of the predictive model used for forecasting stock volatility.
- `data.py:` Defines a class with methods to query live stock data from AlphaVantage using its free API.
- `bot.py:` Includes two classes:
    - `StockBot:` Implements the trading strategy based on the simple moving average (SMA).
    - `StockViz:` Provides visualization capabilities for the trading strategy.
- `main.py:` Houses the Streamlit app code, including the UI logic and integration with the trading strategy.

## Getting Started
### Installation
1. Clone the repository:
   ```bash
   $ git clone https://github.com/your-username/stockbot.git
   $ cd stockbot
2. Install the dependencies
   ```bash
   $ pip install -r requirements.txt

### To use the app (deploy it)
1. Run the streamlit app (in your terminal)
   ```bash
   $ streamlit run main.py
2. The app opens in your web browser (default address: http://localhost:8501).

3. Use the sidebar to select a stock, and other parameters.

## Contributing
Contributions are welcome! If you find a bug, have a feature request, or want to contribute in any way, please go ahead. Thanks🙏

## License
This project is licensed under the MIT License.


## Acknowledgments
- A special thanks to myself for taking on this challenge
- A thank you to the providers of the libraries I used for this project: `statsmodels, streamlit, Alpha Vantage` etc.
- A thumbs up to `Financial Programming with Ritvik, CFA`, the app layout was inspired by his YouTube video.
- Thanks to all for the support
  🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏
