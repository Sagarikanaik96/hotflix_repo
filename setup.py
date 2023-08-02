from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in hotflix_repo/__init__.py
from hotflix_repo import __version__ as version

setup(
	name="hotflix_repo",
	version=version,
	description="hotflix_repo",
	author="hotflix_repo",
	author_email="hotflix_repo@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
