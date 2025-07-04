import streamlit as st
import joblib
from analyzer import suggest_hashtags,save_prediction


model = joblib.load("model/engagement_model.pkl")  # ✅ load your trained model

# ✅ Add title and input
st.markdown("<h1 style='text-align: center;'>🔍 LinkedIn Post Engagement  Analyzer </h1>", unsafe_allow_html=True)
st.markdown("<hr>",unsafe_allow_html=True)
st.markdown(" 💡* Enter your Linkedln post and get engagement prediction, hashtags suggestion, and improvement tips!*")

post_text = st.text_area(" 🗒️ Your Linkedln post:",
height=200,
placeholder="Type your post here...")

# ✅ Prediction and display
if st.button("Predict Engagement"):
    if post_text.strip() != "":
        engagement = model.predict([post_text])[0]
        st.success(f"🎯 Predicted Engagement Level: *{engagement}*")

        hashtags = suggest_hashtags(post_text)
        st.markdown("## 🏷️ Suggested Hashtags:")
        for tag in hashtags:
            st.code(tag, language='')
            # ✅ Save prediction and hashtags
            save_prediction(post_text, engagement, hashtags)

        # ✅ Bonus Tips
        st.markdown("## 📈 Writing Tips")
        if engagement == "High":
            st.info("🔥 Tip: Keep sharing similar content! Use polls or questions for more comments.")
        elif engagement == "Medium":
            st.info("✅ Tip: Try adding 1–2 questions or tagging relevant people.")
        else:
            st.info("📉 Tip: Keep it short, use emojis and try adding 3–5 hashtags.")
    else:
        st.warning("⚠️ Please enter some text before predicting.")
import pandas as pd
# ✅ Download and view history of predictions
st.markdown("### 📜download or view previous predictions")

try:
    history_df = pd.read_csv("data/history.csv")
    st.markdown("#### 📊 Prediction History")
    st.dataframe(history_df)
    st.download_button(
        label="Download History as CSV",
        data=history_df.to_csv(index=False),
        file_name='linkedin_prediction.csv',
        mime='text/csv'
    )   
except FileNotFoundError:
    st.info("❌ No history found. Please make a prediction first.")
st.markdown("---")
st.markdown(
    "<div style='text-align: center;'>Made with ❤️ by Prathvi Partap<br><a href='https://www.linkedin.com/in/prathvi-partap-939964358?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app' target='_blank'>LinkedIn</a></div>",
    unsafe_allow_html=True
)