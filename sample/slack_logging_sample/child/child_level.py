#!/usr/bin/env python
# -*- coding:utf-8 -*-
import logging.config
from ..config_logging import config_logging_dict

logging.config.dictConfig(config_logging_dict)
logger = logging.getLogger('slack_logging_sample')


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
