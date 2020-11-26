from flask import Flask

from flask_security import Security

from cram_school import models
from cram_school.views import register_blueprint
from cram_school.lib import config


def create_app():
    app = Flask(__name__)
    app.jinja_env.auto_reload = True
    app.config.from_object(config.Config())

    # models setup
    models.setup(app)

    # security setup
    Security(app, models.user.USER_DATASTORE)

    # register app
    register_blueprint(app)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
