from flask import Flask
from hbnb.app.api.v1 import api_v1

app = Flask(__name__)
app.register_blueprint(api_v1)

if __name__ == "__main__":
    app.run(debug=True)
