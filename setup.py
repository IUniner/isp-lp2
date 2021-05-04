from setuptools import setup
from setuptools import find_packages

setup(
    name='serializer',
    packages=[
        'serializer_lib',
        'serializer_lib/serializer',
        'serializer_lib/parser_factory',
        'serializer_lib/serializer/serialization',
        'serializer_lib/parsers/json',
        'serializer_lib/parsers/json',
        'serializer_lib/parsers/json',
        'serializer_lib/parsers/json',
        'serializer_lib/parser_factory/parser_objects',
        'serializer_lib/parser_factory/parser_objects/json',
        'serializer_lib/parser_factory/parser_objects/toml',
        'serializer_lib/parser_factory/parser_objects/yaml',
    ],
    version='0.2.1',
    description='Custom serializer by iuniner',
    author='iuniner',
    licence='MIT',
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
    scripts=['bin/iuninerserializer']
)
