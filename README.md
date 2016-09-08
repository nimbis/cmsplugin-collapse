cmsplugin-collapse
===================

A bootstrap accordion plugin for django-cms.

Installation
------------

* pip install cmsplugin-collapse
* Add cmsplugin_collapse to INSTALLED_APPS
* If you want chevrons for the dropdowns, check out this StackOverflow answer:
  http://stackoverflow.com/a/18568997


Requirements
------------

* django >= 1.8
* django-cms >= 3.3.1

Required for included template:
* django-sekizai
* bootstrap

Contributing
------------

See the [Contributing Guidelines](CONTRIBUTING.md).

History
-------

0.4.0:

    * Adding migration required for Django CMS v3.3.1 and later, which is now
      required for this app.

0.3.0:

    * Add missing Django migrations.
    * Extend title to 512 characters.

0.2.5:

    * Removing pip >= 6.0 requirement from setup.py.

0.2.4:

    * Update to Django 1.7 migrations

0.2.2:

    * Add session argument to parse_requirements.

0.2.0:

    * Add accordion-toggle class to title for css decoration.

0.1.3:

    * Fixed template locations.

0.1.2:

    * Fixed url in setup.py and additional import errors.

0.1.1:

    * Fixed renaming problem/import errors.

0.1.0:

    * Initial commit
