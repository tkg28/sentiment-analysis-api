from flask import Flask, request, jsonify
from flask_cors import CORS
from model_utils import load_model, predict_sentiment

app = Flask(__name__)
CORS(app)

model, tokenizer, device = load_model()

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Sentiment Analysis API"})

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    if not data or 'text' not in data:
        return jsonify({"error": "text is required"}), 400

    text = data['text']
    result = predict_sentiment(text, model, tokenizer, device)

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)