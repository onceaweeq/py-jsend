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

 >>> jsend_obj = jsend.success({'key': 'value'})
 >>> jsend_obj.status
 'success'
 >>> jsend_obj.data
 {'key': 'value'}

fail::

 >>> jsend_obj = jsend.fail({'key': 'value'})
 >>> jsend_obj.status
 'fail'
 >>> jsend_obj.data
 {'key': 'value'}
 
error::

 >>> jsend_obj = jsend.error('error message')
 >>> jsend_obj.status
 'error'
 >>> jsend_obj.message
 'error message'
 
is success::

 >>> jsend_obj = jsend.success({'status':'success'})
 >>> jsend_obj.is_success
 True

is fail::

 >>> jsend_obj = jsend.fail({'status':'fail'})
 >>> jsend_obj.is_fail
 True

is error::

 >>> jsend_obj = jsend.error({'status':'error'})
 >>> jsend_obj.is_error
 True


to json string::

 >>> jsend.success({'key': 'value'}).stringify()
 '{"status": "success", "data": {"key": "value"}}'


from json string::

 >>> json_string = '{"status": "success", "data": {"key": "value"}}'
 >>> jsend_obj = jsend.loads(json_string)
 >>> jsend_obj.is_success
 True


example::

 >>> jsend_obj = jsend.success({'key': 'value'})
 >>> jsend_obj.status
 'success'
 >>> jsend_obj.data
 {'key': 'value'}
 >>> json_obj.data['key']
 'value'
 >>> json_obj.data['key'] = 'value2'
 >>> json_obj.stringify()
 '{"status": "success", "data": {"key": "value2"}}'
