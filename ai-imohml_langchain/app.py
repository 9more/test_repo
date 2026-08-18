from flask import Flask, request, jsonify
from flask_cors import CORS
from chain import chain


app = Flask(__name__)
CORS(app)


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    message = data["message"]

    result = chain.invoke({
        "topic": message
    })

    return jsonify({
        "response": str(result)
    })


if __name__ == "__main__":
    app.run(debug=True, port=5001)