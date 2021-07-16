from flask import Flask,render_template,request
app = Flask(__name__)
@app.route('/')
def hello():
    return render_template('login.html')
#@app.route('/register')
@app.route('/login',methods=['POST'])
def register():
    username = request.form.get('username')
    passwd = request.form.get('password')
    
    print(username, passwd)

    return render_template('index.html')
    
if __name__ == "__main__":
    app.run()