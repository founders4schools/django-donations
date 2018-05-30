#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = '1.0.0'

readme = codecs.open('README.rst', 'r', 'utf-8').read()
history = codecs.open('HISTORY.rst', 'r', 'utf-8').read().replace('.. :changelog:', '')

install_requires = [
    'django-money',
    'djangorestframework',
    'requests',
    'py-moneyed',
]

setup(
    name='django-donations',
    version=version,
    description="""Reusable django app to receive & track donations on charitable sites""",
    long_description=readme + '\n\n' + history,
    author='Andrew Miller',
    author_email='dev@founders4schools.org.uk',
    url='https://github.com/founders4schools/django-donations',
    packages=[
        'donations',
    ],
    include_package_data=True,
    install_requires=install_requires,
    license="BSD",
    zip_safe=False,
    keywords='django-donations',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
