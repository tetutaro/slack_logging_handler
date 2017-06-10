#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from setuptools import setup, find_packages
import slack_logging_handler


def setup_packages():
	metadata = dict()
	metadata['name'] = slack_logging_handler.__package__
	metadata['version'] = slack_logging_handler.__version__
	metadata['description'] = slack_logging_handler.__doc__
	metadata['url'] = slack_logging_handler.__url
	metadata['author'] = slack_logging_handler.__author
	metadata['license'] = 'MIT'
	metadata['packages'] = find_packages()
	metadata['include_package_data'] = False
	metadata['install_requires'] = [
		'simplejson',
		'requests',
	]
	setup(**metadata)
	return


if __name__ == "__main__":
	setup_packages()
