import os
from flask import Flask, Blueprint
from jinja2 import Environment
from flask_session import Session
from werkzeug.utils import secure_filename

#create instance of the app
app = Flask(__name__)

#Blueprints
from Application.views.test import test_bp

#register the Blueprints
app.register_blueprint(test_bp)

#Session
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)
