from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def register_error_handlers(app):
    @app.errorhandler(500)
    def base_error_handler(e):
        return render_template('500.html'), 500

    @app.errorhandler(404)
    def error_404_handler(e):
        return render_template('404.html'), 404


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////stadistic.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db = SQLAlchemy(app)

    from .public import public
    app.register_blueprint(public)

    from .api import api
    app.register_blueprint(api)

    from .senderMail import senderMail
    app.register_blueprint(senderMail)

    from .senderSlack import senderSlack
    app.register_blueprint(senderSlack)

    register_error_handlers(app)
    return app
