# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in release/__init__.py
from release import __version__ as version

setup(
	name="release",
	version=version,
	description="Manage releases for Frappe and Frappe Apps",
	author="Frappe Technologies Pvt Ltd",
	author_email="developers@frappe.io",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires,
)
