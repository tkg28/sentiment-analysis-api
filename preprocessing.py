import re

def preprocess_text(text):
    text = re.sub(r'([!！]+)', '!!!', text)
    text = re.sub(r'([?？]+)', '???', text)
    return text


def is_short_and_neutral(text):
    text = text.strip()

    if not text or len(text) < 2:
        return True

    if len(text) > 5:
        return False

    strong_words = ["最高", "最悪", "好き", "嫌い"]

    return not any(word in text for word in strong_words)