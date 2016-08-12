#-*- coding: utf-8 -*-

import MySQLdb
from random import Random

__author__ = 'patrick_psq'

def generate_random(length):
    st = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    len_chars = len(chars)
    for i in xrange(length):
        st += chars[Random().randint(0, len_chars - 1)]
    return st

if __name__ == '__main__':
    code_length = input('Please input the code length: ')
    code_number = input('Please input the number of codes: ')
    code_list = []
    for i in xrange(code_number):
        code_list.append(generate_random(code_length))

    # A much more awesome way to generate a random string
    # >>> ''.join(map(lambda x:(hex(ord(x))[2:]),os.urandom(16)))

    conn = MySQLdb.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        passwd = '123456',
        db = 'test'
    )
    cur = conn.cursor()

    for code in code_list:
        cur.execute("insert into Codes(code) values ('%s')" % (code))

    cur.close()
    conn.commit()
    conn.close()
