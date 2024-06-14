import pandas as pd
import matplotlib.pyplot as plt

company = str(input("Apple\nGoogle\nMicrosoft\nAmazon\nNvidia\nAMD\nIntel\nChoose a company: "))

df = pd.read_csv(f"./data/{company.lower()}_stock_data.csv")

df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(by = 'Date')

df['Close/Last'] = pd.to_numeric(df['Close/Last'].str.replace("$", ""), errors = "coerce")
df['Open'] = pd.to_numeric(df['Open'].str.replace("$", ""), errors = "coerce")
df['High'] = pd.to_numeric(df['High'].str.replace("$", ""), errors = "coerce")
df['Low'] = pd.to_numeric(df['Low'].str.replace("$", ""), errors = "coerce")

plt.figure(figsize = (15, 8))
plt.plot(df['Date'], df['Close/Last'])
plt.xlabel("Date")
plt.ylabel("Closing Price (in USD)")
plt.title(f"{company.upper()} Stock Data")
plt.show()