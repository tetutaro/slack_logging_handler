#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os

config_logging_dict = {
	'version': 1,
	'disable_existing_loggers': False,
	'formatters': {
		'slack': {
			'format': '%(asctime)s: %(name)s-%(module)s: %(message)s',
			'datefmt': '%Y/%m/%d %H:%M:%S',
		},
		'stream': {
			'format': '[%(levelname)s] %(name)s-%(module)s: %(asctime)s: %(message)s',
			'datefmt': '%Y/%m/%d %H:%M:%S',
		},
	},
	'handlers': {
		'slack': {
			'class': 'slack_logging_handler.SlackLoggingHandler',
			'url': os.getenv('SLACK_LOGGING_HANDLER_URL'),
			'username': 'slack_logging_sample',
			'level': 'DEBUG',
			'formatter': 'slack',
		},
		'stream': {
			'class': 'logging.StreamHandler',
			'level': 'WARNING',
			'formatter': 'stream',
		},
	},
	'loggers': {
		'slack_logging_sample': {
			'level': 'DEBUG',
			'handlers': ['slack', 'stream'],
		},
	},
}
