from flask import Flask
from flask_cors import CORS
from routes.prediction import prediction_bp
from routes.patients import patients_bp
from routes.encounters import encounters_bp
from routes.customers import customers_bp
from routes.history import history_bp

app = Flask(__name__)
app = Flask(__name__)

CORS(
    app,
    resources={r"/*": {"origins": ["http://localhost:5173"]}},
)
app.register_blueprint(prediction_bp)
app.register_blueprint(patients_bp)
app.register_blueprint(encounters_bp)
app.register_blueprint(customers_bp)
app.register_blueprint(history_bp)


@app.route("/health")
def health():

    return {"status": "healthy"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
