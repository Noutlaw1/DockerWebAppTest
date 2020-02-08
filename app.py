from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/nick")
def nick():
    return "Hello Nick."

if __name__ == "__main__":
    app.run(host='0.0.0.0')

















