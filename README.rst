py-jsend
========
python jsend
pypi: https://pypi.python.org/pypi/pyjsend/

.. image:: https://travis-ci.org/onceaweeq/py-jsend.svg?branch=master
    :target: https://travis-ci.org/onceaweeq/py-jsend

.. image:: https://badge.fury.io/py/pyjsend.svg
    :target: http://badge.fury.io/py/pyjsend


About jsend
-----------
http://labs.omniti.com/labs/jsend


Install
-------
pip install pyjsend

Usage
-----

import module::

 >>> import jsend

success::

 >>> jsend.success({'key': 'value'})
 {'status': 'success', 'data': {'key': 'value'}}

 >>> jsend.success(data={'key': 'value'}, meta={'meta_key': 'meta_val'})
 {'status': 'success', 'data': {'key': 'value'}, 'meta': {'meta_key', 'meta_val'}}

fail::

 >>> jsend.fail({'key': 'value'})
 {'status': 'fail', 'data': {'key': 'value'}}

error::

 >>> jsend.error('message')
 {'status': 'error', 'message': 'message'}

is success::

 >>> jsend.is_success({'status':'success'})
 True

is fail::

 >>> jsend.is_fail({'status':'fail'})
 True

is error::

 >>> jsend.is_error({'status':'error'})
 True

to json string and load jsend string::

 >>> jsend.success({'key': 'value'}).stringify()
 '{"status": "success", "data": {"key": "value"}}'

 >>> jsend.loads(jsend.success({'key': 'value'}).stringify())
 {u'status': u'success', u'data': {u'key': u'value'}}

