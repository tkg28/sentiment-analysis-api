

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

## 設定（環境変数）

| 変数 | 既定 | 内容 |
| --- | --- | --- |
| `HOST` | `127.0.0.1` | 待ち受けるアドレス。コンテナなどで外から接続するときは `0.0.0.0` にする |
| `PORT` | `5001` | 待ち受けるポート |
| `ALLOWED_ORIGINS` | なし | ブラウザから直接呼ぶサイト（カンマ区切り）。未設定ならどのサイトにも CORS を許可しない。サーバーから呼ぶ場合は設定不要 |

`text` は2000文字まで、リクエストは16KBまでです。超えると 400 または 413 を返します。
