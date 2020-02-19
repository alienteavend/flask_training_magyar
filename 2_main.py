from flask import Flask

# A flask alkalmazas
app = Flask(__name__)


# Az utvonal amit szeretnenk hasznalni, es a hozza tartozo fuggveny ami kezeli
@app.route('/')
def hello_world():
    return 'Hello, World!'


# Futtatas: "python 2_main.py"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
