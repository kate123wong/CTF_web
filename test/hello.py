from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def hello():
<<<<<<< HEAD
    return render_template('admin/index.html')

if __name__ == '__main__':
    app.run()
=======
    return render_template('login.html')
>>>>>>> b7295ec5def8f34901818a5558380049e2a143a7
