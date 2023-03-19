import sqlite3
import random

from flask import Flask, request, render_template, redirect
from flask_cors import CORS

# Connect to the DB
connection = sqlite3.connect("scrabble.db", check_same_thread=False)
# Create a cursor to query the DB
cursor = connection.cursor()

# The Flask server
app = Flask(
    __name__
)
CORS(app)


@app.errorhandler(404)
def page_not_found(e):
    """
    Point all pages to the main page.
    :param e: The error received
    :return: Redirect to home page.
    """
    return redirect('/')


@app.route('/')
def index():  # put application's code here
    """
    The home page
    :return: A vue.js app
    """
    return render_template('index.html')


@app.route('/test')
def test():  # put application's code here
    """
    The home page
    :return: A vue.js app
    """
    return 'Hello world!'


@app.route('/api/sentence', methods=['POST'])
def get_new_sentence():
    """
    Endpoint to create the new sentence.
    :return: JSON object containing the new sentence.
    """
    sentence = request.form['sentence']
    new_sentence = ''
    if sentence:
        words = sentence.strip().split(' ')
        for word in words:
            new_sentence += replace_word(word) + " "

    return {
        'new_sentence': new_sentence.strip().capitalize()
    }, 201


def replace_word(old_word: str):
    """
    Replaces a word with one of the same length starting with the same character.
    :param old_word: The word to be replaced
    :return: str
    """
    old_word = old_word.lower()
    sql = "SELECT word FROM words " \
          "WHERE words.first_letter = ? " \
          "AND words.word_length = ? " \
          "AND words.word != ?"
    cursor.execute(sql, (old_word[0], len(old_word), old_word))
    words = list(sum(cursor.fetchall(), ()))

    return random.choice(words) if len(words) > 0 else old_word


# Run the sever if the file is called from the command line.
if __name__ == '__main__':
    app.run()
