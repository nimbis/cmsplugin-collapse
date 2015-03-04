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

* django >= 1.5
* django-cms >= 3.0

Required for included template:
* django-sekizai
* bootstrap


History
-------

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
