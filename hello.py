from flask import Flask,render_template
from a import api_gt
from a1 import api_gt_death
from b import update
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/get-api')
def get_api():
    return api_gt()

@app.route('/get-api/death')
def get_api_death():
    return api_gt_death()

@app.route('/update-get-api')
def update_get_api():
    return update()


if __name__ == '__main__':
    app.run(debug=True)