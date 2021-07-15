from flask import Flask,render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_USER'] = 'socialcontact'
app.config['MYSQL_PASSWORD'] = 'socialcontact123'
app.config['MYSQL_DB'] = 'socialcontact'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)
@app.route('/mysql')
def users():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT user, host FROM mysql.user''')
    rv = cur.fetchall()
    return str(rv)

@app.route('/')
def hello():
    return render_template('admin/index.html')
