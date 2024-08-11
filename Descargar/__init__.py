from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO()


def create_app():
    app = Flask(__name__)

    socketio.init_app(app)

    from Descargar.controller.descargarYt import yt_bp

    app.register_blueprint(yt_bp)

    return app
