import unittest
import splenda
from tests.helpers import assert_raises


class TestSplenda(unittest.TestCase):
    def test_implements(self):
        @splenda.implements(spec=ServiceToFake)
        class Fake(object):
            def method_to_fake(self):
                return 1

        self.assertEqual(Fake().method_to_fake(), 1)

    def test_implements_raises_error_if_method_does_not_exist_on_spec(self):
        with assert_raises(splenda.MethodMismatchException) as cm:
            @splenda.implements(spec=ServiceToFake)
            class Fake(object):
                def some_other_method(self):
                    return 1

        self.assertEqual(
            str(cm.exception),
            "Fake implements some_other_method. ServiceToFake does not.")

    def test_implements_raises_error_if_method_has_different_arguments(self):
        with assert_raises(splenda.MethodArgumentMismatchException) as cm:
            @splenda.implements(spec=ServiceToFake)
            class Fake(object):
                def method_to_fake_with_args(self, arg1):
                    pass

        self.assertEqual(
            str(cm.exception),
            "Fake implements method_to_fake_with_args with a"
            " different number of arguments then ServiceToFake."
        )


class ServiceToFake(object):
    def method_to_fake(self):
        pass

    def method_to_fake_with_args(self, arg1, arg2):
        pass
