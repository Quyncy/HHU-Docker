from django.test import SimpleTestCase

from app import rechner

class me(SimpleTestCase):

    def test_calc(self):
        res = rechner.calc(5, 6)

        self.assertEquals(res, 11)
