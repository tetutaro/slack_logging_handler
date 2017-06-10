#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import time
import logging
from slack_logging_handler import SlackLoggingHandler

from same_level import same_notset, same_debug, same_info
from same_level import same_warning, same_error, same_critical
from child.child_level import child_notset, child_debug, child_info
from child.child_level import child_warning, child_error, child_critical

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


def sample_notset():
	logger.log(logging.NOTSET, "メインのノットセット")
	time.sleep(1)
	same_notset()
	time.sleep(1)
	child_notset()
	return


def sample_debug():
	logger.debug("メインのデバッグ")
	time.sleep(1)
	same_debug()
	time.sleep(1)
	child_debug()
	return


def sample_info():
	logger.info("メインのインフォ")
	time.sleep(1)
	same_info()
	time.sleep(1)
	child_info()
	return


def sample_warning():
	logger.warning("メインのワーニング")
	time.sleep(1)
	same_warning()
	time.sleep(1)
	child_warning()
	return


def sample_error():
	logger.error("メインのエラー")
	time.sleep(1)
	same_error()
	time.sleep(1)
	child_error()
	return


def sample_critical():
	logger.critical("メインのクリティカル")
	time.sleep(1)
	same_critical()
	time.sleep(1)
	child_critical()
	return


if __name__ == '__main__':
	sample_notset()
	time.sleep(1)
	sample_debug()
	time.sleep(1)
	sample_info()
	time.sleep(1)
	sample_warning()
	time.sleep(1)
	sample_error()
	time.sleep(1)
	sample_critical()
