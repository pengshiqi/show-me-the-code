#-*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def to_do_list():
    return render_template('ToDoList.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
