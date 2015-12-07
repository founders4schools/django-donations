"""Setup file for django-donations."""
from setuptools import setup
# from setuptest import test

from donations import __version__, __version_info__



setup(
    name='django-donations',
    version=__version__,
    packages=[
        'donations',
        'donations.south_migrations',
        'donations.migrations',
        'donations.providers'
    ],
    author='Andrew Miller',
    author_email='andrew.miller@founders4schools.org.uk',
    description='Reusable backend to accept & track donations to your site',
    long_description=open('README.rst').read(),
    url='https://github.com/founders4schools/django-donations/',
    install_requires=[
        'django',
        'django-autoconfig',
        'django-money',
        # this should be replaced when we upgrade to 1.8
        'django-timedeltafield',
        'djangorestframework',
        'requests',
        'py-moneyed',
        'django-environ'
    ],
    tests_require=['django-setuptest', 'requests_mock'],
    # cmdclass={'test': test},
    test_suite='setuptest.setuptest.SetupTestSuite',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Framework :: Django :: 1.6',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
