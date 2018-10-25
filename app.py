from flask import *
app = Flask(__name__)

@app.route('/')
def home_page():
    return None

if __name__ == '__main__':
   app.run(debug = True)