from example_service.componenta import ComponentA


class Example(object):
    @staticmethod
    def foo():
        print("I am Example.foo()")
        a = ComponentA()
        a.bar()
