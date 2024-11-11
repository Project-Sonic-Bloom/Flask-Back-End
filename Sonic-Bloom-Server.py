from flask import Flask

# Allow CORS policy tutorial so angular app can communicate
# https://pypi.org/project/Flask-Cors/
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Home route
@app.route('/')
def home():
    return "Hello, World!"


if __name__ == '__main__':
    app.run(debug=True)
