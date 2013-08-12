from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import Required

class NameForm(Form):
    name = TextField('What is your name?', validators = [ Required() ])

