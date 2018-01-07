import os
import bookstore
import unittest
import tempfile

class BookstoreTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, bookstore.app.config['DATABASE'] = tempfile.mkstemp()
        bookstore.app.testing = True
        self.app = bookstore.app.test_client()
        with bookstore.app.app_context():
            bookstore.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(bookstore.app.config['DATABASE'])

if __name__ == '__main__':
    unittest.main()
