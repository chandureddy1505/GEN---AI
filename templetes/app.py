from flask import Flask, render_template, request
import random

app = Flask(__name__)

quotes = {
    "motivational": [
        "The best way to get started is to quit talking and begin doing.",
        "Don't let yesterday take up too much of today.",
        "It's not whether you get knocked down, it's whether you get up."
    ],
    "humorous": [
        "I'm on a whiskey diet. I've lost three days already.",
        "I used to think I was indecisive, but now I'm not so sure.",
        "Life is short. Smile while you still have teeth."
    ],
    "success": [
        "Success usually comes to those who are too busy to be looking for it.",
        "Don't be afraid to give up the good to go for the great.",
        "I find that the harder I work, the more luck I seem to have."
    ]
}

@app.route('/', methods=['GET', 'POST'])
def home():
    quote = None   # better than empty string
    if request.method == 'POST':
        topic = request.form.get('topic')
        if topic in quotes:
            quote = random.choice(quotes[topic])
        else:
            quote = "No quotes available for this topic."
    return render_template('index.html', quote=quote)

if __name__ == '__main__':
    app.run(debug=True)
