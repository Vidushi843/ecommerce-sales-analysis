
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
import os
print("Files yahan save ho rahi hain:", os.getcwd())

df = pd.read_csv("sales_data.csv")

print("=== pehli 5 rows ===")
print(df.head())

print("\n=== Data ka size ===")
print("Rows aur columns:",df.shape)

print("\n===columns ki info===")
print(df.info())

print("\n=== missing values kahin hain?===")
print(df.isnull().sum())

df = df.drop_duplicates()
print("\n=== Duplicates htane ke baad size===")
print("Rows aur columns:",df.shape)

df["Quantity"] = df["Quantity"].fillna(df["Quantity"].mean())

df["Price"] = df["Price"].fillna(df["Price"].mean())

df["Date"] = pd.to_datetime(df["Date"])

print("\n=== Cleaning ke baad missing values===")
print(df.isnull().sum())

print("\n=== Data clean ho gaya!===")
print(df.head())

# Step 4: Analysis

# Total Revenue column banao (Quantity x Price)
df["Revenue"] = df["Quantity"] * df["Price"]

# Category wise total revenue
print("\n=== Category wise Revenue ===")
print(df.groupby("Category")["Revenue"].sum())

# Product wise total revenue
print("\n=== Top Products by Revenue ===")
print(df.groupby("Product")["Revenue"].sum().sort_values(ascending=False))

# Month wise revenue
df["Month"] = df["Date"].dt.month_name()
print("\n=== Month wise Revenue ===")
print(df.groupby("Month")["Revenue"].sum())

#step 5: Visulatization
plt.figure(figsize=(8,5))
sns.barplot(data=df.groupby("Category")["Revenue"].sum().reset_index(),
            x="Category",y ="Revenue", hue="Category",palette="Blues_d",legend=False)

plt.title("Category wise total Revenue")
plt.xlabel("Category")
plt.ylabel("Revenue(Rs.)")
plt.tight_layout()
plt.savefig("category_revenue.png")
plt.show()
print("Chart 1 save ho gaya!")

#chart 2:rop products by revenue
plt.figure(figsize=(10,5))
product_revenue = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False).reset_index()
sns.barplot(data=product_revenue,x="Product",y="Revenue",hue="Product",palette="Greens_d",legend=False)
plt.title("Top products by revenue")
plt.xlabel("Product")
plt.ylabel("Revenue(Rs.)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("product_revenue.png")
plt.show()
print("Chart 2 save ho gaya!")

#Chart 3 :Month wise revenue(Line chart)
plt.figure(figsize=(8,5))
month_revenue = df.groupby("Month")["Revenue"].sum().reset_index()
sns.lineplot(data=month_revenue,x="Month",y="Revenue",marker="o",color="red")
plt.title("Month wise Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue(Rs.)")
plt.tight_layout()
plt.savefig("month_revenue.png")
plt.show()
print("Chart 3 save ho gaya")

print('pandas library import hogyi')