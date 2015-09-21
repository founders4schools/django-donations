django-donations
================


TODO
====

* verify check
* settings.py to model creation of providers (and make donation provider readonly)
* integrate with coveralls, landscape, pypi, readthedocs & travis
* transfer to f4s github
* tests - unit/integration

* Update the documentation and readme
* tasks.py - recurring donation handling
* forms.py - mixins to handle the donations
* dashboard - track/view donations from the business side - kpis etc

* views/urls? - provide an api hook into the system (/django-donations/donate, /django-donations/verify)

* other providers (paypal etc)



Basic Commands
--------------

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

The testing framework runs Django, Celery (if enabled), Postgres, HitchSMTP (a mock SMTP server), Firefox/Selenium and Redis.
