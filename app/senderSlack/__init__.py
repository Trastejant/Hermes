from flask import Blueprint

senderSlack = Blueprint('senderSlack', __name__, template_folder='templates')
from . import routes