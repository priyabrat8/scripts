#!/usr/bin/env python3

# Ex:- python3 subdomin_enumeration.py google.com

import requests
import sys
import re
import subprocess as sp
from termcolor import colored

def getIpAddress(url):
	ipList = []
	isError = False
	try:
		#getting ipv4 addresses
		output = sp.check_output(["host", "-t","A",url], text=True)
		pattern_ipv4 = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
		ipv4_addresses = re.findall(pattern_ipv4, output)
		for address in ipv4_addresses :
			ipList.append(address)
	except:
		isError = True
		return isError

	return ipList

def request(url):
	try:
		result = requests.get(f'https://{url}')
		if(result):
			print(url)
			ipv4 = getIpAddress(url)
			if type(ipv4) == list :
				print(colored(f"IP: {ipv4[0]} ",'blue'))
			elif ipv4 == True:
				print(colored('Error in finding IP','red'))
	except:
		pass

def main():
	target_url = sys.argv[1]
	print(colored("Press ",'green') + colored('Ctrl + Z','red',attrs=['underline']) + colored(" to exit the terminal\n",'green'))
	print(colored("Finding Subdomins Of ---------> ",'light_cyan') + colored(target_url,'red') + '\n')

	with open('subdomains.txt', 'r') as wordlist:
		for word in wordlist:
			word = word.strip()
			test_url = word + '.' + target_url
			request(test_url)

main()

