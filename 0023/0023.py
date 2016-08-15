#-*- coding: utf-8 -*-

import time
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

posts = [
{
    'name': 'pengshiqi',
    'content': 'my first comment',
    'time': '2016-08-01 00:00:00'
},
{
    'name': 'patrick',
    'content': 'my second comment',
    'time': '2016-08-01 00:00:00'
}
]

@app.route('/', methods=['GET', 'POST'])
def message_board():
    data = request.form

    d = dict(data)

    if d:
        posts.append(dict([('name', d['name'][0]), ('content', d['content'][0]), ('time', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))]))

    return render_template('message_board.html', posts=posts)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
