import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
%matplotlib inline
############################################################
dataset = pd.read_csv('E:/covid/covid_19_data.csv')
dataset.shape
dataset.describe()
######################################################
dataset.plot(x='Hours', y='Scores', style='o')
plt.title('Hours vs Percentage')
plt.xlabel('Hours Studied')
plt.ylabel('Percentage Score')
plt.show()
########################################################
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values
##################################################################
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
##############################################################
regressor = LinearRegression()
regressor.fit(X_train, y_train)
#####################################################
print(regressor.intercept_)
#####################################################
print(regressor.coef_)
###################################################
y_pred = regressor.predict(X_test)
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
df
##########################################################
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))