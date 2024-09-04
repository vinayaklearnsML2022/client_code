from playwright.sync_api import sync_playwright
import time

def playwright(message):

    with sync_playwright() as playwright:
        
    # working code - checked on 28th august 2024
    #  browser = playwright.chromium.launch(headless=False)
    #  page = browser.new_page()
    #  page.goto("https://x.com/login")
    #  time.sleep(5)
    #  page.get_by_label("username").fill("exploretwe66921")
    #  time.sleep(2)
    #  page.get_by_text("Next").dblclick()
    #  time.sleep(2)
    #  page.get_by_text("Password",exact=True).fill("Learntweet.2024")
    #  time.sleep(5)
    #  page.click("text=Log in")
    #  time.sleep(5)
    #  page.goto("https://x.com/SaffronSunanda/status/1828603854155588029")
    #  time.sleep(10)
    #  links = page.get_by_role("button", name="Repost")
    #  links.nth(0).click()
    #  time.sleep(5)
    #  page.get_by_role('menuitem', name='Repost').click()
    #  time.sleep(2)
    #  browser.close()

    # working code - checked on 28th august 2024
    #  browser = playwright.chromium.launch(headless=False)
    #  page = browser.new_page()
    #  page.goto("https://x.com/Priyankabjym/status/1828422806838591666")
    #  time.sleep(10)
    #  page.click('text=Log in')
    #  time.sleep(5)
    #  page.get_by_label("username").fill("exploretwe66921")
    #  time.sleep(2)
    #  page.get_by_text("Next").dblclick()
    #  time.sleep(2)
    #  page.get_by_text("Password",exact=True).fill("Learntweet.2024")
    #  time.sleep(5)
    #  page.get_by_role("button", name="Log in").click()
    #  links = page.get_by_role("button", name="Repost")
    #  links.nth(0).click()
    #  time.sleep(5)
    #  page.get_by_role('menuitem', name='Repost').click()
    #  time.sleep(5)
    #  browser.close()


        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://x.com/")
        time.sleep(5)
    #  links = page.get_by_role("navigation", name="Sign in")
        page.get_by_text("Sign in").dblclick()
        time.sleep(5)

        if page.get_by_label("Phone, email, or username"):
            page.get_by_label("Phone, email, or username").fill("exploretwe66921")
            time.sleep(5)
    
    
        page.get_by_text("Next").dblclick()
        time.sleep(5)

        try:
            page.get_by_text("Password",exact=True).fill("Learntweet.2024")
            time.sleep(2)
            page.get_by_role("button", name="Log in").click()
        except:
            print("password not present")

            try:
                
                page.get_by_text("Phone or email",exact=True).fill("vallinsrinivasan@gmail.com")
                time.sleep(2)
                page.get_by_text("Next").dblclick()
                
                try:
                    
                    page.get_by_text("Password",exact=True).fill("Learntweet.2024")
                    time.sleep(2)
                    page.get_by_role("button", name="Log in").click()
                except:
                    print("password not present")

            except:
                print("Phone or email not present")
                
    
        time.sleep(5)
        page.goto(message)

        time.sleep(5)

        links = page.get_by_role("button", name="Repost")
        links.nth(0).click()
        time.sleep(5)
        page.get_by_role('menuitem', name='Repost').click()
        time.sleep(5)
        browser.close()

