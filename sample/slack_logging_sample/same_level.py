#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import logging.config
from .config_logging import config_logging_dict

logging.config.dictConfig(config_logging_dict)
logger = logging.getLogger('slack_logging_sample')


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
