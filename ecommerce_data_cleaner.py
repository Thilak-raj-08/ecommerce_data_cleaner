import pandas as pd

df = pd.read_csv("raw_orders.csv")
print(df.head(5))
print(df.shape)
print(df.dtypes)
original_rows = len(df)

duplicate_count = df.duplicated().sum()
print(duplicate_count)
print(df[df.duplicated()].head(5))

df = df.drop_duplicates()
print(df.shape)


invalid_quantity_mask = df["Quantity"] <= 0
invalid_quantity_count = invalid_quantity_mask.sum()
print(invalid_quantity_count)
print(df[invalid_quantity_mask].head(5))


df = df[df["Quantity"] > 0].copy()
print(df.shape)
print((df["Quantity"] <= 0).sum())

missing_prices_before = df["Price"].isna().sum()
print(missing_prices_before)
print(df[df["Price"].isna()].head(5))


product_medians = df.groupby("Product")["Price"].transform("median")
print(product_medians.head(10))

df["Price"] = df["Price"].fillna(product_medians)
print(df["Price"].isna().sum())
print(df.head(5))

df["City"] = df["City"].str.strip().str.title()
print(df["City"].unique())

df["Order_Date"] = pd.to_datetime(
    df["Order_Date"],
    format="mixed",
    dayfirst=True,
    errors="coerce"
)
invalid_date_count = df["Order_Date"].isna().sum()
print(invalid_date_count)
print(df["Order_Date"].head(5))

df = df.dropna(subset=["Order_Date"]).copy()
print(df.shape)
print(df["Order_Date"].isna().sum())


print(df.isna().sum())
print(df.duplicated().sum())
rows_removed = original_rows - len(df)
print("Rows Removed:", rows_removed)
df.to_csv("clean_orders.csv", index=False)


