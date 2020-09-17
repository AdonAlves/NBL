# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 12:40:12 2020

@author: adoor
"""

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import normalize
from sklearn.preprocessing import robust_scale
from sklearn import linear_model
from mlxtend.feature_selection import ExhaustiveFeatureSelector as EFS
import pandas as pd 
import matplotlib


from sklearn import linear_model

from mlxtend.feature_selection import ExhaustiveFeatureSelector as EFS
import pickle


data = pd.read_csv('NBL.csv')



# xy = data[['W','L','PCT', 'eDiff']]

# sns.pairplot(xy)



X = data.drop(columns=['Pace','W', 'L','FTM', 'FT%', 'OppFT%', 'OppFTM', 'PCT','PPS', 'FGM','FGA', '3PM', '3PA','TOV', 'AST','Opp3PA','TRB%', 'OppTRB%' ,'OppAST','OppREB' ,'OppSTL', 'OppBLK', 'STL','BLK','OppPPS', 'OppFGM', 'OppFGA', 'Opp3PM', 'OppTOV' , 'OppPPS', 'ORtg', 'DRtg', 'eDiff', 'ORB', 'DRB', 'REB','OppDRB', 'OppORB' ,  'OppTS%',  'OppTotal S%', 'OppFIC40', 'TS%', 'Total S%', 'Poss', 'FIC40', 'OppFIC40', 'FG%', '3P%', 'OppFG%', 'Opp3P%'])



z = [ 'PF',  'OppPF', ]
d = ['OppORB%', 'OppDRB%', 'OppAST%', 'OppTOV%', 'OppSTL%', 'OppBLK%','ORB%', 'DRB%', 'AST%', 'TOV%', 'STL%', 'BLK%']


f = data[['PCT', 'PF', 'OppPF', 'OppeFG%', 'OppORB%', 'OppDRB%', 'OppAST%', 'OppTOV%', 'OppSTL%', 'OppBLK%', 'eFG%', 'ORB%', 'DRB%', 'AST%', 'TOV%', 'STL%', 'BLK%']]
l = list(f.columns)
for i in z:
    f[i] = (f[i] / 28)  #/100

for i in d: 
    f[i] = f[i]/100

cor = f.corr()

Y = f[['PCT']]

X = f[['eFG%', 'OppeFG%' ,'ORB%', 'DRB%', 'TOV%', 'OppTOV%', 'STL%', 'OppPF']]
 
# X_scaled = robust_scale(X, axis=0) 



# for i in range(0, 63) :
#     plt.hist(X_scaled[i])
#     plt.suptitle(i)
#     plt.show()





# quantile_transformer = preprocessing.QuantileTransformer(
#     output_distribution='normal', random_state=42, n_quantiles=73)

# X_trans = quantile_transformer.fit_transform(X)

# plt.hist(z)



X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 5)

lr = linear_model.LinearRegression()
lasso = linear_model.Lasso()
ridge = linear_model.RidgeCV()
bayard = linear_model.ARDRegression()
# bayridge = line_mode.BayesianRidge()


models = [lr, lasso, ridge, bayard]

for model in models: 
    print(model)
    model.fit(X_train, y_train)
    print(model.score(X_test, y_test))
    print(model.intercept_)
    print(model.coef_)
 


# efs = EFS(lr, ### best subset index given 1, 2, 4,6,9,10,11,13,14 -> 'eFG%', 'OppeFG%' ,'ORB%','OppDRB%', 'DRB%', 'TOV%', 'OppTOV%', 'STL%', 'OppPF' , second run through can drop OppDRB% as its the inverse of ORB% 
#           min_features=1,
#           max_features=8,
#           scoring='neg_mean_squared_error',
#           cv=10)

# efs.fit(X_train, y_train)
# print('Best MSE score: %.2f' % efs.best_score_ * (-1))
# print('Best subset:', efs.best_idx_)

