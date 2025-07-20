import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("C:\\Users\\shafe\\OneDrive\\Desktop\\testdata\\time-series-19-covid-combined.csv")

print(data.head())

print(data.info())


data['Recovered'].fillna(0,inplace=True)
data.drop('Province/State',axis = 1, inplace =True )
print(data.isnull().sum())

grouped = data.groupby('Country/Region')

confirmed = grouped['Confirmed']

tot_confirmed = confirmed.sum()

sort_confirm = tot_confirmed.sort_values(ascending = False)

print(sort_confirm.head(10))

sort_confirm.head(10).plot(kind='bar')
plt.tight_layout()
plt.ylabel("number of cases")
plt.title("total confirmed cases")
plt.show()