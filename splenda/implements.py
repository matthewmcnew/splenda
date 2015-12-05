import inspect

from splenda.exceptions import SplendaException


def implements(spec):
    def f(fake_cls):
        methods_of_fake_cls = inspect.getmembers(fake_cls,
                                                 predicate=inspect.isroutine)

        for fake_method_name, fake_method in methods_of_fake_cls:
            spec_method = getattr(spec, fake_method_name, None)

            if not callable(spec_method):
                raise MethodMismatchException(fake_method_name, fake_cls, spec)
            elif not args_match(spec_method, fake_method):
                raise MethodArgumentMismatchException(fake_method_name, fake_cls, spec)

        return fake_cls

    return f


def args_match(spec_method, fake_method):
    if inspect.ismethoddescriptor(spec_method) or inspect.isbuiltin(spec_method):
        return True

    spec_method_args = inspect.getargspec(spec_method)
    fake_method_args = inspect.getargspec(fake_method)
    print(fake_method_args)
    return len(spec_method_args.args) == len(fake_method_args.args)


class MethodMismatchException(SplendaException):
    message = "{fake_name} implements {method_name}. {spec_name} does not."


class MethodArgumentMismatchException(SplendaException):
    message = "{fake_name} implements {method_name}" \
              " with a different number of arguments then {spec_name}."
