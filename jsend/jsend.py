__author__ = 'zirony'

import json


JSEND_STATUS_SUCCESS = 'success'
JSEND_STATUS_FAIL = 'fail'
JSEND_STATUS_ERROR = 'error'
JSEND_STATUSES = (JSEND_STATUS_SUCCESS, JSEND_STATUS_FAIL, JSEND_STATUS_ERROR)


class JSENDObject(object):
    def __init__(self, status=None, data={}, code=0, message=''):
        self.status = status
        self.data = data

        # For error only
        self.code = code
        self.message = message

    @property
    def is_success(self):
        return self.status == JSEND_STATUS_SUCCESS

    @property
    def is_fail(self):
        return self.status == JSEND_STATUS_FAIL

    @property
    def is_error(self):
        return self.status == JSEND_STATUS_ERROR

    def stringify(self):
        jsend_obj = {'status': self.status, 'data': self.data}
        if self.status == JSEND_STATUS_ERROR:
            jsend_obj.update({'code': self.code, 'message': self.message})
        return json.dumps(jsend_obj)


def success(data={}):
    if not isinstance(data, dict):
        raise ValueError('data must be the dict type')
    return JSENDObject(status=JSEND_STATUS_SUCCESS, data=data)


def fail(data={}):
    if not isinstance(data, dict):
        raise ValueError('data must be the dict type')
    return JSENDObject(status=JSEND_STATUS_FAIL, data=data)


def error(message='', code=0, data={}):
    if not isinstance(message, str):
        raise ValueError('message must be the str type')

    if code and not isinstance(code, int):
        raise ValueError('code must be the int type')

    if data and not isinstance(data, dict):
        raise ValueError('data must be the dict type')

    return JSENDObject(status=JSEND_STATUS_ERROR, data=data, code=code, message=message)


def loads(jsend_string):
    if not jsend_string:
        raise ValueError('invalid jsend string is given')

    try:
        json_data = json.loads(jsend_string)
    except (TypeError, ValueError):
        raise ValueError('failed to parse json string')

    if 'status' not in json_data:
        raise ValueError('not in valid jsend type')

    status = json_data['status']
    data = json_data['data']
    code = json_data['code'] if 'code' in json_data else 0
    message = json_data['message'] if 'message' in json_data else ''

    if status  not in JSEND_STATUSES:
        raise ValueError('not in valid jsend type')

    return JSENDObject(status=status, data=data, code=code, message=message)
