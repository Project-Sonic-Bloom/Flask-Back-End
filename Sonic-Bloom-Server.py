from flask import Flask
from flask_cors import CORS

from scripts.main.dataVisualisation import *

# Allow CORS policy tutorial so angular app can communicate
# https://pypi.org/project/Flask-Cors/
app = Flask(__name__)
CORS(app)

# Home route
@app.route('/')
def home():
    return "Hello, World!"

@app.route('/GenerateHeatmap',  methods = ['POST'])
def GenerateHeamap():
    print(hello())
    return

@app.route('/GetScreenshot',  methods = ['GET'])
def GetScreenshot():
    return screenshot()

if __name__ == '__main__':
    app.run(debug=True)
