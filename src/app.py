from sys import stderr

from ui import main

if __name__ == '__main__':
	try:
		main()
	except Exception as e:
		print(e.args, file=stderr)