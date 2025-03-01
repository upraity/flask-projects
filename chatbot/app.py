
import google.generativeai as genai
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

# API Key Set karein
genai.configure(api_key="api")

app = Flask(__name__)
CORS(app)  # CORS Enable for frontend

@app.route("/")
def home():
    # return "Flask Chatbot API is Running! Use /chat for API."
      return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "").lower()

    if not user_input:
        return jsonify({"error": "Message is required"}), 400

    # Agar user chatbot ke baare me puche to introduction do
    intro_keywords = [
        "tum kaun ho", "tum kya karte ho", "kisne banaya", "tumhara naam kya hai", "tum kiske dwara banaye gaye ho",
        "tumhe kisne develop kiya", "tumhari pehchan kya hai", "tum kya ho", "tumhara kaam kya hai", 
        "tumhara purpose kya hai", "tum kisliye bane ho", "tum kahan se aaye ho", "tumhara uddeshya kya hai", 
        "tum kaise kaam karte ho", "tum kis tarah madad kar sakte ho", "tumhe kaise banaya gaya hai", 
        "tumhari capability kya hai", "tum kaisa kaam kar sakte ho", "tum kitna jaante ho", "tumhari knowledge kya hai", 
        "tumhara creator kaun hai", "tumhari team kaun hai", "tumhari language kya hai", "tum kis company ke ho", 
        "tum kahan located ho", "tumhare features kya hain", "tum AI ho kya", "tum ek chatbot ho kya", 
        "tum kaisi AI ho", "tum kis technology par bane ho", "tum kis par based ho", "tumhari training kaise hui", 
        "tum kis model par kaam karte ho", "tumhari memory hai kya", "tum kitna smartho", "tumhari powers kya hain", 
        "tum kis field me expert ho", "tum kis prakriya se seekhte ho", "tum kya samajh sakte ho", "tumhara creator kaun hai",
        "tumhari janakari kisne di", "tum internet se connect ho kya", "tum kis tarah se improve hote ho", 
        "tum apne aap seekh sakte ho kya", "tum human ho kya", "tum machine ho kya", "tum kis level ki AI ho", 
        "tum offline kaam kar sakte ho kya", "tum self aware ho kya", "tum kahan tak seekh sakte ho", 
        "tumhare limitations kya hain", "tumhare advantages kya hain", "tum kis ke liye bane ho", "tum kaunse kaam nahi kar sakte", 
        "tum kis language me likhe gaye ho", "tumhara development kaise hua", "tum offline ho ya online", 
        "tum kis tarah ke sawal ka jawab de sakte ho", "tum kis prakriya ka istemal karte ho", "tum kitni accuracy ke sath jawab dete ho", 
        "tum kis database se connected ho", "tum khud se soch sakte ho kya", "tum mujhe kaise samajhte ho", 
        "tum kis company ke under kaam karte ho", "tum AI ke kis level par ho", "tumhara code kis language me likha gaya hai", 
        "tum kis prakar ke user queries handle kar sakte ho", "tum kis prakriya se sochte ho", "tum kis base par jawab dete ho", 
        "tum kis AI model ka use karte ho", "tumhare peeche ka science kya hai", "tum kis tarah se response generate karte ho", 
        "tum kahan tak samajh sakte ho", "tum kis AI framework par kaam karte ho", "tumhara training data kya hai", 
        "tum kis prakriya se answer generate karte ho", "tum kis data source ka use karte ho", "tum kis prakriya se naye concepts seekhte ho", 
        "tum kis company ke sath judhe ho", "tum AI ethics ko follow karte ho kya", "tum kis authority ke under ho", 
        "tum kya soch sakte ho", "tum kis limit tak kaam kar sakte ho", "tum AI ethics follow karte ho ya nahi", 
        "tumhare response kis tarah se generate hote hain", "tum kis prakar ka learning method use karte ho", 
        "tum kis software ka use karte ho", "tumhare algorithms kaise kaam karte hain", "tum kis tarah ke sawalon ka jawab nahi de sakte", 
        "tumhara system kaise develop kiya gaya", "tum kis prakriya se naye words samajhte ho", "tum kis AI ka version ho", 
        "tum real ho ya virtual", "tum offline bhi kaam kar sakte ho kya", "tumhara upgrade kaise hota hai", 
        "tum kis tarah se naye concepts adopt karte ho", "tumhara evolution kaise hota hai", "tumhari accuracy kaise improve hoti hai"
    ]

    if any(keyword in user_input for keyword in intro_keywords):
        bot_response = (
            "मैं Health Care Chat Bot हूँ।\n"
            "मेरा काम स्वास्थ्य से जुड़ी समस्याओं पर मदद करना है।\n"
            "आप मुझसे बीमारियों, लक्षणों, दवाइयों, डाइट, हेल्थ टिप्स आदि के बारे में पूछ सकते हैं।\n\n"
            # "**आपका सवाल:** " + user_input + "\n\n"
            "मैं आपकी किस तरह से सहायता कर सकता हूँ?"
        )
    else:
        # Agar normal health-related sawal hai to bina introduction ke jawab do
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(user_input)

        # **सिर्फ बॉट का नाम बदलेंगे, बाकी डेटा नहीं छेड़ेंगे**
        bot_response = response.text
        if "Gemini" in bot_response or "Google" in bot_response:
            bot_response = bot_response.replace("Gemini", "Health Care Chat Bot")
            bot_response = bot_response.replace("Google द्वारा विकसित", "AI द्वारा विकसित")  # ज्यादा natural लगे

    return jsonify({"reply": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
