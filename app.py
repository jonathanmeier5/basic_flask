from flask import Flask

app = Flask(__name__)

print(__name__)

from basic_module.views import sample_bp
app.register_blueprint(sample_bp)

