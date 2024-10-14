import openai
import os

def get_gpt3_response(user_input):
    # Set up OpenAI API key
    openai.api_key = os.getenv("OPENAI_API_KEY")  # Ensure you set this in environment variables

    try:
        # Call OpenAI's GPT-3 API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use the appropriate GPT-3 model
            messages=[
                {"role": "user", "content": user_input}
            ],
            max_tokens=150,
            temperature=0.7
        )

        # Extract the generated response
        gpt3_response = response.choices[0].message['content'].strip()
        return gpt3_response

    except Exception as e:
        return f"An error occurred: {str(e)}"
