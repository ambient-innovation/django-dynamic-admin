FROM python:3.9

WORKDIR /src/

COPY pyproject.toml README.md tox.ini /src/
COPY dynamic_admin_forms /src/dynamic_admin/

RUN python -m venv .venv
RUN pip install flit django~=3.2
RUN FLIT_ROOT_INSTALL=1 flit install --symlink

COPY testproj /src/testproj/
RUN rm -f /src/testproj/db.sqlite3

RUN python testproj/manage.py migrate
RUN python testproj/manage.py loaddata testproj/fixtures/fixtures-dev.json

EXPOSE 8000
CMD ["python", "testproj/manage.py", "runserver", "0.0.0.0:8000"]

