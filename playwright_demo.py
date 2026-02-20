#This is my first progrma using playwright module

from playwright.sync_api import sync_playwright#--------------->>imports the palywright synchronous API ()

with sync_playwright() as p:#----------------------------------->># Start Playwright and open a browser session
# 'p' is the Playwright controller
    browser = p.chromium.launch(headless=False)#--------------->>> launch chromuim browser and  headless = False means it shows the window ie windows willl be visible
    website_name = input("Paste the website link here:")
    page = browser.new_page()# ------------------>> Open a new page (tab) in the browser
    page.goto(website_name)
    print(page.title())#------------------------------------->> prints the title oof the curent page
    input("Press Enter to close the browser...") #----------------->>> keeps browesr opens
    browser.close()#-------------------------------->> close the browser tab