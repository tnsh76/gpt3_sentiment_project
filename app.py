from dotenv import load_dotenv
import os
from flask import Flask, render_template, request, redirect, url_for

from utils.gpt3_integration import get_gpt3_response
from utils.sentiment_analysis import analyze_sentiment
from utils.database import insert_data
from utils.report_generation import create_pie_chart

# Initialize Flask app
app = Flask(__name__)

# Load environment variables
load_dotenv()
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
HUGGINGFACE_API_KEY = os.getenv('HUGGINGFACE_API_KEY')

# Global variable to store chat history and sentiments
chat_history = []
sentiments = []

@app.route('/')
def home():
    return render_template('index.html', interactions=chat_history)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    
    if user_input.lower() == 'exit':
        # Generate the pie chart when 'exit' is entered
        create_pie_chart(sentiments)
        return redirect(url_for('report'))

    # GPT-3 API call with error handling
    try:
        gpt3_response = get_gpt3_response(user_input)
    except Exception as e:
        if "exceeded your current quota" in str(e):
            gpt3_response = "Error: You have exceeded your current quota for the OpenAI API."
        else:
            gpt3_response = "Error getting response from GPT-3."

    # Perform sentiment analysis
    sentiment = analyze_sentiment(gpt3_response)
    sentiments.append(sentiment)

    # Store the chat interaction
    interaction = {
        'user_input': user_input,
        'gpt3_response': gpt3_response,
        'sentiment': sentiment
    }
    chat_history.append(interaction)

    # Store interaction in MySQL database with error handling
    try:
        insert_data(user_input, gpt3_response, sentiment)
    except Exception as e:
        print(f"Error inserting data into the database: {str(e)}")

    return render_template('index.html', interactions=chat_history)

@app.route('/report')
def report():
    # Serve the generated pie chart
    return render_template('report.html', chart_image='sentiment_analysis_report.png')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
