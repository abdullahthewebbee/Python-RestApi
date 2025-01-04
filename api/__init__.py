import logging
from logging.handlers import RotatingFileHandler
from flask import Flask

app = Flask(__name__)
app.config.from_object('api.config')
#app.config.from_envvar('API_CONFIG')

# ref: https://gist.github.com/ibeex/3257877
formatter = logging.Formatter(
    "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
handler = RotatingFileHandler(app.config['LOG_FILENAME'],
                              maxBytes=10000000,
                              backupCount=5)
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)
app.logger.addHandler(handler)

# Output the access logs to the same file
log = logging.getLogger('werkzeug')
log.setLevel(logging.DEBUG)
log.addHandler(handler)

@app.errorhandler(404)
def page_not_found(e):
    return "404 not found", 404

# Import the routes from all controllers
from api.examples import get_example
