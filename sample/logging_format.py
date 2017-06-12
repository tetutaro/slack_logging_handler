#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os

logging_dict_config = {
	'version': 1,
	'disable_existing_loggers': True,
	'formatters': {
		'slack': {
			'format': '%(asctime)s: %(name)s: %(message)s',
			'datefmt': '%Y/%m/%d %H:%M:%S',
		},
		'stream': {
			'format': '[%(levelname)s] %(asctime)s: %(message)s',
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
	'root': {
		'level': 'DEBUG',
		'handlers': ['slack', 'stream'],
	},
}
