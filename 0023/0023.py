#-*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def message_board():
    posts = [
    {
        'author': 'pengshiqi',
        'content': 'my first comment'
    },
    {
        'author': 'patrick',
        'content': 'my second comment'
    }
    ]

    data = request.json

    print data

    return render_template('message_board.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
