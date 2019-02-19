# Flask
from flask import Flask
# App
from routes import register_endpoints


def main():
    print("installed")
    app = Flask(__name__)
    register_endpoints(app)
    app.run(debug=True)


if __name__ == "__main__":
    main()
