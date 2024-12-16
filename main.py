from FetchData import get_stock_data, read_stock_data, clean_data

# How to fetch the stock historical data?
## Set the stock symbol
### Common stock symbols:
### Apple: AAPL; S&P500: ^GSPC; Nasdaq: ^IXIC; Nvidia: NVDA, Tesla: TSLA 

# Fetch the stock data:
try:
    # Try to read the stock data from the CSV file
    file_path = "./stock_data/AAPL_2000-12-15_2024-12-15.csv"
    stock_data = read_stock_data(file_path)
except FileNotFoundError as e:
    print(f"Error: {e}. Attempting to fetch stock data online.")
    
    try:
        # If reading fails, fetch the stock data online
        stock_data = get_stock_data('AAPL', start_date='2000-12-15', end_date='2024-12-15', export_csv=True)
    except Exception as e:
        # If fetching also fails, return the error
        print(f"Failed to fetch stock data online: {e}")
        stock_data = None  # or handle the error as needed

cleaned_stock_data = clean_data(stock_data, True)