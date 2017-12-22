from app import app
from functools import wraps
from flask import request

import time

def custom_log(f):
	@wraps(f)
	def wrapper(*args, **kwargs):
		#app.logger.warning("Warning from my logging decorator")
		msg = [time.strftime('%Y-%m-%d %H:%M:%S'),request.url,str(request.remote_addr)]
		app.logger.info("|".join(msg))
		return f(*args, **kwargs)
	return wrapper
				
