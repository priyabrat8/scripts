#!/usr/bin/env python3

# Ex:- web_path_enumeration.py google.com

import requests
import sys
from termcolor import colored

def request(url):
	try:
		result = requests.get(f'https://{url}')
		if(result):
			print("\n"+colored("[+] Disovered:",'green') + f"{url}\n")
			with open('result.txt','a') as file:
				file.write(f"{url}\n")
	except:
		pass

def main():
	target_url = sys.argv[1]
	print(colored("Target: ",'red') + target_url + '\n')
	print("Saving the result in file result.txt\n")
	with open('directory_list.txt', 'r') as wordlist:
		for word in wordlist:
			word = word.strip()
			test_url = target_url+ '/' + word
			print(colored("[-]",'red') + f"Trying word: {word}")
			request(test_url)

main()

