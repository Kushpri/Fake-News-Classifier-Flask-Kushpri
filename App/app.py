from flask import Flask, request, render_template, jsonify
import joblib
import re, string
import os

def clean_text(text):
    text = (text or "").lower()
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r"\W", " ", text)
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'<.*?>+', '', text)
    text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'\w*\d\w*', '', text)
    text = text.strip()
    return text

app = Flask(__name__)

# --- ADJUST THIS PATH if necessary ---
# If app.py sits in App/ and Models/ is a sibling dir, use ../Models/...
PIPELINE_PATH = os.path.join(os.path.dirname(__file__), "..", "Models", "fake_news_pipeline.pkl")
# Or if Models is in the same directory: PIPELINE_PATH = "Models/fake_news_pipeline.pkl"

# try both common paths if the first doesn't exist
if not os.path.exists(PIPELINE_PATH):
    alt = os.path.join(os.path.dirname(__file__), "Models", "fake_news_pipeline.pkl")
    if os.path.exists(alt):
        PIPELINE_PATH = alt

# Load model pipeline once (fail fast if missing)
try:
    pipeline = joblib.load(PIPELINE_PATH)
except Exception as e:
    pipeline = None
    print("ERROR loading pipeline from:", PIPELINE_PATH)
    print(e)

@app.route("/")
def home():
    # Render with no prediction normally
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Accept both form posts and JSON AJAX posts
    if request.is_json:
        payload = request.get_json(silent=True) or {}
        text = payload.get("news", "")
    else:
        text = request.form.get("news", "")

    cleaned = clean_text(text)

    if pipeline is None:
        error_msg = "Model not loaded. Check server logs."
        if request.is_json:
            return jsonify({"error": error_msg}), 500
        return render_template("index.html", prediction="Error", confidence=error_msg)

    try:
        pred = pipeline.predict([cleaned])[0]
        proba = pipeline.predict_proba([cleaned])[0]  # e.g. [prob_class0, prob_class1]
    except Exception as e:
        if request.is_json:
            return jsonify({"error": str(e)}), 500
        return render_template("index.html", prediction="Error", confidence=str(e))

    # Map label and get confidence (assumes 0=fake, 1=real)
    try:
        pred_int = int(pred)
        label_text = "Real News" if pred_int == 1 else "Fake News"
        # probability for the 'real' class at index 1 (adjust if your encoding differs)
        confidence_score = round(float(proba[1]) * 100, 2)
    except Exception:
        # fallback when labels are strings
        label_text = str(pred)
        confidence_score = round(max(proba) * 100, 2) if len(proba) > 0 else 0.0

    if request.is_json:
        return jsonify({"prediction": label_text, "confidence": confidence_score})

    # fallback HTML render (for non-JS clients)
    return render_template("index.html", prediction=label_text, confidence=f"{confidence_score}%")

if __name__ == "__main__":
    app.run(debug=True)
