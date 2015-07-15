py-jsend
========
python jsend

About jsend
-----------
http://labs.omniti.com/labs/jsend


Install
-------
pip install pyjsend

Usage
-----

An example::

 from onceaweek.tools import jsend

 # to generate jsend formatted dictionary
 jsend.success({'key':'value'}) 
 # output = {'status':'success', 'data':{'key':'value'}

 jsend.fail({'json':'object'})
 jsend.error('message')
 
 jsend.is_success(json_string)
 jsend.is_fail(json_string)
 jsend.is_error(json_string)
