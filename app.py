import os

from flask import Flask, request, jsonify
from flask_cors import CORS
from config import MAX_REQUEST_BYTES, MAX_TEXT_CHARS
from model_utils import load_model, predict_sentiment

app = Flask(__name__)
# 大きすぎるリクエストは、読み込む前に 413 で断る
app.config['MAX_CONTENT_LENGTH'] = MAX_REQUEST_BYTES

# ブラウザから直接呼ぶサイトだけを許可する（カンマ区切り。例: https://example.com）
# 未設定ならどのサイトにも許可しない。サーバーから呼ぶ場合は CORS の設定は要らない
allowed_origins = [o.strip() for o in os.environ.get('ALLOWED_ORIGINS', '').split(',') if o.strip()]
if allowed_origins:
    CORS(app, origins=allowed_origins)

model, tokenizer, device = load_model()

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Sentiment Analysis API"})

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(silent=True)

    if not isinstance(data, dict) or not isinstance(data.get('text'), str):
        return jsonify({"error": "text is required"}), 400

    text = data['text']
    if len(text) > MAX_TEXT_CHARS:
        return jsonify({"error": f"text must be {MAX_TEXT_CHARS} characters or less"}), 400

    result = predict_sentiment(text, model, tokenizer, device)

    return jsonify(result)

@app.errorhandler(413)
def too_large(_error):
    return jsonify({"error": "request is too large"}), 413

if __name__ == '__main__':
    # 既定ではこの PC からだけ接続できる。コンテナなどで外から受けるときは HOST=0.0.0.0 にする
    app.run(host=os.environ.get('HOST', '127.0.0.1'), port=int(os.environ.get('PORT', '5001')))
