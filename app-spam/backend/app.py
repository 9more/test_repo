from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("saved_model.pkl","rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    text = request.form["message"]

    prediction = model.predict([text])[0]

    result = "Spam" if prediction == 1 else "Not Spam"

    return render_template(
        "index.html",
        prediction=result,
        message=text
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0")