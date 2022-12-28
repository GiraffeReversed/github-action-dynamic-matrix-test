# todo pip install requests, packaging

import requests
from pprint import pprint
from packaging.version import Version #, parse


def get_pylint_versions():
    resp = requests.get('https://pypi.org/pypi/pylint/json')
    assert resp.status_code == 200

    data = resp.json()

    all_releases = []

    for version_string in data['releases']:
        version = Version(version_string)
        if version.is_prerelease or version.is_devrelease or version.is_postrelease:
            continue
        all_releases.append(version)

    all_releases.sort()

    last_patches = {}
    for version in all_releases:
        last_patches[f'{version.major}.{version.minor}'] = str(version)

    last_patch_versions = list(last_patches.values())
    return last_patch_versions

last_patch_versions = get_pylint_versions()
choosen_versions = last_patch_versions[-3:] 
# print(choosen_versions)

print("versions=['" + "','".join(choosen_versions) + "']")
