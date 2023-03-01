import shlex
from datetime import datetime
from pathlib import Path

from secsy.definitions import *
from secsy.tasks._categories import HTTPCommand


class feroxbuster(HTTPCommand):
	"""Simple, fast, recursive content discovery tool written in Rust"""
	cmd = 'feroxbuster'
	input_flag = '--url'
	file_flag = OPT_PIPE_INPUT
	json_flag = '--json'
	opt_prefix = '--'
	opts = {
		'wordlist': {'type': str, 'help': 'Wordlist'},
		'auto_tune': {'is_flag': True, 'help': 'Automatically lower scan rate when an excessive amount of errors are encountered'},
		'extract_links': {'is_flag': True, 'default': True, 'help': 'Extract links from response body (html, javascript, etc...); make new requests based on findings'},
		'collect_backups': {'is_flag': True, 'help': 'Automatically request likely backup extensions for "found" urls'},
		'collect_extensions': {'is_flag': True, 'help': 'Automatically discover extensions ad add them to --extensions'},
		'collect_words': {'is_flag': True, 'help': 'Automatically discover important words from within responses and add them to the wordlist'},
	}
	opt_key_map = {
		HEADER: 'headers',
		DELAY: OPT_NOT_SUPPORTED,
		DEPTH: 'depth',
		FOLLOW_REDIRECT: 'redirects',
		MATCH_CODES: 'status-codes',
		METHOD: 'methods',
		PROXY: 'proxy',
		RATE_LIMIT: 'rate-limit',
		RETRIES: OPT_NOT_SUPPORTED,
		THREADS: 'threads',
		TIMEOUT: 'timeout',
		USER_AGENT: 'user-agent',
	}
	output_map = {
		STATUS_CODE: 'status',
		CONTENT_TYPE: lambda x: x['headers'].get('content-type'),
		LINES: 'line_count',
		WORDS: 'word_count'
	}

	@staticmethod
	def on_init(self):
		self.output_path = self.get_opt_value('output_path')
		if not self.output_path:
			timestr = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
			self.output_path = f'{TEMP_FOLDER}/feroxbuster_{timestr}.json'
		Path(self.output_path).touch()
		self.cmd += f' --output {self.output_path}'

	@staticmethod
	def on_start(self):
		if self.input_path:
			self.cmd += ' --stdin'
		self.cmd += f' & tail --pid $! -f {shlex.quote(self.output_path)}'
		self.shell = True

	@staticmethod
	def validate_item(self, item):
		return item['type'] == 'response'