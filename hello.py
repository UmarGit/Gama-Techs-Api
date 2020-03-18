from flask import Flask,render_template
from a import api_gt
from b import update

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/get-api')
def get_api():
    return api_gt()
@app.route('/update-get-api')
def update_get_api():
    return update()


if __name__ == '__main__':
    app.run(debug=True)