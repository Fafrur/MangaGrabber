from flask import Flask, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ppop'

from views import *

if __name__ == '__main__':
    app.run(debug=True, port=1488)
