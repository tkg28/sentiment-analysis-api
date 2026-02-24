README.md（最低限だけど評価される）

# Sentiment Analysis API

日本語の感情分析API（BERTベース）

## Usage

```bash
pip install -r requirements.txt
python app.py
API

POST /predict

{
  "text": "最高でした！"
}
Response
{
  "sentiment": "ポジティブ",
  "confidence": 0.98
}
```
