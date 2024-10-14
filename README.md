# GPT-3 Sentiment Analysis Project

## Overview
This project allows users to interact with GPT-3 to generate text responses, perform sentiment analysis on these responses, and generate visual sentiment reports. It uses a MySQL database to store user interactions and a pie chart for visualizing sentiment results.

## Prerequisites
- Python 3.9 or above
- MySQL database
- Hugging Face API Key

## Setup

### 1. Clone the Project
Clone the repository to your local machine:
```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Install Dependencies
Install the required Python packages:
```bash
pip install -r requirements.txt
```

### 3. Set Up MySQL Database
Create the MySQL database and the necessary table:
```sql
CREATE DATABASE gpt3_project;

USE gpt3_project;

CREATE TABLE interactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_input TEXT NOT NULL,
    gpt_response TEXT NOT NULL,
    sentiment VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 4. Configure Environment Variables
Add your Hugging Face API Key to the `gpt3_integration.py` file or set it as an environment variable. You may also want to create a `.env` file to store your MySQL password and other configuration settings.

### 5. Run the Application
To run the application locally:
```bash
python app.py
```

### 6. Docker Deployment
To deploy the application using Docker:
- **Build the Docker image**:
    ```bash
    docker build -t gpt3_sentiment_project .
    ```

- **Run the Docker container** (make sure your MySQL container is running):
    ```bash
    docker run -it --name gpt3_sentiment_app --link mysql-container2:mysql -p 5000:5000 gpt3_sentiment_project
    ```

## Features
- Text interaction with GPT-3
- Sentiment analysis (Positive, Negative, Neutral)
- MySQL database integration to store interactions
- Pie chart visualization of sentiment analysis results
- User-friendly command-line interface

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [OpenAI](https://openai.com/) for the GPT-3 model
- [Hugging Face](https://huggingface.co/) for the API integration
- [MySQL](https://www.mysql.com/) for the database
- [Matplotlib](https://matplotlib.org/) for data visualization