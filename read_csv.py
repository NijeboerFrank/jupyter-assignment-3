import pandas as pd

posts = "Assignment 23-09-2019 - Forensics - Sheet1.csv"

df = pd.read_csv(posts)
df["Legal"] = df["Legal"].apply(str.capitalize)

sellers = "Assignment 23-09-2019 - Forensics - Sellers.csv"

seller_df = pd.read_csv(sellers)


