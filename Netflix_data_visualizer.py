import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("C:\\Users\\shafe\\OneDrive\\Desktop\\testdata\\netflix_titles.csv")
# print(data.info)

# print(data.describe())

# print(data.head())

# print(data.isnull().sum())

data.drop("director",axis=1,inplace=True)
data['country'].fillna('Unknown',inplace=True)
data['cast'].fillna('Unknown',inplace=True)
data['rating'].fillna('Not Rated',inplace=True)
data.drop("duration",axis=1,inplace=True)
data.drop("date_added",axis=1,inplace=True)
# print(data.isnull().sum())

listed_in= (data['listed_in'].str.split(","))
data['listed_in']=data['listed_in'].str.split(",")
print(listed_in.head())
data['listed_in']=data['listed_in'].apply(lambda x : [genre.strip() for genre in x])
all_genre =[genre for sublist in data['listed_in'] for genre in sublist]

genre_series = pd.Series(all_genre)
genre_counts = genre_series.value_counts()
print(genre_counts.head(10))

top_genre = genre_counts.head(10)

print(top_genre)
top_genre.plot(kind='bar')
plt.title("Top 10 Genres on Netflix")
plt.xlabel("Genre")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.show()