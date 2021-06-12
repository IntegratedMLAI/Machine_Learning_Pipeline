import pandas as pd
import numpy as np
import numpy.random as nr
import sklearn.model_selection as ms
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import General_Tools as gt

from sklearn.linear_model import LinearRegression

""" Load the Fake Data Into a Pandas DataFrame """
df_XY = pd.read_csv(
    "./1_Fake_Data_Creation/dbl_feature_linear_data.csv", header=None)
df_XY.columns = ['X1', 'X1-3', 'X2', 'X2-2', 'Y']
print("The Data Frame with X and Y:")
print(df_XY)
print()

""" Convert the DataFrame to a Values Array """
XY_Values = df_XY.values
print("Just The X and Y Values:")
print(XY_Values)
print()

""" Split the X and Y from the XY_Values """
X = XY_Values[:, [0, 2, 3]]
Y = XY_Values[:, -1]
print("The X and Y Values Separately")
print("The X Values")
print(X)
print()
print("The Y Values")
print(Y)
print()

""" Randomize 100 Indices and Split into Train and Test """
nr.seed(9988)
total_pt_cnt = X.shape[0]
num_test_pts = int(total_pt_cnt / 4)
indx = range(X.shape[0])
indx = ms.train_test_split(indx, test_size = num_test_pts)
print("Inspecting the Indices Used for Train and Test Sets")
print(f'Train Set Size: {len(indx[0])}, Test Set Size: {len(indx[1])}')
print()
print("Train Set Indices")
indx[0].sort()
print(indx[0])
print()
print("Test Set Indices")
indx[1].sort()
print(indx[1])
print()

""" Format the 1D Data Arrays Back to 2D Arrays """
x_train = X[indx[0], :]  # .reshape(-1, 1)
y_train = Y[indx[0]]  # .reshape(-1, 1)
x_test = X[indx[1], :]  # .reshape(-1, 1)
y_test = Y[indx[1]]  # .reshape(-1, 1)

""" Visualize What We Have for Train and Test """
fig = plt.figure()
ax = plt.axes(projection='3d')
 
ax.scatter3D(x_train[:, 0], x_train[:, 1], y_train, color='b')
ax.scatter3D(x_test[:, 0], x_test[:, 1], y_test, color='r')
ax.set_xlabel('X1 Values')
ax.set_ylabel('X2 Values')
ax.set_zlabel('Y Values')
ax.set_title('3D Plot Of Linear Fake Data')

plt.show()

""" Load the Linear Regression Model 
    and Fit with Training Data """
mod = LinearRegression(
    fit_intercept=False,
    normalize=False,
    positive=False)
mod.fit(x_train, y_train)
print("The Model Coefficients:")
print(f'The Y Intercept: {mod.intercept_}')
print(f'The Slope / Model Weight: {mod.coef_}')
print()

y_pred = mod.predict(x_test)
print("The Model Performance Metrics:")
gt.print_metrics(y_test, y_pred, 1)

fig = plt.figure()
ax = plt.axes(projection='3d')
 
ax.scatter3D(x_test[:, 0], x_test[:, 1], y_test, 'blue')
ax.plot3D(x_test[:, 0], x_test[:, 1], y_pred, 'red')
ax.set_xlabel('X1 Values')
ax.set_ylabel('X2 Values')
ax.set_zlabel('Y Values')
ax.set_title('3D Plot Of Linear Fake Data')
plt.show()
