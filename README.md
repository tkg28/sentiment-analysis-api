

# Sentiment Analysis API

日本語の感情分析API（BERTベース）
（AIを用いた宿泊施設向けアンケートアプリの機能の一つとして使用）

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
