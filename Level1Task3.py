import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "C:/Users/ganes/Downloads/rayuduintern/Dataset .csv"
df = pd.read_csv(file_path)

df = df.dropna(subset=['Latitude', 'Longitude'])

plt.figure(figsize=(12, 6))
sns.scatterplot(x=df['Longitude'], y=df['Latitude'], hue=df['Aggregate rating'], palette="coolwarm", alpha=0.7)
plt.title("Restaurant Locations Colored by Aggregate Rating")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend(title="Rating")
plt.show()

top_cities = df['City'].value_counts().head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x=top_cities.values, y=top_cities.index, palette="viridis")
plt.title("Top 10 Cities with Most Restaurants")
plt.xlabel("Number of Restaurants")
plt.ylabel("City")
plt.show()

top_countries = df['Country Code'].value_counts().head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x=top_countries.values, y=top_countries.index, palette="coolwarm")
plt.title("Top 10 Countries with Most Restaurants")
plt.xlabel("Number of Restaurants")
plt.ylabel("Country Code")
plt.show()
