from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return {"msg":"My Name one is Dharmendra bajiya git update"}

@app.route("/login")
def index():
    return {"msg":"My Name one is Dharmendra bajiya"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9999)
