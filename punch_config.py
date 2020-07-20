"""
Punch versioning configuration file.

punch is used to change semver version of the project
in every necessary place and properly tag git commit with a release.

Install Punch

    $ pip install

To change version use punch -p <part> where part is major, minor, patch

    $ punch -p patch
"""
__config_version__ = 1

GLOBALS = {"serializer": "{{major}}.{{minor}}.{{patch}}"}

FILES = ["setup.py", "steel_toes/__init__.py", "steel_toes/cli.py"]

VERSION = ["major", "minor", "patch"]

VCS = {
    "name": "git",
    "target_branch": "release-{{major}}.{{minor}}.{{patch}}",
    "commit_message": (
        "Version updated from {{ current_version }}" " to {{ new_version }}"
    ),
}
