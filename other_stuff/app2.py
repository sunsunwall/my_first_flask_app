from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello():
    return "<html><body>Yo - this is the second flask_app!</body></html>"

@app.route('/bye')
def goodbye():
    return "<html><body>Catch you later!</body></html>"

@app.route('/aioverlord')
def aioverlord():
    return "<html><body>\U0001F643 \U0001F643 \U0001F643 Gradient descent solely trained on text cannot generalize - we need more than LLMs for AGI! \U0001F643 \U0001F643 \U0001F643</body></html>"

if __name__ == '__main__':
    @app.after_request
    def add_font(response):
        if response.content_type.startswith('text/html'):
            response.set_data(
                response.get_data(as_text=True).replace(
                    '<body>',
                    '<body style="font-family: Helvetica, Arial, sans-serif;">'
                )
            )
        return response

    app.run(host='0.0.0.0', port=5001)
