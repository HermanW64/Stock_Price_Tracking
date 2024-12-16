import yfinance as yf
import pandas as pd

def get_stock_data(ticker, start_date, end_date, export_csv) -> pd.DataFrame:
    """
    fetch the stock price historical data
    
    ticker: str, stock symbol
    start_date: str, for example: '2000-12-15'
    end_date: str, same as start_date
    export_csv: bool, export the data to a csv file or not
    
    return pd.DataFrame
    """
    stock_data = yf.download(ticker, start=start_date, end=end_date)

    # list data field information
    if export_csv:
        file_path = "./stock_data/" + ticker + "_" + start_date + "_" + end_date + ".csv"
        stock_data.to_csv(file_path)
        print("online stock data saved to " + file_path)

    return stock_data


def read_stock_data(file_path) -> pd.DataFrame:
    """
    read the stock data from a csv file locally
    """
    stock_data = pd.read_csv(file_path)
    print("stock data read locally from: " + file_path)

    return stock_data

def clean_data(stock_data: pd.DataFrame, show_data= False) -> pd.DataFrame:
    """
    clean the stock data
    The columns of dataset look like:
        Price,Adj Close,Close,High,Low,Open,Volume
        Ticker,AAPL,AAPL,AAPL,AAPL,AAPL,AAPL
        Date,,,,,,
    """
    # Remove the entire second and third rows (index 0, 1): we know the stock symbol before
    stock_data = stock_data.drop(index= [0, 1])
    
    # replace "Price" with "Date" in columns: we know the cell values are prices
    stock_data.columns = stock_data.columns.str.replace("Price", "Date")
    
    # remove all NA rows:
    stock_data = stock_data.dropna()
    
    # ensure right field data types
    stock_data['Date'] = pd.to_datetime(stock_data['Date'])
    stock_data['Open'] = stock_data['Open'].astype(float)
    stock_data['High'] = stock_data['High'].astype(float)
    stock_data['Low'] = stock_data['Low'].astype(float)
    stock_data['Close'] = stock_data['Close'].astype(float)
    stock_data['Adj Close'] = stock_data['Adj Close'].astype(float)
    stock_data['Volume'] = stock_data['Volume'].astype(int)

    # round float values
    stock_data['Open'] = stock_data['Open'].round(4)
    stock_data['High'] = stock_data['High'].round(4)
    stock_data['Low'] = stock_data['Low'].round(4)
    stock_data['Close'] = stock_data['Close'].round(4)
    stock_data['Adj Close'] = stock_data['Adj Close'].round(4)
    
    # sort by date, in ascending order
    stock_data.sort_values(by="Date", ascending=True, inplace=True)
    print("stock data cleaned")

    # show data
    if show_data:
        print("cleaned stock data below: ")
        print(stock_data.head(50))

    return stock_data
    