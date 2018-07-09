#%%
#loading required libs
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor

from sklearn.model_selection import cross_val_score, KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn import datasets

#%%
#Loading the dataset
boston = datasets.load_boston()
X = boston.data[:,0:13]
y = boston.target

#%%
#define model
def model():
    #create
    model = Sequential()
    model.add(Dense(13, input_dim = 13, kernel_initializer = 'normal', activation = 'relu'))
    model.add(Dense(6, kernel_initializer='normal', activation='relu'))
    model.add(Dense(1,kernel_initializer = 'normal'))

    #compile
    model.compile(loss='mean_squared_error', optimizer = 'adam')
    return model

#%%
#standardize the dataset
seed = 7
np.random.seed(seed)
estimators = []
estimators.append(('standardize', StandardScaler()))
estimators.append(('mlp', KerasRegressor(build_fn=model, epochs = 200, batch_size = 5, verbose=1)))
pipeline = Pipeline(estimators)
kfold = KFold(n_splits=10, random_state=seed)
results = cross_val_score(pipeline, X, y, cv=kfold)
print("Wider: %.2f (%.2f) MSE" % (results.mean(), results.std()))



