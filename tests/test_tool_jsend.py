from unittest.case import TestCase

import json
import jsend


class TestJsend(TestCase):
    def test_success(self):
        jsend_obj = jsend.success(data={'key': 'value'})
        self.assertTrue(jsend_obj.is_success)
        self.assertEqual(jsend_obj.data['key'], 'value')

    def test_success_data_must_be_dict(self):
        try:
            jsend.success(data=1)
        except ValueError:
            return
        self.fail()

    def test_fail(self):
        jsend_obj = jsend.fail(data={'key': 'value'})
        self.assertTrue(jsend_obj.is_fail)
        self.assertEqual(jsend_obj.data['key'], 'value')

    def test_fail_data_must_be_dict(self):
        try:
            jsend.fail(data=1)
        except ValueError:
            return
        self.fail()

    def test_error(self):
        jsend_obj = jsend.error(message='error message')
        self.assertTrue(jsend_obj.is_error)
        self.assertEqual(jsend_obj.message, 'error message')

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
        jsend_obj = jsend.loads(ret_json_string)
        self.assertTrue(jsend_obj.is_success)


class TestJsendParse(TestCase):
    def test_jsend_from_string(self):
        jsend_str = jsend.success(data={'key': 'value'}).stringify()
        jsend_obj = jsend.loads(jsend_str)
        self.assertEqual(jsend_str, jsend_obj.stringify())
        self.assertTrue(jsend_obj.is_success)
