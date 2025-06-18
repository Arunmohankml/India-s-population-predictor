import pandas as pd  
import numpy as np  
from sklearn.linear_model import LinearRegression  
  
data = pd.read_csv("population.csv")  
x=data["year"].values.reshape(-1,1)  
y=data["population"].values  
model= LinearRegression()  
model.fit(x,y)  
  
maxyear=2100  
while True:  
	year=int(input("Enter the year: "))  
	if year == 0:  
		print("Enter a valid year")  
	else:  
		if(year <= maxyear):  
			predicted=model.predict([[year]])  
			print(f"Predicted population in the year {year} is: {int(predicted[0])}")  
		else:  
			print(f"The year {year} is out of training range , you can predict upto year {maxyear}")  
