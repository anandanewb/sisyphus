import pandas as pd
import numpy as np
import yfinance as yf


tickers = {
    'Anantraj': 'ANANTRAJ.NS',
    'TARC': 'TARC.NS'
}

cp  = {
    'Anantraj': 39.54,
    'TARC': 0
}

computations  = ['CG', 'LTCGTax']

column_multiindex = pd.MultiIndex.from_product([tickers.keys(), computations])  

ticker_prices = {}
ticker_prices['Anantraj'] = yf.Ticker(tickers['Anantraj']).history(period='1d')['Close'].iloc[0]
ticker_prices['TARC'] = yf.Ticker(tickers['TARC']).history(period='1d')['Close'].iloc[0]

quantities = np.arange(500,3000,500)
multiidx = pd.MultiIndex.from_product([tickers.keys(), computations])
df = pd.DataFrame(index=quantities, columns=multiidx)
df[('Anantraj', 'CG')] = ticker_prices['Anantraj'] * quantities
df[('Anantraj', 'LTCGTax')] = ( df[('Anantraj', 'CG')] - cp['Anantraj'] ) * 0.125
df[('TARC', 'CG')] = ticker_prices['TARC'] * quantities 
df[('TARC', 'LTCGTax')] = (df[('TARC', 'CG')] - cp['TARC']) * 0.125
df = df.round()