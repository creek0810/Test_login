

from flask import Flask
# from flask_mongoengine import MongoEngine
from models import extension
from views import (
    login_api,
    login_web,
)

def create_app():
    app = Flask(__name__)
    app.jinja_env.auto_reload = True
    app.config.from_object('app.config')  
    
    
    
    #register login method
    extension.setup(app)
    # extension.security.init_app(app,extension.user_datastore)
    app.register_blueprint(login_api.login_api,url_prefix='')
    app.register_blueprint(login_web.login_web,url_prefix='')       
    return app



if __name__ == '__main__':
    app = create_app()
    app.run()