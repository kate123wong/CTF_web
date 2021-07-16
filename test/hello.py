from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def hello():
    return render_template('login.html')
@app.route('/register')
def register():
    username = request.args.get('username')
    passwd = request.args.get('passwd')
    return render_template('register./html')

