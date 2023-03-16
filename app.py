from flask import Flask, request, redirect
import sqlite3

connection = sqlite3.connect("tutorial.db")
cursor = connection.cursor()
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/sentence')
def get_new_sentence():
    if request.method == 'POST':
        sentence = request.form['sentence']
        if sentence:
            words = sentence.strip().split(' ')
            for word in words:
                print(word)

    return redirect('/')


if __name__ == '__main__':
    app.run()
