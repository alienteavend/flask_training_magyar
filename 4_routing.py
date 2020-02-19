from flask import Flask, url_for, request
from markupsafe import escape

# A flask alkalmazasunk, nevvel
app = Flask(__name__)


# Az utvonal amit szeretnenk hasznalni, es a hozza tartozo fuggveny ami kezeli
@app.route('/')
def hello_world():
    return 'Hello, World!'


# Ez a /hello cimen lesz elerheto
@app.route('/hello')
def hello():
    return 'Hello, World'


# A username itt valtozo, amit a kliens adhat meg
@app.route('/user/<username>')
def show_user_profile(username):
    # Escape fontos felhasznaloi adatoknal!
    return 'User %s' % escape(username)


# Megadhatunk tipusellenorzest is
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


# Es tudunk hivatkozni a cimekre a kodban:
@app.route('/menu')
def show_menu():
    return f"""
    <a href="{url_for('show_user_profile', username='Almafa')}">{url_for('show_user_profile', username='Almafa')}</a><br />
    <a href="{url_for('show_post', post_id='12')}">{url_for('show_post', post_id='12')}</a><br />
    <a href="{url_for('hello')}">{url_for('hello')}</a><br />
    """


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
