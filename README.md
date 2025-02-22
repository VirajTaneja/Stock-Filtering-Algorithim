Stock Screener and Trading Algorithm
This project is a Python-based stock screener and trading algorithm that scans the NASDAQ, S&P 500, and Dow Jones indices to identify the top 5 daily gainers with the following criteria:

Stock price above $3
Negative EPS (indicating unprofitable companies)
PE ratio greater than 25

Features
Real-Time Data Analysis: Utilizes the yfinance library to fetch and analyze live stock data.
Custom Financial Filters: Screens stocks based on specific financial metrics including price, EPS, and PE ratio.
Top Gainers Identification: Displays the top 5 gainers that match the criteria.


The output will display the top 5 gainers that meet the filtering criteria, along with key financial metrics.

🔍 Example Output

Top 5 Gainers:
1. Ticker: ABC | Price: $12.34 | EPS: -0.45 | PE Ratio: 30.2
2. Ticker: XYZ | Price: $8.76 | EPS: -0.12 | PE Ratio: 27.8
3. ...

How It Works
Fetches real-time stock data for NASDAQ, S&P 500, and Dow Jones indices.
Filters stocks based on:
Price > $3
EPS < 0
PE Ratio > 25
Ranks the top 5 gainers of the day that match the criteria.
Displays relevant financial metrics for each stock.

Future Enhancements
Integrate additional financial metrics for more robust filtering.
Implement historical performance analysis.
Integrate trading APIs for automated trading actions.

Thanks for Reading!
