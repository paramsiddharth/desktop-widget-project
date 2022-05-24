import json
from pathlib import Path
from sys import stderr

from helpers import to_dict

CONFIG_FILE = Path('..') / 'config.json'

def get_config():
	try:
		if CONFIG_FILE.is_file():
			with open(CONFIG_FILE) as f:
				data = json.load(f)

			return data
	except Exception as e:
		print(e.args, file=stderr)
	
	return None