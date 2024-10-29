from flask import Flask, jsonify, make_response
import random
from datetime import datetime
from quote import quote

app = Flask(__name__)

user_data = {
    "username": "Abhimanyu",
    "latest_mood": "ruined",
    "latest_mood_date": "2024-10-25",
    "mood_streak": 5,
    "meditation_streak": 3
}

# Endpoint to get the user's dashboard information
@app.route('/api/user/dashboard', methods=['GET'])
def get_user_dashboard():
    return jsonify(user_data), 200

# Endpoint to get a random motivational quote
@app.route('/api/quotes/random', methods=['GET'])
def get_random_quote():
    return True


@app.route('/api/greeting', methods=['GET'])
def get_greeting():
    current_hour = datetime.now().hour
    if current_hour < 12:
        greeting = "Good Morning"
    elif 12 <= current_hour < 18:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"
    
    return jsonify({"greeting": f"{greeting}, Abhimanyu!"}), 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)
