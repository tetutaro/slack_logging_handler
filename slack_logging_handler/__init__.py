#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
package of logging handler which send messages to Slack
'''
import logging
import simplejson as json
import requests

__version__ = '0.1.0'
__url = 'https://github.com/tetutaro/slack_logging_handler'
__author = 'maruyama'


class SlackLoggingHandler(logging.Handler):
	default_emojis = {
		logging.NOTSET: ':question:',
		logging.DEBUG: ':thought_balloon:',
		logging.INFO: ':speech_balloon:',
		logging.WARNING: ':right_anger_bubble:',
		logging.ERROR: ':mega:',
		logging.CRITICAL: ':loudspeaker:',
	}

	def __init__(
		self, url=None, channel=None, username=None, emojis=None,
		format='%(asctime)s: %(module)s-%(name)s: %(message)s'
	):
		logging.Handler.__init__(self)
		if url is None:
			raise ValueError('url must be set')
		self.webhook_url = url
		self.channel = channel
		self.username = username
		self.formatter = logging.Formatter(format)
		if emojis is not None:
			self.emojis = emojis
		else:
			self.emojis = SlackLoggingHandler.default_emojis
		return

	def _make_content(self, record):
		msg = self.format(record)
		content = dict()
		if record.levelno > logging.INFO:
			content['link_names'] = 1
			content['attachments'] = [{
				'fallback': msg,
				'color': 'danger',
				'text': '@channel ' + msg,
			}]
		else:
			content['attachments'] = [{
				'fallback': msg,
				'color': 'good',
				'text': msg,
			}]
		content['icon_emoji'] = self.emojis[record.levelno]
		if self.username:
			content['username'] = self.username + ' ' + record.levelname
		else:
			content['username'] = record.levelname
		if self.channel:
			content['channel'] = self.channel
		return content

	def emit(self, record):
		headers = {'Content-type': 'application/json'}
		content = self._make_content(record)
		try:
			requests.post(self.webhook_url, data=json.dumps(content), headers=headers)
		except:
			self.handleError(record)
		return
