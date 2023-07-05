import os
import requests
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Example Hello World route."""
    name = os.environ.get("NAME", "World")
    return f"Hello {name}!"


@app.route("/api")
def new():
    """Example Hello World route."""
    url = "https://api.ipify.org/"
    x = requests.get(url)
    print(x.text)
    return x.text


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
