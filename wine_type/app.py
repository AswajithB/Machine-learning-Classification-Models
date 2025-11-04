from flask import Flask, render_template, request
import pickle
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the saved model, scaler, and label encoder
with open('wine_type_logistic_model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

with open('label_encoder.pkl', 'rb') as file:
    label_encoder = pickle.load(file)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get all input values from form
        features = [
            float(request.form['fixed_acidity']),
            float(request.form['volatile_acidity']),
            float(request.form['citric_acid']),
            float(request.form['residual_sugar']),
            float(request.form['chlorides']),
            float(request.form['free_sulfur_dioxide']),
            float(request.form['total_sulfur_dioxide']),
            float(request.form['density']),
            float(request.form['pH']),
            float(request.form['sulphates']),
            float(request.form['alcohol']),
            float(request.form['quality'])
        ]

        # Convert to numpy array and reshape for single sample
        features = np.array(features).reshape(1, -1)

        # Scale the input using saved scaler
        scaled_features = scaler.transform(features)

        # Predict wine type
        prediction = model.predict(scaled_features)
        predicted_label = label_encoder.inverse_transform(prediction)[0]

        return render_template('result.html', prediction_text=f'The predicted wine type is: {predicted_label}')

    except Exception as e:
        return render_template('result.html', prediction_text=f'Error: {str(e)}')


if __name__ == "__main__":
    app.run(debug=True)
