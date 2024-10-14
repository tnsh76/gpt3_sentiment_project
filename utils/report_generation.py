import matplotlib.pyplot as plt

def create_pie_chart(sentiments):
    sentiment_counts = {sentiment: sentiments.count(sentiment) for sentiment in set(sentiments)}

    # Create a pie chart
    labels = sentiment_counts.keys()
    sizes = sentiment_counts.values()
    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Save the pie chart to the static folder
    plt.savefig('static/sentiment_analysis_report.png')
    plt.close()
