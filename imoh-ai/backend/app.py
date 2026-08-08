from flask import Flask, request, Response, stream_with_context
from flask_cors import CORS
from model_registry import registry
from router import route_request



app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Imoh AI Backend Running"


@app.route("/chat", methods=["POST"])
def chat():

    payload = request.get_json()
    tool = payload.get("tool", "gemini")
    request_data = payload.get(
    "data",
    {"message": payload.get("message", "")}
            )
    return Response(
        stream_with_context(route_request(request_data, tool)),
        mimetype="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",  # Prevent buffering by reverse proxies
        },
    )
    
@app.route("/health", methods=["GET"])
def health():

    return {
        "status": "healthy",
        "models": list(registry._models.keys()),
    }, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=False)