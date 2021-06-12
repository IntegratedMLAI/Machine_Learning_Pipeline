"""Data Acquisition And Fake Data Generation
In this case, we will actually put models in functions to create
fake classification data with noise, store it, and load it back.

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

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import json

def create_np_clusters(np_seeds, half_range, points_per_cluster):
    num_seeds = np_seeds.shape[0]
    num_dims = np_seeds.shape[1] - 1

    pts = np.empty((num_seeds * points_per_cluster, num_dims + 1))
    labels = np.unique(np_seeds[:, 0])
    for label in labels:
        centers = np_seeds[np_seeds[:, 0] == label, 1:]
        centers = np.tile(centers, (points_per_cluster, 1))
        num_noise_points = centers.shape[0]
        base_noise = np.random.random_sample((num_noise_points, num_dims))
        adjusted_noise = half_range * (2 * base_noise - 1) + centers
        cluster_array = np.zeros((num_noise_points, 1)) + label
        start = int(label * num_noise_points)
        stop = int((label + 1) * num_noise_points)
        pts[start:stop, :] = np.hstack((cluster_array, adjusted_noise))

    return pts

def scatter_plot_points(np_pts):
    num_pts = np_pts.shape[0]
    dims = np_pts.shape[1] - 1
    
    if dims == 2:
        plt.scatter(np_pts[:, 1], np_pts[:, 2], 
                    c=np_pts[:, 0].astype('int'))
        plt.xlabel('X1 Vals')
        plt.ylabel('X2 Vals')
        plt.title('Fake Data Points')
    elif dims == 3:
        fig = plt.figure()
        ax = plt.axes(projection='3d')
    
        X = [pts[i][1] for i in range(num_pts)]
        Y = [pts[i][2] for i in range(num_pts)]
        Z = [pts[i][3] for i in range(num_pts)]
        L = [pts[i][0] for i in range(num_pts)]
        
        ax.scatter3D(X, Y, Z, c=L)
        
        ax.set_xlabel('X1 Values')
        ax.set_ylabel('X2 Values')
        ax.set_zlabel('X3 Values')
        ax.set_title('3D Plot Of Fake Classification Data')
 
    plt.show()

# seeds = [[1, 3, 8, 3], [2, 8, 3, 3], 
#          [3, 3, 3, 8], [4, 8, 8, 8]]
py_seeds = [[0, 3, 3], [1, 8, 8], [2, 3, 8], [3, 8, 3]]
np_pts = create_np_clusters(np.array(py_seeds), 2.2, 100)
print(np_pts[::40])  # Only show every 40th pt

scatter_plot_points(np_pts)

py_pts = np_pts.tolist()  # json no like numpy objects
with open(f'fake_data_classification.json', 'w') as f:
     json.dump(py_pts, f, ensure_ascii=False, indent=4)

with open('fake_data_classification.json') as f:
    clusters = np.array(json.load(f))

print('Cluster Data')
print(clusters[::20])  # only show every 20th point

### Another Model To Create Clusters

num_seeds = 400
num_groups = 2
group_pts = int(num_seeds / num_groups)

np_seeds = np.zeros((num_seeds, 3))
radians = np.arange(0, 2 * np.pi, (2 * np.pi) / group_pts)

for group_num, radius in ((0, 2), (1, 1)):
    start = group_num * group_pts
    stop = (group_num + 1) * group_pts
    np_seeds[start:stop, 0] = group_num
    np_seeds[start:stop, 1] = radius * np.cos(radians) + 5
    np_seeds[start:stop, 2] = radius * np.sin(radians) + 5

np_pts = create_np_clusters(np_seeds, 0.25, 2)
print(np_pts[::80])

## Plot The Model

scatter_plot_points(np_pts)
