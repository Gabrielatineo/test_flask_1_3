from flask import Flask, request

app = Flask(__name__)

@app.route("/init")
def main():
    return {"payload":"welcome to my project"}

@app.route("/read/:<content>", methods=["GET"])
def read(content):
    return {"payload":content}

@app.route("/create/:<content>", methods=["POST"])
def read(content):
    return {"payload":content}

if __name__ == "main":
    app.run(debug=True)
