from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello():
    return "Hello, Welcome my flask_app!"

@app.route('/bye')

def goodbye():
    return "Goodbye from my flask_app!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)