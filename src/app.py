from flask import Flask, request, jsonify
from src.features import hash_feature

app = Flask(__name__)


@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({"error": "No text provided"}), 400

    # Feature engineering
    feature_index = hash_feature(data['text'])

    # Mock model predict
    prediction = float(feature_index) * 0.5

    return jsonify({"prediction": prediction, "bucket": feature_index})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)