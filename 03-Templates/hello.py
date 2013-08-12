from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/index/<name>')
def hello(name):
    return render_template('index.html', name = name)

if __name__ == '__main__':
    app.run(debug = True)

