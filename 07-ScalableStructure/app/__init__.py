from flask import Flask
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object('config')
bootstrap = Bootstrap(app)

import views
