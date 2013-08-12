from flask import Flask, render_template, session, redirect, url_for
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import Required
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)

class NameForm(Form):
    name = TextField('What is your name?', validators = [ Required() ])

@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html',
        form = form, name = session.get('name'))

if __name__ == '__main__':
    app.run(debug = True)

