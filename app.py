from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "Share your tools here!!"

from application import app

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')
