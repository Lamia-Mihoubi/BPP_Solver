from flask import Flask
from flask import request
from flask import jsonify

import os 
import sys
import time
import random
import numpy

import switching as sw
from Instances_generator import generator
from Instances_reader import ReadInstance

app = Flask(__name__)
# here the react will give n +c + list of objects + list of methods with their params 
# you should return the solutions of each method + sol opt if possible 
@app.route('/resultats',methods=['POST'])
def get_resultat():
    #get the request from frontend
    _req = request.get_json() 
    res=(sw.switch((_req)))
    return (jsonify(res)) # return a json respecting the format of resultats.json 

#here the react app will send you n + c , you should return a list of int ( objects) 
#using random generator
@app.route('/random',methods=['POST'])
def random_gen():
    _req=request.get_json()
    n= int(_req['n'])
    c= int(_req['c'])
    grain = random.randint(0,c)
    liste = generator(n=n, c=c, grain=grain, save=False)
    return {"liste":liste}

#here the react app gives you the name of the instance + list of methods 
#you should return the results ( same format que get_resultat ()+ solution optimale)
@app.route('/benchmark',methods=['POST'])
def benchmark_sol():
    _req = request.get_json()
    n = _req['classe']
    F = _req['filename']
    nbr, c, liste = ReadInstance(os.path.join('Instances', F+'.txt'))
    _req['n'] = nbr
    _req['c'] = c
    _req['list'] = liste
    res=(sw.switch((_req)))
    return ({'res':res,'n':nbr,'c':c, 'opt':10})

