from django.test import TestCase, Client

class TimelineTestCase(TestCase):
    def setUp(self):
        self.c = Client()
    
    def test_index_access(self):
        res = self.c.get('/')
        # レスポンスコードが200かどうか
        self.assertEqual(200, res.status_code)

    def test_fail_access(self):
        res = self.c.get('/unknown')
        self.assertEqual(404, res.status_code)
