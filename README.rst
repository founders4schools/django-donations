================
Django Donations
================

.. image:: https://travis-ci.org/founders4schools/django-donations.svg?branch=master
   :target: https://travis-ci.org/founders4schools/django-donations
   :alt: Build

.. image:: https://codecov.io/gh/founders4schools/django-donations/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/founders4schools/django-donations
   :alt: Coverage

.. image:: https://landscape.io/github/founders4schools/django-donations/master/landscape.svg?style=flat-square
   :target: https://landscape.io/github/founders4schools/django-donations/master
   :alt: Code Health

.. image:: https://pyup.io/repos/github/founders4schools/django-donations/shield.svg
   :target: https://pyup.io/repos/github/founders4schools/django-donations/
   :alt: Updates
   
.. image:: https://pyup.io/repos/github/founders4schools/django-donations/python-3-shield.svg
   :target: https://pyup.io/repos/github/founders4schools/django-donations/
   :alt: Python 3   

.. image:: https://badge.fury.io/py/django-donations.svg
   :target: https://badge.fury.io/py/django-donations
   :alt: PyPI package

Reusable django app to receive & track donations on charitable sites

Documentation
-------------

The full documentation is at https://django-donations.readthedocs.io.

Quickstart
----------

Install Django Donations::

    pip install django-donations

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'donations.apps.DonationsConfig',
        ...
    )

Add Django Donations's URL patterns:

.. code-block:: python

    from donations import urls as donations_urls


    urlpatterns = [
        ...
        url(r'^', include(donations_urls)),
        ...
    ]

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

TODO
----

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

Supported Providers
-------------------

* Just Giving SDI

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
