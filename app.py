from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return 'hello'

@app.route("/health")
def health():
    return "<h1 style='color:blue'>Hello There!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
