import numpy as np
import pandas as pd
from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
model = joblib.load("decision_tree_model.pkl")

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/predict', methods=["POST"])
def predict():
    #float_features = [float(x) for x in request.form.values()]
    #feature = [np.array(float_features)]

    # Ambil input dari form dan konversi sesuai kebutuhan
    # Misalnya, jika semua fitur memang perlu dikonversi ke float
    features = [float(x) for x in request.form.values()]
    
    # Ubah bentuk array dari 1D menjadi 2D (1 sample, n features)
    features = np.array(features).reshape(1, -1)
    
    prediction = model.predict(features)

    # Mapping hasil prediksi 0/1 ke "Tidak" / "Ya"
    result = "Ya" if prediction[0] == 1 else "Tidak"

    return render_template("index.html", prediction_text= result)


if __name__ == "__main__":
    app.run(debug=True)