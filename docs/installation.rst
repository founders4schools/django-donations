============
Installation
============

Installable with `pip`::

    $ pip install django-donations

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
