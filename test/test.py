#!/usr/bin/env python3
import sys
sys.path.append('../www')
import unittest
import os
import tempfile
import fsk

class standalonetest(unittest.TestCase):
    def setUp(self):
        self.db_fd, fsk.app.config['DATABASE'] = tempfile.mkstemp()
        fsk.app.config['TESTING'] = True
        self.app = fsk.app.test_client()
    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(fsk.app.config['DATABASE'])

    def login(self,username, password):
        return self.app.post('/login', data=dict(
            username=username,
            password=password
            ), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def test_login_logout(self):
        rv = self.login('admin', 'default')
        assert 'You were logged in'.encode() in rv.data
        rv = self.logout()
        assert 'You were logged out'.encode() in rv.data
        rv = self.login('', 'default')
        assert 'Invalid username/password'.encode() in rv.data
        rv = self.login('admin', '')
        assert 'Invalid username/password'.encode() in rv.data

if __name__ == '__main__':
    unittest.main()