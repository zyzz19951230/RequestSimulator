# -*- coding: utf-8 -*-

"""
模拟客户端向指定的URL发送request，接收并处理response
"""

import requests

METHODS = {"GET": requests.get, "POST": requests.post, "PUT": requests.put, "DELETE": requests.delete,
           "OPTIONS": requests.options, "HEAD": requests.head}

BASE_URL = 'https://github.com'


def send_request(url, method, **kwargs):
    request_func = METHODS[method]
    if request_func is None:
        raise RuntimeError('method not supported: %s' % method)

    response_ = request_func(url, **kwargs)
    return response_


def show_response(response):
    print('------ Response Information ------')
    print('Headers:')
    for k in response.headers:
        print(' %s: %s' % (k, response.headers[k]))
    print()

    print('Status:')
    print('  status_code: %s' % response.status_code)
    print()

    print('Cookies:')
    print(response.cookies)
    print()

    print("Content")
    print("  content: %s" % response.content)
    print()

if __name__ == '__main__':

    res = send_request(BASE_URL, 'GET')

    if res is not None:
        show_response(res)
