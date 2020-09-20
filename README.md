# instagramBot
|| **Important** || If login fails try it twice, about 1 in 20 logins have a different page and will make the login fail
|| **Important** || Must disable Two Factor Authentication before using the bot. 2FA must be disabled while using the bot and should be enabled when not using the bot
|| **Disclaimer** || Made on linux, has not been tested on windows 10, may need modifications to work.
Must have selenium webdrivers and geckodriver installed. 
This link will help you set it up. https://linuxhint.com/using_selenium_firefox_driver/
The lines 8 - 12 must be changed for it to work. 
Username = Your instagram username
Password = Your instagram password
Tag = The tag you will follow people from and comment on
Comments = Keep the commas and the single quotes. May not include escape sequences or any characters Python does not allow in strings
|| If tags are not working, goto lines 109-110 and change the discover page with the browser.get ||
When using use any letter other than U, F, C to do all 3 bots
If internet is too slow for bot, change the sleep timers to be higher
