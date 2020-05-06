from flask import Blueprint


senderMail = Blueprint('senderMail', __name__, template_folder='templates')
from . import routes