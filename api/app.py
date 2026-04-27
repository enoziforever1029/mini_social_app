from flask import Flask
from api.post_api import post_api


def create_app():
    app = Flask(__name__)

    app.register_blueprint(post_api, url_prefix="/api")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)