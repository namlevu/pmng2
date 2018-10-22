# productmng/__init__.py

from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')


db = MongoEngine(app)


def register_blueprints(app):
    # Prevents circular imports
    # from xxx import xxx_bp
    # app.register_blueprint(xxx_bp, url_prefix='/xxx')
    from productmng.views.users import user_bp
    app.register_blueprint(user_bp, url_prefix='/api')
    from productmng.views.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    from productmng.views.products import products_bp
    app.register_blueprint(products_bp, url_prefix='/api')


register_blueprints(app)

if __name__ == '__main__':
    app.run()
