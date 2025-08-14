from flask import Flask

app = Flask(__name__)

@app.route('/') #the route component, in this case "/", 
                # is the part of the URL that will run the code below (IE the function hello in this case)

def hello():
    return "Hello, Welcome my flask_app!"

@app.route('/bye')

def goodbye():
    return "Goodbye from my flask_app!"

@app.route('/aioverlord')

def aioverlord():
    return "Dont rely on LLMs for everything!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)