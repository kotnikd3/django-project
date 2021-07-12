from unittest import TestCase

from blog.views import test


class Test(TestCase):
    def test_test(self):
        t = test("kotnik")
        self.assertEqual(t, "kotnikda")
