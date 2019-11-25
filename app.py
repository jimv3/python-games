from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import random
import uuid
from HangmanGame import HangmanGame

app = Flask(__name__)
bootstrap = Bootstrap(app)
sessions = {}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hangman')
def hangman():
    global sessions
    session_id = uuid.uuid4().hex
    game = HangmanGame()
    sessions[session_id] = game
    return create_hangman_page(session_id, game)


@app.route('/hangman/<session_id>/<guess>')
def hangman_make_guess(session_id, guess):
    global sessions
    game = sessions[session_id]
    game.make_guess(guess)
    if game.game_is_done():
        del sessions[session_id]
        return render_template('hangman_game_over.html', gallows=game.display_gallows(), board=game.display_board(), winner=game.is_winner(), secret_word=game._secret_word)
    else:
        return create_hangman_page(session_id, game)

def create_hangman_page(session_id, game):
    return render_template('hangman.html', gallows=game.display_gallows(), category=game.get_category(), board=game.display_board(), session_id=session_id, missed=game.missed(), already_guessed=game.already_guessed())

if __name__ == '__main__':
    app.run()
