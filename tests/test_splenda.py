import unittest

import splenda


class TestSplenda(unittest.TestCase):
    def test_implements(self):
        @splenda.implements(spec=ServiceToFake)
        class Fake(object):
            def method_to_fake(self):
                return 1

        self.assertEqual(Fake().method_to_fake(), 1)

    def test_implements_throws_error_if_method_does_not_exist_on_spec(self):
        with self.assertRaises(splenda.MethodMismatchException) as cm:
            @splenda.implements(spec=ServiceToFake)
            class Fake(object):
                def some_other_method(self):
                    return 1

        self.assertEqual(
            str(cm.exception),
            "Fake implements some_other_method. ServiceToFake does not.")


class ServiceToFake(object):
    def method_to_fake(self):
        pass
