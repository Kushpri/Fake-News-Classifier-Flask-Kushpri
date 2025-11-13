📰 Fake News Detection System (Machine Learning + Flask Web App)

This project is an end-to-end Fake News Classification System that uses a Machine Learning pipeline deployed through a Flask backend.
The app allows users to input a news article and get:

✔ Fake/Real Prediction
✔ Confidence Score (%)
✔ Clean AJAX UI
✔ ML Pipeline (TF-IDF + Logistic Regression)

🚀 Features
🔍 Machine Learning

TF-IDF Vectorizer + Logistic Regression

Includes combined ML pipeline for faster inference

Trained on 30,000+ articles (Fake + True)

Outputs prediction + confidence score

🌐 Web App

Flask backend with template rendering

AJAX-enabled frontend (no page reload)

Clean and simple UI

🧹 Engineering Improvements

Robust preprocessing

Single-step pipeline loading

Organized repository structure

Notebook stored separately

Large CSV files excluded via .gitignore

📁 Project Structure
Fake_News_Detection/
│
├── App/
│   ├── app.py                  # Flask backend
│   └── templates/
│       └── index.html          # Frontend UI
│
├── Models/
│   ├── fake_news_pipeline.pkl  # Final combined ML pipeline
│   ├── lr_model.pkl            # Raw Logistic Regression model
│   └── vectorizer.pkl          # TF-IDF Vectorizer
│
├── Notebook/
│   └── Fake_News_Analysis.ipynb   # Model training, evaluation
│
├── Fake.csv                      # Dataset (large file)
├── True.csv                      # Dataset (large file)
├── .gitignore
└── Deepfake detection (Fake News Analysis).pdf

📸 Demo Screenshot

Add your UI screenshot here

![App Screenshot]("D:\Pictures\Screenshots\Screenshot (1862).png")

🧠 Model Details
✔ Preprocessing

Lowercasing

URL removal

Punctuation removal

Numeric cleanup

Regex-based noise removal

Whitespace normalization

✔ Features

TF-IDF (unigrams, bigrams)

✔ Classifier

Logistic Regression

Probability-based predictions using predict_proba()

✔ Final Output

"Fake News" / "Real News"

Confidence Score: e.g. 87.52%

🏃‍♀️ How to Run Locally
1. Clone the repository
git clone https://github.com/Kushpri/Fake-News-Classifier-Flask-Kushpri.git
cd Fake-News-Classifier-Flask-Kushpri

2. Create virtual environment
python -m venv venv
venv\Scripts\activate


(Mac/Linux)

source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Run the app
cd App
python app.py


Open your browser at:

http://127.0.0.1:5000/

📡 API Endpoint (If You Want to Use JSON)
POST /predict
Request:
{
  "news": "The government announced a new policy today."
}

Response:
{
  "prediction": "Fake News",
  "confidence": "10.55%"
}

📊 Dataset

This project uses the popular Fake/Real news dataset containing:

Fake.csv – Fake News Articles

True.csv – Real News Articles

Dataset Source:
🔗 True.csv - https://drive.google.com/file/d/1Bjxjg_r7sAas6BR-jA9fr8NTVzD1F8m_/view?usp=sharing
🔗 Fake.csv - https://drive.google.com/file/d/18vR0SP4EXkH8URTVL_12bIhUZA0TICab/view?usp=sharing

(Full dataset is not uploaded to GitHub due to size limits.)

🧪 Notebook

The entire training pipeline, evaluation metrics, and preprocessing steps are available in:

Notebook/Fake_News_Analysis.ipynb


Includes:

Exploratory Data Analysis

Model training

Accuracy, Confusion Matrix

Pipeline export code

🌐 Deployment

Deploy-ready for:

Render

Railway.app

Heroku

Docker

To deploy, include:

web: gunicorn App.app:app

👩‍💻 Author
Priti Kushwaha
📧 kushpri2003@gmail.com
🔗 GitHub: https://github.com/Kushpri

🔗 LinkedIn: https://linkedin.com/in/priti-kushwaha-ab4a5b236

⭐ Support

If you liked this project, consider giving the repository a star!
