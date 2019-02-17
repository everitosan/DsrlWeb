# Flask
from flask import Flask
# App
from routes import register_endpoints
# Utils
from Utils.Gphoto2 import check_installed


if __name__ == "__main__" and check_installed():
    app = Flask(__name__)
    register_endpoints(app)
    app.run(debug=True)
