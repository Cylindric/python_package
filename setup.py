from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="example_service",
    version="0.0.1",
    author="Mark Hanford",
    author_email="mhanford@ukcloud.com",
    description="A small package to demonstrate python packages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.il2management.local/projects/mp/repos/",
    packages=["example_service"],
    entry_points={
        'console_scripts': [
            'example=example_service.example_cli:main'
        ]
    },
    license='Internal',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    zip_safe=False
)
