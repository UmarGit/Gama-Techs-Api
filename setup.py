import requests
from flask import Flask, jsonify, request 
from a import api_gt
  
# creating a Flask app 
app = Flask(__name__) 


@app.route("/")
def home(): 
        return '<h1>FLASK API</h1>'

@app.route('/coronavirus', methods = ['GET', 'POST']) 
def datas(): 
    if(request.method == 'GET'):       

        return api_gt()
        
# driver function 
if __name__ == '__main__': 
  
    app.run(debug = True) 