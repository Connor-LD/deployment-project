### Import Packages
from flask import Flask, jsonify, request
import pickle
import pandas as pd
import traceback
# from my_transformers import DenseTransformer

### Import model
with open('../data/loan_model.pkl', 'rb') as f:
    loan_model = pickle.load(f)

### Create App
app = Flask(__name__)

### Homepage
@app.route('/')
def welcome():
   return "Welcome! Use this Flask App for Loan Approval predictions"

### /predict
@app.route('/predict', methods=['POST','GET'])
def predict():
    
    if request.method == 'GET':
       return "Prediction page. Try using post with params to get specific prediction."

    if request.method == 'POST':
        try:
            data = request.get_json(force=True)         ## Extract data from the POST request
            data_df = pd.DataFrame(data, index=[0])     ## Convert to pandas DataFrame
            predictions = loan_model.predict(data_df)   ## Make predictions using the trained model
            return jsonify(predictions.tolist())        ## Return the predictions as a JSON response
        except:
            return jsonify({
                   "trace": traceback.format_exc()
                   })

if __name__ == '__main__':
    app.run(debug=True)