
import google.generativeai as genai
from flask import Flask, request, jsonify
from flask_cors import CORS

# Google Gemini API Key सेट करें
genai.configure(api_key="AIzaSyCr2Lx6jYvB4UuifiVgrJsJtQwWmqIWEjg")

app = Flask(__name__)
CORS(app)  # CORS Enable for frontend

# 🔹 Home Route for Debugging (Fix 404 Error)
@app.route("/")
def home():
    return render_template("index.html")
    
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
