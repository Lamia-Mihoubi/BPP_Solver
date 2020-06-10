import time
from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

# here the react will give n +c + list of objects + list of methods with their params 
# you should return the solutions of each method + sol opt if possible 
@app.route('/resultats',methods=['POST'])
def get_resultat():
    #get the request from frontend
    _req = request.get_json() 
    #les champs de _req sont les variables dans le state de "ChooseMthd.js"
    # u can get la variable x by _req["x"] , the checked variables are to decide where exec that method oupas 
    # other vars are the params of methods 
    result='' 
    #get les differents champs 
    n= _req['n']
    c= _req['c']
    liste=_req['list'] # here i guess you should transform it to a simple liste d'entier (to give to methods)
    #we still havn't implemented the list sending part , so u can do ur tests with a static list here
    #list=[5,2,1,5,8] 


    return ({
        "o1": liste[0]
    }) # return a json respecting the format of resultats.json 

#here the react app will send you n + c , you should return a list of int ( objects) 
#using random generator
@app.route('/random',methods=['POST'])
def random_gen():
    _req=request.get_json()
    n=_req['n']
    c=_req['c']
    return jsonify([n,c])

#here the react app gives you the name of the instance + list of methods 
#you should return the results ( same format que get_resultat ()+ solution optimale)
@app.route('/benchmark',methods=['POST'])
def benchmark_sol():
    _req = request.get_json()
    n= _req['classe']
    F= _req['filename']

    return ({
        "Fname": n+F,
    })

