from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)
Bootstrap(app)

# Configure db
# db = yaml.load(open('db.yaml'))  yaml.load has deprecated
db = yaml.safe_load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    # cur.execute("INSERT INTO user VALUES(%s)",['Mike'])
    # mysql.connection.commit()
    result_value = cur.execute("SELECT * FROM user")
    if result_value > 0:
        users = cur.fetchall()
        print(users)  # you can see the result inside Terminal, after refresh the browser
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/css')
def css():
    return render_template('css.html')

@app.route('/testing', methods=['GET','POST'])   # arrange method post
def sendme():
    # Perhatikan bagian ini
    if request.method == 'POST':
        # return 'Successfully registered'
        return request.form['password']       # get data from form input
    return render_template('testingpage.html')

if __name__ == '__main__':
    app.run(debug=True)






