# from flask import Flask, request, jsonify
# import google.generativeai as genai
# import nltk

# # NLTK dependency install & download tokenizer
# nltk.download('punkt')

# # हेल्थ-रिलेटेड कीवर्ड्स की लिस्ट (बड़ा डेटा हो सकता है)
# HEALTH_KEYWORDS = set([
#     "health", "medicine", "doctor", "hospital", "diet", "exercise", "treatment", "symptoms",
#     "pain", "illness", "nutrition", "fever", "infection", "disease", "bp", "sugar", "cancer",
#     "heart", "lungs", "cough", "headache", "blood pressure", "diabetes", "cholesterol", "therapy",
#     "surgery", "vaccine", "covid", "dentist", "eye", "mental health", "stress", "depression",
#     "anxiety", "meditation", "skin", "allergy", "rash", "hair fall", "weight loss", "gym"
# ])

# app = Flask(__name__)

# # Google Gemini API Setup
# genai.configure(api_key="<api>")
# model = genai.GenerativeModel('gemini-pro')

# # हेल्थ रिलेटेड सवाल चेक करने का फ़ंक्शन
# def is_health_related(text):
#     words = set(nltk.word_tokenize(text.lower()))
#     return any(word in HEALTH_KEYWORDS for word in words)

# @app.route('/chat', methods=['POST'])
# def chat():
#     data = request.json
#     user_input = data.get("message", "").strip()

#     # हेल्थ से संबंधित नहीं है तो यूजर को अलर्ट करना
#     if not is_health_related(user_input):
#         return jsonify({"reply": "⚕️ यह चैटबॉट सिर्फ हेल्थ से जुड़े सवालों के लिए है। क्या आप अपनी या किसी और की सेहत से जुड़ा कुछ पूछना चाहते हैं?"})

#     # Google Gemini API से जवाब प्राप्त करें
#     response = model.generate_content(user_input)
#     reply_text = response.text if response else "मुझे समझ नहीं आया, कृपया फिर से पूछें।"

#     # कैशिंग का सपोर्ट (localStorage के लिए UI में सेटअप करना होगा)
#     return jsonify({"reply": reply_text, "cache": True})

# if __name__ == '__main__':
#     app.run(debug=True)


import google.generativeai as genai
from flask import Flask, request, jsonify
from flask_cors import CORS

# Google Gemini API Key सेट करें
genai.configure(api_key="AIzaSyCr2Lx6jYvB4UuifiVgrJsJtQwWmqIWEjg")

app = Flask(__name__)
CORS(app)  # CORS Enable for frontend

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")

    if not user_input:
        return jsonify({"error": "Message is required"}), 400

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(user_input)
    
    return jsonify({"reply": response.text})

if __name__ == "__main__":
    app.run(debug=True)
