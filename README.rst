.. image:: https://pypip.in/v/pyjsend/badge.png
    :target: https://crate.io/packages/pyjsend/
    :alt: Latest PyPI version

.. image:: https://pypip.in/d/pyjsend/badge.png
    :target: https://crate.io/packages/pyjsend/
    :alt: Number of PyPI downloads

py-jsend
========
python jsend
pypi: https://pypi.python.org/pypi/pyjsend/

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

