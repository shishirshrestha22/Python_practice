#python code to automate tms account

#first playwright synchronous API is imported

from playwright.sync_api import sync_playwright

with sync_playwright() as p:#------------------>> this starts playwright from here
    try:
        browser = p.chromium.launch(headless= False)#------------->. this line opens browser
        page = browser.new_page()#------------->> this opens new tab in browser
        page.goto("https://auth.naasasecurities.com.np/realms/naasa/protocol/openid-connect/auth"
            "?client_id=blaze&scope=openid%20profile&response_type=code"
            "&redirect_uri=https://x.naasasecurities.com.np/login")
        #this above line is link to the website

        #page.pause()#--------->> this line prevents browse from closing
        page.wait_for_selector("input")
        page.fill("input","shishirstha2212@gmail.com")#--------------------->>> this line fills the email in usernsme section

        page.wait_for_selector("input[type='password']",timeout=15000)#--------------------timeout = 15000 waits for 15 seconds until the selector appears

        page.fill("input[type='password']",'demopassword.com')

        page.click("button")
        input("Press ENTER to close browser....")
    except Exception as e:#----------------------------->> this handles exception or prevents code from crash and 'e' shows the reason of crash in program
        print("ERROR OCCURED:",e)

        input("Press Enter to close browser..")