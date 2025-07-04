def suggest_hashtags(text):
    hashtags = []
    text_lower = text.lower()

    if "ai" in text_lower or "artificial intelligence" in text_lower:
        hashtags += ["#AI", "#ArtificialIntelligence", "#MachineLearning"]

    if "career" in text_lower or "interview" in text_lower:
        hashtags += ["#CareerGrowth", "#JobSearch", "#ResumeTips"]

    if "project" in text_lower or "python" in text_lower:
        hashtags += ["#Python", "#ProjectWork", "#CodingLife"]

    if "motivation" in text_lower or "success" in text_lower:
        hashtags += ["#MotivationMonday", "#SuccessMindset"]

    if not hashtags:
        hashtags = ["#LinkedIn", "#Networking", "#PersonalBrand"]

    return hashtags[:5]
import csv
def save_prediction(post, engagement, hashtags):
    with open("data/history.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([post, engagement, ", ".join(hashtags)])