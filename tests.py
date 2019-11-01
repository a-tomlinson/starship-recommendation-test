# -*- coding: utf-8 -*-

import json
import unittest

from main import app


class MainTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_sum_matrix(self):
        r = self.app.post('/api/matrix/sum', 
            data=json.dumps({"matrix": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}), 
            headers={'Accept': 'application/json', 'Content-Type': 'application/json'})

        self.assertEqual(r.status_code, 200)

        result = json.loads(r.get_data(as_text=True))
        self.assertEqual(result['result'], 45)

    def test_sum_matrix_invalid_data(self):
        r = self.app.post('/api/matrix/sum', 
            data=json.dumps({"matrix": [[1, 2, 3], 'matrix', [7, 8, 9]]}), 
            headers={'Accept': 'application/json', 'Content-Type': 'application/json'})

        self.assertEqual(r.status_code, 200)

        result = json.loads(r.get_data(as_text=True))
        self.assertEqual(result['error'], 'Please, introduce a valid matrix')

    def test_sum_diagonal_matrix(self):
        r = self.app.post('/api/matrix/diagonal_sum', 
            data=json.dumps({"matrix": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}), 
            headers={'Accept': 'application/json', 'Content-Type': 'application/json'})

        self.assertEqual(r.status_code, 200)

        result = json.loads(r.get_data(as_text=True))
        self.assertEqual(result['result'], 15)

    def test_sum_diagonal_matrix_invalid_data(self):
        r = self.app.post('/api/matrix/diagonal_sum', 
            data=json.dumps({"matrix": [[1, 2, 3], 'matrix', [7, 8, 9]]}), 
            headers={'Accept': 'application/json', 'Content-Type': 'application/json'})

        self.assertEqual(r.status_code, 200)

        result = json.loads(r.get_data(as_text=True))
        self.assertEqual(result['error'], 'Please, introduce a valid matrix')

    def test_encode_string(self):
        r = self.app.post('/api/string/encode', 
            data=json.dumps({ "string": "aaAabaccCBb" }), 
            headers={'Accept': 'application/json', 'Content-Type': 'application/json'})

        self.assertEqual(r.status_code, 200)

        result = json.loads(r.get_data(as_text=True))
        self.assertEqual(result['result'], 'A4B1A1C3B2')


    def test_encode_string_invalid_data(self):
        r = self.app.post('/api/string/encode', 
            data=json.dumps({"string": [1, 2, 3]}), 
            headers={'Accept': 'application/json', 'Content-Type': 'application/json'})

        self.assertEqual(r.status_code, 200)

        result = json.loads(r.get_data(as_text=True))
        self.assertEqual(result['error'], 'Please, introduce a string')


if __name__ == '__main__':
    unittest.main()
