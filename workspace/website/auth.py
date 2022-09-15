from flask import Blueprint, render_template_string, request, redirect, flash, render_template
import numpy as np
from scipy import spatial
import pandas as pd
import matplotlib.pyplot as plt
from sko.ACA import ACA_TSP
import mpld3
import os
from website import views
import random
import json
from google.cloud import storage
import io




auth = Blueprint('auth', __name__)

@auth.route('/articles')
def articles():
    return render_template('articles.html')

@auth.route('/experiences' , methods=['GET', 'POST'])
def experiences():
        if request.method == 'POST':
           if request.form['scriptbutton'] == 'Run Script':
             return render_template('index.html')
        return render_template('experiences.html')


@auth.route('/ant-colony' , methods=['GET' , 'POST'])
def ant_colony():
    ant=[]
    if request.method == 'POST':
        a=str(random.randint(1,10))
        liste= request.form.get('nbr')
        l=liste.split(",")
        n=len(l)
        b=0
        try:
         for k in range(n//2):
            ant.append([])
         for i in range(n//2):
            for j in range(2):
                c=int(l[b])
                ant[i].append(c)
                b=b+1

         num_points = n//2
         points_coordinate =  np.array(ant) # Generate the coordinates of the point
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
         plt.title('la plus courte distance entre les pts')

         a=random.randint(1,100)
         a=str(a)
         fname="website/tmp/"+a+".png"
         fname1=a+".png"
         credential_path = "website/static/anil.json"
         os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path         
         storage_client = storage.Client()
         bucket = storage_client.bucket('anil-a3bb8.appspot.com')
         blob = bucket.blob(fname1)
         buf = io.BytesIO()
         plt.savefig(buf, format='png')
         blob.upload_from_string(
          buf.getvalue(),
          content_type='image/png')
         buf.close()
         u = blob.public_url       
         return render_template('index.html' , value=u)        
        except ValueError:
            flash('entrer une valeur valide', category='error')
    return render_template('ant-colony.html')
