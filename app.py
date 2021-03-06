from flask import Flask
import logging

logging.basicConfig(filename='error.log',level=logging.DEBUG)

app = Flask(__name__)

handler = logging.FileHandler('error.log')
app.logger.addHandler(handler)

#Use this to turn off werkzeug logger in testing
log = logging.getLogger('werkzeug')
#log.setLevel(logging.ERROR)
log.disabled = True

#Ensure that all tools are imported appropriately
#the real question is, why do we need to import this?
from tools import lg

from basic_module.views import sample_bp
app.register_blueprint(sample_bp)

