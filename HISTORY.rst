.. :changelog:

History
-------

Unreleased
++++++++++

* Django 1.11 compatibility

0.6.0 (2017-30-01)
++++++++++++++++++

* Clean-up references to `django-timedeltafield` (`#9`_). This required to squash
  the existing migrations. Make sure that you migrated to 0.5.0 first and
  applied all migrations everywhere.
* Fix test setup. Now Django 1.10 is officially supported.

.. _#9: https://github.com/founders4schools/django-donations/issues/9

0.5.0 (2017-27-01)
++++++++++++++++++

* Migrate to Django's `DurationField` (`#8`_). You need to upgrade your
  `DONATION_FREQUENCIES` setting. Values should now be python `timedelta`.

.. _#8: https://github.com/founders4schools/django-donations/issues/8

0.4.0 (2017-27-01)
++++++++++++++++++

* Fix bug with urllib import on Python 3 `#4`_
* Remove dependency on `django-autoconfig`
* Regenerate with cookie cutter for Django standalone app, resulting in:
  * Cleanup a few unused files
  * Remove the example project which isn't kept up to date
  * Add a changelog
  * Switch testing to use tox
  * Switch from coveralls to codecov.io
* Test views

.. _#4: https://github.com/founders4schools/django-donations/issues/4

0.3.0 (2016-10-20)
++++++++++++++++++

* Drop support for Django 1.6 and 1.7
* Support Django 1.9
* Prepare Django 1.10

0.2.7 (2015-12-17)
++++++++++++++++++

* Add the app config for Django 1.7+

0.2.6 (2015-12-07)
++++++++++++++++++

* Some Python 3 compatibilty fixes
* Prepare for Django 1.9 compatibility

0.2.5 (2015-11-23)
++++++++++++++++++

* Django 1.8 compatibility
* Fix a few issues with Python 3

0.2.4 (2015-11-12)
++++++++++++++++++

* Doc improvements
* Django 1.7 compatibility

0.2.3 (2015-10-23)
++++++++++++++++++

* Fix a crash with anonymous donor

0.2.2 (2015-10-22)
++++++++++++++++++

* Mostly tests improvements

0.2.0 (2015-10-19)
++++++++++++++++++

* Fix various unicode crashes
* Fix that prevented the server from starting when config was being
  loaded before the tables were created.
* Capture Donor name from JustGiving

0.1.3 (2016-10-16)
++++++++++++++++++

* Fix a Unicode crash in models and providers
* Revert erroneous change in `setup.py`

0.1.2 (2015-10-16)
++++++++++++++++++

* Admin improvements
* Installation fixes

0.1.1 (2015-10-13)
++++++++++++++++++

* Fix packaging on PyPI
* Docs improvements

0.0.2 (2015-10-12)
++++++++++++++++++

* Squash South migrations
* Autoconfig enhancements

0.0.1 (2015-10-12)
++++++++++++++++++

* First release on PyPI.
