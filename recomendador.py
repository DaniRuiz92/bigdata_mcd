# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 08:56:27 2017

@author: Daniel
"""
import pandas as pd
import numpy as np

url_users = 'https://raw.githubusercontent.com/wesm/pydata-book/master/ch02/movielens/users.dat'
url_ratings = 'https://raw.githubusercontent.com/wesm/pydata-book/master/ch02/movielens/ratings.dat'
url_movies = 'https://raw.githubusercontent.com/wesm/pydata-book/master/ch02/movielens/movies.dat'

users = pd.read_csv(url_users,header=None, delimiter="::").rename(columns={0:'userid', 1:'gender', 2: 'age', 3: 'occupation', 4:'zipcode'})
ratings = pd.read_csv(url_ratings,header=None, delimiter="::").rename(columns={0: 'userid', 1: 'movieid', 2: 'rating', 3:'timestamp'})
movie = pd.read_csv(url_movies,header=None, delimiter="::").rename(columns={0: 'movieid', 1: 'title', 2: 'genre'})

merged = pd.merge(ratings,movie, on=['movieid'])
merged = pd.merge(merged,users,on=['userid'])
data = merged.copy()

del users, ratings, movie, url_users, url_ratings, url_movies, merged

print(np.unique(data.loc['genre']))
