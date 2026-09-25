from flask import Flask

from routes.prediction import prediction_bp
from routes.patients import patients_bp
from routes.encounters import encounters_bp

app = Flask(__name__)

app.register_blueprint(prediction_bp)
app.register_blueprint(patients_bp)
app.register_blueprint(encounters_bp)


@app.route("/health")
def health():

    return {"status": "healthy"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
