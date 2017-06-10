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


def child_notset():
	logger.log(logging.NOTSET, "１階層下のノットセット")
	return


def child_debug():
	logger.debug("１階層下のデバッグ")
	return


def child_info():
	logger.info("１階層下のインフォ")
	return


def child_warning():
	logger.warning("１階層下のワーニング")
	return


def child_error():
	logger.error("１階層下のエラー")
	return


def child_critical():
	logger.critical("１階層下のクリティカル")
	return
