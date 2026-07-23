from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "Imoh AI Backend Running"

@app.route("/chat", methods=["POST"])
def chat():
    print("CHAT ENDPOINT HIT")

    data = request.get_json()

    message = data.get("message", "")

    return jsonify({
        "response": f"Hello from Imoh AI. You said: {message}"
    })


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5001
    )