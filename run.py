from flask import Flask, session

app = Flask(__name__)
app.config['SECRET_KEY'] = '1231231sfafq2131sfw44556df'

from views import *

if __name__ == '__main__':
    app.run(debug=True, port=1488)
