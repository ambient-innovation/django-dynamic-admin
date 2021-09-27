# django-dynamic-admin

Add simple interactions to the otherwise static django admin.

## Installation

- Install the package via pip:
  
    ```pip install django-dynamic-admin```
    
    or via pipenv:

    ```pipenv install django-dynamic-admin```
- Add the module to `INSTALLED_APPS`:
    ```python
    INSTALLED_APPS = (
        ...,
        'dynamic_admin',
        'django.contrib.admin'
        ...
    )    
    ```
    Ensure that the `dynamic_admin` comes before the 
    default `django.contrib.admin` in the list of installed apps,
    because otherwise the templates, which are overwritten by `dynamic_admin`
    won't be found.
- Ensure that the `dynamic_admin` templates are found via using `APP_DIRS` setting:
  ```python
  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'APP_DIRS': True,
          ...
      },
  ]
  ```
