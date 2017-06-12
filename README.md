Slack Logging Handler
=====================

Python logging handler for Slack using incoming webhook

* change icon(emoji) by log level
* change color by log level
	* NOTSET, DEBUG, INFO: green
	* WARNING, ERROR, CRITICAL: red
* send notification to @channel when log level is high (WARNING, ERROR, CRITICAL)

## Install

* `> pip install simplejson requests`
* `> pip install git+https://github.com/tetutaro/slack_logging_handler`

## Usage

see [sample](sample)
