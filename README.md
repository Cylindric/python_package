# Example Package

## Things to have in a package

* `README.md`
* `requirements.txt`
* `setup.py`
* `example_service/`` directory
* `example_service/example.py`
* `example_service/example_cli.py` (optional, if you need a CLI wrapper)
* `example_service/tests/`` directory
* `example_service/tests/__init__.py`
* `example_service/tests/test_*.py`

## Things to test in a packages

### From the root of the project, python can import and use the package
```
user@host: ~/example> python
Python 3.7.3 (default, Apr 09 2019, 05:18:21) [GCC] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> from example_service.example import Example
>>> e = Example()
>>> e.foo()
I am Example.foo()
>>>
```

### From the root of the project, the (optional) CLI script can be called
```
user@host: ~/example> example_service/example_cli.py
I am ExampleCli.init()
I am Example.foo()
```
