from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/lifecaffeine/tell_smth_nice')
def tell_something_nice():
    return "your smart ;)"

if __name__ == '__main__':
    app.run()
