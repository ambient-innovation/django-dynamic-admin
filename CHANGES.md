# Changelog

**3.3.2** (2026-07-03)
  * Updated company and maintainer information to "Beyonder Deutschland"

**3.3.1** (2026-07-03)
  * **Breaking change:** Dropped support for Python 3.10 (nearing end-of-life in October 2026)
  * Added support for Python 3.14
  * Added native uv support to the rendered Read the Docs configuration
  * Replaced the unmaintained "m2r2" documentation dependency with "sphinx-mdinclude"
  * Added a Code of Conduct, issue templates and a pull request template to rendered packages
  * Made the single-version CI and Read the Docs jobs track the newest supported Python version
  * Bumped rendered single-version jobs to Python 3.14
  * Added a cache suffix to the uv setup step to avoid CI cache namespace conflicts
  * Excluded unsupported Python/Django combinations (Python 3.14 with Django 4.2 and 5.2) from the rendered CI matrix
  * Fixed the rendered ruff target-version to track the minimum supported Python (matching requires-python) instead of the newest
  * Removed the stale .md source suffix from the rendered Sphinx config, since sphinx-mdinclude provides only the mdinclude directive (not a Markdown source parser)

**3.3.0** (2026-07-03)
  * Empty release...

**3.2.14** (2026-03-30)
* Maintenance via ambient-package-update

**3.2.13** (2026-03-30)
  * Maintenance updates via ambient-package-update

**3.2.12** (2026-03-08)
  * Allow setting a list as a field value

**3.2.11** (2025-10-15)
  * Maintenance updates via ambient-package-update

**3.2.10** (2025-10-09)
  * Maintenance updates via ambient-package-update

**3.2.9** (2025-05-29)
  * Maintenance updates via ambient-package-update

**3.2.8** (2025-04-03)
  * Maintenance updates via ambient-package-update

* *3.2.7* (2025-02-15)
  * Internal updates via `ambient-package-update`

* *3.2.6* (2024-11-15)
  * Internal updates via `ambient-package-update`

* *3.2.5* (2024-10-14)
  * Added Python 3.13 support
  * Added Djade linter to pre-commit
  * Improved GitHub action triggers
  * Updated dev dependencies and linters

* *3.2.4* (2024-09-11)
  * Added GitHub action trigger for PRs

* *3.2.3* (2024-09-11)
  * Fixed coverage setup due to GitHub changes

* *3.2.2* (2024-09-11)
  * Fixed package name

**3.2.1**
  * Fixed test matrix

**3.2.0**
  * Added Django 5.1 support

**3.1.3**
  * Added SECURITY.md
  * Updated linters
  * Internal updates via `ambient-package-update`

**3.1.2**
  * Updated GitHub actions

**3.1.1**
  * Black-end documentation code

**3.1.0**
  * Dropped support for Python 3.8
  * Added multiple ruff linters

**3.0.4**
  * Linted docs with `blacken-docs` via `ambient-package-update`

**3.0.3**
  * Restructured Readme content

**3.0.2**
  * Internal updates via `ambient-package-update`

**3.0.1**
  * Internal updates via `ambient-package-update`

**3.0.0**
  * Dropped Django 3.2 & 4.1 support (via `ambient-package-update`)
  * Internal updates via `ambient-package-update`

**2.2.1**

- Fixed security issue with URL not being wrapped in `admin_view`
- Improved documentation

**2.2.0**

- Added Django 5.0 support
- Multiple maintenance improvements

**2.1.1**

- 100% coverage and bugfix in edge case
- Updates via ambient package updater

**2.1.0**

- Added Python 3.12 support

**2.0.1**

- Meta updates via ambient-package-update

**2.0.0**

- Dropped support for deprecated Django versions 2.2, 3.0, 3.1 & 4.0
- Updated linters and added more strict linting rules

**1.0.1**

- Tiy code cleanup

**1.0.0**

- Reduce amount of requests, move to ambient-package-update

**0.1.8**

- Improve support for select2 widgets used by Jazzmin

**0.1.7**

- Improve Jazzmin support and forms with file fields

**0.1.6**

- Support dynamic fields for custom form fields

**0.1.5**

- Jazzmin "support"

**0.1.4**

- README fixes

**0.1.3**

- Change Demo-GIF hosting

**0.1.2**

- README fixes

**0.1.1**

- README fixes

**0.1.0**

- Initial release
