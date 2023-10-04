from django.test import TestCase


class DummyTest(TestCase):
    """
    This package is a frontend-only package, therefore unit-tests don't apply properly.
    """

    def test_dummy(self):
        self.assertEqual(1, 1)
