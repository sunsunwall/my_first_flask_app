import flask from Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Yo - this is the second flask app!"

@app.route('/bye')
def goodbye():
    return "Goodbye from my second flask_app!"

@app.route('/aioverlord')
def aioverlord():
    return "Gradient descent solely trained on text cannot generalize - we need more than LLMs for AGI!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)