from googlesearch import search
import requests
import sys
import os

os.system("cls")


if len(sys.argv) == 1:
	print(f"Usage: python {sys.argv[0]} <result_count>")
	sys.exit(1)

if sys.argv[1] is None:
	print(f"Usage: python {sys.argv[0]} <result_count>")
	sys.exit(1)



dork = input("Dork: ")
urller = []
response = search(dork, num_results=int(sys.argv[1]))

for url in response:
    urller.append(url)

for url in urller:
	try:
		r = requests.get(url).text.lower()
		if "telerik_stylesheet" in r:
			print("[+] " + url)
			f = open("hits.txt", "a")
			f.write(url + "\n")
			f.close()
		else:
			print("[-] " + url)
	except requests.exceptions.ConnectionError:
		pass
	except Exception as e:
		print("Error: " + str(e))


print("\nDone.")
