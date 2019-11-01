## App Utilities
import os
# import env
from db import db

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_restful import Api

from resources.user import UserRegister, UserLogin, UserLogout, login_manager
from project.algorithms.views import algorithms_blueprint

# App Settings
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['PROPAGATE_EXCEPTIONS'] = True

app.config['DEBUG'] = False
api = Api(app)

Bootstrap(app)
login_manager.init_app(app)

# Register Blueprint
app.register_blueprint(algorithms_blueprint)

# Register Resources
api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')


@app.errorhandler(404)
def error404(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def error500(error):
    return render_template('500.html'), 500


## DB INIT
db.init_app(app)

## APP INITIATION
if __name__ == '__main__':

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    # app.run()

    # # Docker
    # app.run(host='0.0.0.0')
    #
    # Heroku
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)