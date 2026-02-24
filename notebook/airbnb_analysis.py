import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

#Data Loading
df = pd.read_csv("/Users/edaarcn/Documents/airbnb-barcelona-price-analysis/data/listings.csv")

print("Shape :", df.shape) #Dataset dimensions: (19410, 18)
print("\nColonnes :")
print(df.columns.tolist()) #Columns' name
"""Columns : ['id', 'name', 'host_id', 'host_name', 'neighbourhood_group', 'neighbourhood', 'latitude', 
'longitude', 'room_type', 'price', 'minimum_nights', 'number_of_reviews', 'last_review', 'reviews_per_month', 
'calculated_host_listings_count', 'availability_365', 'number_of_reviews_ltm', 'license']"""
print(df.head())
print("Missing price values:", df["price"].isna().sum()) #Missing price values: 4134

#Data Cleaning 
df = df.dropna(subset=["price"]) #Remove rows where values are NaN in the price column
print("Shape after:", df.shape) #Shape after: (15276, 18)

print(df["price"].describe())
"""
count    15276.000000
mean       187.312713 > Right-skewed distribution, indicating the presence of very high-priced listings
std        363.967170 > standard deviation
min          9.000000
25%         70.000000
50%        131.000000 > median
75%        215.000000
max      10000.000000"""

q95 = df["price"].quantile(0.95)
print("95e percentile:", q95) #425 euros

df = df[df["price"] <= q95] 
print("New shape:", df.shape) #New shape: (14513, 18)
#The top 5% of the highest prices were excluded to prevent extreme values from biasing the analysis.

print(df["price"].describe())
"""
count    14513.000000
mean       142.282092
std         90.651967
min          9.000000
25%         68.000000
50%        123.000000
75%        200.000000
max        425.000000"""

#Analysis 
#1. What is the impact of room type on price?

mean1 = df.groupby("room_type")["price"].mean() 
median1 = df.groupby("room_type")["price"].median() 
#Rows were grouped by room type, and the average price was calculated for each group.
print("Mean:\n", mean1)
print("\nMedian:\n", median1)
"""
Mean:                            Median: 
room_type
Entire home/apt    171.651016           162.0 > small difference, stable distribution
Hotel room         208.595745           200.0 > same as entire home/apt
Private room        80.476243           62.0  > mean significantly higher than the median (presence of a few higher-priced private rooms)
Shared room         58.196078           43.0"""

#Visualization
plt.figure(figsize=(8,5))

sns.boxplot(x="room_type", y="price", data=df)

plt.title("Price Distribution by Property Type")
plt.xlabel("Type de logement")
plt.ylabel("Prix (€)")
plt.xticks(rotation=45)

plt.show()

#2. How do prices vary across neighborhoods? 
print(df.groupby("neighbourhood_group")["price"].median().sort_values(ascending=False))
#Median, as prices remain skewed; the median better represents the “typical” price.
"""
Eixample               165.0
Les Corts              146.0
Gràcia                 135.0
Sant Martí             135.0
Sarrià-Sant Gervasi    130.0
Sants-Montjuïc         112.0
Ciutat Vella            89.0 
Sant Andreu             78.0
Horta-Guinardó          74.0
Nou Barris              64.0
La localisation influence fortement le prix."""
print(df.groupby("neighbourhood_group")["room_type"].value_counts())
"""
Ciutat Vella         Entire home/apt    2120
                     Private room       1192
                     Hotel room            5
                     Shared room           4
Eixample             Entire home/apt    3513
                     Private room       1450
                     Shared room          52
                     Hotel room           29
Gràcia               Entire home/apt     931
                     Private room        354
                     Shared room          12
                     Hotel room            6
Horta-Guinardó       Entire home/apt     223
                     Private room        174
Les Corts            Entire home/apt     226
                     Private room         79
                     Shared room           2
Nou Barris           Private room         99
                     Entire home/apt      85
Sant Andreu          Entire home/apt     117
                     Private room        106
                     Shared room           2
Sant Martí           Entire home/apt    1000
                     Private room        357
                     Shared room          16
                     Hotel room            3
Sants-Montjuïc       Entire home/apt     976
                     Private room        450
                     Shared room           7
                     Hotel room            4
Sarrià-Sant Gervasi  Entire home/apt     606
                     Private room        306
                     Shared room           7"""

#Cross-Analysis (Neighborhood x Room Type)
print(df.groupby(["neighbourhood_group", "room_type"])["price"].median())
"""
Ciutat Vella         Entire home/apt    100.5
                     Hotel room         243.0
                     Private room        73.0
                     Shared room         63.0
Eixample             Entire home/apt    198.0
                     Hotel room         181.0
                     Private room        63.5
                     Shared room         46.0
Gràcia               Entire home/apt    163.0
                     Hotel room         203.5
                     Private room        55.5
                     Shared room         39.5
Horta-Guinardó       Entire home/apt    124.0
                     Private room        45.0
Les Corts            Entire home/apt    161.0
                     Private room        59.0
                     Shared room         53.5
Nou Barris           Entire home/apt    174.0
                     Private room        45.0
Sant Andreu          Entire home/apt    101.0
                     Private room        54.5
                     Shared room         53.5
Sant Martí           Entire home/apt    161.0
                     Hotel room         312.0
                     Private room        62.0
                     Shared room         43.0
Sants-Montjuïc       Entire home/apt    152.0
                     Hotel room         176.5
                     Private room        55.0
                     Shared room         42.0
Sarrià-Sant Gervasi  Entire home/apt    150.5
                     Private room        51.0
                     Shared room         22.0"""

#3. Does the number of reviews influence pricing?
print(df["number_of_reviews"].describe())
"""
count    14513.000000
mean        61.766279
std        120.613000
min          0.000000
25%          1.000000
50%          9.000000
75%         69.000000
max       1820.000000
The distribution of the number of reviews is highly skewed: 
the majority of listings have fewer than 10 reviews, while a small minority concentrate a very high volume of reviews.
"""

#Visualization
"""plt.scatter(df["number_of_reviews"], df["price"])
plt.xscale("log")
plt.title("Prix vs Nombre d'avis")
plt.xlabel("Nombre d'avis")
plt.ylabel("Prix (€)")
plt.show()"""

print((df["number_of_reviews"] == 0).sum())

print(df.groupby(df["number_of_reviews"] == 0)["price"].median())
#False    140.0 et True      91.0