from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

import RPi_IO.models
import RPi_WEB.views

