#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import logging
from slack_logging_handler import SlackLoggingHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
slack_handler = SlackLoggingHandler(
	os.getenv('SLACK_LOGGING_HANDLER_URL'),
	username='slack_logging_sample',
	format='%(asctime)s: %(name)s: %(message)s'
)
slack_handler.setLevel(logging.DEBUG)
logger.addHandler(slack_handler)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.WARNING)
logger.addHandler(stream_handler)


def same_notset():
	logger.log(logging.NOTSET, "同レベルのノットセット")
	return


def same_debug():
	logger.debug("同レベルのデバッグ")
	return


def same_info():
	logger.info("同レベルのインフォ")
	return


def same_warning():
	logger.warning("同レベルのワーニング")
	return


def same_error():
	logger.error("同レベルのエラー")
	return


def same_critical():
	logger.critical("同レベルのクリティカル")
	return
