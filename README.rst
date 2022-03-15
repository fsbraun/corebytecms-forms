Installation
===========

Run ``pip install git+https://github.com/svandeneertwegh/djangocms-formbuilder``.

And also ``pip install aldryn-forms-recaptcha-plugin``.

Update ``INSTALLED_APPS`` with ::

    INSTALLED_APPS = [
        ...
        'absolute',
        'aldryn_forms',
        'aldryn_forms.contrib.email_notifications',
        'emailit',
        'filer',

        'aldryn_forms_recaptcha_plugin',
        'snowpenguin.django.recaptcha3',  # must be below the plugin
        ...
    ]
    
    RECAPTCHA_PUBLIC_KEY = env('RECAPTCHA_PRIVATE_KEY', '123')
    RECAPTCHA_PRIVATE_KEY = env('RECAPTCHA_PRIVATE_KEY', '123') 
    # set this to 0 (or 1) to deactivate (or always activate) the captcha protection
    RECAPTCHA_SCORE_THRESHOLD = 0.85

Configure ``aldryn-boilerplates`` (https://pypi.python.org/pypi/aldryn-boilerplates/).

To use the old templates, set ``ALDRYN_BOILERPLATE_NAME='legacy'``.
To use https://github.com/aldryn/aldryn-boilerplate-standard (recommended, will be renamed to
``aldryn-boilerplate-bootstrap3``) set ``ALDRYN_BOILERPLATE_NAME='bootstrap3'``.

Also ensure you define an `e-mail backend <https://docs.djangoproject.com/en/dev/topics/email/#dummy-backend>`_ for your app.


Creating a Form
===============

You can create forms in the admin interface now. Search for the label ``Aldryn_Forms``.

Create a CMS page and install the ``Forms`` app there (choose ``Forms`` from the ``Advanced Settings -> Application`` dropdown).

Now redeploy/restart the site again.

The above CMS site has become a forms POST landing page - a place where submission errors get displayed if there are any.


Available Plug-ins
==================

``Form`` plugin lets you embed certain forms on a CMS page.

``Fieldset`` groups fields.

``Text Field`` renders text input.

``Text Area Field`` renders text input.

``Yes/No Field`` renders checkbox.

``Select Field`` renders single select input.

``Multiple Select Field`` renders multiple checkboxes.

``File field`` renders a file upload input.

``Image field`` same as ``file field`` but validates that the uploaded file is an image.


Based on aldryn-forms package.
