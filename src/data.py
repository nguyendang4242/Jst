import requests
import time
from bs4 import BeautifulSoup

def initialize():
	'''
		Initializes Jst by downloading data and saving it to a file
	'''
	url = 'https://old.reddit.com/r/Jokes'
	headers = {'User-Agent' : 'Mozilla/5.0'}
	page = requests.get(url, headers=headers)
	f = open("jokes.txt", "w", encoding='utf-8')

	soup = BeautifulSoup(page.text, 'html.parser')

	attrs = {'class': 'thing', 'data-domain': 'self.Jokes'}

	for post in soup.find_all('div', attrs=attrs):
		title = post.find('a', class_='title').text
		
		post_link = post.find('a', class_='title').get('data-href-url')
		
		time.sleep(2)		#Limit request rate

		post_page = requests.get('http://old.reddit.com' + post_link, headers=headers)
		post_soup = BeautifulSoup(post_page.text, 'html.parser')

		user_post = post_soup.find('div', class_='thing').find('div', class_='md').text
		
		f.write("Title: " + title + "\n" + user_post + "\n")
