#============ Import related libraries =================
from flask import redirect, request
import numpy as np
from scipy import spatial
import pandas as pd
import matplotlib.pyplot as plt
from sko.ACA import ACA_TSP
import mpld3
import os
if os.path.exists("templates/index.html"):
       os.remove("templates/index.html")
 # adding the element
def ant():
num_points = int(request.form.get('nbr'))
points_coordinate =  np.array(liste) # Generate the coordinates of the point
print(points_coordinate)
distance_matrix = spatial.distance.cdist(points_coordinate, points_coordinate, metric='euclidean')# The function is used to calculate the distance between two input sets
def cal_total_distance(routine):
 num_points, = routine.shape
 return sum([distance_matrix[routine[i % num_points], routine[(i + 1) % num_points]] for i in range(num_points)])
#=============ACA_TSP solve ==================================
aca = ACA_TSP(func=cal_total_distance, n_dim=num_points,
size_pop=50, max_iter=200,
distance_matrix=distance_matrix)
best_x, best_y = aca.run()
#============= visualization =======================
fig, ax = plt.subplots(1, 2)
best_points_ = np.concatenate([best_x, [best_x[0]]])
best_points_coordinate = points_coordinate[best_points_, :]
ax[0].plot(best_points_coordinate[:, 0], best_points_coordinate[:, 1], 'o-r')
pd.DataFrame(aca.y_best_history).cummin().plot(ax=ax[1])


html_str = mpld3.fig_to_html(fig)
Html_file= open("website/templates/index.html","w")
Html_file.write(html_str)
Html_file.close()






    