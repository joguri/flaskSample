import unittest
import App
import tempfile
import os
from bson.json_util import dumps, loads


class AppNoteTestCase(unittest.TestCase):

    def setUp(self):
        self.db, App.app.config['DATABASE'] = tempfile.mkstemp()
        App.app.config['TESTING'] = True
        self.app = App.app.test_client()

    def utilCreate(self, title, content, id):
        obj_str = {'title': title,
                   'content': content,
                   'id': id}
        rv = self.app.post('/note/', data=dumps(obj_str))
        return loads(rv.data)[0]['_id']

    def utilDelete(self, title, content, id):
        self.app.delete('/note/' + id)

    def tearDown(self):
        os.close(self.db)
        os.unlink(App.app.config['DATABASE'])

    def test_empty_db(self):
        rv = self.app.get('/note/')
        print rv.data
        assert 'Created with the tests' in rv.data

    def test_addOne(self):
        id = utilCreate('Created with the tests',
                        'This was created in the test called test_addOne',
                        44)
        print "Test Result: ", id


if __name__ == '__main__':
    unittest.main()