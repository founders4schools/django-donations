=====
Usage
=====

Settings
--------

There are few settings which are global, and other specific to each provider.

* ``CURRENCIES``
* ``DONATION_VERIFY_API_URL_NAME``
* ``DONATION_VERIFY_FINISHED_URL``

Providers settings
++++++++++++++++++

* ``JUST_GIVING_WEB_URL``
* ``JUST_GIVING_API_URL``
* ``JUST_GIVING_CHARITY_ID``
* ``JUST_GIVING_APP_ID``

Views
-----

Subclass ``DonateView`` or POST to ``DonateAPI`` with the correct data.

When using ``DonateView``, there is the ``DonationForm`` which can be sub-classed
to customize or just used by itself.
