from flask import Flask, request, json
import sqlite3
import random

connection = sqlite3.connect("scrabble.db", check_same_thread=False)
cursor = connection.cursor()
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/sentence', methods=['POST'])
def get_new_sentence():
    sentence = request.form['sentence']
    new_sentence = ''
    if sentence:
        words = sentence.strip().split(' ')
        for word in words:
            print(word)
            new_sentence += replace_word(word) + " "

    return {
        'new_sentence': new_sentence.strip().capitalize()
    }


def replace_word(old_word: str):
    old_word = old_word.lower()
    sql = "SELECT word FROM words " \
          "WHERE words.first_letter = ? " \
          "AND words.word_length = ? " \
          "AND words.word != ?"
    cursor.execute(sql, (old_word[0], len(old_word), old_word))
    words = list(sum(cursor.fetchall(), ()))

    return random.choice(words) if len(words) > 0 else old_word


if __name__ == '__main__':
    app.run()
