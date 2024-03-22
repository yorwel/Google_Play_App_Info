import os
import re
import requests
from bs4 import BeautifulSoup
ch=''
def main():

	def screen_clear():                                   #clearing terminal screen
		if os.name == 'nt':
			os.system('cls')
		else:
			os.system('clear')

	def intro():
		print("\t\t\t\t\t-----Google Play App Info------")
		box_msg(''' Created by Gautham Prakash @: gauthamp10@gmail.com''')


	def box_msg(msg):                                     #for printing text in a box
		row = len(msg)
		h = ''.join(['+'] + ['-' *row] + ['+'])
		result= h + '\n'"|"+msg+"|"'\n' + h
		print(result)

	def print_lines():                                    #printing dotted lines
		print(("-"*68))

	def get_app_link(query):
		# html_page = requests.get("https://play.google.com/store/search?q="+query+"&c=apps")
		# soup = BeautifulSoup(html_page.text,'html.parser')
		# applink=soup.find('a',attrs={'class':'poRVub'})
		# return applink['href']
			try:
				html_page = requests.get("https://play.google.com/store/search?q=" + query + "&c=apps")
				# html_page = requests.get("https://play.google.com/store/apps/details?id=com." + query)
				soup = BeautifulSoup(html_page.text, 'html.parser')
				applink = soup.find('a', attrs={'class': 'Si6A0c Gy4nib'}) # Specify class
				if applink:
					return "https://play.google.com" + applink.get('href')
				else:
					print("Error: App link not found.")
					return None
			except Exception as e:
				print("Error occurred while fetching app link:", str(e))
				return None

	def get_info(url,soup):
		info_box = [info_box.text.strip() for info_box in soup.find_all('div', 'ubGTjb')] # Specify class
		name=soup.find('meta',attrs={'itemprop':'name'})
		price=soup.find('meta',attrs={'itemprop':'price'})
		priceCurrency=soup.find('meta',attrs={'itemprop':'priceCurrency'})
		desc=soup.find('meta',attrs={'itemprop':'description'})
		contentRating=soup.find('meta',attrs={'itemprop':'contentRating'})
		applicationCategory=soup.find('meta',attrs={'itemprop':'applicationCategory'})
		ratingValue=soup.find('meta',attrs={'itemprop':'ratingValue'})
		reviewCount=soup.find('meta',attrs={'itemprop':'reviewCount'})
		availability=soup.find('meta',attrs={'itemprop':'availability'})
		for item in info_box:
			if item.startswith("Updated"):
				updated=str(item[7:])
			if item.startswith("Size"):
				appSize=str(item[4:])
			if item.startswith("Installs"):
				installCount=str(item[8:])
			if item.startswith("Requires Android"):
				minAndroid=str(item[16:])
			if item.startswith("Current Version"):
				curVersion=str(item[15:])
		print("App name: ",name['content'])
		print("Price: ",price['content']+priceCurrency['content'])
		print("Description: ",desc['content'][:80]+".....")
		print("Content Rated for: ",contentRating['content'])
		print("Category: ",applicationCategory['content'])
		print("Rating: ",ratingValue['content'])
		print("Total Reviews: ",reviewCount['content'])
		print("Availability: ",availability['content'].rsplit('/',1)[1])
		print("App URL: ",url)
		print("Last Updated: ",updated)
		print("Size: ",appSize)
		print("Installs: ",installCount)
		print("Minimum Android Required: ",minAndroid)
		print("Lastest Version: ",curVersion)

	screen_clear()
	intro()
	query=input("Enter the app name: ")
	query=query.replace(' ','+')

	try:
		url='https://play.google.com'+get_app_link(query)
		print_lines()
		data=requests.get(url)
		soup = BeautifulSoup(data.text,'html.parser')
		get_info(url,soup)
	except Exception as e:
		print("Error occured!-", str(e))
	print_lines()

if __name__ == '__main__':                                       #Calling main(), the actual entry point for the scraper

	main()
	exit(0)
