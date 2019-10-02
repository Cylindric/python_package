#!/usr/bin/env python

from example import Example


class ExampleCli(object):
    def __init__(self):
        print('I am ExampleCli.init()')
        e = Example()
        e.foo()


if __name__ == '__main__':
    ExampleCli()
