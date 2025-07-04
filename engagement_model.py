import streamlit as st
import joblib
import os

# ✅ Load trained model
model_path = "model/engagement_model.pkl"
if os.path.exists(model_path) and os.path.getsize(model_path) > 0:
    model = joblib.load(model_path)
else:
    st.error("❌ Model file not found or is empty. Please run 'engagement_model.py' first.")
    st.stop()

# ✅ Streamlit App UI
st.title("📈 LinkedIn Post Engagement Predictor")

# ✅ Text input from user
post_text = st.text_area("🔥 Enter your LinkedIn post content here:")

# ✅ Predict on button click
if st.button("Predict Engagement"):
    if post_text.strip() != "":
        engagement = model.predict([post_text])[0]
        st.success(f"✅ Predicted Engagement Level: *{engagement}*")
    else:
        st.warning("⚠️ Please enter some text before predicting.")
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

# Load the dataset
df = pd.read_csv("data/posts.csv")

# Split features and target
X = df["post"]
y = df["engagement"]

# Create a pipeline: TF-IDF + Classifier
model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression())
])

# Train the model
model.fit(X, y)

# Save the model
joblib.dump(model, "model/engagement_model.pkl")

print("✅ Model trained and saved to model/engagement_model.pkl")