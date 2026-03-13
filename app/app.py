from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    env_name = os.getenv("ENV_NAME", "local")
    api_key = os.getenv("API_KEY", "not-set")
    return f"Hello from Kubernetes! ENV={env_name}, API_KEY_PRESENT={api_key != 'not-set'}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
