"""Data Acquisition And Fake Data Generation
In this case, we will actually put models in functions
to create fake regression data with noise, store it, and load it back.

Our goals for creating good fake regression data are to:
1. create fake features;
2. create constant random noise OR create noise that varies as a 
   function of features and/or labels as needed;
3. feed the fake features into a model that generates the labels
4. add the noise to the features

The few ways that we will show will work for most cases. 
However, we PROMISE that you will run into something weird. 
Stay calm, py-thon, and search. Your growing coding and logic
and concept skills will serve you well. Search multiple references 
for your issue, and you will get over your problem soon."""

# pip install plotly-express

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# import plotly.express as px


def feature_column(start, stop, num_pts):
    step = (stop - start)/num_pts
    the_pts = np.arange(start, stop, step)
    return the_pts

def noise_envelope(Dims, Amp):
    return Amp * (2 * np.random.random_sample(Dims) - 1)

def model(X):
    return (1.50 * X[:, 0] + 
         0.05 * X[:, 0] ** 2 +
         0.03 * np.multiply(X[:, 0], X[:, 1]) + 
         0.75 * X[:, 1] + 
         0.01 * X[:, 1] ** 2)


num_pts = 300
X = np.zeros((num_pts, 2))  # print(X.shape)
X[:, 0] = feature_column(0, 30, num_pts)
X[:, 1] = 10 * np.sin(feature_column(0, np.pi, num_pts))

Y = model(X) + noise_envelope(num_pts, 7)

fake_df = pd.DataFrame( data=np.hstack((X, Y.reshape(-1, 1))) )
fake_df.columns = ['x1', 'x2', 'y']
print(fake_df.head(7))  # show top 7 lines, default = 5
print()

print(fake_df.corr())

# fig = px.scatter_3d(fake_df, x='x1', y='x2', z='y')
# fig.show()