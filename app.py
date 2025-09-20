from flask import Flask, render_template, request
import pickle
import numpy as np

# Load trained model
with open("baby_model.pkl", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        # Get form values
        weight = float(request.form["weight"])
        length = float(request.form["length"])
        head_circ = float(request.form["head_circumference"])

        # Prepare input for model (exclude gender)
        features = np.array([[weight, length, head_circ]])
        prediction = model.predict(features)

        return render_template(
            "index.html",
            prediction_text=f"Predicted Gestational Age: {prediction[0]:.2f} weeks"
        )

if __name__ == "__main__":
    app.run(debug=True)
