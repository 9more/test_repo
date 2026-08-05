from flask import Flask, request, Response, stream_with_context
from flask_cors import CORS

from router import route_request

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "Imoh AI Backend Running"


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()
    message = data["message"]
    tool = data.get("tool", "gemini")

    return Response(
        stream_with_context(route_request(message, tool)),
        mimetype="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",  # Prevent buffering by reverse proxies
        },
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=False)