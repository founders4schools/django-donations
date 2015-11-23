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


Quick Start
-----------

Easiest way to install is via `pip`::

    pip install django-donations

Then add the app to your settings.py:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'donations',
        ...
    )

    from donations import setup
    setup()

And to your urls patterns:

.. code-block:: python

    urlpatterns = patterns(
        ...
        url(r'^donate/', include('donations.urls')),
        ...
    )

Just Giving Configuration
-------------------------

The app needs to be configured with your JustGiving API settings:

.. code-block:: python

    # Ability to point to Production or Sandbox URLs
    JUST_GIVING_WEB_URL = 'http://v3-sandbox.justgiving.com'
    JUST_GIVING_API_URL = 'http://api-sandbox.justgiving.com'
    # Replace below with your personal details
    JUST_GIVING_CHARITY_ID = '123456'
    JUST_GIVING_APP_ID = 'changeme'
    # Add a list of all the currencies you need to support
    CURRENCIES = ['GBP']

With django autoconfig
^^^^^^^^^^^^^^^^^^^^^^

Some of the setup is in database, you need to create a Provider and donation frequencies. To make it easier to set them up, we recommend to use `django autoconfig <https://github.com/mikebryant/django-autoconfig>`_, which will load the required objects when starting up. The only thing that needs to be added to your settings.py is:

.. code-block:: python

    from django_autoconfig.autoconfig import configure_settings
    configure_settings(globals())

Manually
^^^^^^^^

TODO

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

This project is configured to use `bumpversion
<https://github.com/peritus/bumpversion>`_, only prerequisite
is to have it installed. When the tests have passed and you're happy with the code base, just need to run::

  $ bumpversion [major|minor|patch]

Depending on which digit of the version needs to be updated, and then push with tags::

  $ git push --tags

Travis will take care of creating a new packaged, and upload it to PyPi.
