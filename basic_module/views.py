import requests as r

from flask import request, Blueprint
from flask.views import MethodView
from app import app

@app.route('/')
def hello_world():
	return 'Hello, World!'

sample_bp = Blueprint('sample_bp',__name__)

class SampleAPI(MethodView):
	#you can add login decorators, etc here

	decorators = []

	def get(self):
		return "This was a get request"


sample_view = SampleAPI.as_view('sample_view')

sample_bp.add_url_rule(
	'/sample/', view_func=sample_view, methods=['GET']
)
 
