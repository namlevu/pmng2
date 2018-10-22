# productmng/__init__.py

from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object('config')
app.config.from_pyfile('config.py')


db = MongoEngine(app)


def register_blueprints(app):
    # TODO: Prevents circular imports
    print('register_blueprints')
    # from xxx import xxx_bp
    # app.register_blueprint(xxx_bp, url_prefix='/xxx')


register_blueprints(app)

if __name__ == '__main__':
    app.run()
