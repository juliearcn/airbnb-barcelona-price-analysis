import pandas as pd
import numpy as np

#Data Loading
df = pd.read_csv("/Users/edaarcn/Documents/airbnb-barcelona-price-analysis/data/listings.csv")

#Data Cleaning
df = df.dropna(subset=["price"]) #Remove rows where values are NaN in the price column

q95 = df["price"].quantile(0.95)

df = df[df["price"] <= q95]
#print(df.shape)

df.to_csv("listings_clean.csv", index = False)

"""df_new = pd.read_csv("/Users/edaarcn/Documents/airbnb-barcelona-price-analysis/listings_clean.csv")
print(df.shape)"""

