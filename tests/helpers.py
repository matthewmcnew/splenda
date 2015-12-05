from contextlib import contextmanager

class Context(object):
    pass

@contextmanager
def assert_raises(expected_exception):
    '''
    unittest.TestCase Python 2.6 compatible assert_raises context manager
    '''
    context = Context()
    try:
        yield context
    except expected_exception as e:
        context.exception = e
    except Exception as e:
        raise Exception('Unexpected exception thrown:', e)
    else:
       raise Exception('{} not thrown'.format(expected_exception))