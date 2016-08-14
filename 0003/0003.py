#-*- coding: utf-8 -*-

import redis
from random import Random

__author__ = 'patrick_psq'

def generate_random(length):
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    st = ''.join([chars[Random().randint(0, len(chars) - 1)] for i in xrange(length)])
    return st

if __name__ == '__main__':
    code_length = input('Please input the code length: ')
    code_number = input('Please input the number of codes: ')
    code_list = []
    for i in xrange(code_number):
        code_list.append(generate_random(code_length))

    # A much more awesome way to generate a random string
    # >>> ''.join(map(lambda x:(hex(ord(x))[2:]),os.urandom(16)))

    r = redis.StrictRedis(host='localhost', port=6379, db=0)

    for i in xrange(code_number):
        r.set(str(i), code_list[i])

    for i in xrange(code_number):
        print(r.get(str(i)))
