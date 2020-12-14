from flask import Flask,render_template
#########Migrations#############
app = Flask(__name__)
from flask_cors import CORS
CORS(app, resources=r'/*')
@app.route('/test')
def vue():
    print("some test")
    return render_template('test.html',**locals())
