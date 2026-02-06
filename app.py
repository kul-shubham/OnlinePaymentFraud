from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

# Route for home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_data():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        # Mapping form data to CustomData class
        data = CustomData(
            step=int(request.form.get('step')),
            type=request.form.get('type'),
            amount=float(request.form.get('amount')),
            oldbalanceOrg=float(request.form.get('oldbalanceOrg')),
            newbalanceOrig=float(request.form.get('newbalanceOrig')),
            oldbalanceDest=float(request.form.get('oldbalanceDest')),
            newbalanceDest=float(request.form.get('newbalanceDest'))
        )

        # Convert to DataFrame
        pred_df = data.get_data_as_data_frame()
        print(pred_df)

        # Initialize and run the Prediction Pipeline
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)

        # Map prediction (e.g., 1 to 'Fraud', 0 to 'Safe')
        output = "Fraud" if results[0] == 1 else "Not Fraud"

        return render_template('home.html', results=output)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
