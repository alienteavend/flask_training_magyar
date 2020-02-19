from flask import Flask

# A flask alkalmazas
app = Flask(__name__)


# JSONt adunk vissza
@app.route('/')
def me_api():
    return {
        "model": 'AAA231',
        "year": 2011,
        "type": "Almafa"
    }
