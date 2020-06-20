from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hi!'

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # port default 5000, if you wanna change use post=number_port




