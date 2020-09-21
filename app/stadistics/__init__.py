from flask import Blueprint

senderSlack = Blueprint('stadistic', __name__, template_folder='templates')
from . import routes
