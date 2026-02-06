import sys
import os
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            # Paths to your saved artifacts from the transformation and trainer steps
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")

            # Load the model and preprocessor using your utils helper
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)

            # Transform input data and make prediction
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e, sys)

class CustomData:
    def __init__(self, step: int, type: str, amount: float, oldbalanceOrg: str, 
                 newbalanceOrig: float, oldbalanceDest: float, newbalanceDest: float):
        self.step = step
        self.type = type
        self.amount = amount
        self.oldbalanceOrg = oldbalanceOrg
        self.newbalanceOrig = newbalanceOrig
        self.oldbalanceDest = oldbalanceDest
        self.newbalanceDest = newbalanceDest

    def get_data_as_data_frame(self):
        try:
            # Must match the exact column names used during model training
            custom_data_input_dict = {
                "step": [self.step],
                "type": [self.type],
                "amount": [self.amount],
                "oldbalanceOrg": [self.oldbalanceOrg],
                "newbalanceOrig": [self.newbalanceOrig],
                "oldbalanceDest": [self.oldbalanceDest],
                "newbalanceDest": [self.newbalanceDest],
            }
            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)
