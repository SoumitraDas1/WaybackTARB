import requests
from bs4 import BeautifulSoup

check=["Page not found","404","404s and heartbreaks"]
tag =['head','title','h1']
if __name__=="__main__":
	url = input()					#get url input -> http://www.example.com
	soft = False
	responce = requests.get(url)
	if responce.status_code == 404:	#check if the webserver gives a 404 error responce 
		print("404 NOT FOUND")
	else:
		if responce.status_code == 200: #if resonce is 200 ok then
			soup = BeautifulSoup(responce.content, 'html.parser')	#webscrapping using BeautifulSoup
			for t in tag:											#checking if any tag have 
				i = soup.find(t)									#any text like 404, Page not found
				for c in check:										#404s and heartbreaks
					if c in i.text:									#if the text match to any keyword 
						soft = True									#soft variable becomes True
						break				
			if soft == True:										#So if soft =True then 
				print("Soft 404 Detected")							#a soft 404 detected
			else:	print("[Responce] 200 OK")						#else it a Good page 
		else:	print(responce)
