from example_service.componentb import ComponentB


class ComponentA(object):
    @staticmethod
    def bar():
        print("I am ComponentA.bar()")
        b = ComponentB()
        b.bar()
