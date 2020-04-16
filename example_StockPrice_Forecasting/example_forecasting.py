# Example: Stock price forecasting
# Source: https://pythonprogramming.net/forecasting-predicting-machine-learning-tutorial/

import quandl, math
import numpy as np
import pandas as pd
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression

df = quandl.get("WIKI/GOOGL")
df = df[['Adj. Open',  'Adj. High',  'Adj. Low',  'Adj. Close', 'Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Close'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]
forecast_col = 'Adj. Close'
df.fillna(value=-99999, inplace=True)
forecast_out = int(math.ceil(0.01 * len(df)))
df['label'] = df[forecast_col].shift(-forecast_out)

X = np.array(df.drop(['label'], 1))
X = preprocessing.scale(X)
X = X[:-forecast_out]
df.dropna(inplace=True)
y = np.array(df['label'])
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

clf = LinearRegression(n_jobs=-1)
clf.fit(X_train, y_train)
confidence = clf.score(X_test, y_test)
print(confidence)

#handle all of the rows from the definition of X onward:
X = np.array(df.drop(['label'], 1))
X = preprocessing.scale(X)
X_lately = X[-forecast_out:]
X = X[:-forecast_out]

df.dropna(inplace=True)

y = np.array(df['label'])

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)
clf = LinearRegression(n_jobs=-1)
clf.fit(X_train, y_train)
confidence = clf.score(X_test, y_test)
print(confidence)


#Note that first we take all data, preprocess it, and then we split it up.
#Our X_lately variable contains the most recent features, which we're going to predict against.
#As you should see so far, defining a classifier, training, and testing was all extremely 
#simple. 

#Predicting is also super easy:
forecast_set = clf.predict(X_lately)

#The forecast_set is an array of forecasts, showing that not only could you just seek out 
#a single prediction, but you can seek out many at once. 

#To see what we have thus far:
print(forecast_set, confidence, forecast_out)

#Those forecasts are simply for one day out. Not accounting for weekends, holidays, etc.

#We import datetime to work with datetime objects, matplotlib's pyplot package for graphing, 
#and style to make our graphs look decent. 

import datetime
import matplotlib.pyplot as plt
from matplotlib import style

#Let's set a style:
style.use('ggplot')

#Next, we're going to add a new column to our dataframe, the forecast column:
df['Forecast'] = np.nan


#We said we're going to just start the forecasts as tomorrow 
#(recall that we predict 10% out into the future, and we saved that last 10% of our data 
#to do this, thus, we can begin immediately predicting since -10% 
#has data that we can predict 10% out and be the next prediction). 
#We need to first grab the last day in the dataframe, and begin assigning each new forecast 
#to a new day. 

#We will start that like so:
last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day

#Now we have the next day we wish to use, 
#and one_day is 86,400 seconds. 
#Now we add the forecast to the existing dataframe:
for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += 86400
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)]+[i]

#So here all we're doing is iterating through the forecast set, 
#taking each forecast and day, and then setting those values in the dataframe 
#(making the future "features" NaNs). The last line's code just simply takes all of 
#the first columns, setting them to NaNs, and then the final column is whatever i is 
#(the forecast in this case). I have chosen to do this one-liner for loop like this so that, 
#if we decide to change up the dataframe and features, the code can still work. 
#All that is left? Graph it!	

df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
	
	
	
