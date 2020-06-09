import time
from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

# here the react will give n +c + list of objects + list of methods with their params 
# you should return the solutions of each method + sol opt if possible 
@app.route('/resultats',methods=['POST'])
def get_resultat():
    _req = request.get_json()
    #console.log(_req)
    n = _req['n']
    return (
        {"n": n}
        )

#here the react app will send you n + c , you should return a list of int ( objects) 
#ie random generation
@app.route('/random',methods=['POST'])
def random_gen():
    return ''

#here the react app gives you the name of the instance + list of methods 
#you should return the results ( same format que get_resultat ())
@app.route('/benchmark',methods=['POST'])
def benchmark_sol():
    return ''

