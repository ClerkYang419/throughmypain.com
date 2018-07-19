#!/usr/bin/env python3

from unittest import TestCase
from unittest import mock
# from unittest import mock
# from mock import patch
import app

class standalonetest(TestCase):
    
    @patch('__builtin__.open')
    def test_login(self, mock_open):
        mock_open.return_value.read.return_value = \
            'netease|password\n'
        self.assertTrue(app.valid_login('netease', 'password'))

    @patch('__builtin__.open')
    def test_login_bad_creds(self, mock_open):
        mock_open.return_value.read.return_value = \
            'netease|password'
        self.assertFalse(app.valid_login('netease', 'badpassword'))

    @patch('__builtin__.open')
    def test_login_error(self, mock_open):
        mock_open.side_effect = IOError()
        self.assertFalse(app.valid_login('netease', 'password'))