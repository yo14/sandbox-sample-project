from flask import Flask, render_template
from flask_bootstrap import Bootstrap   # step 01 import library

app = Flask(__name__)
Bootstrap(app)     # step 02 to activate boostrap

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/css')
def css():
    return render_template('css.html')

if __name__ == '__main__':
    app.run(debug=True)






