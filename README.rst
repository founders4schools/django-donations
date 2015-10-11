Django Donations
================


TODO
====

* example project/sort out config folder
    * setup.py/requirements.txt
* auto_config.py/app_settings.py
* integrate with coveralls, landscape, pypi, readthedocs & travis
* tests - unit/integration
* task to periodically verify pending donations

* Update the documentation and readme
(* dashboard - track/view donations from the business side - kpis etc
* views/urls? - provide an api hook into the system (/donations - dashboard))

v2 and beyond
-------------
(* other providers (paypal etc))
* tasks.py - recurring donation handling - this is not possible right now as SDI is not an API to be automated


Basic Commands - Update to be correct
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
