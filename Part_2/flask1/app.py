from flask import Flask, render_template
import random

app = Flask(__name__)

quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "We need to be willing to be comfortable with discomfort in order to grow. - Michael Port",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill"
    ]

@app.route('/')
def random_quote():
    quote = random.choice(quotes)
    # Add an HTML header with an h1 element
    return f"<h1>Welcome to the first example Flask App #1!</h1><p>Random Quote: {quote}</p>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5005)