from ambient_package_update.metadata.author import PackageAuthor
from ambient_package_update.metadata.constants import (
    DEV_DEPENDENCIES,
    SUPPORTED_DJANGO_VERSIONS,
    SUPPORTED_PYTHON_VERSIONS,
)
from ambient_package_update.metadata.maintainer import PackageMaintainer
from ambient_package_update.metadata.package import PackageMetadata
from ambient_package_update.metadata.readme import ReadmeContent
from ambient_package_update.metadata.ruff_ignored_inspection import RuffIgnoredInspection

METADATA = PackageMetadata(
    package_name="django_dynamic_admin_forms",
    module_name="django_dynamic_admin_forms",
    github_package_name="django_dynamic_admin",
    company="Ambient Innovation: GmbH",
    authors=[
        PackageAuthor(
            name="Ambient Digital",
            email="hello@ambient.digital",
        ),
        PackageAuthor(
            name="Fabian Binz",
            email="fabian.binz@ambient.digital",
        ),
    ],
    maintainer=PackageMaintainer(name="Ambient Digital", url="https://ambient.digital/", email="hello@ambient.digital"),
    license_year=2022,
    development_status="5 - Production/Stable",
    has_migrations=False,
    readme_content=ReadmeContent(
        tagline="Add simple interactions to the otherwise static django admin.",
    ),
    supported_django_versions=SUPPORTED_DJANGO_VERSIONS,
    supported_python_versions=SUPPORTED_PYTHON_VERSIONS,
    dependencies=[
        f"Django>={SUPPORTED_DJANGO_VERSIONS[0]}",
    ],
    optional_dependencies={
        "dev": [
            *DEV_DEPENDENCIES,
            "unittest-parametrize~=1.4",
        ],
    },
    ruff_ignore_list=[
        RuffIgnoredInspection(
            key="RUF012", comment="Mutable class attributes should be annotated with `typing.ClassVar`"
        ),
        RuffIgnoredInspection(key="TRY003", comment="Avoid specifying long messages outside the exception class"),
    ],
)
