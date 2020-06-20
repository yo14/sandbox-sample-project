from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    fruits = ['Apple','Mango','Orange']
    return render_template('index.html', fruits=fruits)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)




