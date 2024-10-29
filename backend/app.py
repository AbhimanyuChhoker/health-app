from flask import Flask, jsonify, request
import random
from datetime import datetime

app = Flask(__name__)

# Sample user data
user_data = {
    "username": "Abhimanyu",
    "latest_mood": "happy",
    "latest_mood_date": "2024-10-29",
    "mood_streak": 7,
    "meditation_streak": 4,
    "journal_entries": [
        {"date": "2024-10-28", "entry": "Had a productive day!"},
        {"date": "2024-10-27", "entry": "Feeling peaceful after meditation."}
    ],
    "mood_history" : []
}

quotes = [
    "Believe you can and you're halfway there.",
    "You are stronger than you think.",
    "Every day is a second chance.",
    "Start where you are. Use what you have. Do what you can.",
    "It always seems impossible until it’s done.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "The only limit to our realization of tomorrow is our doubts of today.",
    "Don’t watch the clock; do what it does. Keep going.",
    "Everything you’ve ever wanted is on the other side of fear.",
    "Hardships often prepare ordinary people for an extraordinary destiny."
]

#* Dashboard Page APIs

# Endpoint to get the user's dashboard information
@app.route('/api/user/dashboard', methods=['GET'])
def get_user_dashboard():
    dashboard_data = {
        "username": user_data["username"],
        "latest_mood": user_data["latest_mood"],
        "latest_mood_date": user_data["latest_mood_date"],
        "mood_streak": user_data["mood_streak"],
        "meditation_streak": user_data["meditation_streak"],
        "journal_highlight": user_data["journal_entries"][:1]  # Latest entry as highlight
    }
    return jsonify(dashboard_data), 200

# Endpoint to get a greeting based on the time of day
@app.route('/api/greeting', methods=['GET'])
def get_greeting():
    current_hour = datetime.now().hour
    if current_hour < 12:
        greeting = "Good Morning"
    elif 12 <= current_hour < 18:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"
    
    return jsonify({"greeting": f"{greeting}, {user_data['username']}!"}), 200

# Endpoint to get a random motivational quote
@app.route('/api/quotes/random', methods=['GET'])
def get_random_quote():
    random_quote = random.choice(quotes)
    return jsonify({"quote": random_quote}), 200

#* Mood Tracker Page APIs
@app.route('/api/mood', methods=['POST'])
def log_mood():
    new_mood = request.json.get("mood")
    mood_date = datetime.now().strftime("%Y-%m-%d")

    # Update latest mood and streak
    user_data["latest_mood"] = new_mood
    user_data["latest_mood_date"] = mood_date
    user_data["mood_streak"] += 1

    # Append to mood history
    user_data["mood_history"].append({"date": mood_date, "mood": new_mood})

    # Response optimized for frontend
    return jsonify({
        "status": "success",
        "latest_mood": new_mood,
        "date": mood_date,
        "mood_streak": user_data["mood_streak"]
    }), 201

# Endpoint to retrieve mood history
@app.route('/api/mood/history', methods=['GET'])
def get_mood_history():
    return jsonify({
        "status": "success",
        "mood_history": user_data["mood_history"]
    }), 200
if __name__ == "__main__":
    app.run(debug=True, port=5000)
