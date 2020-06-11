import time
import random
from flask import Flask
from flask import request
from flask import jsonify
from MH.WOA import WOA
from MH.ILWOA import ILWOA
from MH.Recuit_Sim import RS
from MH.Instances_generator import generator, generate_obj_list2 
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
    result={"BB":{}, "DP":{}, "BF":{}, "BFD":{}, "FF":{}, "FFD":{}, "NF":{}, "NFD":{}, "AG":{}, "WOA":{}, "ILWOA":{}, "RS":{} } 
    #get les differents champs 
    n= _req['n']
    c= _req['c']
    liste=_req['list'] # here i guess you should transform it to a simple liste d'entier (to give to methods)
    #we still havn't implemented the list sending part , so u can do ur tests with a static list here
    #list=[5,2,1,5,8] 
    n=12
    c=100
    liste = [100, 90, 28,16, 1, 17, 12,37,15,18,14,2]
    if(_req['checked_BB']): #true if user checked Branch and Bound
        #execute BB 
        #get results (list de boites+ t_exec)
        print("")
    if(_req['checked_DP']):
        #execute DP 
        print('')

    if(_req['checked_BF']):
        #execute BF
        print('')
    if(_req['checked_BFD']):
        #execute BFD
        print('')
    if(_req['checked_FF']):
        #execute FF
        print('')
    if(_req['checked_FFD']):
        #execute FFD
        print('')
    if(_req['checked_NF']): 
        #execute NF
        print('')
    if(_req['checked_NFD']):
        #execute NFD
        print('')
    if(_req['checked_AG']):
        #execute AG
        print('')
    if(_req['checked_WOA']):
        #execute WOA
        obj_list = generate_obj_list2(liste, n)
        woa = WOA(objects_list=obj_list, capacity=100)
        nb_bins, t_exec, solution = woa.optimize(nb_whales=30, max_iter=117, b=8.96, a=10)
        solution = solution.tolist()
        result["WOA"] = {"nb_bins": nb_bins, "t_exec": t_exec, "solution": solution}

    if(_req['checked_ILWOA']):
        obj_list = generate_obj_list2(liste, n)
        woa = WOA(objects_list=obj_list, capacity=100)
        nb_bins, t_exec, solution = woa.optimize(nb_whales=30, max_iter=117, b=8.96, a=10)
        solution = solution.tolist()
        result["ILWOA"] = {"nb_bins": nb_bins, "t_exec": t_exec, "solution": solution}
    if(_req['checked_RS']):
        #execute RS
        print('')



    return result # return a json respecting the format of resultats.json 

#here the react app will send you n + c , you should return a list of int ( objects) 
#using random generator
@app.route('/random',methods=['POST'])
def random_gen():
    #get the request from frontend
    _req = request.get_json() 
    #les champs de _req sont les variables dans le state de "ChooseMthd.js"
    # u can get la variable x by _req["x"] , the checked variables are to decide where exec that method oupas 
    # other vars are the params of methods 
    liste = []
    #get les differents champs 
    n= _req['n']
    c= _req['c']
    grain = random.randint(0,c)
    liste = generator(n=n, c=c, grain=grain, save=False)
    return {"liste":liste}

#here the react app gives you the name of the instance + list of methods 
#you should return the results ( same format que get_resultat ()+ solution optimale)
@app.route('/benchmark',methods=['POST'])
def benchmark_sol():
    _req = request.get_json() 
    instance_name = _req['instance_name']
    
    return ''

