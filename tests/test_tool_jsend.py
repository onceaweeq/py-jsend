from unittest.case import TestCase

import json
import jsend


class TestJsend(TestCase):
    def test_success(self):
        ret = jsend.success(data={'key': 'value'})
        self.assertTrue(jsend.is_success(ret))
        self.assertEqual(ret['data']['key'], 'value')

    def test_success_with_meta(self):
        ret = jsend.success(data={'key': 'value'}, meta={'meta_key': 'meta_value'})
        self.assertTrue(ret['meta']['meta_key'], 'meta_value')
        self.assertTrue(ret['data']['key'], 'value')

    def test_success_data_must_be_dict(self):
        try:
            jsend.success(data=1)
        except ValueError:
            return
        self.fail()

    def test_success_meta_must_be_dict(self):
        try:
            jsend.success(data={'key', 'value'}, meta=1)
        except ValueError:
            return
        self.fail()

    def test_fail(self):
        ret = jsend.fail(data={'key': 'value'})
        self.assertTrue(jsend.is_fail(ret))
        self.assertEqual(ret['data']['key'], 'value')

    def test_fail_data_must_be_dict(self):
        try:
            jsend.fail(data=1)
        except ValueError:
            return
        self.fail()

    def test_error(self):
        ret = jsend.error(message='error message')
        self.assertTrue(jsend.is_error(ret))
        self.assertEqual(ret['message'], 'error message')

    def test_error_unicode(self):
        ret = jsend.error(message=u'error message')
        self.assertTrue(jsend.is_error(ret))
        self.assertEqual(ret['message'], u'error message')

    def test_error_bytes(self):
        ret = jsend.error(message=b'error message')
        self.assertTrue(jsend.is_error(ret))
        self.assertEqual(ret['message'], b'error message')

    def test_error_message_must_be_str(self):
        try:
            jsend.error(message=1)
        except ValueError:
            return
        self.fail()

    def test_error_code_must_be_number(self):
        try:
            jsend.error(code='1')
        except ValueError:
            return
        self.fail()

    def test_error_data_must_be_dict(self):
        try:
            jsend.error(data=1)
        except ValueError:
            return
        self.fail()

    def test_jsend_to_stringify(self):
        ret_json_string = jsend.success().stringify()
        ret_json = json.loads(ret_json_string)
        self.assertTrue(jsend.is_success(ret_json))

    def test_jsend_to_stringify_f(self):
        ret_json_string = jsend.success().stringify()
        try:
            jsend.is_success(ret_json_string)
        except TypeError:
            return

        self.fail()


class TestJsendLoads(TestCase):
    def test_jsend_from_string(self):
        jsend_str = jsend.success(data={'key': 'value'}).stringify()
        jsend_obj = jsend.loads(jsend_str)
        self.assertEqual(jsend_str, jsend_obj.stringify())
