from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello from Flask running on GitHub Actions!"


@app.route("/health")
def health():
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    app.run(host="110.226.152.118",port=8000, debug=True)
