#!/usr/bin/env python

from example_service.example import Example


def main():
    print('I am ExampleCli.init()')
    e = Example()
    e.foo()


if __name__ == '__main__':
    main()
