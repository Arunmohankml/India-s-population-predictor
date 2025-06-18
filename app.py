import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("population.csv")

latest_year=data["Year"].max()
latest_data=data[data["Year"]==latest_year]

new=latest_data.sort_values(by="Value", ascending=False).head(10)
print(new["Country Name"])
plt.bar(new["Country Code"], new["Value"])
plt.title("2023 population data")
plt.xlabel("countries")
plt.ylabel("population")
plt.savefig("population.png")
