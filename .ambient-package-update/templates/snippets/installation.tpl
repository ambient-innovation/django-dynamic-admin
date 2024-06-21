## Installation

- Install the package via pip:

   `pip install django-dynamic-admin-forms`

   or via pipenv:

   `pipenv install django-dynamic-admin-forms`

- Add the module to `INSTALLED_APPS`:
    ```python
    INSTALLED_APPS = (
        'django_dynamic_admin_forms',
        'django.contrib.admin',
    )
    ```
    Ensure that the `dynamic_admin_forms` comes before the
    default `django.contrib.admin` in the list of installed apps,
    because otherwise the templates, which are overwritten by `dynamic_admin_forms`
    won't be found.

- Ensure that the `dynamic_admin_forms` templates are found via using `APP_DIRS` setting:
  ```python
  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'APP_DIRS': True,
      },
  ]
  ```

- Run `python manage.py collectstatic` to include this apps Javascript code in your `settings.STATIC_ROOT` directory
