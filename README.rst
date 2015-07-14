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

 from onceaweek.tools import jsend
 
 jsend.success({'json':'object'})
 
 jsend.fail({'json:'object'})
 
 jsend.error('message')
 
 jsend.is_success(json_string)
 
 jsend.is_fail(json_string)
 
 jsend.is_error(json_string)
