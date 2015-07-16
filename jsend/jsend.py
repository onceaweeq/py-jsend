__author__ = 'zirony'

import json


class DictEx(dict):
    def stringify(self):
        return json.dumps(self)


def success(data={}):
    if not isinstance(data, dict):
        raise ValueError('data must be the dict type')
    return DictEx({'status': 'success', 'data': data})


def fail(data={}):
    if not isinstance(data, dict):
        raise ValueError('data must be the dict type')
    return DictEx({'status': 'fail', 'data': data})


def error(message='', code=None, data=None):
    ret = {}
    if not isinstance(message, str):
        raise ValueError('message must be the str type')
    if code:
        if not isinstance(code, int):
            raise ValueError('code must be the int type')
        ret['code'] = code
    if data:
        if not isinstance(data, dict):
            raise ValueError('data must be the dict type')
        ret['data'] = data

    ret['status'] = 'error'
    ret['message'] = message
    return DictEx(ret)


def loads(jsend_string):
    if not jsend_string:
        raise ValueError('invalid jsend string is given')

    try:
        json_data = json.loads(jsend_string)
    except (TypeError, ValueError):
        raise ValueError('failed to parse json string')

    if ('status' not in json_data or
            json_data['status'] not in ('success', 'fail', 'error')):
        raise ValueError('not in valid jsend type')

    return DictEx(json_data)


def is_success(jsend_msg):
    return jsend_msg['status'] == 'success'


def is_fail(jsend_msg):
    return jsend_msg['status'] == 'fail'


def is_error(jsend_msg):
    return jsend_msg['status'] == 'error'
