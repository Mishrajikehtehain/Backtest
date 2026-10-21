import pandas as pd
import yfinance as yf

#Symbol Input
inp = "GOOG"

ticker = yf.Ticker(inp)
df = ticker.history(period = "30d", interval = "1d")

#cleaning data
#Removing Duplicates
df = df.loc[~df.index.duplicated(keep='first')]
#Removing NaN 
df = df.dropna(subset=['Open', 'High', 'Low', 'Close'])
#Removing Anamolies
df = df[(df['Close'] > 0) & (df['Volume'] >= 0)]

#Saving In CSV
df.to_csv(r"X:\Portfolio\Historic_Data\%s_historic_data.csv"%(inp))

print("Saved!")