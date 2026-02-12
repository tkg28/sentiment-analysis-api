from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
import os
from preprocessing import preprocess_text, is_short_and_neutral

def load_model():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(current_dir, "model")

    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    tokenizer = AutoTokenizer.from_pretrained(model_path)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    model.eval()

    return model, tokenizer, device


def predict_sentiment(text, model, tokenizer, device):

    if is_short_and_neutral(text):
        return {
            "sentiment": "ニュートラル",
            "confidence": 1.0
        }

    text = preprocess_text(text)

    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    inputs = {k: v.to(device) for k, v in inputs.items()}

    with torch.no_grad():
        logits = model(**inputs).logits

    probs = torch.softmax(logits, dim=-1)
    pred = torch.argmax(probs).item()

    labels = ["ネガティブ", "ニュートラル", "ポジティブ"]

    return {
        "sentiment": labels[pred],
        "confidence": round(torch.max(probs).item(), 4)
    }