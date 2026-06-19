from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/lifecaffeine/tell_smth_nice')
def tell_something_nice():
    starts = [
        "Hi there, ",
        "Greetings, "
    ]
    middles = [
        "you aren't like anyone else, you are unique, meaning you're special. Out of every single person on earth, who looks exactly the same as next one, you look like yourself, and that's a good thing!",
        "how's life going? Probably not, but also probably yes, doesn't matter anyway. What I want to deliever to you is that you can always express any feeling you want, because why wouldn't you?"
    ]
    end = [
        " Unfortunately I will have to interrupt nicetelling to tell you that LifeCaffeine is still in beta, but still, come back next day :-)"
    ]

    partone = random.choice(starts)
    parttwo = random.choice(middles)
    partthree = random.choice(end)

    return partone + parttwo + partthree

if __name__ == '__main__':
    app.run()
