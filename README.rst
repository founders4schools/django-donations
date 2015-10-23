Django Donations
================

.. image:: https://img.shields.io/travis/founders4schools/django-donations.svg?style=flat-square
   :target: https://travis-ci.org/founders4schools/django-donations

.. image:: https://img.shields.io/coveralls/founders4schools/django-donations.svg?style=flat-square
   :target: https://coveralls.io/github/founders4schools/django-donations?branch=master

.. image:: https://landscape.io/github/founders4schools/django-donations/master/landscape.svg?style=flat-square
  :target: https://landscape.io/github/founders4schools/django-donations/master
  :alt: Code Health

.. image:: https://img.shields.io/requires/github/founders4schools/django-donations.svg?style=flat-square
   :target: https://requires.io/github/founders4schools/django-donations/requirements/?branch=master
   
.. image:: https://badge.fury.io/py/django-donations.svg
    :target: https://badge.fury.io/py/django-donations


TODO
====

* Update the documentation and readme
* integrate with readthedocs or pythonhosted or both!
* tests - unit/integration
* task to periodically verify pending donations

(* dashboard - track/view donations from the business side - kpis etc
* views/urls? - provide an api hook into the system (/donations - dashboard))

v2 and beyond
-------------
* (other providers (paypal etc))
* tasks.py - recurring donation handling - this is not possible right now as SDI is not an API to be automated

Usage
-----

Example app is under `./example/app`. Basically subclass `DonateView` or POST to `DonateAPI` with the correct data.... (example needed)
When using `DonateView`, there is the `DonationForm` which can be subclassed to customize or just used by itself.

Settings
--------


Supported Providers
-------------------

* Just Giving SDI


Basic Commands - Update to be correct
-------------------------------------

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run manage.py test
    $ coverage html
    $ open htmlcov/index.html

Running end to end integration tests
------------------------------------

N.B. The integration tests will not run on Windows.

To install the test runner::

  $ pip install hitch

To run the tests, enter the django-donations/tests directory and run the following commands::

  $ hitch init

Then run the stub test::

  $ hitch test stub.test

This will download and compile python, postgres and redis and install all python requirements so the first time it runs it may take a while.

Subsequent test runs will be much quicker.

The testing framework runs Django, Celery (if enabled), Postgres, HitchSMTP (a mock SMTP server), Firefox/Selenium and Redis.*/

Create a New Release
--------------------

This project is configured to use [bumpversion](https://github.com/peritus/bumpversion) , only prerequisite
is to have it installed. When the tests have passed and you're happy with the code base, just need to run::

  $ bumpversion [major|minor|patch]

Depending on which digit of the version needs to be updated, and then push with tags::

  $ git push --tags

Travis will take care of creating a new packaged, and upload it to PyPi.
