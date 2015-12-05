import inspect


def implements(spec):
    def f(fake_class):
        methods_of_klass = inspect.getmembers(fake_class,
                                              predicate=inspect.isroutine)
        for method_name, method in methods_of_klass:
            spec_method = getattr(spec, method_name, None)

            if not callable(spec_method):
                raise MethodMismatchException(method_name, fake_class, spec)
        return fake_class

    return f


class MethodMismatchException(Exception):

    def __init__(self, method_name, fake_class, spec_class):
        self.fake_class = fake_class
        self.spec_class = spec_class
        self.method_name = method_name

    def __str__(self):
        spec_name = self.spec_class.__name__
        fake_name = self.fake_class.__name__
        return "{0} implements {1}. {2} does not.".format(
            fake_name, self.method_name, spec_name)
