# William
# 03/14/2023

import numpy as np
import datetime as dt
import yfinance as yf

def calculate_beta_of_a_stock():
    '''Beta is a measure to determine the volatility of an asset or portfolio in relation to the overall market.
    A stock that swings more than the market over time has a beta greater than 1.0. If a stock moves less than the market, the stock's beta is less than 1.0.
    As a result, beta is often used as a risk-reward measure, meaning it helps investors determine how much risk they are willing to take to achieve the return for taking on that risk.
    
    Index used to calculate beta is S&P 500. 
    Data s
    '''

    #get tickers
    tickers = input(f"Please enter the tickers you you want separated by a space.\nExample: aapl tsla msft\nInvalid tickers will fail to be pulled by database. Enter:").strip().lower()
    index = "^GSPC"
    tickers = tickers+" "+index


    #set time period range or value
    time_period_start = dt.datetime(2018,3,1)
    time_period_end = dt.date.today()

    #fetching data for tickers
    data = yf.download(tickers,time_period_start,time_period_end)

    # adjusting data so it only has adj close and date info for all tickers
    adjusted_close_data = data.loc[:,"Adj Close"]

    # to calculate returns you normally see ((x-y)/y) + 1 which is equal to y/x
    #We now need to find the natural log of our returns. we do this because we are accounting for continuous compounding read here https://medium.datadriveninvestor.com/why-we-use-log-returns-for-stock-returns-820cec4510ba
    log_returns=np.log(data.loc[:,"Adj Close"]/data.loc[:,"Adj Close"].shift())

    #covariance calc -  Covariance is the measure of a stocks return to that market
    covariance = log_returns.cov()

    #Variance Calc - Variance is the measure of how the market moves relative to the mean (expected vs actual)
    index_variance = log_returns[index].var()

    
    #beta Calc
    beta_calculation = covariance.loc[index]/index_variance
    print(beta_calculation)

    return beta_calculation,adjusted_close_data, log_returns