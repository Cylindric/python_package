from example_service.example import Example


class TestExample(object):

    def test_example(self):
        e = Example()
        e.foo()
