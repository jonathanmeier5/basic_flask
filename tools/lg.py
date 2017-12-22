from app import app
from functools import wraps
from flask import request
import time

@app.before_request
def standard_logger():
	msg = [time.strftime('%Y-%m-%d %H:%M:%S'),request.url,str(request.remote_addr)]
	app.logger.warning("|".join(msg))
	#app.logger.warning("Using app.before_request hook")

