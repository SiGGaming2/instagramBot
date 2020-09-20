from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import random
import string
import random

username = 'username123'
password = 'password123'
tag = 'funny'

comments = [' comment 1', 'comment 2', 'comment 3', 'comment 4', 'comment 5', 'comment 6', 'comment 7', 'comment 8', 'comment 10', 'comment 11', 'comment 12' ]

browser = webdriver.Firefox(executable_path= r"./drivers/geckodriver") 
browser.get(('https://www.instagram.com/accounts/login/?source=auth_switcher'))
sleep(2) 
def commentbot():
	commentAmount = 0
	x=1
	while x < 10:
		x+=1
		i = random.randint(1, 12)
		try:
			commentForm = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form').click()
		except:
			if x==2:
				nextPost = browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]').click()
			else:
				nextPost = browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]').click()
		commentForm = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea')
		commentForm.send_keys(comments[i])
		sleep(1)
		commentSend = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button').click()
		commentAmount+=1	
		sleep(4)
		if x == 2:
			nextPost = browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a').click()
		else:
			nextPost = browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]').click()
		sleep(4)
	print('Total Comments: ' + str(commentAmount))
	browser.refresh()
	sleep(3) 
#---------------------------------------------------------------------------------------------------------------------------------------
def followbot():
	try:
		followList = browser.find_element_by_xpath("//button[text()='others']").click()
	except:
		followList = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[2]/div/div/button').click()
	sleep(2)
	v = 0
	followed = 0
	while v <= 7:
		v+=1
		b = 1
		while b <= 6:
			sleep(1) 
			if v == 1:
				d = 5
			else:
				d = 4
			try:
				try:
					followButton = browser.find_element_by_xpath('/html/body/div['+str(d)+']/div/div/div[2]/div/div/div['+str(b)+']/div[3]').click()
				except: 
					followButton = browser.find_element_by_xpath("//button[text()='Follow']").click()
				followed +=1
			except:
				b=6
			b +=1
		browser.refresh()
		sleep(3)
		try:
			followList = browser.find_element_by_xpath("//button[text()='others']").click()
		except:
			followList = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[2]/div/div[2]/button').click()
	print('Followed: ' + str(followed))
	browser.refresh()
	sleep(3)
#-------------------------------------------------------------------------------------------------------------------------------		
def unfollower():
	unfollowed = 0
	profilebutton = browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span').click()
	sleep(1)
	secondprofilebutton = browser.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/a[1]/div').click()
	sleep(1)
	c = 1
	while c < 10:
		sleep(1)
		following = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a').click()
		a = 1
		while a < 8:
			sleep(1)
			try:
				unfollowButton = browser.find_element_by_xpath("//button[text()='Following']").click()
			except:
				unfollowButton = browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li['+str(a)+']/div/div[3]/button').click()
			sleep(0.5)
			confirmUnfollow = browser.find_element_by_xpath('//button[text()="Unfollow"]').click()
			unfollowed +=1
			a +=1
		sleep(.4)
		browser.refresh()
		c+=1
	print('Total unfollowed: ' + str(unfollowed))
		
#----------------------------------------------------------------------------------------------------------------------------------
def gotoFirstPost():
	browser.get('https://www.instagram.com/explore/tags/'+str(tag))
	#discoverPage = browser.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]/a').click()
	#Use this if tags dont work
	sleep(2)
	postPath = browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div').click()
	sleep(3)
def start():
	usernameForm = browser.find_element_by_name('username').send_keys(username)
	passwordForm = browser.find_element_by_name('password').send_keys(password)
	nextButton = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[3]/button').click()
	#browser.quit()
	sleep(7)
	saveLogin = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
	sleep(3)
	notification = browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
	i = input("C = comment, F = follow, U = unfollow\n")
	if i == 'U'or i =='u':
		unfollower()
	else:
		gotoFirstPost()
		if i == 'C' or i == 'c':
			commentbot()
		elif i == 'F' or i =='f':
			followbot()
		else:
			followbot()
			gotoFirstPost()
			commentbot()
			unfollower()

start()
